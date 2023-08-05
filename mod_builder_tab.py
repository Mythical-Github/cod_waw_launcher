from PySide6.QtCore import Qt, Signal, Slot, QThread, QTimer
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

import level
import utility

import os
import sys

from typing import Union, Type, List, Dict
import subprocess
from functools import partial
import re
import json


class ModBuilderTab():
    def __init__(self, main_window) -> None:
        self.main_window = main_window

        self.main_window.ui.buildModBtn.clicked.connect(self.build_mod)
        self.mod_builder_checked_state_path = os.path.join(os.getcwd(), 'mod_builder_checked_state.json')
        if not os.path.exists(self.mod_builder_checked_state_path):
            with open(self.mod_builder_checked_state_path, 'w+') as file:
                json.dump({}, file)

        signal_slots = [
            ("updateConsole", self.updateConsole),
            ("disableBuildBtn", self.disableBuildBtn),
            ("updateExeArgs", self.updateExeArgs),
            ("updateSuccessErrorMsgArea", self.updateSuccessErrorMsgArea)
        ]

        self.init_thread("mod_ff_thread", ModFFThread, signal_slots)
        self.init_thread("iwd_thread", IWDThread, signal_slots)
        self.init_thread("build_sounds_thread", BuildSoundsThread, signal_slots)

        self.init_mod_builder_section()
        self.init_iwd_file_list()

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
    def disableBuildBtn(self, is_enabled:bool) -> None:
        # Enable
        if is_enabled and not self.main_window.ui.buildModBtn.isEnabled():
            self.main_window.ui.buildModBtn.setEnabled(True)
        # Disable
        elif not is_enabled and self.main_window.ui.buildModBtn.isEnabled():
            self.main_window.ui.buildModBtn.setEnabled(False)
        QApplication.processEvents()
    
    @Slot(str)
    def updateExeArgs(self, text:str) -> None:
        # Update the GUI within the main thread
        self.main_window.ui.exeArgs.clear()

        if '7za a -tzip -r' in text.split(' : ')[-1]:
            self.main_window.ui.exeArgs.setText('7za a -tzip -r output_zip_path... source_directory...')
        else:
            self.main_window.ui.exeArgs.setText(text.split(' : ')[-1])
        level.LOG.append(text)
        QApplication.processEvents()

    @Slot(str)
    def updateSuccessErrorMsgArea(self, message:str) -> None:
        self.main_window.ui.consoleSuccessErrorOutput.clear()
        self.main_window.ui.consoleSuccessErrorOutput.setText(message.split(' : ')[-1])
        level.LOG.append(message)
        QApplication.processEvents()
    
    def build_mod(self) -> None:
        self.saveCheckedState()

        mod_csv_path = f'{level.MOD_DIR}\mod.csv'
        mod_csv_section_text = self.main_window.ui.modCsv.toPlainText()
        mod_csv_file_contents = utility.read_file(mod_csv_path, "Reading Mod.csv", True)
        if mod_csv_section_text != mod_csv_file_contents:
            utility.overwrite_file(mod_csv_path, "Overwriting Mod.csv", mod_csv_section_text)

        # Counter for running threads
        self.running_threads = 0

        # Slot to handle finished threads
        def thread_finished():
            self.running_threads -= 1
            if self.running_threads == 0:
                QTimer.singleShot(2000, self.main_window.copy_any_mod_files_over_to_appdata_if_not_present)

        # Connect finished signals to the slot
        self.mod_ff_thread.finished.connect(thread_finished)
        self.iwd_thread.finished.connect(thread_finished)
        self.build_sounds_thread.finished.connect(thread_finished)

        # Start mod_ff_thread if the checkbox is checked
        if self.main_window.ui.linkFastFile.isChecked():
            self.running_threads += 1
            self.mod_ff_thread.start()

        # Start iwd_thread after mod_ff_thread finishes, if the checkbox is checked
        if self.main_window.ui.buildIWD.isChecked() and self.isAnyCheckboxChecked(self.tree_widget):
            checked_items = sorted(self.getCheckedItems())
            array = [item for item in checked_items if utility.has_extension(item)]
            
            self.iwd_thread.set_array(array)
            
            if self.mod_ff_thread.isRunning():
                self.mod_ff_thread.finished.connect(self.iwd_thread.start)
            else:
                self.running_threads += 1
                self.iwd_thread.start()
        else:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Ignoring IWD build as nothing is checked")

        # Start build_sounds_thread after iwd_thread finishes, if the checkbox is checked
        if self.main_window.ui.BuildSoundsCheckBox.isChecked():
            if self.mod_ff_thread.isRunning() and self.iwd_thread.isRunning():
                self.iwd_thread.finished.connect(self.build_sounds_thread.start)
            elif self.mod_ff_thread.isRunning():
                self.mod_ff_thread.finished.connect(self.build_sounds_thread.start)
            elif self.iwd_thread.isRunning():
                self.iwd_thread.finished.connect(self.build_sounds_thread.start)
            else:
                self.running_threads += 1
                self.build_sounds_thread.start()

    def isAnyCheckboxChecked(self, parent_item:QTreeWidget) -> Union[True, False]:
        for i in range(parent_item.topLevelItemCount()):
            child_item = parent_item.topLevelItem(i)
            if child_item.checkState(0) == Qt.Checked:
                return True
        return False

    def init_mod_builder_section(self) -> None:
        # Populate the QComboBox with folder names from the specified path
        self.populate_folder_names()

        level.MOD_NAME = self.main_window.ui.modDropDownList.currentText()
        level.MOD_DIR = os.path.join(level.MODS_DIR, level.MOD_NAME)

        level.MOD_TREE_INDEXES[level.MOD_NAME] = {}
        self.tree_items_index = 0

        # list needs to be populated and mod-name assigned before connecting this signal as it needs the above info not to be None
        self.main_window.ui.modDropDownList.currentIndexChanged.connect(self.handleComboBoxSelection)

        self.populate_mod_csv_area()
    
    def populate_mod_csv_area(self) -> None:
        mod_csv_path = f'{level.MOD_DIR}\mod.csv'
        contents = utility.read_file(mod_csv_path, "Reading Mod.csv", True)
        mod_csv_text_edit = self.main_window.ui.modCsv
        mod_csv_text_edit.clear()
        if contents:
            mod_csv_text_edit.insertPlainText(contents)
    
    def populate_folder_names(self) -> None:
        path = level.MODS_DIR

        # Clear the existing items in the QComboBox
        self.main_window.ui.modDropDownList.clear()

        # Get the folder names in the specified path
        folder_names = [item for item in os.listdir(path) if os.path.isdir(os.path.join(path, item))]

        # Add the folder names to the QComboBox
        self.main_window.ui.modDropDownList.addItems(folder_names)

    def handleComboBoxSelection(self, index:int) -> None:
        level.MOD_NAME = self.main_window.ui.modDropDownList.currentText()
        level.MOD_DIR = os.path.join(level.MODS_DIR, level.MOD_NAME)

        level.MOD_TREE_INDEXES[level.MOD_NAME] = {}
        self.tree_items_index = 0

        # had to add this check for the Refresh Mod feature. i think its the connected signal triggering timing.
        # nothing to worry about tho, a simple check saves the day.
        if utility.contains_letters(level.MOD_NAME):
            self.populate_mod_csv_area()

            # Populate the tree widget with files from the specified folder
            self.populate_tree_widget(level.MOD_DIR)
            self.tree_widget.expandAll()
        # else:
        #     print(f"level.MOD_NAME: {level.MOD_NAME} - is not valid")

    def init_iwd_file_list(self) -> None:
        # Create the QTreeWidget
        self.tree_widget = self.main_window.ui.iwdTree
        self.tree_widget.setHeaderHidden(True)
        self.tree_widget.invisibleRootItem()
        self.tree_widget.itemChanged.connect(self.handleItemStateChanged)

        self.excluded_file_extensions_iwd = ('.exe', '.iwd', '.ff', '.files', '.log', '.bat', '.txt', '.jpeg', '.jpg', '.tga', '.dds', '.png')
        self.add_checked_state_manually = True
        
        # Populate the tree widget with files from the specified folder
        self.populate_tree_widget(level.MOD_DIR)
        self.tree_widget.expandAll()

    def populate_tree_widget(self, path:str) -> None:
        # clear tree for new mod data
        self.tree_widget.clear()
        # Recursively populate the tree widget
        self.populate_tree_widget_recursive(path, None)
        self.tree_widget.scrollToTop()

        if os.path.getsize(self.mod_builder_checked_state_path) > 0:
            if utility.is_key_in_json_file(level.MOD_NAME, self.mod_builder_checked_state_path):
                self.loadCheckedState()

    def populate_tree_widget_recursive(self, path:str, parent_item:Union[None, QTreeWidgetItem]) -> None:
        # Get the items in the current path and sort them alphabetically
        items = sorted(os.listdir(path))

        # Separate folders and files
        folders = []
        files = []
        for item in items:
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                folders.append(item)
            elif os.path.isfile(item_path):
                # Exlcude files with specific extensions
                exclude = item.endswith(self.excluded_file_extensions_iwd)
                if not exclude:
                    files.append(item)

        # Iterate over folders and add them to the tree widget
        for folder in folders:
            folder_path = os.path.join(path, folder)
            parent_item = self.tree_widget if parent_item is None else parent_item
            tree_item = QTreeWidgetItem(parent_item, [folder])
            tree_item.setFlags(tree_item.flags() | Qt.ItemIsUserCheckable)
            tree_item.setCheckState(0, Qt.Unchecked)
            self.populate_tree_widget_recursive(folder_path, tree_item)

        # Iterate over files and add them to the tree widget
        for file in files:
            file_path = os.path.join(path, file)
            file_path = file_path.replace(level.MOD_DIR + "\\", '')
            tree_item = QTreeWidgetItem(parent_item, [file])
            tree_item.setFlags(tree_item.flags() | Qt.ItemIsUserCheckable)
            tree_item.setCheckState(0, Qt.Unchecked)
            # Store index as data attribute
            tree_item.setData(0, Qt.UserRole, self.tree_items_index)
            # retrieve index test
            level.MOD_TREE_INDEXES[level.MOD_NAME][self.tree_items_index] = {
                file: file_path
            }
            self.tree_items_index += 1

    def getCheckedItems(self) -> List:
        checked_items = []
        self.getCheckedItemsRecursive(self.tree_widget, checked_items)
        return checked_items
    
    def getCheckedItemsRecursive(self, parent_item:Union[QTreeWidget, QTreeWidgetItem], checked_items:List) -> None:
        if isinstance(parent_item, QTreeWidget):
            for i in range(parent_item.topLevelItemCount()):
                child_item = parent_item.topLevelItem(i)
                if child_item.checkState(0) == Qt.Checked:
                    checked_items.append(child_item.text(0))
                self.getCheckedItemsRecursive(child_item, checked_items)
        elif isinstance(parent_item, QTreeWidgetItem):
            for i in range(parent_item.childCount()):
                child_item = parent_item.child(i)
                if child_item.checkState(0) == Qt.Checked:
                    index = child_item.data(0, Qt.UserRole)
                    if index is not None:
                        checked_items.append(level.MOD_TREE_INDEXES[level.MOD_NAME][index][child_item.text(0)])
                self.getCheckedItemsRecursive(child_item, checked_items)

    def handleItemStateChanged(self, item:QTreeWidgetItem, column:int) -> None:
        # Signal handler for item check state changed
        if item.checkState(column) == Qt.Checked:
            if item.childCount() > 0:
                self.checkFolderItems(item, Qt.Checked)
        elif item.checkState(column) == Qt.Unchecked:
            if item.childCount() > 0:
                self.checkFolderItems(item, Qt.Unchecked)
    
    def checkFolderItems(self, item:Union[QTreeWidget, QTreeWidgetItem], check_state:Union[Qt.Checked, Qt.Unchecked]) -> None:
        # Recursive function to check/uncheck all child items of a folder item
        for i in range(item.childCount()):
            child_item = item.child(i)
            child_item.setCheckState(0, check_state)
            if child_item.childCount() > 0:
                self.checkFolderItems(child_item, check_state)
    
    def saveCheckedState(self) -> None:
        # Save the checked state information
        checked_state = {}
        root_item = self.tree_widget.invisibleRootItem()
        root_key = level.MOD_NAME
        checked_state[root_key] = {}
        self.saveCheckedStateRecursive(root_item, checked_state[root_key])

        json_data = utility.load_json_data(self.mod_builder_checked_state_path)
        if json_data is not None:
            # Check if there are root keys
            if len(json_data) == 0:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} No root keys found in the JSON file. Adding first mod to json file")
                utility.save_json_data(self.mod_builder_checked_state_path, checked_state)
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
            
                utility.save_json_data(self.mod_builder_checked_state_path, new_dict)

    def saveCheckedStateRecursive(self, parent_item:Union[QTreeWidget, QTreeWidgetItem], checked_state:Union[Qt.Checked, Qt.Unchecked]) -> None:
        # Recursive function to save the checked state
        for i in range(parent_item.childCount()):
            child_item = parent_item.child(i)
            child_text = child_item.text(0)
            child_state = child_item.checkState(0) == Qt.Checked

            if child_item.childCount() > 0:
                # If the child item has children, create a nested dictionary
                checked_state[child_text] = {}
                self.saveCheckedStateRecursive(child_item, checked_state[child_text])
                checked_state[child_text]['checked'] = child_state
            else:
                # If the child item has no children, store the checked state directly
                checked_state[child_text] = child_state

    def loadCheckedState(self) -> None:
        json_data = utility.load_json_data(self.mod_builder_checked_state_path)
        if json_data is not None:
            self.keys = self.getAllKeysRecursive(json_data)
            self.applyCheckedStateRecursive(self.tree_widget, json_data[level.MOD_NAME])
    
    def getAllKeysRecursive(self, dictionary:Dict) -> List:
        keys = []
        for key, value in dictionary.items():
            keys.append(key)
            if isinstance(value, dict):
                nested_keys = self.getAllKeysRecursive(value)
                keys.extend(nested_keys)
        return keys

    def applyCheckedStateRecursive(self, parent_item:Union[QTreeWidget, QTreeWidgetItem], checked_state:Union[Qt.Checked, Qt.Unchecked]) -> None:
        x = parent_item.topLevelItemCount() if isinstance(parent_item, QTreeWidget) else parent_item.childCount()
        for i in range(x):
            child_item = parent_item.topLevelItem(i) if isinstance(parent_item, QTreeWidget) else parent_item.child(i)
            child_text = child_item.text(0)
            if child_text in self.keys:
                check_state = checked_state.get(child_text)
                if isinstance(check_state, bool):
                    child_item.setCheckState(0, Qt.Checked if check_state else Qt.Unchecked)
                else:
                    check_state = check_state.get('checked', False)
                    child_item.setCheckState(0, Qt.Checked if check_state else Qt.Unchecked)
                    if child_item.childCount() > 0:
                        self.applyCheckedStateRecursive(child_item, checked_state.get(child_text, {}))


