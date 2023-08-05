########################################################################
# AUTHOR: -Phil81334
# COMMUNITY: Disorderly Manor (a.k.a Nut House)
# DESCRIPTION: WaW Launcher | Beta | Dark Mode
############################## ---/--/--- ##############################

from PySide6.QtCore import QModelIndex, QRectF, Qt, QEvent, QCoreApplication, QObject, Signal, Slot, QTimer, QPoint, QRectF, QRect, QThread
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QPalette, QIcon
from PySide6.QtWidgets import ( QApplication, QDockWidget, QMainWindow, QVBoxLayout, QLabel, QDialog, QDialogButtonBox, QSizePolicy, QScrollArea, QWidget,
                               QTreeWidget, QTreeWidgetItem, QCheckBox, QStyleFactory, QProxyStyle, QStyle, QStyleOptionViewItem, QStyledItemDelegate, QListView,
                                QMessageBox, QPushButton )

from ui_launcher import Ui_MainWindow
from mod_builder_tab import ModBuilderTab
from level_compiler_tab import LevelCompilerTab
from run_game_tab import RunGameTab

# convert .qrc to .py
# pyside6-rcc -o resources_rc.py resources.qrc

import level
import utility

import os
import sys

import subprocess
import webbrowser

# Note: json files must have at minimum: {}

