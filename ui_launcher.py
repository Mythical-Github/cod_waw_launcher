# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'launcherFXFTOh.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QCommandLinkButton,
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QScrollArea, QSizePolicy, QTabWidget, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 820)
        icon = QIcon()
        icon.addFile(u":/images/images/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"/*\n"
"light: 1F1F1F\n"
"dark: 181818\n"
"*/\n"
"#centralwidget {\n"
"	background-color: #181818;\n"
"}\n"
"\n"
"#frame_7, #frame_8, #frame_9, #frame_11, #frame_12, #frame_13, #frame_14, #frame_15, #frame_16, #frame_17 {\n"
"	border: 1px solid grey;\n"
"}\n"
"\n"
"#killExeBtn {\n"
"	background-color: #F08080;\n"
"	border: 2px solid grey;\n"
"}\n"
"\n"
"#killExeBtn:hover {\n"
"	border: 2px solid blue;\n"
"}\n"
"\n"
"#activeExes, #rgCommanLine {\n"
"	background-color: lightgrey;\n"
"	border: 2px solid grey;\n"
"}\n"
"\n"
"#radiantBtn, #effectsEditorBtn, #assetManagerBtn, #assetViewerBtn, #converterBtn, #clearConsoleBtn, #refreshModLists {\n"
"	background-color: lightgrey;\n"
"	border: 1px solid white;\n"
"}\n"
"\n"
"#console, #exeArgs, #iwdTree, #modCsv, #mainSectionTabWidget, #modBuilderTab, #levelTab, #exploreTab, #consoleSuccessErrorOutput, #linksTab {\n"
"	background-color: #1F1F1F;\n"
"}\n"
"\n"
"QPushButton, QTabBar::tab {\n"
"	color: #000;\n"
"}\n"
"\n"
"#iwdTree, #modCsv, #linkFastFile, #buildIWD, #proce"
                        "ssesArea, #toolsArea, #modBuilderArea, #buildModArea, #iwdFileListArea, #modCsvArea, #console, QCheckBox, QRadioButton, #exploreArea, #wawArea, #developmentDirectoriesArea, #rawFoldersArea, #exeArgs, #rgCustomLineGrouBox, #rgModGroupBox, #rgDevmapLabel, #rgIntroplayedLabel, #rgDeveloperLabel, #rgCheatsLabel, #rgTestclientsLabel, #rgPunkBusterLabel, #rgFullscreenLabel, #rgShipIWDLabel, #rgLogfileLabel, #rgDeveloperScriptLabel, #consoleSuccessErrorOutput, #linksTabGroupBox, #discordBtn, #siteBtn, #githubBtn, #youtubeBtn {\n"
"	color: #fff;\n"
"}\n"
"\n"
"#modCsv, #console {\n"
"	font-family: Consolas, monospace;\n"
"	font-size: 11px;\n"
"}\n"
"\n"
"#compileLevelOptionsArea, #compile_mapname_list, #runGameTab, #scrollAreaWidgetContents {\n"
"	color: #fff;\n"
"	background-color: #1F1F1F;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.mainFrame = QFrame(self.centralwidget)
        self.mainFrame.setObjectName(u"mainFrame")
        self.mainFrame.setFrameShape(QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.mainFrame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.topFrame = QFrame(self.mainFrame)
        self.topFrame.setObjectName(u"topFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topFrame.sizePolicy().hasHeightForWidth())
        self.topFrame.setSizePolicy(sizePolicy)
        self.topFrame.setMinimumSize(QSize(0, 500))
        self.topFrame.setMaximumSize(QSize(16777215, 500))
        self.topFrame.setFrameShape(QFrame.StyledPanel)
        self.topFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toolsArea = QGroupBox(self.topFrame)
        self.toolsArea.setObjectName(u"toolsArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolsArea.sizePolicy().hasHeightForWidth())
        self.toolsArea.setSizePolicy(sizePolicy1)
        self.toolsArea.setMinimumSize(QSize(160, 263))
        self.toolsArea.setMaximumSize(QSize(160, 263))
        self.verticalLayout_4 = QVBoxLayout(self.toolsArea)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.radiantBtn = QPushButton(self.toolsArea)
        self.radiantBtn.setObjectName(u"radiantBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.radiantBtn.sizePolicy().hasHeightForWidth())
        self.radiantBtn.setSizePolicy(sizePolicy2)
        self.radiantBtn.setMinimumSize(QSize(0, 28))
        self.radiantBtn.setMaximumSize(QSize(150, 28))
        icon1 = QIcon()
        icon1.addFile(u":/stock_launcher_icons/icons/launcher/radiant.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.radiantBtn.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.radiantBtn)

        self.effectsEditorBtn = QPushButton(self.toolsArea)
        self.effectsEditorBtn.setObjectName(u"effectsEditorBtn")
        sizePolicy2.setHeightForWidth(self.effectsEditorBtn.sizePolicy().hasHeightForWidth())
        self.effectsEditorBtn.setSizePolicy(sizePolicy2)
        self.effectsEditorBtn.setMinimumSize(QSize(0, 28))
        self.effectsEditorBtn.setMaximumSize(QSize(150, 28))
        icon2 = QIcon()
        icon2.addFile(u":/stock_launcher_icons/icons/launcher/effects_editor.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.effectsEditorBtn.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.effectsEditorBtn)

        self.assetManagerBtn = QPushButton(self.toolsArea)
        self.assetManagerBtn.setObjectName(u"assetManagerBtn")
        sizePolicy2.setHeightForWidth(self.assetManagerBtn.sizePolicy().hasHeightForWidth())
        self.assetManagerBtn.setSizePolicy(sizePolicy2)
        self.assetManagerBtn.setMinimumSize(QSize(0, 28))
        self.assetManagerBtn.setMaximumSize(QSize(150, 28))
        icon3 = QIcon()
        icon3.addFile(u":/stock_launcher_icons/icons/launcher/asset_manager.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.assetManagerBtn.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.assetManagerBtn)

        self.assetViewerBtn = QPushButton(self.toolsArea)
        self.assetViewerBtn.setObjectName(u"assetViewerBtn")
        sizePolicy2.setHeightForWidth(self.assetViewerBtn.sizePolicy().hasHeightForWidth())
        self.assetViewerBtn.setSizePolicy(sizePolicy2)
        self.assetViewerBtn.setMinimumSize(QSize(0, 28))
        self.assetViewerBtn.setMaximumSize(QSize(150, 28))
        icon4 = QIcon()
        icon4.addFile(u":/stock_launcher_icons/icons/launcher/asset_viewer.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.assetViewerBtn.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.assetViewerBtn)

        self.converterBtn = QPushButton(self.toolsArea)
        self.converterBtn.setObjectName(u"converterBtn")
        sizePolicy2.setHeightForWidth(self.converterBtn.sizePolicy().hasHeightForWidth())
        self.converterBtn.setSizePolicy(sizePolicy2)
        self.converterBtn.setMinimumSize(QSize(0, 28))
        self.converterBtn.setMaximumSize(QSize(150, 28))
        icon5 = QIcon()
        icon5.addFile(u":/icons_black/icons/black/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.converterBtn.setIcon(icon5)

        self.verticalLayout_4.addWidget(self.converterBtn)

        self.clearConsoleBtn = QPushButton(self.toolsArea)
        self.clearConsoleBtn.setObjectName(u"clearConsoleBtn")
        sizePolicy2.setHeightForWidth(self.clearConsoleBtn.sizePolicy().hasHeightForWidth())
        self.clearConsoleBtn.setSizePolicy(sizePolicy2)
        self.clearConsoleBtn.setMinimumSize(QSize(0, 28))
        self.clearConsoleBtn.setMaximumSize(QSize(150, 28))
        icon6 = QIcon()
        icon6.addFile(u":/icons_black/icons/black/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.clearConsoleBtn.setIcon(icon6)

        self.verticalLayout_4.addWidget(self.clearConsoleBtn)

        self.refreshModLists = QPushButton(self.toolsArea)
        self.refreshModLists.setObjectName(u"refreshModLists")
        sizePolicy2.setHeightForWidth(self.refreshModLists.sizePolicy().hasHeightForWidth())
        self.refreshModLists.setSizePolicy(sizePolicy2)
        self.refreshModLists.setMinimumSize(QSize(0, 28))
        self.refreshModLists.setMaximumSize(QSize(150, 28))
        icon7 = QIcon()
        icon7.addFile(u":/icons_black/icons/black/refresh-cw.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshModLists.setIcon(icon7)

        self.verticalLayout_4.addWidget(self.refreshModLists)


        self.horizontalLayout_2.addWidget(self.toolsArea, 0, Qt.AlignTop)

        self.frame = QFrame(self.topFrame)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.mainSectionTabWidget = QTabWidget(self.frame)
        self.mainSectionTabWidget.setObjectName(u"mainSectionTabWidget")
        self.mainSectionTabWidget.setMovable(False)
        self.modBuilderTab = QWidget()
        self.modBuilderTab.setObjectName(u"modBuilderTab")
        self.horizontalLayout_5 = QHBoxLayout(self.modBuilderTab)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.modBuilderArea = QGroupBox(self.modBuilderTab)
        self.modBuilderArea.setObjectName(u"modBuilderArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.modBuilderArea.sizePolicy().hasHeightForWidth())
        self.modBuilderArea.setSizePolicy(sizePolicy3)
        self.modBuilderArea.setMinimumSize(QSize(350, 0))
        self.modBuilderArea.setMaximumSize(QSize(350, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.modBuilderArea)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.modDropDownList = QComboBox(self.modBuilderArea)
        self.modDropDownList.setObjectName(u"modDropDownList")
        self.modDropDownList.setMouseTracking(False)
        self.modDropDownList.setFocusPolicy(Qt.NoFocus)
        self.modDropDownList.setContextMenuPolicy(Qt.NoContextMenu)

        self.verticalLayout_3.addWidget(self.modDropDownList)

        self.buildModArea = QGroupBox(self.modBuilderArea)
        self.buildModArea.setObjectName(u"buildModArea")
        self.verticalLayout_6 = QVBoxLayout(self.buildModArea)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.linkFastFile = QCheckBox(self.buildModArea)
        self.linkFastFile.setObjectName(u"linkFastFile")

        self.verticalLayout_6.addWidget(self.linkFastFile)

        self.buildIWD = QCheckBox(self.buildModArea)
        self.buildIWD.setObjectName(u"buildIWD")

        self.verticalLayout_6.addWidget(self.buildIWD)

        self.BuildSoundsCheckBox = QCheckBox(self.buildModArea)
        self.BuildSoundsCheckBox.setObjectName(u"BuildSoundsCheckBox")

        self.verticalLayout_6.addWidget(self.BuildSoundsCheckBox)

        self.buildModBtn = QPushButton(self.buildModArea)
        self.buildModBtn.setObjectName(u"buildModBtn")

        self.verticalLayout_6.addWidget(self.buildModBtn)


        self.verticalLayout_3.addWidget(self.buildModArea, 0, Qt.AlignTop)

        self.modCsvArea = QGroupBox(self.modBuilderArea)
        self.modCsvArea.setObjectName(u"modCsvArea")
        self.verticalLayout_8 = QVBoxLayout(self.modCsvArea)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.modCsv = QPlainTextEdit(self.modCsvArea)
        self.modCsv.setObjectName(u"modCsv")
        self.modCsv.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.verticalLayout_8.addWidget(self.modCsv)


        self.verticalLayout_3.addWidget(self.modCsvArea)


        self.horizontalLayout_5.addWidget(self.modBuilderArea)

        self.iwdFileListArea = QGroupBox(self.modBuilderTab)
        self.iwdFileListArea.setObjectName(u"iwdFileListArea")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.iwdFileListArea.sizePolicy().hasHeightForWidth())
        self.iwdFileListArea.setSizePolicy(sizePolicy4)
        self.horizontalLayout_6 = QHBoxLayout(self.iwdFileListArea)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.iwdTree = QTreeWidget(self.iwdFileListArea)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.iwdTree.setHeaderItem(__qtreewidgetitem)
        self.iwdTree.setObjectName(u"iwdTree")

        self.horizontalLayout_6.addWidget(self.iwdTree)


        self.horizontalLayout_5.addWidget(self.iwdFileListArea)

        self.mainSectionTabWidget.addTab(self.modBuilderTab, "")
        self.levelTab = QWidget()
        self.levelTab.setObjectName(u"levelTab")
        self.horizontalLayout_4 = QHBoxLayout(self.levelTab)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.compile_mapname_list = QListWidget(self.levelTab)
        self.compile_mapname_list.setObjectName(u"compile_mapname_list")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.compile_mapname_list.sizePolicy().hasHeightForWidth())
        self.compile_mapname_list.setSizePolicy(sizePolicy5)

        self.horizontalLayout_4.addWidget(self.compile_mapname_list)

        self.compileLevelOptionsArea = QGroupBox(self.levelTab)
        self.compileLevelOptionsArea.setObjectName(u"compileLevelOptionsArea")
        self.verticalLayout_9 = QVBoxLayout(self.compileLevelOptionsArea)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.CLO_Frame_3 = QFrame(self.compileLevelOptionsArea)
        self.CLO_Frame_3.setObjectName(u"CLO_Frame_3")
        sizePolicy2.setHeightForWidth(self.CLO_Frame_3.sizePolicy().hasHeightForWidth())
        self.CLO_Frame_3.setSizePolicy(sizePolicy2)
        self.CLO_Frame_3.setFrameShape(QFrame.StyledPanel)
        self.CLO_Frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.CLO_Frame_3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 6)
        self.CLO_Frame_6 = QFrame(self.CLO_Frame_3)
        self.CLO_Frame_6.setObjectName(u"CLO_Frame_6")
        sizePolicy1.setHeightForWidth(self.CLO_Frame_6.sizePolicy().hasHeightForWidth())
        self.CLO_Frame_6.setSizePolicy(sizePolicy1)
        self.CLO_Frame_6.setFrameShape(QFrame.StyledPanel)
        self.CLO_Frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.CLO_Frame_6)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(6, 0, 0, 0)
        self.CLO_Frame_8 = QFrame(self.CLO_Frame_6)
        self.CLO_Frame_8.setObjectName(u"CLO_Frame_8")
        sizePolicy1.setHeightForWidth(self.CLO_Frame_8.sizePolicy().hasHeightForWidth())
        self.CLO_Frame_8.setSizePolicy(sizePolicy1)
        self.CLO_Frame_8.setFrameShape(QFrame.StyledPanel)
        self.CLO_Frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.CLO_Frame_8)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.compileBspCheckbox = QCheckBox(self.CLO_Frame_8)
        self.compileBspCheckbox.setObjectName(u"compileBspCheckbox")
        sizePolicy1.setHeightForWidth(self.compileBspCheckbox.sizePolicy().hasHeightForWidth())
        self.compileBspCheckbox.setSizePolicy(sizePolicy1)
        self.compileBspCheckbox.setMinimumSize(QSize(135, 0))
        self.compileBspCheckbox.setMaximumSize(QSize(135, 16777215))
        self.compileBspCheckbox.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.compileBspCheckbox)

        self.line_4 = QFrame(self.CLO_Frame_8)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_10.addWidget(self.line_4)

        self.onlyEntsCheckbox = QCheckBox(self.CLO_Frame_8)
        self.onlyEntsCheckbox.setObjectName(u"onlyEntsCheckbox")
        sizePolicy1.setHeightForWidth(self.onlyEntsCheckbox.sizePolicy().hasHeightForWidth())
        self.onlyEntsCheckbox.setSizePolicy(sizePolicy1)
        self.onlyEntsCheckbox.setMinimumSize(QSize(75, 0))
        self.onlyEntsCheckbox.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_10.addWidget(self.onlyEntsCheckbox)


        self.verticalLayout_11.addWidget(self.CLO_Frame_8)

        self.CLO_Frame_9 = QFrame(self.CLO_Frame_6)
        self.CLO_Frame_9.setObjectName(u"CLO_Frame_9")
        sizePolicy1.setHeightForWidth(self.CLO_Frame_9.sizePolicy().hasHeightForWidth())
        self.CLO_Frame_9.setSizePolicy(sizePolicy1)
        self.CLO_Frame_9.setFrameShape(QFrame.StyledPanel)
        self.CLO_Frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.CLO_Frame_9)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.compileLightsCheckbox = QCheckBox(self.CLO_Frame_9)
        self.compileLightsCheckbox.setObjectName(u"compileLightsCheckbox")
        sizePolicy1.setHeightForWidth(self.compileLightsCheckbox.sizePolicy().hasHeightForWidth())
        self.compileLightsCheckbox.setSizePolicy(sizePolicy1)
        self.compileLightsCheckbox.setMinimumSize(QSize(135, 0))
        self.compileLightsCheckbox.setMaximumSize(QSize(135, 16777215))

        self.horizontalLayout_8.addWidget(self.compileLightsCheckbox)

        self.line = QFrame(self.CLO_Frame_9)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line)

        self.compileLightsFastCheckbox = QRadioButton(self.CLO_Frame_9)
        self.compileLightsFastCheckbox.setObjectName(u"compileLightsFastCheckbox")
        sizePolicy1.setHeightForWidth(self.compileLightsFastCheckbox.sizePolicy().hasHeightForWidth())
        self.compileLightsFastCheckbox.setSizePolicy(sizePolicy1)
        self.compileLightsFastCheckbox.setMinimumSize(QSize(75, 0))
        self.compileLightsFastCheckbox.setMaximumSize(QSize(75, 16777215))
        self.compileLightsFastCheckbox.setChecked(True)

        self.horizontalLayout_8.addWidget(self.compileLightsFastCheckbox)

        self.line_2 = QFrame(self.CLO_Frame_9)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_8.addWidget(self.line_2)

        self.compileLightsExtraCheckbox = QRadioButton(self.CLO_Frame_9)
        self.compileLightsExtraCheckbox.setObjectName(u"compileLightsExtraCheckbox")
        sizePolicy1.setHeightForWidth(self.compileLightsExtraCheckbox.sizePolicy().hasHeightForWidth())
        self.compileLightsExtraCheckbox.setSizePolicy(sizePolicy1)
        self.compileLightsExtraCheckbox.setMinimumSize(QSize(75, 0))
        self.compileLightsExtraCheckbox.setMaximumSize(QSize(75, 16777215))

        self.horizontalLayout_8.addWidget(self.compileLightsExtraCheckbox)


        self.verticalLayout_11.addWidget(self.CLO_Frame_9)


        self.horizontalLayout_9.addWidget(self.CLO_Frame_6)

        self.CLO_Frame_7 = QFrame(self.CLO_Frame_3)
        self.CLO_Frame_7.setObjectName(u"CLO_Frame_7")
        sizePolicy2.setHeightForWidth(self.CLO_Frame_7.sizePolicy().hasHeightForWidth())
        self.CLO_Frame_7.setSizePolicy(sizePolicy2)
        self.CLO_Frame_7.setFrameShape(QFrame.StyledPanel)
        self.CLO_Frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.CLO_Frame_7)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 8, 0)
        self.frame_10 = QFrame(self.CLO_Frame_7)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.modSpecificMapCheckbox = QCheckBox(self.frame_10)
        self.modSpecificMapCheckbox.setObjectName(u"modSpecificMapCheckbox")
        sizePolicy1.setHeightForWidth(self.modSpecificMapCheckbox.sizePolicy().hasHeightForWidth())
        self.modSpecificMapCheckbox.setSizePolicy(sizePolicy1)
        self.modSpecificMapCheckbox.setMinimumSize(QSize(135, 0))
        self.modSpecificMapCheckbox.setMaximumSize(QSize(135, 16777215))

        self.horizontalLayout_11.addWidget(self.modSpecificMapCheckbox)


        self.verticalLayout_12.addWidget(self.frame_10)

        self.modSpecificMapList = QComboBox(self.CLO_Frame_7)
        self.modSpecificMapList.setObjectName(u"modSpecificMapList")
        sizePolicy2.setHeightForWidth(self.modSpecificMapList.sizePolicy().hasHeightForWidth())
        self.modSpecificMapList.setSizePolicy(sizePolicy2)

        self.verticalLayout_12.addWidget(self.modSpecificMapList)


        self.horizontalLayout_9.addWidget(self.CLO_Frame_7)


        self.verticalLayout_9.addWidget(self.CLO_Frame_3)

        self.line_5 = QFrame(self.compileLevelOptionsArea)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setMinimumSize(QSize(0, 0))
        self.line_5.setStyleSheet(u"#line_5 {margin: 10;}")
        self.line_5.setMidLineWidth(0)
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.line_5)

        self.CLO_Frame_4 = QFrame(self.compileLevelOptionsArea)
        self.CLO_Frame_4.setObjectName(u"CLO_Frame_4")
        sizePolicy1.setHeightForWidth(self.CLO_Frame_4.sizePolicy().hasHeightForWidth())
        self.CLO_Frame_4.setSizePolicy(sizePolicy1)
        self.CLO_Frame_4.setFrameShape(QFrame.StyledPanel)
        self.CLO_Frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.CLO_Frame_4)
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(8, 6, 0, 0)
        self.connectPathsCheckbox = QCheckBox(self.CLO_Frame_4)
        self.connectPathsCheckbox.setObjectName(u"connectPathsCheckbox")
        sizePolicy1.setHeightForWidth(self.connectPathsCheckbox.sizePolicy().hasHeightForWidth())
        self.connectPathsCheckbox.setSizePolicy(sizePolicy1)
        self.connectPathsCheckbox.setMinimumSize(QSize(135, 0))
        self.connectPathsCheckbox.setMaximumSize(QSize(135, 16777215))

        self.verticalLayout_10.addWidget(self.connectPathsCheckbox)

        self.compileReflectionsCheckbox = QCheckBox(self.CLO_Frame_4)
        self.compileReflectionsCheckbox.setObjectName(u"compileReflectionsCheckbox")
        sizePolicy1.setHeightForWidth(self.compileReflectionsCheckbox.sizePolicy().hasHeightForWidth())
        self.compileReflectionsCheckbox.setSizePolicy(sizePolicy1)
        self.compileReflectionsCheckbox.setMinimumSize(QSize(135, 0))
        self.compileReflectionsCheckbox.setMaximumSize(QSize(135, 16777215))

        self.verticalLayout_10.addWidget(self.compileReflectionsCheckbox)

        self.buildLevelFastfilesCheckbox = QCheckBox(self.CLO_Frame_4)
        self.buildLevelFastfilesCheckbox.setObjectName(u"buildLevelFastfilesCheckbox")
        sizePolicy1.setHeightForWidth(self.buildLevelFastfilesCheckbox.sizePolicy().hasHeightForWidth())
        self.buildLevelFastfilesCheckbox.setSizePolicy(sizePolicy1)
        self.buildLevelFastfilesCheckbox.setMinimumSize(QSize(135, 0))
        self.buildLevelFastfilesCheckbox.setMaximumSize(QSize(135, 16777215))

        self.verticalLayout_10.addWidget(self.buildLevelFastfilesCheckbox)


        self.verticalLayout_9.addWidget(self.CLO_Frame_4)

        self.CLO_Frame_5 = QFrame(self.compileLevelOptionsArea)
        self.CLO_Frame_5.setObjectName(u"CLO_Frame_5")
        sizePolicy1.setHeightForWidth(self.CLO_Frame_5.sizePolicy().hasHeightForWidth())
        self.CLO_Frame_5.setSizePolicy(sizePolicy1)
        self.CLO_Frame_5.setFrameShape(QFrame.StyledPanel)
        self.CLO_Frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.CLO_Frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 8, 9)
        self.compileLevelBtn = QPushButton(self.CLO_Frame_5)
        self.compileLevelBtn.setObjectName(u"compileLevelBtn")
        sizePolicy1.setHeightForWidth(self.compileLevelBtn.sizePolicy().hasHeightForWidth())
        self.compileLevelBtn.setSizePolicy(sizePolicy1)
        self.compileLevelBtn.setMinimumSize(QSize(150, 100))
        self.compileLevelBtn.setMaximumSize(QSize(150, 100))

        self.horizontalLayout_7.addWidget(self.compileLevelBtn)


        self.verticalLayout_9.addWidget(self.CLO_Frame_5, 0, Qt.AlignRight|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.compileLevelOptionsArea)

        self.mainSectionTabWidget.addTab(self.levelTab, "")
        self.exploreTab = QWidget()
        self.exploreTab.setObjectName(u"exploreTab")
        self.horizontalLayout_12 = QHBoxLayout(self.exploreTab)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.exploreArea = QGroupBox(self.exploreTab)
        self.exploreArea.setObjectName(u"exploreArea")
        self.horizontalLayout_13 = QHBoxLayout(self.exploreArea)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.wawArea = QGroupBox(self.exploreArea)
        self.wawArea.setObjectName(u"wawArea")
        self.verticalLayout_13 = QVBoxLayout(self.wawArea)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.rootDirBtn = QPushButton(self.wawArea)
        self.rootDirBtn.setObjectName(u"rootDirBtn")

        self.verticalLayout_13.addWidget(self.rootDirBtn)

        self.modsFolderDirBtn = QPushButton(self.wawArea)
        self.modsFolderDirBtn.setObjectName(u"modsFolderDirBtn")

        self.verticalLayout_13.addWidget(self.modsFolderDirBtn)


        self.horizontalLayout_13.addWidget(self.wawArea, 0, Qt.AlignTop)

        self.developmentDirectoriesArea = QGroupBox(self.exploreArea)
        self.developmentDirectoriesArea.setObjectName(u"developmentDirectoriesArea")
        self.verticalLayout_14 = QVBoxLayout(self.developmentDirectoriesArea)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.btnDirBtn = QPushButton(self.developmentDirectoriesArea)
        self.btnDirBtn.setObjectName(u"btnDirBtn")

        self.verticalLayout_14.addWidget(self.btnDirBtn)

        self.mapSourceDirBtn = QPushButton(self.developmentDirectoriesArea)
        self.mapSourceDirBtn.setObjectName(u"mapSourceDirBtn")

        self.verticalLayout_14.addWidget(self.mapSourceDirBtn)

        self.modelExportBtn = QPushButton(self.developmentDirectoriesArea)
        self.modelExportBtn.setObjectName(u"modelExportBtn")

        self.verticalLayout_14.addWidget(self.modelExportBtn)

        self.rawDirBtn = QPushButton(self.developmentDirectoriesArea)
        self.rawDirBtn.setObjectName(u"rawDirBtn")

        self.verticalLayout_14.addWidget(self.rawDirBtn)

        self.sourceDataDirBtn = QPushButton(self.developmentDirectoriesArea)
        self.sourceDataDirBtn.setObjectName(u"sourceDataDirBtn")

        self.verticalLayout_14.addWidget(self.sourceDataDirBtn)

        self.textureAssetsDirBnt = QPushButton(self.developmentDirectoriesArea)
        self.textureAssetsDirBnt.setObjectName(u"textureAssetsDirBnt")

        self.verticalLayout_14.addWidget(self.textureAssetsDirBnt)

        self.zoneSourceDirBtn = QPushButton(self.developmentDirectoriesArea)
        self.zoneSourceDirBtn.setObjectName(u"zoneSourceDirBtn")

        self.verticalLayout_14.addWidget(self.zoneSourceDirBtn)


        self.horizontalLayout_13.addWidget(self.developmentDirectoriesArea, 0, Qt.AlignTop)

        self.rawFoldersArea = QGroupBox(self.exploreArea)
        self.rawFoldersArea.setObjectName(u"rawFoldersArea")
        self.verticalLayout_15 = QVBoxLayout(self.rawFoldersArea)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.animTreesDirBtn = QPushButton(self.rawFoldersArea)
        self.animTreesDirBtn.setObjectName(u"animTreesDirBtn")

        self.verticalLayout_15.addWidget(self.animTreesDirBtn)

        self.clientScriptsDir = QPushButton(self.rawFoldersArea)
        self.clientScriptsDir.setObjectName(u"clientScriptsDir")

        self.verticalLayout_15.addWidget(self.clientScriptsDir)

        self.englishStringsDirBtn = QPushButton(self.rawFoldersArea)
        self.englishStringsDirBtn.setObjectName(u"englishStringsDirBtn")

        self.verticalLayout_15.addWidget(self.englishStringsDirBtn)

        self.fxDirBtn = QPushButton(self.rawFoldersArea)
        self.fxDirBtn.setObjectName(u"fxDirBtn")

        self.verticalLayout_15.addWidget(self.fxDirBtn)

        self.mapsDirBtn = QPushButton(self.rawFoldersArea)
        self.mapsDirBtn.setObjectName(u"mapsDirBtn")

        self.verticalLayout_15.addWidget(self.mapsDirBtn)

        self.soundAliasesDirBtn = QPushButton(self.rawFoldersArea)
        self.soundAliasesDirBtn.setObjectName(u"soundAliasesDirBtn")

        self.verticalLayout_15.addWidget(self.soundAliasesDirBtn)

        self.visionDirBtn = QPushButton(self.rawFoldersArea)
        self.visionDirBtn.setObjectName(u"visionDirBtn")

        self.verticalLayout_15.addWidget(self.visionDirBtn)

        self.weaponsDirBtn = QPushButton(self.rawFoldersArea)
        self.weaponsDirBtn.setObjectName(u"weaponsDirBtn")

        self.verticalLayout_15.addWidget(self.weaponsDirBtn)


        self.horizontalLayout_13.addWidget(self.rawFoldersArea, 0, Qt.AlignTop)


        self.horizontalLayout_12.addWidget(self.exploreArea)

        self.mainSectionTabWidget.addTab(self.exploreTab, "")
        self.runGameTab = QWidget()
        self.runGameTab.setObjectName(u"runGameTab")
        self.horizontalLayout_14 = QHBoxLayout(self.runGameTab)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.frame_3 = QFrame(self.runGameTab)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.rgModGroupBox = QGroupBox(self.frame_4)
        self.rgModGroupBox.setObjectName(u"rgModGroupBox")
        self.horizontalLayout_18 = QHBoxLayout(self.rgModGroupBox)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.rgSelectModOption = QComboBox(self.rgModGroupBox)
        self.rgSelectModOption.setObjectName(u"rgSelectModOption")

        self.horizontalLayout_18.addWidget(self.rgSelectModOption)


        self.horizontalLayout_17.addWidget(self.rgModGroupBox)


        self.verticalLayout_16.addWidget(self.frame_4)

        self.rgArgsOptionsFrame = QFrame(self.frame_3)
        self.rgArgsOptionsFrame.setObjectName(u"rgArgsOptionsFrame")
        self.rgArgsOptionsFrame.setMinimumSize(QSize(0, 0))
        self.rgArgsOptionsFrame.setFrameShape(QFrame.StyledPanel)
        self.rgArgsOptionsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.rgArgsOptionsFrame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.rgScrollArea = QScrollArea(self.rgArgsOptionsFrame)
        self.rgScrollArea.setObjectName(u"rgScrollArea")
        self.rgScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 870, 312))
        self.scrollAreaWidgetContents.setMinimumSize(QSize(0, 0))
        self.verticalLayout_17 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_7 = QFrame(self.scrollAreaWidgetContents)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(6, 0, 0, 0)
        self.rgDevmapLabel = QLabel(self.frame_7)
        self.rgDevmapLabel.setObjectName(u"rgDevmapLabel")

        self.horizontalLayout_19.addWidget(self.rgDevmapLabel)

        self.rgDevmapOption = QComboBox(self.frame_7)
        self.rgDevmapOption.setObjectName(u"rgDevmapOption")
        self.rgDevmapOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_19.addWidget(self.rgDevmapOption)


        self.verticalLayout_17.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.scrollAreaWidgetContents)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(6, 0, 0, 0)
        self.rgCheatsLabel = QLabel(self.frame_8)
        self.rgCheatsLabel.setObjectName(u"rgCheatsLabel")

        self.horizontalLayout_20.addWidget(self.rgCheatsLabel)

        self.rgCheatsOption = QComboBox(self.frame_8)
        self.rgCheatsOption.setObjectName(u"rgCheatsOption")
        self.rgCheatsOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_20.addWidget(self.rgCheatsOption)


        self.verticalLayout_17.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.scrollAreaWidgetContents)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(6, 0, 0, 0)
        self.rgDeveloperLabel = QLabel(self.frame_9)
        self.rgDeveloperLabel.setObjectName(u"rgDeveloperLabel")

        self.horizontalLayout_21.addWidget(self.rgDeveloperLabel)

        self.rgDeveloperOption = QComboBox(self.frame_9)
        self.rgDeveloperOption.setObjectName(u"rgDeveloperOption")
        self.rgDeveloperOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_21.addWidget(self.rgDeveloperOption)


        self.verticalLayout_17.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.scrollAreaWidgetContents)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(6, 0, 0, 0)
        self.rgDeveloperScriptLabel = QLabel(self.frame_11)
        self.rgDeveloperScriptLabel.setObjectName(u"rgDeveloperScriptLabel")

        self.horizontalLayout_22.addWidget(self.rgDeveloperScriptLabel)

        self.rgDeveloperScriptOption = QComboBox(self.frame_11)
        self.rgDeveloperScriptOption.setObjectName(u"rgDeveloperScriptOption")
        self.rgDeveloperScriptOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_22.addWidget(self.rgDeveloperScriptOption)


        self.verticalLayout_17.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(6, 0, 0, 0)
        self.rgLogfileLabel = QLabel(self.frame_12)
        self.rgLogfileLabel.setObjectName(u"rgLogfileLabel")

        self.horizontalLayout_23.addWidget(self.rgLogfileLabel)

        self.rgLogfileOption = QComboBox(self.frame_12)
        self.rgLogfileOption.setObjectName(u"rgLogfileOption")
        self.rgLogfileOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_23.addWidget(self.rgLogfileOption)


        self.verticalLayout_17.addWidget(self.frame_12)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(6, 0, 0, 0)
        self.rgIntroplayedLabel = QLabel(self.frame_17)
        self.rgIntroplayedLabel.setObjectName(u"rgIntroplayedLabel")

        self.horizontalLayout_28.addWidget(self.rgIntroplayedLabel)

        self.rgIntroplayedOption = QComboBox(self.frame_17)
        self.rgIntroplayedOption.setObjectName(u"rgIntroplayedOption")
        self.rgIntroplayedOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_28.addWidget(self.rgIntroplayedOption)


        self.verticalLayout_17.addWidget(self.frame_17)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(6, 0, 0, 0)
        self.rgShipIWDLabel = QLabel(self.frame_13)
        self.rgShipIWDLabel.setObjectName(u"rgShipIWDLabel")

        self.horizontalLayout_24.addWidget(self.rgShipIWDLabel)

        self.rgShipIWDOption = QComboBox(self.frame_13)
        self.rgShipIWDOption.setObjectName(u"rgShipIWDOption")
        self.rgShipIWDOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_24.addWidget(self.rgShipIWDOption)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(6, 0, 0, 0)
        self.rgFullscreenLabel = QLabel(self.frame_14)
        self.rgFullscreenLabel.setObjectName(u"rgFullscreenLabel")

        self.horizontalLayout_25.addWidget(self.rgFullscreenLabel)

        self.rgFullscreenOption = QComboBox(self.frame_14)
        self.rgFullscreenOption.setObjectName(u"rgFullscreenOption")
        self.rgFullscreenOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_25.addWidget(self.rgFullscreenOption)


        self.verticalLayout_17.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(6, 0, 0, 0)
        self.rgPunkBusterLabel = QLabel(self.frame_15)
        self.rgPunkBusterLabel.setObjectName(u"rgPunkBusterLabel")

        self.horizontalLayout_26.addWidget(self.rgPunkBusterLabel)

        self.rgPunkBusterOption = QComboBox(self.frame_15)
        self.rgPunkBusterOption.setObjectName(u"rgPunkBusterOption")
        self.rgPunkBusterOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_26.addWidget(self.rgPunkBusterOption)


        self.verticalLayout_17.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(6, 0, 0, 0)
        self.rgTestclientsLabel = QLabel(self.frame_16)
        self.rgTestclientsLabel.setObjectName(u"rgTestclientsLabel")

        self.horizontalLayout_27.addWidget(self.rgTestclientsLabel)

        self.rgTestclientsOption = QComboBox(self.frame_16)
        self.rgTestclientsOption.setObjectName(u"rgTestclientsOption")
        self.rgTestclientsOption.setMaximumSize(QSize(350, 16777215))

        self.horizontalLayout_27.addWidget(self.rgTestclientsOption)


        self.verticalLayout_17.addWidget(self.frame_16)

        self.rgScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_16.addWidget(self.rgScrollArea)


        self.verticalLayout_16.addWidget(self.rgArgsOptionsFrame)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.rgCustomLineGrouBox = QGroupBox(self.frame_6)
        self.rgCustomLineGrouBox.setObjectName(u"rgCustomLineGrouBox")
        self.horizontalLayout_29 = QHBoxLayout(self.rgCustomLineGrouBox)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.rgCommandLine = QLineEdit(self.rgCustomLineGrouBox)
        self.rgCommandLine.setObjectName(u"rgCommandLine")
        self.rgCommandLine.setReadOnly(True)

        self.horizontalLayout_29.addWidget(self.rgCommandLine)


        self.horizontalLayout_15.addWidget(self.rgCustomLineGrouBox, 0, Qt.AlignBottom)

        self.runGameBtn = QPushButton(self.frame_6)
        self.runGameBtn.setObjectName(u"runGameBtn")
        sizePolicy1.setHeightForWidth(self.runGameBtn.sizePolicy().hasHeightForWidth())
        self.runGameBtn.setSizePolicy(sizePolicy1)
        self.runGameBtn.setMinimumSize(QSize(150, 100))
        self.runGameBtn.setMaximumSize(QSize(150, 100))

        self.horizontalLayout_15.addWidget(self.runGameBtn)


        self.verticalLayout_16.addWidget(self.frame_6)


        self.horizontalLayout_14.addWidget(self.frame_3)

        self.mainSectionTabWidget.addTab(self.runGameTab, "")
        self.linksTab = QWidget()
        self.linksTab.setObjectName(u"linksTab")
        self.horizontalLayout_31 = QHBoxLayout(self.linksTab)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.linksTabGroupBox = QGroupBox(self.linksTab)
        self.linksTabGroupBox.setObjectName(u"linksTabGroupBox")
        self.horizontalLayout_32 = QHBoxLayout(self.linksTabGroupBox)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_18 = QFrame(self.linksTabGroupBox)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_19)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.discordBtn = QCommandLinkButton(self.frame_19)
        self.discordBtn.setObjectName(u"discordBtn")

        self.verticalLayout_18.addWidget(self.discordBtn)

        self.siteBtn = QCommandLinkButton(self.frame_19)
        self.siteBtn.setObjectName(u"siteBtn")

        self.verticalLayout_18.addWidget(self.siteBtn)

        self.githubBtn = QCommandLinkButton(self.frame_19)
        self.githubBtn.setObjectName(u"githubBtn")

        self.verticalLayout_18.addWidget(self.githubBtn)

        self.youtubeBtn = QCommandLinkButton(self.frame_19)
        self.youtubeBtn.setObjectName(u"youtubeBtn")

        self.verticalLayout_18.addWidget(self.youtubeBtn)


        self.horizontalLayout_33.addWidget(self.frame_19, 0, Qt.AlignLeft|Qt.AlignTop)


        self.horizontalLayout_32.addWidget(self.frame_18)


        self.horizontalLayout_31.addWidget(self.linksTabGroupBox)

        self.mainSectionTabWidget.addTab(self.linksTab, "")

        self.verticalLayout_2.addWidget(self.mainSectionTabWidget)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.exeArgs = QLineEdit(self.frame_5)
        self.exeArgs.setObjectName(u"exeArgs")
        self.exeArgs.setMinimumSize(QSize(0, 30))
        self.exeArgs.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.exeArgs)

        self.consoleSuccessErrorOutput = QLineEdit(self.frame_5)
        self.consoleSuccessErrorOutput.setObjectName(u"consoleSuccessErrorOutput")
        self.consoleSuccessErrorOutput.setMinimumSize(QSize(0, 30))
        self.consoleSuccessErrorOutput.setMaximumSize(QSize(100, 16777215))
        self.consoleSuccessErrorOutput.setReadOnly(True)

        self.horizontalLayout_30.addWidget(self.consoleSuccessErrorOutput)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.topFrame)

        self.bottomFrame = QFrame(self.mainFrame)
        self.bottomFrame.setObjectName(u"bottomFrame")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.bottomFrame.sizePolicy().hasHeightForWidth())
        self.bottomFrame.setSizePolicy(sizePolicy6)
        self.bottomFrame.setMinimumSize(QSize(0, 300))
        self.bottomFrame.setFrameShape(QFrame.StyledPanel)
        self.bottomFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.bottomFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.processesArea = QGroupBox(self.bottomFrame)
        self.processesArea.setObjectName(u"processesArea")
        sizePolicy5.setHeightForWidth(self.processesArea.sizePolicy().hasHeightForWidth())
        self.processesArea.setSizePolicy(sizePolicy5)
        self.processesArea.setMinimumSize(QSize(160, 0))
        self.processesArea.setMaximumSize(QSize(160, 16777215))
        self.verticalLayout_5 = QVBoxLayout(self.processesArea)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(6, 6, 6, 6)
        self.activeExes = QListWidget(self.processesArea)
        self.activeExes.setObjectName(u"activeExes")
        sizePolicy5.setHeightForWidth(self.activeExes.sizePolicy().hasHeightForWidth())
        self.activeExes.setSizePolicy(sizePolicy5)
        self.activeExes.setMinimumSize(QSize(0, 0))
        self.activeExes.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_5.addWidget(self.activeExes)

        self.killExeBtn = QPushButton(self.processesArea)
        self.killExeBtn.setObjectName(u"killExeBtn")
        sizePolicy2.setHeightForWidth(self.killExeBtn.sizePolicy().hasHeightForWidth())
        self.killExeBtn.setSizePolicy(sizePolicy2)
        self.killExeBtn.setMinimumSize(QSize(0, 80))
        self.killExeBtn.setMaximumSize(QSize(16777215, 80))
        self.killExeBtn.setFlat(False)

        self.verticalLayout_5.addWidget(self.killExeBtn)


        self.horizontalLayout_3.addWidget(self.processesArea)

        self.frame_2 = QFrame(self.bottomFrame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 6, 0, 0)
        self.console = QPlainTextEdit(self.frame_2)
        self.console.setObjectName(u"console")
        self.console.setMinimumSize(QSize(0, 0))
        self.console.setMaximumSize(QSize(16777215, 16777215))
        self.console.setReadOnly(True)

        self.verticalLayout_7.addWidget(self.console)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.bottomFrame)


        self.horizontalLayout.addWidget(self.mainFrame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainSectionTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"WaW Launcher (Dark Mode)", None))
        self.toolsArea.setTitle(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.radiantBtn.setText(QCoreApplication.translate("MainWindow", u"Radiant", None))
        self.effectsEditorBtn.setText(QCoreApplication.translate("MainWindow", u"Effects Editor", None))
        self.assetManagerBtn.setText(QCoreApplication.translate("MainWindow", u"Asset Manager", None))
        self.assetViewerBtn.setText(QCoreApplication.translate("MainWindow", u"Asset Viewer", None))
        self.converterBtn.setText(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.clearConsoleBtn.setText(QCoreApplication.translate("MainWindow", u"Clear Console", None))
        self.refreshModLists.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.modBuilderArea.setTitle(QCoreApplication.translate("MainWindow", u"Mod", None))
        self.buildModArea.setTitle(QCoreApplication.translate("MainWindow", u"Build Mod", None))
        self.linkFastFile.setText(QCoreApplication.translate("MainWindow", u"Link Fast File", None))
        self.buildIWD.setText(QCoreApplication.translate("MainWindow", u"Build IWD", None))
        self.BuildSoundsCheckBox.setText(QCoreApplication.translate("MainWindow", u"Build Sounds", None))
        self.buildModBtn.setText(QCoreApplication.translate("MainWindow", u"Build Mod", None))
        self.modCsvArea.setTitle(QCoreApplication.translate("MainWindow", u"Fastfile mod.csv", None))
        self.iwdFileListArea.setTitle(QCoreApplication.translate("MainWindow", u"IWD File List", None))
        self.mainSectionTabWidget.setTabText(self.mainSectionTabWidget.indexOf(self.modBuilderTab), QCoreApplication.translate("MainWindow", u"Mod Builder", None))
        self.compileLevelOptionsArea.setTitle(QCoreApplication.translate("MainWindow", u"Compile Level Options", None))
        self.compileBspCheckbox.setText(QCoreApplication.translate("MainWindow", u"Compile BSP", None))
        self.onlyEntsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Only Ents", None))
        self.compileLightsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Compile Lights", None))
        self.compileLightsFastCheckbox.setText(QCoreApplication.translate("MainWindow", u"Fast", None))
        self.compileLightsExtraCheckbox.setText(QCoreApplication.translate("MainWindow", u"Extra", None))
        self.modSpecificMapCheckbox.setText(QCoreApplication.translate("MainWindow", u"Mod Specific Map", None))
        self.connectPathsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Connect Paths", None))
        self.compileReflectionsCheckbox.setText(QCoreApplication.translate("MainWindow", u"Compile Reflections", None))
        self.buildLevelFastfilesCheckbox.setText(QCoreApplication.translate("MainWindow", u"Build Fastfiles", None))
        self.compileLevelBtn.setText(QCoreApplication.translate("MainWindow", u"Compile Level", None))
        self.mainSectionTabWidget.setTabText(self.mainSectionTabWidget.indexOf(self.levelTab), QCoreApplication.translate("MainWindow", u"Level", None))
        self.exploreArea.setTitle(QCoreApplication.translate("MainWindow", u"Explore", None))
        self.wawArea.setTitle(QCoreApplication.translate("MainWindow", u"Call of Duty: World at War", None))
        self.rootDirBtn.setText(QCoreApplication.translate("MainWindow", u"Game Directory", None))
        self.modsFolderDirBtn.setText(QCoreApplication.translate("MainWindow", u"Mods Folder", None))
        self.developmentDirectoriesArea.setTitle(QCoreApplication.translate("MainWindow", u"Development Directories", None))
        self.btnDirBtn.setText(QCoreApplication.translate("MainWindow", u"Bin", None))
        self.mapSourceDirBtn.setText(QCoreApplication.translate("MainWindow", u"Map Source", None))
        self.modelExportBtn.setText(QCoreApplication.translate("MainWindow", u"Model Export", None))
        self.rawDirBtn.setText(QCoreApplication.translate("MainWindow", u"Raw", None))
        self.sourceDataDirBtn.setText(QCoreApplication.translate("MainWindow", u"Source Data", None))
        self.textureAssetsDirBnt.setText(QCoreApplication.translate("MainWindow", u"Texture Assets", None))
        self.zoneSourceDirBtn.setText(QCoreApplication.translate("MainWindow", u"Zone Source", None))
        self.rawFoldersArea.setTitle(QCoreApplication.translate("MainWindow", u"Raw Folders", None))
        self.animTreesDirBtn.setText(QCoreApplication.translate("MainWindow", u"Anim Trees", None))
        self.clientScriptsDir.setText(QCoreApplication.translate("MainWindow", u"Clientscripts", None))
        self.englishStringsDirBtn.setText(QCoreApplication.translate("MainWindow", u"English Strings", None))
        self.fxDirBtn.setText(QCoreApplication.translate("MainWindow", u"FX", None))
        self.mapsDirBtn.setText(QCoreApplication.translate("MainWindow", u"Maps", None))
        self.soundAliasesDirBtn.setText(QCoreApplication.translate("MainWindow", u"Sound Aliases", None))
        self.visionDirBtn.setText(QCoreApplication.translate("MainWindow", u"Vision", None))
        self.weaponsDirBtn.setText(QCoreApplication.translate("MainWindow", u"Weapons", None))
        self.mainSectionTabWidget.setTabText(self.mainSectionTabWidget.indexOf(self.exploreTab), QCoreApplication.translate("MainWindow", u"Explore", None))
        self.rgModGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Mod", None))
        self.rgDevmapLabel.setText(QCoreApplication.translate("MainWindow", u"devmap (Loads Map)", None))
        self.rgCheatsLabel.setText(QCoreApplication.translate("MainWindow", u"thereisacow (Enables Cheats)", None))
        self.rgDeveloperLabel.setText(QCoreApplication.translate("MainWindow", u"developer (Used to give more debug info)", None))
        self.rgDeveloperScriptLabel.setText(QCoreApplication.translate("MainWindow", u"developer_script (Used to give more script debug info)", None))
        self.rgLogfileLabel.setText(QCoreApplication.translate("MainWindow", u"logfile (Spits out a console log)", None))
        self.rgIntroplayedLabel.setText(QCoreApplication.translate("MainWindow", u"com_introplayed (Skips the intro movies)", None))
        self.rgShipIWDLabel.setText(QCoreApplication.translate("MainWindow", u"sv_pure (Determines if the game will use the shipped iwd files only)", None))
        self.rgFullscreenLabel.setText(QCoreApplication.translate("MainWindow", u"r_fullscreen (Enables Fullscreen)", None))
        self.rgPunkBusterLabel.setText(QCoreApplication.translate("MainWindow", u"sv_punkbuster (Toggles the use of Punk Buster)", None))
        self.rgTestclientsLabel.setText(QCoreApplication.translate("MainWindow", u"scr_testclients (How many test bots do you want?)", None))
        self.rgCustomLineGrouBox.setTitle(QCoreApplication.translate("MainWindow", u"Command Line", None))
        self.runGameBtn.setText(QCoreApplication.translate("MainWindow", u"Run Game", None))
        self.mainSectionTabWidget.setTabText(self.mainSectionTabWidget.indexOf(self.runGameTab), QCoreApplication.translate("MainWindow", u"Run Game", None))
        self.linksTabGroupBox.setTitle(QCoreApplication.translate("MainWindow", u"Links", None))
        self.discordBtn.setText(QCoreApplication.translate("MainWindow", u"Discord", None))
        self.siteBtn.setText(QCoreApplication.translate("MainWindow", u"Site", None))
        self.githubBtn.setText(QCoreApplication.translate("MainWindow", u"Github", None))
        self.youtubeBtn.setText(QCoreApplication.translate("MainWindow", u"YouTube", None))
        self.mainSectionTabWidget.setTabText(self.mainSectionTabWidget.indexOf(self.linksTab), QCoreApplication.translate("MainWindow", u"Links", None))
        self.exeArgs.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Executable Args..", None))
        self.consoleSuccessErrorOutput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Success..", None))
        self.processesArea.setTitle(QCoreApplication.translate("MainWindow", u"Processes", None))
        self.killExeBtn.setText(QCoreApplication.translate("MainWindow", u"No Active Process\n"
"\n"
"Start one and then use\n"
"this button to stop it", None))
    # retranslateUi