class ModFFThread(QThread):
    updateConsole = Signal(str)
    disableBuildBtn = Signal(bool)
    updateExeArgs = Signal(str)
    updateSuccessErrorMsgArea = Signal(str)

    def __init__(self, mod_builder_tab:ModBuilderTab):
        super().__init__()
        self.mod_builder_tab = mod_builder_tab

    def interrupt(self):
        self.manually_killed = True

    def run(self):
        self.manually_killed = False
        
        # Temp disable build mod btn
        self.disableBuildBtn.emit(False)

        # Copy mod.csv from mods/modname to zone_source
        old_csv = os.path.join(level.MOD_DIR, "mod.csv")
        new_csv = os.path.join(os.path.join(level.ROOT_DIR, "zone_source"), "mod.csv")
        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Copying  {old_csv}")
        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}      to  {new_csv}\n")
        success = utility.copy_files(old_csv, new_csv)

        if success:
            # Compile mod.ff via running linker_pc command
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} build mod.ff begin")
            self.mod_builder_tab.main_window.ui.activeExes.addItem("Build: Mod")

            success = True
            try:
                args = ["linker_pc", "-nopause", "-language", "english", "-moddir", level.MOD_NAME, "mod"]
                self.updateExeArgs.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} {' '.join(args)}")
                process = subprocess.Popen(args, cwd=level.BIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                level.SUBPROCESSES["Build: Mod"] = ["linker_pc", process]

                for line in iter(partial(process.stdout.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
                for line in iter(partial(process.stderr.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

                process.communicate()                
            except subprocess.CalledProcessError as e:
                # Handle subprocess error
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
                success = False
            except Exception as e:
                # Handle any other unexpected errors
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
                success = False
            
            if not self.manually_killed:
                self.mod_builder_tab.main_window.remove_process("Build: Mod")
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} build mod.ff complete")
            else:
                level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")
                success = False

            if success:
                # Move compiled mod.ff from zone/english to mods/modname
                source = os.path.join(os.path.join(level.ROOT_DIR, "zone\english"), "mod.ff")
                destination = os.path.join(level.MOD_DIR, "mod.ff")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \nMoving  {source}")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}     to  {destination}")
                success = utility.move_files(source, destination)

                if success:
                    source = os.path.join(level.MOD_DIR, "mod.ff")
                    destination = os.path.join(os.path.join(level.ACTIVISION_MODS_DIR, level.MOD_NAME), "mod.ff")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Copying  {source}")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}      to  {destination}")
                    success = utility.copy_files(source, destination)

                    # End of line. You made it!
                    if success:
                        self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Success")
                    # So close!
                    else:
                        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
                        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}                    copy mod.ff error!")
                        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
                        self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
                else:
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}                    move mod.ff error!")
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
            else:
                if not self.manually_killed:
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
                else:
                    self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Error: -1")
        else:
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}                   copy mod.csv error!")
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
            self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")

        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n############################## ---/--/--- ##############################\n")
        # re-enable build mod btn
        self.disableBuildBtn.emit(True)
        self.mod_builder_tab.main_window.save_logfile()