class WarningDialog(QWidget):
    def __init__(self, msg, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Warning")
        self.setGeometry(350, 250, 300, 200)

        # Set an icon for the window
        icon = QIcon(os.path.join(os.getcwd(), "images\logo.png").replace('\\', '/'))
        self.setWindowIcon(icon)

        # Show a warning message box
        QMessageBox.warning(self, "Warning", msg)
        sys.exit(0)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle(f"WaW Launcher | Beta | Dark Mode | {level.ROOT_DIR}")
        self.closeEvent = self.save_before_exit

        self.mod_builder_tab = ModBuilderTab(self)
        self.level_compiler_tab = LevelCompilerTab(self)
        self.run_game_tab = RunGameTab(self)
        self.explore_tab()

        self.ui.clearConsoleBtn.clicked.connect(self.clear_console_and_args)
        self.ui.refreshModLists.clicked.connect(self.refreshModLists)

        self.ui.radiantBtn.clicked.connect(lambda: self.init_exe("Radiant", "CoDWaWRadiant", ["CoDWaWRadiant.exe"], level.BIN_DIR))
        self.ui.effectsEditorBtn.clicked.connect(lambda: self.init_exe("Effects Editor", "EffectsEd3", ["EffectsEd3.exe"], level.BIN_DIR))
        self.ui.assetManagerBtn.clicked.connect(lambda: self.init_exe("Asset Manager", "asset_manager", ["asset_manager.exe"], level.BIN_DIR))
        self.ui.assetViewerBtn.clicked.connect(lambda: self.init_exe("Asset Viewer", "AssetViewer", ["AssetViewer.exe"], level.BIN_DIR))
        self.ui.converterBtn.clicked.connect(lambda: self.init_exe("Converter", "converter", ["converter.exe"], level.BIN_DIR))
        self.ui.killExeBtn.clicked.connect(lambda: self.remove_process())

        # DM <discord>, <website>, <github org> & <youtube> hyperlink buttons
        self.ui.discordBtn.clicked.connect(lambda: self.hyperlink('https://discord.gg/jtTH2FRrhu'))
        self.ui.siteBtn.clicked.connect(lambda: self.hyperlink('https://disorderly-manor.com/'))
        self.ui.githubBtn.clicked.connect(lambda: self.hyperlink('https://github.com/Disorderly-Manor'))
        self.ui.youtubeBtn.clicked.connect(lambda: self.hyperlink('https://www.youtube.com/@Disorderly-Manor-sd9jr'))

    def copy_any_mod_files_over_to_appdata_if_not_present(self) -> None:
        dir1 = level.MOD_DIR
        dir2 = os.path.join(level.ACTIVISION_MODS_DIR, level.MOD_NAME)

        excluded_extension = ('.files', '.txt')
        files_dir1 = os.listdir(dir1)
        copied_anything = False
        for file in files_dir1:
            base_name, extension = os.path.splitext(file)
            if os.path.isfile(os.path.join(level.MOD_DIR, file)):
                if extension not in excluded_extension:
                    if not os.path.exists(os.path.join(os.path.join(level.ACTIVISION_MODS_DIR, level.MOD_NAME), file)):
                        file_path_dir1 = os.path.join(dir1, file)
                        file_path_dir2 = os.path.join(dir2, file)
                        success = utility.copy_files(file_path_dir1, file_path_dir2)
                        if success:
                            msg = f"Copying  {file_path_dir1}"
                            msg2 = f"     to  {file_path_dir2}"
                            self.ui.console.appendPlainText(msg)
                            self.ui.console.appendPlainText(msg2)
                            QApplication.processEvents()
                            copied_anything = True
        
        if copied_anything:
            self.ui.console.appendPlainText("\n############################## ---/--/--- ##############################\n")
    
    def clear_console_and_args(self):
        self.ui.console.clear()
        self.ui.exeArgs.clear()
        self.ui.consoleSuccessErrorOutput.clear()
    
    def refreshModLists(self):
        self.clear_console_and_args()
        self.mod_builder_tab.populate_folder_names()
        self.level_compiler_tab.populate_map_source_list()
        self.level_compiler_tab.populate_mod_specific_list()
        self.run_game_tab.populateModOption()
        self.run_game_tab.populateDevmapOption()

    def save_before_exit(self, event):
        self.mod_builder_tab.saveCheckedState()
        self.level_compiler_tab.saveCheckedState()
        self.save_logfile()

        if event is not None:
            event.accept()
    
    def save_logfile(self):
        with open(os.path.join(level.MOD_DIR, 'launcher_logfile.txt'), 'w+') as file:
            file.writelines('\n'.join(level.LOG))

    def explore_tab(self):
        self.ui.rootDirBtn.clicked.connect(lambda: utility.open_file_explorer(level.ROOT_DIR))
        self.ui.modsFolderDirBtn.clicked.connect(lambda: utility.open_file_explorer(level.MOD_DIR))

        self.ui.btnDirBtn.clicked.connect(lambda: utility.open_file_explorer(level.BIN_DIR))
        self.ui.mapSourceDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, 'map_source')))
        self.ui.modelExportBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, 'model_export')))
        self.ui.rawDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, 'raw')))
        self.ui.sourceDataDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, 'source_data')))
        self.ui.textureAssetsDirBnt.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, 'texture_assets')))
        self.ui.zoneSourceDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, 'zone_source')))

        self.ui.animTreesDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\animtrees')))
        self.ui.clientScriptsDir.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\clientscripts')))
        self.ui.englishStringsDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\english\localizedstrings')))
        self.ui.fxDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\fx')))
        self.ui.mapsDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\maps')))
        self.ui.soundAliasesDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\soundaliases')))
        self.ui.visionDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\vision')))
        self.ui.weaponsDirBtn.clicked.connect(lambda: utility.open_file_explorer(os.path.join(level.ROOT_DIR, r'raw\weapons')))

    def init_exe(self, which_exe_process, taskkill_process_name, exe_args, process_dir):
        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} which_exe_process: {which_exe_process}")
        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} taskkill_process_name: {taskkill_process_name}")
        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} exe_args: {exe_args}")
        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process_dir: {process_dir}")

        self.start_process(which_exe_process, taskkill_process_name, exe_args, process_dir)
    
    def start_process(self, which_exe_process, taskkill_process_name, exe_args, process_dir):
        if which_exe_process not in level.SUBPROCESSES:
            thread = StockExes(self, which_exe_process, taskkill_process_name, exe_args, process_dir)
            thread.start()
            # Store the thread to keep a reference to it
            safe_name = self.sanitize_string(which_exe_process)  # adds _ in place of whitespace
            setattr(self, f"thread_{safe_name}", thread)
    
    def sanitize_string(self, s):
        return s.replace(' ', '_')

    def remove_process(self, which:str=None) -> None:
        if which is None:
            current_item = self.ui.activeExes.currentItem()
        else:
            current_item = which

        attempt_one, attempt_two = False, False

        if current_item is not None:
            if which is None:
                current_text = current_item.text()
            else:
                current_text = which

            if which is None:  # user manually killed process

                # stock exe's
                if current_text == 'Radiant':
                    if self.thread_Radiant.isRunning():
                        self.thread_Radiant.interrupt()
                elif current_text == 'Effects Editor':
                    if self.thread_Effects_Editor.isRunning():
                        self.thread_Effects_Editor.interrupt()
                elif current_text == 'Asset Manager':
                    if self.thread_Asset_Manager.isRunning():
                        self.thread_Asset_Manager.interrupt()
                elif current_text == 'Asset Viewer':
                    if self.thread_Asset_Viewer.isRunning():
                        self.thread_Asset_Viewer.interrupt()
                elif current_text == 'Converter':
                    if self.thread_Converter.isRunning():
                        self.thread_Converter.interrupt()
                # build
                elif current_text == 'Build: Mod':
                    if self.mod_builder_tab.mod_ff_thread.isRunning():
                        self.mod_builder_tab.mod_ff_thread.interrupt()
                elif current_text == 'Build: IWD':
                    if self.mod_builder_tab.iwd_thread.isRunning():
                        self.mod_builder_tab.iwd_thread.interrupt()
                elif current_text == 'Build: Sounds':
                    if self.mod_builder_tab.build_souunds_thread.isRunning():
                        self.mod_builder_tab.build_souunds_thread.interrupt()
                # compile
                    # level
                elif current_text == 'Compile: BSP':
                    if self.mod_builder_tab.compile_level_thread.isRunning():
                        self.mod_builder_tab.compile_level_thread.interrupt('bsp')
                elif current_text == 'Compile: LIGHTS':
                    if self.mod_builder_tab.compile_level_thread.isRunning():
                        self.mod_builder_tab.compile_level_thread.interrupt('lights')
                elif current_text == 'Compile: NODES':
                    if self.mod_builder_tab.compile_level_thread.isRunning():
                        self.mod_builder_tab.compile_level_thread.interrupt('nodes')
                elif current_text == 'Compile: PROBES':
                    if self.mod_builder_tab.compile_level_thread.isRunning():
                        self.mod_builder_tab.compile_level_thread.interrupt('probes')
                elif current_text == 'Compile: FF':
                    if self.mod_builder_tab.compile_level_thread.isRunning():
                        self.mod_builder_tab.compile_level_thread.interrupt('mapname_ff')
                    # patch
                elif current_text == 'Compile: Patch':
                    if self.mod_builder_tab.compile_patch_thread.isRunning():
                        self.mod_builder_tab.compile_patch_thread.interrupt()
                # run game
                elif current_text == 'WaW':
                    if self.run_game_tab.run_game_thread.isRunning():
                        self.run_game_tab.run_game_thread.interrupt()
            
            if current_text in level.SUBPROCESSES:
                process_name, process = level.SUBPROCESSES[current_text]
                
                pid = process.pid
                try:
                    # Terminate the process using taskkill
                    subprocess.run(['taskkill', '/F', '/T', '/PID', str(pid)], capture_output=True, text=True)
                    attempt_one = True
                except subprocess.CalledProcessError as e:
                    level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
                except Exception as e:
                    level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
                
                # Wait for the process to finish
                process.wait()
                
                if process.poll() is None:
                    # If the process is still running, attempt to terminate it by the exe name
                    try:
                        subprocess.run(['taskkill', '/F', '/T', '/IM', f'{process_name}.exe'])
                        attempt_two = True
                    except subprocess.CalledProcessError as e:
                        # Handle subprocess error
                        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
                    except Exception as e:
                        # Handle any other unexpected errors
                        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")

                if any([attempt_one, attempt_two]):
                    # Remove the subprocess from the dictionary
                    level.SUBPROCESSES.pop(current_text)

                    row = None
                    if which is None:
                        row = self.ui.activeExes.row(current_item)
                    else:
                        found_item = None
                        for index in range(self.ui.activeExes.count()):
                            item = self.ui.activeExes.item(index)
                            if item.text() == which:
                                found_item = item
                                break

                        if found_item is not None:
                            row = self.ui.activeExes.row(found_item)
                       
                    if row is not None:
                        self.ui.activeExes.takeItem(row)

    def hyperlink(self, url):
        try: webbrowser.open_new(url)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Failure, Please check your internet connection")
            msg.exec()
            pass


