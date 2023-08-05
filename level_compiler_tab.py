from PySide6.QtCore import QModelIndex, QRectF, Qt, QEvent, QCoreApplication, QObject, Signal, Slot, QTimer, QPoint, QRectF, QRect, QThread
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QPalette, QIcon, QColor
from PySide6.QtWidgets import ( QApplication, QDockWidget, QMainWindow, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QSizePolicy, QScrollArea, QWidget,
                               QTreeWidget, QTreeWidgetItem, QCheckBox, QStyleFactory, QProxyStyle, QStyle, QStyleOptionViewItem, QStyledItemDelegate, QListView,
                                QMessageBox, QPushButton, QListWidget )

import level
import utility

import os
import sys

from typing import Type
import subprocess
from functools import partial
import json


class LevelCompilerTab():
    def __init__(self, main_window) -> None:
        self.main_window = main_window

        self.main_window.ui.compileLevelBtn.clicked.connect(self.compile_level)
        self.level_compiler_checked_state_path = os.path.join(os.getcwd(), 'level_compiler_checked_state.json')
        if not os.path.exists(self.level_compiler_checked_state_path):
            with open(self.level_compiler_checked_state_path, 'w+') as file:
                json.dump({}, file)

        self.populate_map_source_list()
        self.populate_mod_specific_list()

        if self.main_window.ui.modSpecificMapCheckbox.isChecked():
            self.main_window.ui.modSpecificMapList.setEnabled(True)
        else:
            self.main_window.ui.modSpecificMapList.setEnabled(False)

        self.main_window.ui.modSpecificMapCheckbox.stateChanged.connect(self.handle_mod_specific_map_checkbox_state_changed)
        self.main_window.ui.compile_mapname_list.currentItemChanged.connect(self.handle_map_selection_change)
        self.main_window.ui.compile_mapname_list.setCurrentRow(0)

        selected_item = self.main_window.ui.compile_mapname_list.currentItem()
        selected_item.setBackground(QColor(0, 120, 215))
        level.MAP_NAME = selected_item.text()

        self.saveUpdatedCheckedStatesAdhoc()

        signal_slots = [
            ("updateConsole", self.updateConsole),
            ("disableCompileBtn", self.disableCompileBtn),
            ("updateExeArgs", self.updateExeArgs),
            ("updateSuccessErrorMsgArea", self.updateSuccessErrorMsgArea)
        ]

        self.init_thread(attr_name="compile_level_thread", _class=LevelFFThread, signal_slots=signal_slots)
        self.init_thread(attr_name="compile_patch_thread", _class=PatchFFThread, signal_slots=signal_slots)

    def init_thread(self, attr_name:str, _class:Type, signal_slots:list, *args:None, **kwargs:None) -> None:
        var = _class(self, *args, **kwargs)

        for signal, slot in signal_slots:
            getattr(var, signal).connect(slot)
        
        setattr(self, attr_name, var)
    
    @Slot(str)
    def updateConsole(self, message:str) -> None:
        self.main_window.ui.console.appendPlainText(message.split(' : ')[-1])
        level.LOG.append(message)
        QApplication.processEvents()

    @Slot(bool)
    def disableCompileBtn(self, is_enabled:bool) -> None:
        # Enable
        if is_enabled and not self.main_window.ui.compileLevelBtn.isEnabled():
            self.main_window.ui.compileLevelBtn.setEnabled(True)
        # Disable
        elif not is_enabled and self.main_window.ui.compileLevelBtn.isEnabled():
            self.main_window.ui.compileLevelBtn.setEnabled(False)
        QApplication.processEvents()
    
    @Slot(str)
    def updateExeArgs(self, text):
        self.main_window.ui.exeArgs.clear()
        self.main_window.ui.exeArgs.setText(text.split(' : ')[-1])
        level.LOG.append(text)
        QApplication.processEvents()

    @Slot(str)
    def updateSuccessErrorMsgArea(self, message:str) -> None:
        self.main_window.ui.consoleSuccessErrorOutput.clear()
        self.main_window.ui.consoleSuccessErrorOutput.setText(message.split(' : ')[-1])
        level.LOG.append(message)
        QApplication.processEvents()

    def compile_level(self):
        if "_patch" not in level.MAP_NAME:
            self.compile_level_thread.start()
        else:
            self.compile_patch_thread.start()

    def handle_mod_specific_map_checkbox_state_changed(self, state):
        # Enable or disable the modSpecificMapList based on the checkbox state
        self.main_window.ui.modSpecificMapList.setEnabled(state)
    
    def handle_map_selection_change(self, current_item, previous_item):
        # Reset the background color for the previous item
        if previous_item:
            previous_item.setBackground(QColor('#1F1F1F'))

        # Set the background color for the current item
        if current_item:
            current_item.setBackground(QColor(0, 120, 215))  # Set your desired highlight color
            level.MAP_NAME = current_item.text()
            self.loadCheckedState()
        
        self.autoSelectModSpecificMap()

    def autoSelectModSpecificMap(self):
        # Get all item names from the QComboBox
        item_names = []
        for i in range(self.main_window.ui.modSpecificMapList.count()):
            item_name = self.main_window.ui.modSpecificMapList.itemText(i)
            item_names.append(item_name)

        # Find the index of the name in the QListWidget
        match = False
        if "_patch" in level.MAP_NAME:
            self.disable_unused_checkbox_options(True)
            curr_selected_map = level.MAP_NAME.replace("_patch", "")
        else:
            self.disable_unused_checkbox_options(False)
            curr_selected_map = level.MAP_NAME

        if curr_selected_map in item_names:
            # print(f"selected map name: {curr_selected_map}")
            match = True

        # If the index is found, set the corresponding item in the QComboBox as selected
        if match:
            self.main_window.ui.modSpecificMapList.setCurrentText(curr_selected_map)
            self.selected_mod_specific_name = curr_selected_map
        else:
            self.selected_mod_specific_name = None

    def disable_unused_checkbox_options(self, _bool):
        style = "line-through" if _bool else "none"

        self.main_window.ui.compileBspCheckbox.setStyleSheet("#compileBspCheckbox {text-decoration: " + style + ";}")
        self.main_window.ui.compileLightsCheckbox.setStyleSheet("#compileLightsCheckbox {text-decoration: " + style + ";}")
        self.main_window.ui.connectPathsCheckbox.setStyleSheet("#connectPathsCheckbox {text-decoration: " + style + ";}")
        self.main_window.ui.compileReflectionsCheckbox.setStyleSheet("#compileReflectionsCheckbox {text-decoration: " + style + ";}")

        self.main_window.ui.onlyEntsCheckbox.setStyleSheet("#onlyEntsCheckbox {text-decoration: " + style + ";}")
        self.main_window.ui.compileLightsFastCheckbox.setStyleSheet("#compileLightsFastCheckbox {text-decoration: " + style + ";}")
        self.main_window.ui.compileLightsExtraCheckbox.setStyleSheet("#compileLightsExtraCheckbox {text-decoration: " + style + ";}")

        self.main_window.ui.modSpecificMapCheckbox.setStyleSheet("#modSpecificMapCheckbox {text-decoration: " + style + ";}")

        value = False if _bool else True
        self.main_window.ui.compileBspCheckbox.setEnabled(value)
        self.main_window.ui.compileLightsCheckbox.setEnabled(value)
        self.main_window.ui.connectPathsCheckbox.setEnabled(value)
        self.main_window.ui.compileReflectionsCheckbox.setEnabled(value)

        self.main_window.ui.onlyEntsCheckbox.setEnabled(value)
        self.main_window.ui.compileLightsFastCheckbox.setEnabled(value)
        self.main_window.ui.compileLightsExtraCheckbox.setEnabled(value)

        self.main_window.ui.modSpecificMapCheckbox.setEnabled(value)

    def populate_map_source_list(self):
        self.main_window.ui.compile_mapname_list.clear()
        # Specify the map source folder path
        map_source_dir = os.path.join(level.ROOT_DIR, "map_source")
        files = []

        for filename in os.listdir(map_source_dir):
            # Check if its a file
            if os.path.isfile(os.path.join(map_source_dir, filename)):
                # Ensure its a valid file
                if filename.endswith('.map'):
                    # Start with main level file
                    if '_patch' not in filename:
                        # Check if its _patch file exists
                        if os.path.isfile(os.path.join(map_source_dir, f"{os.path.splitext(filename)[0]}_patch.map")):
                            # Valid map found. Append both level and _patch filenames
                            files.append(filename)  # level
                            files.append(f"{os.path.splitext(filename)[0]}_patch.map")  # patch

        for file in files:
            filename = os.path.splitext(file)[0] # remove extension
            self.main_window.ui.compile_mapname_list.addItem(filename)

    def populate_mod_specific_list(self):
        self.main_window.ui.modSpecificMapList.clear()
        # Specify the mods folder path
        mods_folder = level.MODS_DIR
        folders = [folder for folder in os.listdir(mods_folder) if os.path.isdir(os.path.join(mods_folder, folder))]
        for folder in folders:
            self.main_window.ui.modSpecificMapList.addItem(folder)
    
    def loadCheckedState(self):
        if os.path.getsize(self.level_compiler_checked_state_path) > 0:
            if utility.is_key_in_json_file(level.MAP_NAME, self.level_compiler_checked_state_path):
                json_data = utility.load_json_data(self.level_compiler_checked_state_path)
                self.applyCheckedStates(json_data)
            else:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Nothing to load from level compiler json file. Applying default states / adding to json file.")
                self.applyCheckedStatesDefault()
                self.saveCheckedState()

    def saveCheckedState(self):
        # Save the checked state information
        checked_state = self.getCheckedStates()

        json_data = utility.load_json_data(self.level_compiler_checked_state_path)
     
        # Check if there are root keys
        if len(json_data) == 0:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} No root keys found in the JSON file. Adding first map to json file.")
            utility.save_json_data(self.level_compiler_checked_state_path, checked_state)
        else:
            new_dict = {}

            # Add old mod keys data to new dict
            root_keys = list(json_data.keys())
            for key in root_keys:
                new_dict[key] = json_data[key]

            # Add new mod key data to new dict
            root_keys = list(checked_state.keys())
            for key in checked_state:
                new_dict[key] = checked_state[key]
                break
        
            utility.save_json_data(self.level_compiler_checked_state_path, new_dict)
    
    def getCheckedStates(self):
        checked_state = {}
        mod_key = level.MAP_NAME
        checked_state[mod_key] = {}

        checked_state[mod_key]["bsp"] = self.main_window.ui.compileBspCheckbox.isChecked()
        checked_state[mod_key]["lights"] = self.main_window.ui.compileLightsCheckbox.isChecked()
        checked_state[mod_key]["paths"] = self.main_window.ui.connectPathsCheckbox.isChecked()
        checked_state[mod_key]["reflections"] = self.main_window.ui.compileReflectionsCheckbox.isChecked()
        checked_state[mod_key]["fastfiles"] = self.main_window.ui.buildLevelFastfilesCheckbox.isChecked()

        checked_state[mod_key]["only_ents"] = self.main_window.ui.onlyEntsCheckbox.isChecked()
        checked_state[mod_key]["fast"] = self.main_window.ui.compileLightsFastCheckbox.isChecked()
        checked_state[mod_key]["extra"] = self.main_window.ui.compileLightsExtraCheckbox.isChecked()

        checked_state[mod_key]["mod_specific_map"] = self.main_window.ui.modSpecificMapCheckbox.isChecked()

        return checked_state

    def applyCheckedStates(self, checked_state):
        mod_key = level.MAP_NAME

        # Apply the checked states to the widgets
        self.main_window.ui.compileBspCheckbox.setChecked(checked_state[mod_key]["bsp"])
        self.main_window.ui.compileLightsCheckbox.setChecked(checked_state[mod_key]["lights"])
        self.main_window.ui.connectPathsCheckbox.setChecked(checked_state[mod_key]["paths"])
        self.main_window.ui.compileReflectionsCheckbox.setChecked(checked_state[mod_key]["reflections"])
        self.main_window.ui.buildLevelFastfilesCheckbox.setChecked(checked_state[mod_key]["fastfiles"])

        self.main_window.ui.onlyEntsCheckbox.setChecked(checked_state[mod_key]["only_ents"])
        self.main_window.ui.compileLightsFastCheckbox.setChecked(checked_state[mod_key]["fast"])
        self.main_window.ui.compileLightsExtraCheckbox.setChecked(checked_state[mod_key]["extra"])

        self.main_window.ui.modSpecificMapCheckbox.setChecked(checked_state[mod_key]["mod_specific_map"])

    def applyCheckedStatesDefault(self):
        _bool = True if "_patch" not in level.MAP_NAME else False
        self.main_window.ui.compileBspCheckbox.setChecked(_bool)
        self.main_window.ui.compileLightsCheckbox.setChecked(_bool)
        self.main_window.ui.connectPathsCheckbox.setChecked(_bool)
        self.main_window.ui.compileReflectionsCheckbox.setChecked(_bool)
        self.main_window.ui.buildLevelFastfilesCheckbox.setChecked(True)

        self.main_window.ui.onlyEntsCheckbox.setChecked(False)
        self.main_window.ui.compileLightsFastCheckbox.setChecked(True)
        self.main_window.ui.compileLightsExtraCheckbox.setChecked(False)

        self.main_window.ui.modSpecificMapCheckbox.setChecked(_bool)
    
    def saveUpdatedCheckedStatesAdhoc(self):
        # by adding the 'e' (event) param, it means that the signal wont execute until it receives the signal, in this case the 'stateChanged' signal. Removing the event param will cause the slot to be executed as the signal is defined.
        self.main_window.ui.compileBspCheckbox.stateChanged.connect(lambda e: self.saveCheckedState())
        self.main_window.ui.compileLightsCheckbox.stateChanged.connect(lambda e: self.saveCheckedState())
        self.main_window.ui.connectPathsCheckbox.stateChanged.connect(lambda e: self.saveCheckedState())
        self.main_window.ui.compileReflectionsCheckbox.stateChanged.connect(lambda e: self.saveCheckedState())
        self.main_window.ui.buildLevelFastfilesCheckbox.stateChanged.connect(lambda e: self.saveCheckedState())

        self.main_window.ui.onlyEntsCheckbox.stateChanged.connect(lambda e: self.saveCheckedState())
        self.main_window.ui.compileLightsFastCheckbox.toggled.connect(lambda e: self.saveCheckedState())
        self.main_window.ui.compileLightsExtraCheckbox.toggled.connect(lambda e: self.saveCheckedState())

        self.main_window.ui.modSpecificMapCheckbox.stateChanged.connect(lambda e: self.saveCheckedState())