class IWDThread(QThread):
    updateConsole = Signal(str)
    disableBuildBtn = Signal(bool)
    updateExeArgs = Signal(str)
    updateSuccessErrorMsgArea = Signal(str)

    def __init__(self, mod_builder_tab:ModBuilderTab) -> None:
        super().__init__()
        self.mod_builder_tab = mod_builder_tab
        self.array = None
        self.should_continue = True  # added flag to control the loop

    def set_array(self, array:List) -> None:
        self.array = array

    def interrupt(self):
        self.manually_killed = True

    def run(self):
        self.manually_killed = False
        
        # Temp disable build mod btn
        self.disableBuildBtn.emit(False)

        # Initialize creation of mapname.iwd
        source = os.path.join(level.MOD_DIR, f"{level.MOD_NAME}.iwd")
        destination = os.path.join(os.path.join(level.ACTIVISION_MODS_DIR, level.MOD_NAME), f"{level.MOD_NAME}.iwd")
        
        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} 7-Zip (A) 9.20  Copyright (c) 1999-2010 Igor Pavlov  2010-11-18")
        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Scanning\n")
        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Creating archive {source}\n")

        # Compress the items in the array
        output_zip_path = os.path.join(level.MOD_DIR, f"{level.MOD_NAME}.iwd")
        array = sorted(self.array)
        
        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} build iwd begin")
        self.mod_builder_tab.main_window.ui.activeExes.addItem("Build: IWD")

        success = True
        try:
            for item in array:
                if self.manually_killed:
                    break
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Compressing {item}")
                source_directory = os.path.join(level.MOD_DIR, item.split('\\')[-1]).replace("\\", "/")
                
                args = ['7za', 'a', '-tzip', '-r', output_zip_path, source_directory]
                self.updateExeArgs.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} {' '.join(args)}")
                process = subprocess.Popen(args, cwd=level.BIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                level.SUBPROCESSES["Build: IWD"] = ["7za", process]

                # Wait for the process to complete and get all of the output.
                stdout_data, stderr_data = process.communicate()

                # Process the stdout data.
                # Note: I am manually outputting the iwd info to console that's why i only append to log and not emit updateConole method
                if stdout_data:
                    for line in stdout_data.split('\n'):
                        if 'error' in line.lower():
                            success = False
                            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} {line.strip()}")

                # Process the stderr data.
                if stderr_data:
                    success = False
                    for line in stderr_data.split('\n'):
                        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.strip()}")

        except subprocess.CalledProcessError as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
            success = False
        except Exception as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
            success = False

        if not self.manually_killed:
            self.mod_builder_tab.main_window.remove_process("Build: IWD")
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} build iwd complete")
        else:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")
            success = False

        if success:
            self.updateConsole.emit(f"\n{utility.get_class_and_method_name(sys._getframe(0))} \nCopying  {source}")
            self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}      to  {destination}")
            success = utility.copy_files(source, destination)
            # End of line. You made it!
            if success:
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \nEverything is Ok")
                self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Success")
            # So close!
            else:
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n################################################")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))}         copy {level.MOD_NAME}.iwd error !")
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} ################################################\n")
                self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
        else:
            if not self.manually_killed:
                self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Failer")
            else:
                self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Error: -1")

        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n############################## ---/--/--- ##############################\n")
        # re-enable build mod btn
        self.disableBuildBtn.emit(True)
        self.mod_builder_tab.main_window.save_logfile()