class StockExes(QThread):
    def __init__(self, main_window, which_exe_process, taskkill_process_name, exe_args, process_dir):
        super().__init__()
        self.main_window = main_window
        self.which_exe_process = which_exe_process
        self.taskkill_process_name = taskkill_process_name
        self.exe_args = exe_args
        self.process_dir = process_dir
        self.manually_killed = False
        self.which_exe = None

    def interrupt(self):
        self.manually_killed = True

    def run(self):
        level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} {self.which_exe_process} starting")
        self.main_window.ui.activeExes.addItem(self.which_exe_process)
        try:
            process = subprocess.Popen(self.exe_args, cwd=self.process_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            level.SUBPROCESSES[self.which_exe_process] = [self.taskkill_process_name, process]
            process.communicate()
        except subprocess.CalledProcessError as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Error executing command: {e}")
        except Exception as e:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} Unexpected error: {e}")
        
        if not self.manually_killed:
            self.main_window.remove_process(self.which_exe_process)
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} {self.which_exe_process} closing")
        else:
            level.LOG.append(f"{utility.get_class_and_method_name(sys._getframe(0))} process was manually killed by user")
        
        self.main_window.save_logfile()


def exit_dialog(msg):
    app = QApplication(sys.argv)
    dialog = WarningDialog(msg)
    dialog.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        pass
    
