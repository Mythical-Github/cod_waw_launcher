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


class RunGameTab():
    def __init__(self, main_window) -> None:
        self.main_window = main_window

        self.main_window.ui.runGameBtn.clicked.connect(self.run_game)

        self.populateModOption()
        self.populateDevmapOption()
        self.populateTheRest()

        self.main_window.ui.rgSelectModOption.currentIndexChanged.connect(lambda: self.updateAll("modOption", "mods/", self.main_window.ui.rgSelectModOption))
        self.main_window.ui.rgDevmapOption.currentIndexChanged.connect(lambda: self.updateAll("devmapOption", "+devmap", self.main_window.ui.rgDevmapOption))
        self.main_window.ui.rgCheatsOption.currentIndexChanged.connect(lambda: self.updateAll("cheatsOption", "+set thereisacow", self.main_window.ui.rgCheatsOption))
        self.main_window.ui.rgDeveloperOption.currentIndexChanged.connect(lambda: self.updateAll("developerOption", "+set developer", self.main_window.ui.rgDeveloperOption))
        self.main_window.ui.rgDeveloperScriptOption.currentIndexChanged.connect(lambda: self.updateAll("developerScriptOption", "+set developer_script", self.main_window.ui.rgDeveloperScriptOption))
        self.main_window.ui.rgLogfileOption.currentIndexChanged.connect(lambda: self.updateAll("logFileOption", "+set logfile", self.main_window.ui.rgLogfileOption))
        self.main_window.ui.rgIntroplayedOption.currentIndexChanged.connect(lambda: self.updateAll("introPlayedOption", "+set com_introplayed", self.main_window.ui.rgIntroplayedOption))
        self.main_window.ui.rgShipIWDOption.currentIndexChanged.connect(lambda: self.updateAll("shipIWDOption", "+set sv_pure", self.main_window.ui.rgShipIWDOption))
        self.main_window.ui.rgFullscreenOption.currentIndexChanged.connect(lambda: self.updateAll("fullScreenOption", "+set r_fullscreen", self.main_window.ui.rgFullscreenOption))
        self.main_window.ui.rgPunkBusterOption.currentIndexChanged.connect(lambda: self.updateAll("punkBusterOption", "+set sv_punkbuster", self.main_window.ui.rgPunkBusterOption))
        self.main_window.ui.rgTestclientsOption.currentIndexChanged.connect(lambda: self.updateAll("testClientsOption", "+set scr_testclients", self.main_window.ui.rgTestclientsOption))

        self.cmd_line = {
            "modOption": "raw",
            "devmapOption": "",
            "cheatsOption": "",
            "developerOption": "",
            "developerScriptOption": "",
            "logFileOption": "",
            "introPlayedOption": "",
            "shipIWDOption": "",
            "fullScreenOption": "",
            "punkBusterOption": "",
            "testClientsOption": ""
        }

        self.updateCommandLine()
    
        signal_slots = [
            ("updateConsole", self.updateConsole),
            ("disableRunGameBtn", self.disableRunGameBtn)
        ]
        self.init_thread(attr_name="run_game_thread", _class=RunGameThread, signal_slots=signal_slots)

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
    def disableRunGameBtn(self, is_enabled:bool) -> None:
        # Enable
        if is_enabled and not self.main_window.ui.runGameBtn.isEnabled():
            self.main_window.ui.runGameBtn.setEnabled(True)
        # Disable
        elif not is_enabled and self.main_window.ui.runGameBtn.isEnabled():
            self.main_window.ui.runGameBtn.setEnabled(False)
        QApplication.processEvents()
    
    def run_game(self):
        self.run_game_thread.start()
    
    def populateModOption(self):
        self.main_window.ui.rgSelectModOption.clear()
        path = level.MODS_DIR
        folder_names = [
            item
            for item in os.listdir(path)
            if os.path.isdir(os.path.join(path, item))
        ]
        folder_names.insert(0, "(not set)")
        self.main_window.ui.rgSelectModOption.addItems(folder_names)
    
    def populateDevmapOption(self):
        self.main_window.ui.rgDevmapOption.clear()
        path = level.MODS_DIR
        maps = []
        mods = [
            item
            for item in os.listdir(path)
            if os.path.isdir(os.path.join(path, item))
        ]
        for mapname in mods:
            if os.path.isfile(os.path.join(level.MAP_SOURCE_DIR, f'{mapname}.map')):
                maps.append(mapname)
            # Decided that although this is available in the stock launcher, ive never used it. So temp disabling it.
            # patch = f"{mapname}_patch"
            # if os.path.isfile(os.path.join(level.MAP_SOURCE_DIR, f'{patch}.map')):
            #     maps.append(patch)

        maps.sort(key=utility.custom_sort_key)
        maps.insert(0, "(not set)")
        self.main_window.ui.rgDevmapOption.addItems(maps)
    
    def populateTheRest(self):
        items = ["(not set)", "0", "1"]
        self.main_window.ui.rgCheatsOption.addItems(items)
        self.main_window.ui.rgDeveloperScriptOption.addItems(items)
        self.main_window.ui.rgIntroplayedOption.addItems(items)
        self.main_window.ui.rgShipIWDOption.addItems(items)
        self.main_window.ui.rgFullscreenOption.addItems(items)
    
        items.append("2")
        self.main_window.ui.rgDeveloperOption.addItems(items)
        self.main_window.ui.rgLogfileOption.addItems(items)
        self.main_window.ui.rgPunkBusterOption.addItems(items)

        items.extend(["3", "4", "5", "6", "7", "8", "9", "10"])
        self.main_window.ui.rgTestclientsOption.addItems(items)
    
    def updateAll(self, which, p2, widget):
        curr_selection = widget.currentText()

        if "(not set)" not in curr_selection:
            if "mods/" in p2:
                self.cmd_line[which] = f'{p2}{curr_selection}'
            else:
                self.cmd_line[which] = f'{p2} {curr_selection}'
        else:
            if which == "modOption":
                self.cmd_line[which] = "raw"
            else:
                self.cmd_line[which] = ""
        
        self.updateCommandLine()
    
    def updateCommandLine(self):
        self.main_window.ui.rgCommandLine.clear()
        _str = "+set fs_game "
        for key, value in self.cmd_line.items():
            if value != "":
                _str += f"{value} "
        self.main_window.ui.rgCommandLine.setText(_str)