class LevelFFThread(QThread):
    updateConsole = Signal(str)
    disableCompileBtn = Signal(bool)
    updateExeArgs = Signal(str)
    updateSuccessErrorMsgArea = Signal(str)

    def __init__(self, level_compiler_tab:LevelCompilerTab):
        super().__init__()
        self.level_compiler_tab = level_compiler_tab
        self.manually_killed = {
            'bsp': None,
            'lights': None,
            'nodes': None,
            'probes': None,
            'mapname_ff': None
        }

    def interrupt(self, which):
        self.manually_killed[which] = True

    def run(self):
        self.manually_killed['bsp'] = False
        self.manually_killed['lights'] = False
        self.manually_killed['nodes'] = False
        self.manually_killed['probes'] = False
        self.manually_killed['mapname_ff'] = False

        # Temp disable compile map btn
        self.disableCompileBtn.emit(False)

        mapname_dot_map_path = os.path.join(os.path.join(level.ROOT_DIR, "map_source"), f"{level.MAP_NAME}.map")
        raw_maps_mapname_path = os.path.join(os.path.join(level.ROOT_DIR, "raw\maps"), level.MAP_NAME)

        # BSP
        if self.level_compiler_tab.main_window.ui.compileBspCheckbox.isChecked():
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile bsp begin")
            self.level_compiler_tab.main_window.ui.activeExes.addItem("Compile: BSP")

            try:
                args = ["cod2map", "-platform", "pc", "-loadfrom", mapname_dot_map_path, raw_maps_mapname_path]
                process = subprocess.Popen(args, cwd=level.BIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                level.SUBPROCESSES["Compile: BSP"] = ["cod2map", process]
                
                for line in iter(partial(process.stdout.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
                for line in iter(partial(process.stderr.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

                process.communicate()
            except subprocess.CalledProcessError as e:
                # Handle subprocess error
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
            except Exception as e:
                # Handle any other unexpected errors
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
            
            if not self.manually_killed['bsp']:
                self.level_compiler_tab.main_window.remove_process("Compile: BSP")
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile bsp complete")
            else:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")

        # LIGHTS
        if self.level_compiler_tab.main_window.ui.compileLightsCheckbox.isChecked():
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile lights begin")
            self.level_compiler_tab.main_window.ui.activeExes.addItem("Compile: LIGHTS")

            try:
                args = ["cod2rad", "-platform", "pc", "-fast", "-modelshadow", raw_maps_mapname_path]
                process = subprocess.Popen(args, cwd=level.BIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                level.SUBPROCESSES["Compile: LIGHTS"] = ["cod2rad", process]
                
                for line in iter(partial(process.stdout.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
                for line in iter(partial(process.stderr.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

                process.communicate()
            except subprocess.CalledProcessError as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
            except Exception as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")

            if not self.manually_killed['lights']:
                self.level_compiler_tab.main_window.remove_process("Compile: LIGHTS")
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile lights complete")
            else:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")

        # PATHNODES
        if self.level_compiler_tab.main_window.ui.connectPathsCheckbox.isChecked():
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile nodes begin")
            self.level_compiler_tab.main_window.ui.activeExes.addItem("Compile: NODES")

            try:
                args = ["sp_tool", "allowdupe", "+set", "developer", "1", "+set", "logfile", "2", "+set", "thereisacow", "1337", "+set", "com_introplayed", "1", "+set", "r_fullscreen", "0", "+set", "fs_usedevdir", "1", "+set", "g_connectpaths", "2", "+set", "useFastFile", "0", "+devmap", level.MAP_NAME]        
                process = subprocess.Popen(args, cwd=level.ROOT_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                level.SUBPROCESSES["Compile: NODES"] = ["sp_tool", process]
                
                for line in iter(partial(process.stdout.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
                for line in iter(partial(process.stderr.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

                process.communicate()
            except subprocess.CalledProcessError as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
            except Exception as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")

            if not self.manually_killed['nodes']:
                self.level_compiler_tab.main_window.remove_process("Compile: NODES")
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile nodes complete")
            else:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")

        # REFLECTION PROBES
        if self.level_compiler_tab.main_window.ui.compileReflectionsCheckbox.isChecked():
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile probes begin")
            self.level_compiler_tab.main_window.ui.activeExes.addItem("Compile: PROBES")

            try:
                args = ["sp_tool", "allowdupe", "+set", "developer", "1", "+set", "logfile", "2", "+set", "thereisacow", "1337", "+set", "com_introplayed", "1", "+set", "r_fullscreen", "0", "+set", "fs_usedevdir", "1", "+set", "ui_autoContinue", "1", "+set", "r_reflectionProbeGenerateExit", "1", "+set", "sys_smp_allowed", "0", "+set", "useFastFile", "0", "+set", "r_fullscreen", "0", "+set", "com_hunkMegs", "512", "+set", "r_reflectionProbeRegenerateAll", "1", "+set",  "r_zFeather", "1", "+set", "r_smp_backend_allowed", "1", "+set", "r_reflectionProbeGenerate", "1", "+devmap", level.MAP_NAME]
                process = subprocess.Popen(args, cwd=level.ROOT_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                level.SUBPROCESSES["Compile: PROBES"] = ["sp_tool", process]
                
                for line in iter(partial(process.stdout.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
                for line in iter(partial(process.stderr.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

                process.communicate()
            except subprocess.CalledProcessError as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
            except Exception as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")

            if not self.manually_killed['probes']:
                self.level_compiler_tab.main_window.remove_process("Compile: PROBES")
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile probes complete")
            else:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")

        # FASTFILE
        if self.level_compiler_tab.main_window.ui.buildLevelFastfilesCheckbox.isChecked():
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile mapname.ff begin")
            self.level_compiler_tab.main_window.ui.activeExes.addItem("Compile: FF")

            success = True
            try:
                args = ["linker_pc", "-nopause", "-language", "english", "-moddir", level.MAP_NAME, level.MAP_NAME]
                process = subprocess.Popen(args, cwd=level.BIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                level.SUBPROCESSES["Compile: FF"] = ["linker_pc", process]
                
                for line in iter(partial(process.stdout.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
                for line in iter(partial(process.stderr.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

                process.communicate()
            except subprocess.CalledProcessError as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
                success = False
            except Exception as e:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
                success = False

            if not self.manually_killed['mapname_ff']:
                self.level_compiler_tab.main_window.remove_process("Compile: FF")
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile mapname.ff complete")
            else:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")
                success = False
            
            if success:
                # MOVE .ff FILES
                source = os.path.join(os.path.join(level.ROOT_DIR, "zone\english"), f"{level.MAP_NAME}.ff")
                destination = os.path.join(level.MOD_DIR, f"{level.MAP_NAME}.ff")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \nMoving  {source}")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}     to  {destination}")
                success = utility.move_files(source, destination)

                if success:
                    source = os.path.join(level.MOD_DIR, f"{level.MAP_NAME}.ff")
                    destination = os.path.join(os.path.join(level.ACTIVISION_MODS_DIR, level.MAP_NAME), f"{level.MAP_NAME}.ff")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Copying  {source}")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}      to  {destination}")
                    success = utility.copy_files(source, destination)

                    # End of line. You made it!
                    if success:
                        self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Success")
                    # So close!
                    else:
                        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
                        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}                    copy mapname.ff error!")
                        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
                        self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
                else:
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}                    move mapname.ff error!")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
            else:
                if not self.manually_killed:
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
                else:
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Error: -1")

        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n############################## ---/--/--- ##############################\n")
        # re-enable run game btn
        self.disableCompileBtn.emit(True)
        self.level_compiler_tab.main_window.save_logfile()


class PatchFFThread(QThread):
    updateConsole = Signal(str)
    disableCompileBtn = Signal(bool)
    updateExeArgs = Signal(str)
    updateSuccessErrorMsgArea = Signal(str)

    def __init__(self, level_compiler_tab:LevelCompilerTab):
        super().__init__()
        self.level_compiler_tab = level_compiler_tab

    def interrupt(self):
        self.manually_killed = True

    def run(self):
        self.manually_killed = False

        self.disableCompileBtn.emit(False)

        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile mapname_patch.ff begin")
        self.level_compiler_tab.main_window.ui.activeExes.addItem("Compile: Patch")

        success = True
        try:
            args = ["linker_pc", "-nopause", "-language", "english", "-moddir", level.MAP_NAME.replace('_patch', ''), level.MAP_NAME]
            self.updateExeArgs.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} {' '.join(args)}")
            process = subprocess.Popen(args, cwd=level.BIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            level.SUBPROCESSES["Compile: Patch"] = ["linker_pc", process]
            
            for line in iter(partial(process.stdout.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
            for line in iter(partial(process.stderr.readline, 2048), ''):
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

            process.communicate()
        except subprocess.CalledProcessError as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
            success = False
        except Exception as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
            success = False

        if not self.manually_killed:
            self.level_compiler_tab.main_window.remove_process("Compile: Patch")
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} compile mapname_patch.ff complete")
        else:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")
            success = False

        if success:
            # Move compiled mapname_patch.ff from zone/english to mods/mapname
            source = os.path.join(os.path.join(level.ROOT_DIR, "zone\english"), f"{level.MAP_NAME}.ff")
            destination = os.path.join(level.MOD_DIR, f"{level.MAP_NAME}.ff")
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \nMoving  {source}")
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}     to  {destination}")
            success = utility.move_files(source, destination)

            if success:
                source = os.path.join(level.MOD_DIR, f"{level.MAP_NAME}.ff")
                destination = os.path.join(os.path.join(level.ACTIVISION_MODS_DIR, level.MAP_NAME.replace('_patch', '')), f"{level.MAP_NAME}.ff")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Copying  {source}")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}      to  {destination}")
                success = utility.copy_files(source, destination)

                # End of line. You made it!
                if success:
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Success")
                # So close!
                else:
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}                    copy mapname_patch.ff error!")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
        else:
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}                    move mapname_patch.ff error!")
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
            if not self.manually_killed:
                self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
            else:
                self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Error: -1")

        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n############################## ---/--/--- ##############################\n")
        # re-enable run game btn
        self.disableCompileBtn.emit(True)
        self.level_compiler_tab.main_window.save_logfile()
        