if __name__ == "__main__":
    level.CWD = os.getcwd()

    game_dir_file_path = os.path.join(level.CWD, "game_dir.txt")
    if not os.path.exists(game_dir_file_path):
        with open(game_dir_file_path, 'w') as file:
            file.write('')  # Creates an empty file
        exit_dialog("A 'game_dir.txt' file has been created, do not delete this.\nAdd a valid waw root directory to the game_dir.txt file.")
    else:
        with open(game_dir_file_path, 'r') as file:
            dir = file.read()
        
        if dir and "Call of Duty World at War" in dir:
            level.ROOT_DIR = dir

            level.BIN_DIR = rf"{level.ROOT_DIR}\bin"
            if not os.path.exists(level.BIN_DIR):
                exit_dialog("Cannot detect the 'bin' folder.")

            level.MODS_DIR = rf"{level.ROOT_DIR}\mods"
            if not os.path.exists(level.MODS_DIR):
                exit_dialog("Cannot detect the 'mods' folder.")

            level.ACTIVISION_MODS_DIR = os.getenv('APPDATA').replace('Roaming', 'Local\Activision\CodWaW\mods')
            if not os.path.exists(level.ACTIVISION_MODS_DIR):
                exit_dialog("Cannot detect the 'activision' folder.")

            level.MAP_SOURCE_DIR = rf"{level.ROOT_DIR}\map_source"
            if not os.path.exists(level.MAP_SOURCE_DIR):
                exit_dialog("Cannot detect the 'map_source' folder.")

            app = QApplication(sys.argv)
            window = MainWindow()
            window.show()
            try:
                sys.exit(app.exec())
            except SystemExit:
                pass
        else:
            exit_dialog("Add a valid waw root directory to the game_dir.txt file.")