class RunGameThread(QThread):
    updateConsole = Signal(str)
    disableRunGameBtn = Signal(bool)

    def __init__(self, run_game_tab:RunGameTab):
        super().__init__()
        self.run_game_tab = run_game_tab
    
    def interrupt(self):
        self.manually_killed = True

    def run(self):
        self.manually_killed = False

        # Temp disable run game btn
        self.disableRunGameBtn.emit(False)

        args = ["CoDWaW"]
        for key, value in self.run_game_tab.cmd_line.items():
            if " " in value:
                value = value.strip()

            if key == "modOption" and value != "":
                args.extend(["+set", "fs_game", value])
                continue
            elif key == "devmapOption" and value != "":
                args.extend(["+", "devmap", value.replace("+devmap", "").strip()])
                continue
            elif key == "cheatsOption" and value != "":
                args.extend(["+set", "thereisacow", value.replace("+set thereisacow", "").strip()])
                continue
            elif key == "developerOption" and value != "":
                args.extend(["+set", "developer", value.replace("+set developer", "").strip()])
                continue
            elif key == "developerScriptOption" and value != "":
                args.extend(["+set", "developer_script", value.replace("+set developer_script", "").strip()])
                continue
            elif key == "logFileOption" and value != "":
                args.extend(["+set", "logfile", value.replace("+set logfile", "").strip()])
                continue
            elif key == "introPlayedOption" and value != "":
                args.extend(["+set", "com_introplayed", value.replace("+set com_introplayed", "").strip()])
                continue
            elif key == "shipIWDOption" and value != "":
                args.extend(["+set", "sv_pure", value.replace("+set sv_pure", "").strip()])
                continue
            elif key == "fullScreenOption" and value != "":
                args.extend(["+set", "r_fullscreen", value.replace("+set r_fullscreen", "").strip()])
                continue
            elif key == "punkBusterOption" and value != "":
                args.extend(["+set", "sv_punkbuster", value.replace("+set sv_punkbuster", "").strip()])
                continue
            elif key == "testClientsOption" and value != "":
                args.extend(["+set", "scr_testclients", value.replace("+set scr_testclients", "").strip()])
                continue
        
        i = 1
        for arg in args:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} {i}: {arg}")
            i += 1

        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} run game begin")
        self.run_game_tab.main_window.ui.activeExes.addItem("WaW")

        try:
            # subprocess.Popen(args, cwd=level.ROOT_DIR, shell=True)
            process = subprocess.Popen(args, cwd=level.ROOT_DIR, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            level.SUBPROCESSES["WaW"] = ["CoDWaW", process]

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
        
        if not self.manually_killed:
            self.run_game_tab.main_window.remove_process("WaW")
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} run game complete")
        else:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")

        self.disableRunGameBtn.emit(True)
