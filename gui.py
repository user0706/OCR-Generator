# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(564, 289)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/Icons/logo.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QToolButton{\n"
"    border:none;\n"
"}\n"
"QToolButton:hover{\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: none;\n"
"    border-radius: 5%;\n"
"    background-color: none;\n"
"}\n"
"\n"
"QSplitter::handle {\n"
"    image: url(:/img/Icons/more-svgrepo-com.svg);\n"
"    border-left: 1px solid rgba(0, 0, 0, 10%);\n"
"    border-right: 1px solid rgba(0, 0, 0, 10%);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal {\n"
"    width: 2px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical {\n"
"    height: 13px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"    height:18px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    color: rgba(0, 0, 0, 85%);\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgba(0, 0, 0, 30%);\n"
"}\n"
"QLineEdit:disabled{\n"
"    color: rgba(0, 0, 0, 50%);\n"
"}\n"
"\n"
"QScrollArea {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgba(0, 0, 0, 30%);\n"
"}\n"
"\n"
"QCheckBox, QCheckBox:disabled{\n"
"    color: rgba(0, 0, 0, 85%);\n"
"}\n"
"QLabel{\n"
"    color: rgba(0, 0, 0, 85%);\n"
"}\n"
"QGroupBox{\n"
"    color: rgba(0, 0, 0, 85%);\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgba(0, 0, 0, 30%);\n"
"    height:20px;\n"
"}\n"
"QSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"\n"
"    width: 20px;\n"
"    border:none;\n"
"}\n"
"QSpinBox::up-button:hover {\n"
"    background-color: rgba(0, 0, 0, 10%);\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed {\n"
"   background-color: rgba(0, 0, 0, 15%);\n"
"}\n"
"QSpinBox::up-arrow {\n"
"    image: url(:/img/Icons/up-arrow-svgrepo-com.svg);\n"
"    width: 7px;\n"
"    height: 5px;\n"
"}\n"
"QSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"\n"
"    width: 20px;\n"
"    border:none;\n"
"}\n"
"QSpinBox::down-button:hover {\n"
"    background-color: rgba(0, 0, 0, 10%);\n"
"}\n"
"\n"
"QSpinBox::down-button:pressed {\n"
"   background-color: rgba(0, 0, 0, 15%);\n"
"}\n"
"QSpinBox::down-arrow {\n"
"    image: url(:/img/Icons/down-arrow-svgrepo-com.svg);\n"
"    width: 7px;\n"
"    height: 5px;\n"
"}\n"
"\n"
"/*Double Spin Box */\n"
"QDoubleSpinBox {\n"
"    background-color:rgb(255, 255, 255);\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgba(0, 0, 0, 30%);\n"
"    height:20px;\n"
"}\n"
"QDoubleSpinBox::up-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: top right;\n"
"\n"
"    width: 20px;\n"
"    border:none;\n"
"}\n"
"QDoubleSpinBox::up-button:hover {\n"
"    background-color: rgba(0, 0, 0, 10%);\n"
"}\n"
"\n"
"QDoubleSpinBox::up-button:pressed {\n"
"   background-color: rgba(0, 0, 0, 15%);\n"
"}\n"
"QDoubleSpinBox::up-arrow {\n"
"    image: url(:/img/Icons/up-arrow-svgrepo-com.svg);\n"
"    width: 7px;\n"
"    height: 5px;\n"
"}\n"
"QDoubleSpinBox::down-button {\n"
"    subcontrol-origin: border;\n"
"    subcontrol-position: bottom right;\n"
"\n"
"    width: 20px;\n"
"    border:none;\n"
"}\n"
"QDoubleSpinBox::down-button:hover {\n"
"    background-color: rgba(0, 0, 0, 10%);\n"
"}\n"
"\n"
"QDoubleSpinBox::down-button:pressed {\n"
"   background-color: rgba(0, 0, 0, 15%);\n"
"}\n"
"QDoubleSpinBox::down-arrow {\n"
"    image: url(:/img/Icons/down-arrow-svgrepo-com.svg);\n"
"    width: 7px;\n"
"    height: 5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.widget_LeftArea = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_LeftArea.sizePolicy().hasHeightForWidth())
        self.widget_LeftArea.setSizePolicy(sizePolicy)
        self.widget_LeftArea.setMinimumSize(QtCore.QSize(150, 0))
        self.widget_LeftArea.setStyleSheet("")
        self.widget_LeftArea.setObjectName("widget_LeftArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_LeftArea)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.widget_LeftArea)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fontComboBox = QtWidgets.QFontComboBox(self.frame)
        self.fontComboBox.setStyleSheet("QComboBox{\n"
"    height:18px;\n"
"    color: rgba(0, 0, 0, 85%);\n"
"}\n"
"QComboBox:editable {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-style:solid;\n"
"    border-width: 1px;\n"
"    border-color: rgba(0, 0, 0, 30%);\n"
"}\n"
"\n"
"\n"
"QComboBox:on { /* shift the text when the popup opens */\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border:none;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    padding:3px;\n"
"    min-width:3px;\n"
"    max-width:3px;\n"
"    image: url(:/img/Icons/down-arrow-svgrepo-com.svg);\n"
"}\n"
"")
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout.addWidget(self.fontComboBox)
        self.toolButton_AddFont = QtWidgets.QToolButton(self.frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/Icons/add-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_AddFont.setIcon(icon1)
        self.toolButton_AddFont.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_AddFont.setObjectName("toolButton_AddFont")
        self.horizontalLayout.addWidget(self.toolButton_AddFont)
        self.verticalLayout_2.addWidget(self.frame)
        self.scrollArea_Fonts = QtWidgets.QScrollArea(self.widget_LeftArea)
        self.scrollArea_Fonts.setStyleSheet("background-color:rgb(255, 255, 255);")
        self.scrollArea_Fonts.setLineWidth(1)
        self.scrollArea_Fonts.setWidgetResizable(True)
        self.scrollArea_Fonts.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.scrollArea_Fonts.setObjectName("scrollArea_Fonts")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 177, 207))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scrollArea_Fonts.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea_Fonts)
        self.frame_7 = QtWidgets.QFrame(self.widget_LeftArea)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_FontCount = QtWidgets.QLabel(self.frame_7)
        self.label_FontCount.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_FontCount.setObjectName("label_FontCount")
        self.horizontalLayout_6.addWidget(self.label_FontCount, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.toolButton_Remove = QtWidgets.QToolButton(self.frame_7)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/Icons/error-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_Remove.setIcon(icon2)
        self.toolButton_Remove.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_Remove.setObjectName("toolButton_Remove")
        self.horizontalLayout_6.addWidget(self.toolButton_Remove, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.widget_CentralArea = QtWidgets.QWidget(self.splitter)
        self.widget_CentralArea.setObjectName("widget_CentralArea")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_CentralArea)
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.widget_CentralArea)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox_UnicodeChar = QtWidgets.QCheckBox(self.frame_6)
        self.checkBox_UnicodeChar.setEnabled(False)
        self.checkBox_UnicodeChar.setText("")
        self.checkBox_UnicodeChar.setCheckable(True)
        self.checkBox_UnicodeChar.setChecked(True)
        self.checkBox_UnicodeChar.setObjectName("checkBox_UnicodeChar")
        self.horizontalLayout_3.addWidget(self.checkBox_UnicodeChar)
        self.label_UnicodeChar = QtWidgets.QLabel(self.frame_6)
        self.label_UnicodeChar.setEnabled(False)
        self.label_UnicodeChar.setStyleSheet("QLabel{\n"
"    color: rgba(0, 0, 0, 50%);\n"
"}\n"
"QLabel:disabled{\n"
"    color: rgba(0, 0, 0, 85%);\n"
"}")
        self.label_UnicodeChar.setObjectName("label_UnicodeChar")
        self.horizontalLayout_3.addWidget(self.label_UnicodeChar)
        self.verticalLayout_4.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox_CharString = QtWidgets.QCheckBox(self.frame_5)
        self.checkBox_CharString.setText("")
        self.checkBox_CharString.setObjectName("checkBox_CharString")
        self.horizontalLayout_2.addWidget(self.checkBox_CharString)
        self.lineEdit_CharString = QtWidgets.QLineEdit(self.frame_5)
        self.lineEdit_CharString.setEnabled(False)
        self.lineEdit_CharString.setStyleSheet("")
        self.lineEdit_CharString.setObjectName("lineEdit_CharString")
        self.horizontalLayout_2.addWidget(self.lineEdit_CharString)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.verticalLayout_3.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.widget_CentralArea)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.label_Character = QtWidgets.QLabel(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Character.sizePolicy().hasHeightForWidth())
        self.label_Character.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_Character.setFont(font)
        self.label_Character.setStyleSheet("")
        self.label_Character.setText("")
        self.label_Character.setScaledContents(True)
        self.label_Character.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Character.setObjectName("label_Character")
        self.horizontalLayout_5.addWidget(self.label_Character)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.progressBar = QtWidgets.QProgressBar(self.frame_3)
        self.progressBar.setMinimumSize(QtCore.QSize(80, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(80, 16777215))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    text-align: center;\n"
"    height:10px;\n"
"    border-style:solid;\n"
"    border-width:1px;\n"
"    border-color: rgba(0, 0, 0, 30%)\n"
"}\n"
"QProgressBar::chunk {\n"
"    background-color: rgba(0, 202, 0, 50%);\n"
"}")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_5.addWidget(self.progressBar, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addWidget(self.frame_3, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem3)
        self.widget = QtWidgets.QWidget(self.widget_CentralArea)
        self.widget.setObjectName("widget")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setEnabled(True)
        self.label.setMinimumSize(QtCore.QSize(54, 13))
        self.label.setMaximumSize(QtCore.QSize(54, 13))
        self.label.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label.setObjectName("label")
        self.horizontalLayout_12.addWidget(self.label)
        self.label_Successful = QtWidgets.QLabel(self.widget_2)
        self.label_Successful.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_Successful.setText("")
        self.label_Successful.setObjectName("label_Successful")
        self.horizontalLayout_12.addWidget(self.label_Successful)
        self.verticalLayout_11.addWidget(self.widget_2)
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.widget_7)
        self.label_8.setMinimumSize(QtCore.QSize(54, 13))
        self.label_8.setMaximumSize(QtCore.QSize(54, 13))
        self.label_8.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.label_Failed = QtWidgets.QLabel(self.widget_7)
        self.label_Failed.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_Failed.setText("")
        self.label_Failed.setObjectName("label_Failed")
        self.horizontalLayout_13.addWidget(self.label_Failed)
        self.verticalLayout_11.addWidget(self.widget_7)
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_6 = QtWidgets.QLabel(self.widget_6)
        self.label_6.setMinimumSize(QtCore.QSize(54, 13))
        self.label_6.setMaximumSize(QtCore.QSize(54, 13))
        self.label_6.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_14.addWidget(self.label_6)
        self.label_Phase = QtWidgets.QLabel(self.widget_6)
        self.label_Phase.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_Phase.setText("")
        self.label_Phase.setObjectName("label_Phase")
        self.horizontalLayout_14.addWidget(self.label_Phase)
        self.verticalLayout_11.addWidget(self.widget_6)
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_7 = QtWidgets.QLabel(self.widget_8)
        self.label_7.setMinimumSize(QtCore.QSize(54, 13))
        self.label_7.setMaximumSize(QtCore.QSize(54, 13))
        self.label_7.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_15.addWidget(self.label_7)
        self.label_Font = QtWidgets.QLabel(self.widget_8)
        self.label_Font.setStyleSheet("color: rgba(0, 0, 0, 50%);")
        self.label_Font.setText("")
        self.label_Font.setObjectName("label_Font")
        self.horizontalLayout_15.addWidget(self.label_Font)
        self.verticalLayout_11.addWidget(self.widget_8)
        self.verticalLayout_3.addWidget(self.widget, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.frame_4 = QtWidgets.QFrame(self.widget_CentralArea)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 9)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolButton_Build = QtWidgets.QToolButton(self.frame_4)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/img/Icons/transfer-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_Build.setIcon(icon3)
        self.toolButton_Build.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_Build.setCheckable(False)
        self.toolButton_Build.setObjectName("toolButton_Build")
        self.horizontalLayout_4.addWidget(self.toolButton_Build)
        self.toolButton_OpenInFolder = QtWidgets.QToolButton(self.frame_4)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/img/Icons/folder-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_OpenInFolder.setIcon(icon4)
        self.toolButton_OpenInFolder.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_OpenInFolder.setObjectName("toolButton_OpenInFolder")
        self.horizontalLayout_4.addWidget(self.toolButton_OpenInFolder)
        self.verticalLayout_3.addWidget(self.frame_4, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.widget_RightArea = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_RightArea.sizePolicy().hasHeightForWidth())
        self.widget_RightArea.setSizePolicy(sizePolicy)
        self.widget_RightArea.setMinimumSize(QtCore.QSize(162, 0))
        self.widget_RightArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_RightArea.setBaseSize(QtCore.QSize(0, 0))
        self.widget_RightArea.setStyleSheet("")
        self.widget_RightArea.setObjectName("widget_RightArea")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_RightArea)
        self.verticalLayout.setContentsMargins(0, 9, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_9 = QtWidgets.QFrame(self.widget_RightArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.groupBox = QtWidgets.QGroupBox(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_8 = QtWidgets.QFrame(self.groupBox)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.lineEdit_SampsDir = QtWidgets.QLineEdit(self.frame_8)
        self.lineEdit_SampsDir.setEnabled(True)
        self.lineEdit_SampsDir.setReadOnly(True)
        self.lineEdit_SampsDir.setObjectName("lineEdit_SampsDir")
        self.horizontalLayout_8.addWidget(self.lineEdit_SampsDir)
        self.toolButton_ChangeSampsDir = QtWidgets.QToolButton(self.frame_8)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/img/Icons/change-directory.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_ChangeSampsDir.setIcon(icon5)
        self.toolButton_ChangeSampsDir.setIconSize(QtCore.QSize(20, 20))
        self.toolButton_ChangeSampsDir.setObjectName("toolButton_ChangeSampsDir")
        self.horizontalLayout_8.addWidget(self.toolButton_ChangeSampsDir)
        self.verticalLayout_7.addWidget(self.frame_8)
        self.toolButton_DeleteSamps = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_DeleteSamps.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/img/Icons/trash-svgrepo-com.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_DeleteSamps.setIcon(icon6)
        self.toolButton_DeleteSamps.setIconSize(QtCore.QSize(18, 18))
        self.toolButton_DeleteSamps.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.toolButton_DeleteSamps.setObjectName("toolButton_DeleteSamps")
        self.verticalLayout_7.addWidget(self.toolButton_DeleteSamps, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.verticalLayout_10.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.widget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        self.spinBox_UniStart = QtWidgets.QSpinBox(self.widget_3)
        self.spinBox_UniStart.setMaximum(5000000)
        self.spinBox_UniStart.setObjectName("spinBox_UniStart")
        self.horizontalLayout_9.addWidget(self.spinBox_UniStart)
        self.verticalLayout_8.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.groupBox_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_10.addWidget(self.label_4)
        self.spinBox_UniEnd = QtWidgets.QSpinBox(self.widget_4)
        self.spinBox_UniEnd.setMaximum(5000000)
        self.spinBox_UniEnd.setProperty("value", 0)
        self.spinBox_UniEnd.setObjectName("spinBox_UniEnd")
        self.horizontalLayout_10.addWidget(self.spinBox_UniEnd)
        self.verticalLayout_8.addWidget(self.widget_4)
        self.verticalLayout_10.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(140, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.widget_5 = QtWidgets.QWidget(self.groupBox_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.widget_5)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_11.addWidget(self.label_5)
        self.doubleSpinBox_Delay = QtWidgets.QDoubleSpinBox(self.widget_5)
        self.doubleSpinBox_Delay.setSuffix("")
        self.doubleSpinBox_Delay.setDecimals(3)
        self.doubleSpinBox_Delay.setSingleStep(0.01)
        self.doubleSpinBox_Delay.setProperty("value", 0.05)
        self.doubleSpinBox_Delay.setObjectName("doubleSpinBox_Delay")
        self.horizontalLayout_11.addWidget(self.doubleSpinBox_Delay)
        self.verticalLayout_9.addWidget(self.widget_5)
        self.verticalLayout_10.addWidget(self.groupBox_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 19, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_10.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_9)
        self.horizontalLayout_7.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OCR Generator"))
        self.toolButton_AddFont.setToolTip(_translate("MainWindow", "Add"))
        self.toolButton_AddFont.setText(_translate("MainWindow", "..."))
        self.label_FontCount.setText(_translate("MainWindow", "0"))
        self.toolButton_Remove.setToolTip(_translate("MainWindow", "Remove"))
        self.toolButton_Remove.setText(_translate("MainWindow", "..."))
        self.label_UnicodeChar.setText(_translate("MainWindow", "All unicode characters"))
        self.lineEdit_CharString.setPlaceholderText(_translate("MainWindow", "A series of characters"))
        self.label.setText(_translate("MainWindow", "Successful:"))
        self.label_8.setText(_translate("MainWindow", "Failed:"))
        self.label_6.setText(_translate("MainWindow", "Phase:"))
        self.label_7.setText(_translate("MainWindow", "Font:"))
        self.toolButton_Build.setToolTip(_translate("MainWindow", "Build/Stop"))
        self.toolButton_Build.setText(_translate("MainWindow", "..."))
        self.toolButton_OpenInFolder.setToolTip(_translate("MainWindow", "Open in folder"))
        self.toolButton_OpenInFolder.setText(_translate("MainWindow", "..."))
        self.groupBox.setTitle(_translate("MainWindow", "Extraction directory"))
        self.toolButton_ChangeSampsDir.setToolTip(_translate("MainWindow", "Change directory"))
        self.toolButton_ChangeSampsDir.setText(_translate("MainWindow", "..."))
        self.toolButton_DeleteSamps.setText(_translate("MainWindow", "Delete all samples"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Unicode range"))
        self.label_3.setText(_translate("MainWindow", "Start:"))
        self.label_4.setText(_translate("MainWindow", "End:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Visual"))
        self.label_5.setText(_translate("MainWindow", "Delay:"))
        self.doubleSpinBox_Delay.setToolTip(_translate("MainWindow", "<html><head/><body><p>Delay between sample extraction</p></body></html>"))
import src_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
