# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_copy2.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPlainTextEdit, QProgressBar, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QSpinBox, QSplitter,
    QStackedWidget, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(940, 560)
        MainWindow.setMinimumSize(QSize(940, 560))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Bg App */\n"
"#bgApp {	\n"
"	background"
                        "-color: rgb(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(18"
                        "9, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb("
                        "189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Extra Content */\n"
"#extraContent{\n"
"	border"
                        "-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { background-color: rgb(44, 49, 57); border-sty"
                        "le: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb"
                        "(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"QTableWidget */\n"
"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-co"
                        "lor: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-c"
                        "olor: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
""
                        "QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     su"
                        "bcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	back"
                        "ground-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subco"
                        "ntrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/images/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    h"
                        "eight: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLi"
                        "nkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setStyleSheet(u"")
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.frame_3 = QFrame(self.topLogoInfo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 0, 45, 45))
        self.frame_3.setMinimumSize(QSize(45, 45))
        self.frame_3.setMaximumSize(QSize(45, 45))
        self.frame_3.setStyleSheet(u"image: url(:/images/images/images/defectDetect.svg);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_imgs = QPushButton(self.topMenu)
        self.btn_imgs.setObjectName(u"btn_imgs")
        sizePolicy.setHeightForWidth(self.btn_imgs.sizePolicy().hasHeightForWidth())
        self.btn_imgs.setSizePolicy(sizePolicy)
        self.btn_imgs.setMinimumSize(QSize(0, 45))
        self.btn_imgs.setFont(font)
        self.btn_imgs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_imgs.setLayoutDirection(Qt.LeftToRight)
        self.btn_imgs.setStyleSheet(u"QPushButton#btn_imgs{  \n"
"background-image: url(:/icons/images/icons/cil-satelite.png);\n"
"}\n"
"QMenu {\n"
"                       background-color: rgba(50, 50, 50, 180); /* \u534a\u900f\u660e\u7070\u9ed1\u8272\u80cc\u666f */\n"
"                       color: white; \n"
"                       border: 1px solid #333;\n"
"                   }\n"
" QMenu::item {\n"
"                       background-color: transparent;\n"
"                   }\n"
"QMenu::item:selected {\n"
"                       background-color: rgba(80, 80, 80, 180);\n"
"                   }")

        self.verticalLayout_8.addWidget(self.btn_imgs)

        self.btn_camera = QPushButton(self.topMenu)
        self.btn_camera.setObjectName(u"btn_camera")
        sizePolicy.setHeightForWidth(self.btn_camera.sizePolicy().hasHeightForWidth())
        self.btn_camera.setSizePolicy(sizePolicy)
        self.btn_camera.setMinimumSize(QSize(0, 45))
        self.btn_camera.setFont(font)
        self.btn_camera.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_camera.setLayoutDirection(Qt.LeftToRight)
        self.btn_camera.setStyleSheet(u"QPushButton#btn_camera{  \n"
"background-image: url(:/icons/images/icons/cil-camera.png); \n"
"}\n"
"QMenu {\n"
"                       background-color: rgba(50, 50, 50, 180); /* \u534a\u900f\u660e\u7070\u9ed1\u8272\u80cc\u666f */\n"
"                       color: white; \n"
"                       border: 1px solid #333;\n"
"                   }\n"
" QMenu::item {\n"
"                       background-color: transparent;\n"
"                   }\n"
"QMenu::item:selected {\n"
"                       background-color: rgba(80, 80, 80, 180);\n"
"                   }")

        self.verticalLayout_8.addWidget(self.btn_camera)

        self.btn_video = QPushButton(self.topMenu)
        self.btn_video.setObjectName(u"btn_video")
        sizePolicy.setHeightForWidth(self.btn_video.sizePolicy().hasHeightForWidth())
        self.btn_video.setSizePolicy(sizePolicy)
        self.btn_video.setMinimumSize(QSize(0, 45))
        self.btn_video.setFont(font)
        self.btn_video.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_video.setLayoutDirection(Qt.LeftToRight)
        self.btn_video.setStyleSheet(u"QPushButton#btn_video{  \n"
"background-image: url(:/icons/images/icons/cil-movie.png)\uff1b\n"
"}\n"
"QMenu {\n"
"                       background-color: rgba(50, 50, 50, 180); /* \u534a\u900f\u660e\u7070\u9ed1\u8272\u80cc\u666f */\n"
"                       color: white; \n"
"                       border: 1px solid #333;\n"
"                   }\n"
" QMenu::item {\n"
"                       background-color: transparent;\n"
"                   }\n"
"QMenu::item:selected {\n"
"                       background-color: rgba(80, 80, 80, 180);\n"
"                   }")

        self.verticalLayout_8.addWidget(self.btn_video)

        self.btn_widgets_train = QPushButton(self.topMenu)
        self.btn_widgets_train.setObjectName(u"btn_widgets_train")
        sizePolicy.setHeightForWidth(self.btn_widgets_train.sizePolicy().hasHeightForWidth())
        self.btn_widgets_train.setSizePolicy(sizePolicy)
        self.btn_widgets_train.setMinimumSize(QSize(0, 45))
        self.btn_widgets_train.setFont(font)
        self.btn_widgets_train.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_widgets_train.setLayoutDirection(Qt.LeftToRight)
        self.btn_widgets_train.setStyleSheet(u"background-image:url(:/icons/images/icons/cil-view-quilt.png);")

        self.verticalLayout_8.addWidget(self.btn_widgets_train)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)

        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.titleRightInfo = QLabel(self.contentTopBg)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy1)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setItalic(True)
        self.titleRightInfo.setFont(font1)
        self.titleRightInfo.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\"")
        self.titleRightInfo.setLocale(QLocale(QLocale.Croatian, QLocale.Croatia))
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.titleRightInfo)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font2)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setStyleSheet(u"")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.pagesContainer)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;\n"
"")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.home)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_group = QFrame(self.home)
        self.frame_group.setObjectName(u"frame_group")
        self.frame_group.setMinimumSize(QSize(0, 100))
        self.frame_group.setMaximumSize(QSize(16777215, 100))
        self.frame_group.setStyleSheet(u"QFrame #frame_group{\n"
"background-color: rgb(44, 49, 58);\n"
"\n"
"border-radius:15px;\n"
"}")
        self.frame_group.setFrameShape(QFrame.StyledPanel)
        self.frame_group.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_group)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_model = QFrame(self.frame_group)
        self.frame_model.setObjectName(u"frame_model")
        self.frame_model.setMinimumSize(QSize(150, 80))
        self.frame_model.setMaximumSize(QSize(150, 80))
        self.frame_model.setStyleSheet(u"QFrame #frame_model{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(66, 226, 192),  stop:1 rgb(62, 154, 193));\n"
"border: 1px outset rgb(72, 158, 204)\n"
"}\n"
"\n"
"")
        self.frame_model.setFrameShape(QFrame.StyledPanel)
        self.frame_model.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_model)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.pushButton_start = QPushButton(self.frame_model)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setItalic(True)
        self.pushButton_start.setFont(font3)
        self.pushButton_start.setStyleSheet(u"background-color: rgb(255, 85, 127);\n"
"border-color: rgb(255, 85, 127);\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"")

        self.verticalLayout_23.addWidget(self.pushButton_start)

        self.lineEdit_mode = QLineEdit(self.frame_model)
        self.lineEdit_mode.setObjectName(u"lineEdit_mode")
        self.lineEdit_mode.setStyleSheet(u"border-color: rgb(255, 255, 255);\n"
"font: 700 italic 10pt \"Segoe UI\";")

        self.verticalLayout_23.addWidget(self.lineEdit_mode)


        self.verticalLayout_24.addLayout(self.verticalLayout_23)


        self.horizontalLayout_5.addWidget(self.frame_model)

        self.frame_delay = QFrame(self.frame_group)
        self.frame_delay.setObjectName(u"frame_delay")
        self.frame_delay.setMinimumSize(QSize(150, 80))
        self.frame_delay.setMaximumSize(QSize(150, 80))
        self.frame_delay.setStyleSheet(u"QFrame#frame_delay{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(66, 226, 192),  stop:1 rgb(62, 154, 193));\n"
"border: 1px outset rgb(72, 158, 204)\n"
"}\n"
"\n"
"")
        self.frame_delay.setFrameShape(QFrame.StyledPanel)
        self.frame_delay.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_delay)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_delay = QLabel(self.frame_delay)
        self.label_delay.setObjectName(u"label_delay")
        self.label_delay.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"")
        self.label_delay.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.label_delay)

        self.spinBox_delay = QSpinBox(self.frame_delay)
        self.spinBox_delay.setObjectName(u"spinBox_delay")
        self.spinBox_delay.setMinimumSize(QSize(0, 30))
        self.spinBox_delay.setStyleSheet(u"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(66, 226, 192),  stop:1 rgb(62, 154, 193));\n"
"border-radius: 8px;\n"
"border: 2px outset  rgb(255, 255, 255);")
        self.spinBox_delay.setMaximum(100000)

        self.verticalLayout_36.addWidget(self.spinBox_delay)


        self.verticalLayout_35.addLayout(self.verticalLayout_36)


        self.horizontalLayout_5.addWidget(self.frame_delay)

        self.frame_classes = QFrame(self.frame_group)
        self.frame_classes.setObjectName(u"frame_classes")
        self.frame_classes.setMinimumSize(QSize(150, 80))
        self.frame_classes.setMaximumSize(QSize(150, 80))
        self.frame_classes.setStyleSheet(u"QFrame#frame_classes{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219)\n"
"}\n"
"\n"
"")
        self.frame_classes.setFrameShape(QFrame.StyledPanel)
        self.frame_classes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_classes)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_classes_hint = QLabel(self.frame_classes)
        self.label_classes_hint.setObjectName(u"label_classes_hint")
        self.label_classes_hint.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"border-bottom: 1px solid white;")
        self.label_classes_hint.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_classes_hint)

        self.label_classes = QLabel(self.frame_classes)
        self.label_classes.setObjectName(u"label_classes")
        self.label_classes.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"")
        self.label_classes.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.label_classes)


        self.verticalLayout_25.addLayout(self.verticalLayout_26)


        self.horizontalLayout_5.addWidget(self.frame_classes)

        self.frame_targets = QFrame(self.frame_group)
        self.frame_targets.setObjectName(u"frame_targets")
        self.frame_targets.setMinimumSize(QSize(150, 80))
        self.frame_targets.setMaximumSize(QSize(150, 80))
        self.frame_targets.setStyleSheet(u"QFrame#frame_targets{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219)\n"
"}\n"
"")
        self.frame_targets.setFrameShape(QFrame.StyledPanel)
        self.frame_targets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_targets)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_targets_hint = QLabel(self.frame_targets)
        self.label_targets_hint.setObjectName(u"label_targets_hint")
        self.label_targets_hint.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"border-bottom: 1px solid white;")
        self.label_targets_hint.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_targets_hint)

        self.label_targets = QLabel(self.frame_targets)
        self.label_targets.setObjectName(u"label_targets")
        self.label_targets.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"")
        self.label_targets.setAlignment(Qt.AlignCenter)

        self.verticalLayout_28.addWidget(self.label_targets)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)


        self.horizontalLayout_5.addWidget(self.frame_targets)

        self.frame_fps = QFrame(self.frame_group)
        self.frame_fps.setObjectName(u"frame_fps")
        self.frame_fps.setMinimumSize(QSize(150, 80))
        self.frame_fps.setMaximumSize(QSize(150, 80))
        self.frame_fps.setStyleSheet(u"QFrame#frame_fps{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219)\n"
"}\n"
"\n"
"")
        self.frame_fps.setFrameShape(QFrame.StyledPanel)
        self.frame_fps.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_fps)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_FPS_hint = QLabel(self.frame_fps)
        self.label_FPS_hint.setObjectName(u"label_FPS_hint")
        self.label_FPS_hint.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"border-bottom: 1px solid white;")
        self.label_FPS_hint.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_FPS_hint)

        self.label_FPS = QLabel(self.frame_fps)
        self.label_FPS.setObjectName(u"label_FPS")
        self.label_FPS.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 12pt \"Microsoft YaHei UI\";\n"