class BuildSoundsThread(QThread):
    updateConsole = Signal(str)
    disableBuildBtn = Signal(bool)
    updateExeArgs = Signal(str)
    updateSuccessErrorMsgArea = Signal(str)

    def __init__(self, mod_builder_tab):
        super().__init__()
        self.mod_builder_tab = mod_builder_tab

    def interrupt(self):
        self.manually_killed = True

    def run(self):
        self.manually_killed = False

        # Temp disable build mod btn
        self.disableBuildBtn.emit(False)  # Emit the signal to disable the button

        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} build sounds begin")
        self.mod_builder_tab.main_window.ui.activeExes.addItem("Build: Sounds")

        success = True
        successError = None
        try:
            args = ["MODSound", "-pc", "-ignore_orphans"]
            self.updateExeArgs.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} {' '.join(args)}")
            process = subprocess.Popen(args, cwd=level.BIN_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            level.SUBPROCESSES["Build: Sounds"] = ["MODSound", process]
            
            # Process the output in real-time
            for line in iter(partial(process.stdout.readline, 2048), ''):
                self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE INFO: {line.rstrip()}")
                if "error" in line.strip().lower():
                    successError = line.rstrip()
            
            for line in iter(partial(process.stderr.readline, 2048), ''):
                    self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} EXE ERROR: {line.rstrip()}")

            # Wait for the process to complete
            process.communicate()
        except subprocess.CalledProcessError as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
            success = False
        except Exception as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
            success = False
        
        if not self.manually_killed:
            self.mod_builder_tab.main_window.remove_process("Build: Sounds")
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} build sounds complete")
        else:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")
            success = False
        
        if success:
            self.updateSuccessErrorMsgArea.emit("Success")
        else:
            if not self.manually_killed:
                self.updateSuccessErrorMsgArea.emit(re.sub(r'\s+', ' ', successError))
            else:
                self.updateSuccessErrorMsgArea.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} Error: -1")

        self.updateConsole.emit(f"{utility.get_class_and_method_name(sys._getframe(0))} \n############################## ---/--/--- ##############################\n")
        # re-enable build mod btn
        self.disableBuildBtn.emit(True)
        self.mod_builder_tab.main_window.save_logfile()