"")
        self.label_FPS.setAlignment(Qt.AlignCenter)

        self.verticalLayout_30.addWidget(self.label_FPS)


        self.verticalLayout_29.addLayout(self.verticalLayout_30)


        self.horizontalLayout_5.addWidget(self.frame_fps)


        self.verticalLayout_13.addWidget(self.frame_group)

        self.splitter = QSplitter(self.home)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.label_video = QLabel(self.splitter)
        self.label_video.setObjectName(u"label_video")
        self.label_video.setStyleSheet(u"border:2px solid rgb(189, 147, 249);\n"
"border-radius:15px;")
        self.label_video.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_video)
        self.label_result = QLabel(self.splitter)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setStyleSheet(u"border:2px solid rgb(189, 147, 249);\n"
"border-radius:15px;")
        self.label_result.setAlignment(Qt.AlignCenter)
        self.splitter.addWidget(self.label_result)

        self.verticalLayout_13.addWidget(self.splitter)

        self.progressBar = QProgressBar(self.home)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 15))
        self.progressBar.setMaximumSize(QSize(16777215, 0))
        self.progressBar.setStyleSheet(u"QProgressBar{ \n"
"font: 700 10pt \"Microsoft YaHei UI\";\n"
"color: rgb(255, 255, 255); \n"
"text-align:center; \n"
"border-radius: 10px; \n"
"background-color: rgba(215, 215, 215,100);\n"
"} \n"
"\n"
"QProgressBar:chunk{ \n"
"border-radius:0px; \n"
"background: rgba(189, 147, 249, 200);\n"
"border-radius: 7px;\n"
"}")
        self.progressBar.setValue(0)

        self.verticalLayout_13.addWidget(self.progressBar)

        self.label_status = QLabel(self.home)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setMaximumSize(QSize(16777215, 25))
        self.label_status.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"")

        self.verticalLayout_13.addWidget(self.label_status)

        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout_15 = QVBoxLayout(self.widgets)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(20, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.splitter_3 = QSplitter(self.row_3)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.frame = QFrame(self.splitter_3)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"background-color: rgb(44, 49, 58);\n"
"border:2px solid rgb(187, 145, 246);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.splitter_2 = QSplitter(self.frame)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_10 = QLabel(self.splitter_2)
        self.label_10.setObjectName(u"label_10")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy2)
        self.label_10.setMinimumSize(QSize(55, 0))
        self.label_10.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_10.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_10)
        self.comboBox_device = QComboBox(self.splitter_2)
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.setObjectName(u"comboBox_device")
        self.comboBox_device.setLayoutDirection(Qt.LeftToRight)
        self.splitter_2.addWidget(self.comboBox_device)

        self.gridLayout.addWidget(self.splitter_2, 6, 0, 1, 2)

        self.horizontalSlider_epoch = QSlider(self.frame)
        self.horizontalSlider_epoch.setObjectName(u"horizontalSlider_epoch")
        self.horizontalSlider_epoch.setMaximum(500)
        self.horizontalSlider_epoch.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_epoch, 5, 1, 1, 1)

        self.horizontalSlider_batchsize = QSlider(self.frame)
        self.horizontalSlider_batchsize.setObjectName(u"horizontalSlider_batchsize")
        self.horizontalSlider_batchsize.setOrientation(Qt.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider_batchsize, 4, 1, 1, 1)

        self.spinBox_batchsize = QSpinBox(self.frame)
        self.spinBox_batchsize.setObjectName(u"spinBox_batchsize")
        self.spinBox_batchsize.setMinimumSize(QSize(0, 30))
        self.spinBox_batchsize.setStyleSheet(u"background: rgb(52, 59, 72);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(187, 145, 246);\n"
"")

        self.gridLayout.addWidget(self.spinBox_batchsize, 4, 2, 1, 1)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(55, 0))
        self.label_9.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy3)
        self.label_12.setMinimumSize(QSize(0, 30))
        self.label_12.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_12, 0, 1, 1, 1)

        self.lineEdit_weights = QLineEdit(self.frame)
        self.lineEdit_weights.setObjectName(u"lineEdit_weights")
        self.lineEdit_weights.setMinimumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.lineEdit_weights, 2, 1, 1, 1)

        self.pushButton_weights = QPushButton(self.frame)
        self.pushButton_weights.setObjectName(u"pushButton_weights")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.pushButton_weights.sizePolicy().hasHeightForWidth())
        self.pushButton_weights.setSizePolicy(sizePolicy4)
        self.pushButton_weights.setMinimumSize(QSize(60, 30))
        self.pushButton_weights.setMaximumSize(QSize(150, 16777215))
        self.pushButton_weights.setFont(font)
        self.pushButton_weights.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_weights.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_weights.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton_weights, 2, 2, 1, 1)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setMinimumSize(QSize(55, 0))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.pushButton_data = QPushButton(self.frame)
        self.pushButton_data.setObjectName(u"pushButton_data")
        self.pushButton_data.setMinimumSize(QSize(50, 30))
        self.pushButton_data.setFont(font)
        self.pushButton_data.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_data.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_data.setIcon(icon4)

        self.gridLayout.addWidget(self.pushButton_data, 3, 2, 1, 1)

        self.lineEdit_data = QLineEdit(self.frame)
        self.lineEdit_data.setObjectName(u"lineEdit_data")
        self.lineEdit_data.setMinimumSize(QSize(150, 30))

        self.gridLayout.addWidget(self.lineEdit_data, 3, 1, 1, 1)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(55, 0))
        self.label_8.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(55, 0))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.spinBox_epoch = QSpinBox(self.frame)
        self.spinBox_epoch.setObjectName(u"spinBox_epoch")
        self.spinBox_epoch.setMinimumSize(QSize(0, 30))
        self.spinBox_epoch.setStyleSheet(u"background: rgb(52, 59, 72);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(187, 145, 246);\n"
"")
        self.spinBox_epoch.setMinimum(10)
        self.spinBox_epoch.setMaximum(300)

        self.gridLayout.addWidget(self.spinBox_epoch, 5, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 8, 1, 1, 1)

        self.pushButton_train = QPushButton(self.frame)
        self.pushButton_train.setObjectName(u"pushButton_train")
        sizePolicy3.setHeightForWidth(self.pushButton_train.sizePolicy().hasHeightForWidth())
        self.pushButton_train.setSizePolicy(sizePolicy3)
        self.pushButton_train.setMinimumSize(QSize(0, 30))
        self.pushButton_train.setLayoutDirection(Qt.RightToLeft)
        self.pushButton_train.setStyleSheet(u"QPushButton#pushButton_train{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219);\n"
"font: 700 italic 14pt \"Segoe UI\"\n"
"}\n"
"\n"
"")

        self.gridLayout.addWidget(self.pushButton_train, 1, 0, 1, 3)

        self.splitter_3.addWidget(self.frame)
        self.frame_2 = QFrame(self.splitter_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 16777215))
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"background-color: rgb(44, 49, 58);\n"
"border:2px solid rgb(187, 145, 246);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 30))
        self.label_11.setStyleSheet(u"color: rgba(255, 255, 255,210);\n"
"padding-left:12px;\n"
"font: 700 italic 14pt \"Segoe UI\";\n"
"")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_11)

        self.pushButton_yamlTrain = QPushButton(self.frame_2)
        self.pushButton_yamlTrain.setObjectName(u"pushButton_yamlTrain")
        self.pushButton_yamlTrain.setStyleSheet(u"QPushButton#pushButton_yamlTrain{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;\n"
"background-color: qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0 rgb(243, 175, 189),  stop:1 rgb(155, 118, 218));\n"
"border: 1px outset rgb(153, 117, 219);\n"
"font: 700 italic 14pt \"Segoe UI\"\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_yamlTrain)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_hyp = QLabel(self.frame_2)
        self.label_hyp.setObjectName(u"label_hyp")
        self.label_hyp.setMinimumSize(QSize(98, 0))
        self.label_hyp.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_hyp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_hyp)

        self.lineEdit_hyp = QLineEdit(self.frame_2)
        self.lineEdit_hyp.setObjectName(u"lineEdit_hyp")
        self.lineEdit_hyp.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_9.addWidget(self.lineEdit_hyp)

        self.pushButton_hyp = QPushButton(self.frame_2)
        self.pushButton_hyp.setObjectName(u"pushButton_hyp")
        sizePolicy.setHeightForWidth(self.pushButton_hyp.sizePolicy().hasHeightForWidth())
        self.pushButton_hyp.setSizePolicy(sizePolicy)
        self.pushButton_hyp.setMinimumSize(QSize(60, 30))
        self.pushButton_hyp.setMaximumSize(QSize(150, 16777215))
        self.pushButton_hyp.setFont(font)
        self.pushButton_hyp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_hyp.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_hyp.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.pushButton_hyp)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_thyp = QLabel(self.frame_2)
        self.label_thyp.setObjectName(u"label_thyp")
        self.label_thyp.setStyleSheet(u"font: 700 italic 10pt \"Segoe UI\";")
        self.label_thyp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_thyp)

        self.lineEdit_thyp = QLineEdit(self.frame_2)
        self.lineEdit_thyp.setObjectName(u"lineEdit_thyp")
        self.lineEdit_thyp.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_10.addWidget(self.lineEdit_thyp)

        self.pushButton_thyp = QPushButton(self.frame_2)
        self.pushButton_thyp.setObjectName(u"pushButton_thyp")
        sizePolicy.setHeightForWidth(self.pushButton_thyp.sizePolicy().hasHeightForWidth())
        self.pushButton_thyp.setSizePolicy(sizePolicy)
        self.pushButton_thyp.setMinimumSize(QSize(60, 30))
        self.pushButton_thyp.setMaximumSize(QSize(150, 16777215))
        self.pushButton_thyp.setFont(font)
        self.pushButton_thyp.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_thyp.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pushButton_thyp.setIcon(icon4)

        self.horizontalLayout_10.addWidget(self.pushButton_thyp)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.plainTextEdit_yaml = QPlainTextEdit(self.frame_2)
        self.plainTextEdit_yaml.setObjectName(u"plainTextEdit_yaml")
        self.plainTextEdit_yaml.setMinimumSize(QSize(200, 150))
        self.plainTextEdit_yaml.setMaximumSize(QSize(16777215, 16777215))
        self.plainTextEdit_yaml.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.plainTextEdit_yaml)

        self.splitter_3.addWidget(self.frame_2)

        self.verticalLayout_16.addWidget(self.splitter_3)

        self.plainTextEdit_traintext = QPlainTextEdit(self.row_3)
        self.plainTextEdit_traintext.setObjectName(u"plainTextEdit_traintext")
        self.plainTextEdit_traintext.setStyleSheet(u"QFrame#plainTextEdit_traintext{\n"
"background-color: rgb(44, 49, 58);\n"
"border:2px solid rgb(187, 145, 246);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"")

        self.verticalLayout_16.addWidget(self.plainTextEdit_traintext)


        self.verticalLayout_15.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.new_page = QWidget()
        self.new_page.setObjectName(u"new_page")
        self.verticalLayout_20 = QVBoxLayout(self.new_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label = QLabel(self.new_page)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label)

        self.stackedWidget.addWidget(self.new_page)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setSizeIncrement(QSize(0, 0))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_4 = QLabel(self.extraRightBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(40, 40))
        self.label_4.setMaximumSize(QSize(20, 16777215))
        self.label_4.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.comboBox_select_model = QComboBox(self.extraRightBox)
        self.comboBox_select_model.addItem("")
        self.comboBox_select_model.addItem("")
        self.comboBox_select_model.setObjectName(u"comboBox_select_model")
        self.comboBox_select_model.setMinimumSize(QSize(0, 25))
        self.comboBox_select_model.setMaximumSize(QSize(16777215, 30))
        self.comboBox_select_model.setSizeIncrement(QSize(0, 0))
        self.comboBox_select_model.setStyleSheet(u"QComboBox#comboBox_select_model{  }\n"
"QMenu {\n"
"                       background-color: rgba(50, 50, 50, 180); /* \u534a\u900f\u660e\u7070\u9ed1\u8272\u80cc\u666f */\n"
"                       color: white; \n"
"                       border: 1px solid #333;\n"
"                   }\n"
" QMenu::item {\n"
"                       background-color: transparent;\n"
"                   }\n"
"QMenu::item:selected {\n"
"                       background-color: rgba(80, 80, 80, 180);\n"
"                   }")

        self.horizontalLayout_6.addWidget(self.comboBox_select_model)


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.extraRightBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 40))
        self.label_2.setMaximumSize(QSize(20, 16777215))
        self.label_2.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.label_2)

        self.horizontalSlider_iou = QSlider(self.extraRightBox)
        self.horizontalSlider_iou.setObjectName(u"horizontalSlider_iou")
        self.horizontalSlider_iou.setValue(45)
        self.horizontalSlider_iou.setOrientation(Qt.Horizontal)

        self.horizontalLayout_7.addWidget(self.horizontalSlider_iou)

        self.spinBox_iou = QSpinBox(self.extraRightBox)
        self.spinBox_iou.setObjectName(u"spinBox_iou")
        self.spinBox_iou.setStyleSheet(u"background: rgb(52, 59, 72);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(187, 145, 246);\n"
"")
        self.spinBox_iou.setValue(45)

        self.horizontalLayout_7.addWidget(self.spinBox_iou)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.extraRightBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(30, 40))
        self.label_3.setMaximumSize(QSize(20, 16777215))
        self.label_3.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.label_3)

        self.horizontalSlider_conf = QSlider(self.extraRightBox)
        self.horizontalSlider_conf.setObjectName(u"horizontalSlider_conf")
        self.horizontalSlider_conf.setValue(25)
        self.horizontalSlider_conf.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.horizontalSlider_conf)

        self.spinBox_conf = QSpinBox(self.extraRightBox)
        self.spinBox_conf.setObjectName(u"spinBox_conf")
        self.spinBox_conf.setStyleSheet(u"background: rgb(52, 59, 72);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(187, 145, 246);\n"
"")
        self.spinBox_conf.setValue(25)

        self.horizontalLayout_8.addWidget(self.spinBox_conf)


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_img_size = QLabel(self.extraRightBox)
        self.label_img_size.setObjectName(u"label_img_size")
        self.label_img_size.setMinimumSize(QSize(30, 40))
        self.label_img_size.setMaximumSize(QSize(20, 16777215))
        self.label_img_size.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.label_img_size)

        self.spinBox_conf_2 = QSpinBox(self.extraRightBox)
        self.spinBox_conf_2.setObjectName(u"spinBox_conf_2")
        self.spinBox_conf_2.setStyleSheet(u"background: rgb(52, 59, 72);\n"
"border-radius: 2px;\n"
"border: 1px solid rgb(187, 145, 246);\n"
"")
        self.spinBox_conf_2.setMinimum(320)
        self.spinBox_conf_2.setMaximum(1280)
        self.spinBox_conf_2.setValue(640)

        self.horizontalLayout_11.addWidget(self.spinBox_conf_2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.verticalSpacer = QSpacerItem(20, 352, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        self.leftBox = QFrame(self.styleSheet)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy5)
        self.leftBox.setMinimumSize(QSize(0, 0))
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.appMargins.addWidget(self.leftBox)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"detect", None))
        self.btn_imgs.setText(QCoreApplication.translate("MainWindow", u"open images", None))
        self.btn_camera.setText(QCoreApplication.translate("MainWindow", u"open a camera", None))
        self.btn_video.setText(QCoreApplication.translate("MainWindow", u"open a video", None))
        self.btn_widgets_train.setText(QCoreApplication.translate("MainWindow", u"train", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"Steel plate defect detection system", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"start", None))
        self.lineEdit_mode.setText(QCoreApplication.translate("MainWindow", u"images", None))
        self.label_delay.setText(QCoreApplication.translate("MainWindow", u"delay", None))
        self.label_classes_hint.setText(QCoreApplication.translate("MainWindow", u"Total Classes", None))
        self.label_classes.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_targets_hint.setText(QCoreApplication.translate("MainWindow", u"Total Targets", None))
        self.label_targets.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_FPS_hint.setText(QCoreApplication.translate("MainWindow", u"FPS", None))
        self.label_FPS.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_video.setText("")
        self.label_result.setText("")
        self.label_status.setText(QCoreApplication.translate("MainWindow", u"welcome", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"device", None))
        self.comboBox_device.setItemText(0, QCoreApplication.translate("MainWindow", u"GPU", None))
        self.comboBox_device.setItemText(1, QCoreApplication.translate("MainWindow", u"CPU", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"epoch", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Training parameter setting", None))
        self.lineEdit_weights.setText(QCoreApplication.translate("MainWindow", u"pre-trained weights path", None))
        self.pushButton_weights.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"batchsize", None))
        self.pushButton_data.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.lineEdit_data.setText(QCoreApplication.translate("MainWindow", u"data path", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"data", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"weights", None))
        self.pushButton_train.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Training parameter setting by yaml", None))
        self.pushButton_yamlTrain.setText(QCoreApplication.translate("MainWindow", u"Train", None))
        self.label_hyp.setText(QCoreApplication.translate("MainWindow", u"hyp parameter", None))
        self.pushButton_hyp.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.label_thyp.setText(QCoreApplication.translate("MainWindow", u"train parameter", None))
        self.pushButton_thyp.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.plainTextEdit_yaml.setPlainText(QCoreApplication.translate("MainWindow", u"lr0: 0.01  # initial learning rate (SGD=1E-2, Adam=1E-3)\n"
"lrf: 0.01  # final OneCycleLR learning rate (lr0 * lrf)\n"
"momentum: 0.937  # SGD momentum/Adam beta1\n"
"weight_decay: 0.0005  # optimizer weight decay 5e-4\n"
"warmup_epochs: 3.0  # warmup epochs (fractions ok)\n"
"warmup_momentum: 0.8  # warmup initial momentum\n"
"warmup_bias_lr: 0.1  # warmup initial bias lr\n"
"box: 0.05  # box loss gain\n"
"cls: 0.5  # cls loss gain\n"
"cls_pw: 1.0  # cls BCELoss positive_weight\n"
"obj: 1.0  # obj loss gain (scale with pixels)\n"
"obj_pw: 1.0  # obj BCELoss positive_weight\n"
"iou_t: 0.20  # IoU training threshold\n"
"anchor_t: 4.0  # anchor-multiple threshold\n"
"# anchors: 3  # anchors per output layer (0 to ignore)\n"
"fl_gamma: 0.0  # focal loss gamma (efficientDet default gamma=1.5)\n"
"hsv_h: 0.015  # image HSV-Hue augmentation (fraction)\n"
"hsv_s: 0.7  # image HSV-Saturation augmentation (fraction)\n"
"hsv_v: 0.4  # image HSV-Value augmentation (fraction)\n"
"degrees: 0.0  # image rotation (+/- deg)\n"
""
                        "translate: 0.1  # image translation (+/- fraction)\n"
"scale: 0.5  # image scale (+/- gain)\n"
"shear: 0.0  # image shear (+/- deg)\n"
"perspective: 0.0  # image perspective (+/- fraction), range 0-0.001\n"
"flipud: 0.0  # image flip up-down (probability)\n"
"fliplr: 0.5  # image flip left-right (probability)\n"
"mosaic: 1.0  # image mosaic (probability)\n"
"mixup: 0.05  # image mixup (probability)\n"
"copy_paste: 0.0  # image copy paste (probability)\n"
"paste_in: 0.05  # image copy paste (probability), use 0 for faster training\n"
"loss_ota: 1 # use ComputeLossOTA, use 0 for faster training\n"
"", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"NEW PAGE TEST", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Model", None))
        self.comboBox_select_model.setItemText(0, QCoreApplication.translate("MainWindow", u"yolov7.pt", None))
        self.comboBox_select_model.setItemText(1, QCoreApplication.translate("MainWindow", u"yolov7tiny.pt", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IOU", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Conf", None))
        self.label_img_size.setText(QCoreApplication.translate("MainWindow", u"imgS", None))
    # retranslateUi

