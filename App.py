# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'App.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
    QToolButton, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(980, 560)
        self.stackedWidget = QStackedWidget(Dialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 990, 560))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setStyleSheet("""
        #page {
            background-color: #f0f0f0;
        }
        """)
        self.frame_5 = QFrame(self.page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(720, 260, 191, 171))
        self.frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.label_5 = QLabel(self.frame_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 30, 151, 21))
        self.label_5.setStyleSheet(u"color: rgb(101, 119, 152);\n"
"font: 700 15pt \"Yu Gothic UI\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 90, 191, 41))
        self.label_6.setStyleSheet(u"color: rgba(45, 45, 45, 120);\n"
"font: 700 26pt \"Tahoma\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, -12, 1001, 71))
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.search = QLineEdit(self.frame_2)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(200, 30, 181, 26))
        self.search_button = QPushButton(self.frame_2)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setGeometry(QRect(160, 30, 31, 26))
        self.search_button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        icon = QIcon()
        icon.addFile(u"icons/search_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_button.setIcon(icon)
        self.search_button.setFlat(True)
        self.settings_button = QPushButton(self.frame_2)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(870, 30, 31, 26))
        self.settings_button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/settings_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.settings_button.setIcon(icon1)
        self.settings_button.setFlat(True)
        self.exit_button = QPushButton(self.frame_2)
        self.exit_button.setObjectName(u"exit_button")
        self.exit_button.setGeometry(QRect(920, 30, 31, 26))
        self.exit_button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"icons/exit_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.exit_button.setIcon(icon2)
        self.exit_button.setFlat(True)
        self.info_button = QPushButton(self.frame_2)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(820, 30, 31, 26))
        self.info_button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"icons/info_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_button.setIcon(icon3)
        self.info_button.setFlat(True)
        self.welcome_label = QLabel(self.page)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(190, 80, 531, 101))
        self.welcome_label.setStyleSheet(
    'font: 900 28pt "Arial";'
    'color: #000000;'
)
        self.frame_4 = QFrame(self.page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(460, 260, 191, 171))
        self.frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 30, 151, 21))
        self.label_3.setStyleSheet(u"color: rgb(101, 119, 152);\n"
"font: 700 15pt \"Yu Gothic UI\";")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 90, 191, 41))
        self.label_4.setStyleSheet(u"color: rgba(45, 45, 45, 120);\n"
"font: 700 26pt \"Tahoma\";")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(200, 260, 191, 171))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 40px;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 151, 21))
        self.label.setStyleSheet(u"color: rgb(101, 119, 152);\n"
"font: 700 15pt \"Yu Gothic UI\";")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 90, 191, 41))
        self.label_2.setStyleSheet(u"color: rgba(45, 45, 45, 120);\n"
"font: 700 26pt \"Tahoma\";")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frame = QFrame(self.page)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, -1, 151, 571))
        self.frame.setStyleSheet(u"\n"
"background-color: rgb(25, 86, 179);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.Students_button = QPushButton(self.frame)
        self.Students_button.setObjectName(u"Students_button")
        self.Students_button.setGeometry(QRect(0, 140, 151, 61))
        self.Students_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"background-color: rgb(25, 86, 179);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"icons/Student's_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Students_button.setIcon(icon4)
        self.Students_button.setIconSize(QSize(60, 80))
        self.Students_button.setCheckable(False)
        self.Students_button.setChecked(False)
        self.Students_button.setAutoRepeat(False)
        self.Students_button.setAutoExclusive(False)
        self.Students_button.setFlat(True)
        self.Icon_tool_button = QToolButton(self.frame)
        self.Icon_tool_button.setObjectName(u"Icon_tool_button")
        self.Icon_tool_button.setGeometry(QRect(10, 0, 121, 61))
        self.Icon_tool_button.setStyleSheet(u"QToolButton {\n"
"  background-color: transparent;\n"
"  border: none;\n"
"  padding: 6px 8px;\n"
"  color: #2B2B2B;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"  background-color: rgba(0, 0, 0, 0.04);\n"
"  border-radius: 6px;\n"
"}\n"
"\n"
"QToolButton:pressed {\n"
"  background-color: rgba(0, 0, 0, 0.08);\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icons/icon_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Icon_tool_button.setIcon(icon5)
        self.Icon_tool_button.setIconSize(QSize(120, 120))
        self.Grades_button = QPushButton(self.frame)
        self.Grades_button.setObjectName(u"Grades_button")
        self.Grades_button.setGeometry(QRect(0, 260, 151, 61))
        self.Grades_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"background-color: rgb(25, 86, 179);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"icons/grades_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Grades_button.setIcon(icon6)
        self.Grades_button.setIconSize(QSize(70, 50))
        self.Grades_button.setFlat(True)
        self.Attendance_button = QPushButton(self.frame)
        self.Attendance_button.setObjectName(u"Attendance_button")
        self.Attendance_button.setGeometry(QRect(0, 320, 151, 61))
        self.Attendance_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"background-color: rgb(25, 86, 179);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"icons/Attendance_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Attendance_button.setIcon(icon7)
        self.Attendance_button.setIconSize(QSize(50, 80))
        self.Attendance_button.setFlat(True)
        self.Statistics_button = QPushButton(self.frame)
        self.Statistics_button.setObjectName(u"Statistics_button")
        self.Statistics_button.setGeometry(QRect(0, 380, 151, 61))
        self.Statistics_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"background-color: rgb(25, 86, 179);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u"icons/statistics_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Statistics_button.setIcon(icon8)
        self.Statistics_button.setIconSize(QSize(70, 50))
        self.Statistics_button.setFlat(True)
        self.Classes_button = QPushButton(self.frame)
        self.Classes_button.setObjectName(u"Classes_button")
        self.Classes_button.setGeometry(QRect(0, 200, 151, 61))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(16)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Classes_button.sizePolicy().hasHeightForWidth())
        self.Classes_button.setSizePolicy(sizePolicy)
        self.Classes_button.setMouseTracking(True)
        self.Classes_button.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Classes_button.setAutoFillBackground(False)
        self.Classes_button.setStyleSheet(u"QPushButton{font: 900 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"background-color: rgb(25, 86, 179);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"color: rgb(255, 255, 255);\n"
"text-align: left;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u"icons/classes_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Classes_button.setIcon(icon9)
        self.Classes_button.setIconSize(QSize(60, 60))
        self.Classes_button.setFlat(True)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_n = QLabel(self.page_2)
        self.label_n.setObjectName(u"label_n")
        self.label_n.setGeometry(QRect(0, -20, 991, 601))
        self.label_n.setPixmap(QPixmap(u"background.png"))
        self.frame_n = QFrame(self.page_2)
        self.frame_n.setObjectName(u"frame_n")
        self.frame_n.setGeometry(QRect(560, 50, 371, 461))
        self.frame_n.setStyleSheet(u"    background-color: rgba(255, 255, 255, 30);\n"
"    border-radius: 25px;\n"
"    border: 1px solid rgba(255, 255, 255, 140);")
        self.frame_n.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_n.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_n = QLineEdit(self.frame_n)
        self.lineEdit_n.setObjectName(u"lineEdit_n")
        self.lineEdit_n.setGeometry(QRect(40, 160, 291, 41))
        self.lineEdit_n.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    background-color: rgba(255, 255, 255, 220);\n"
"    border: none;\n"
"    color: #003366;\n"
"}\n"
"")
        self.lineEdit_2_n = QLineEdit(self.frame_n)
        self.lineEdit_2_n.setObjectName(u"lineEdit_2_n")
        self.lineEdit_2_n.setGeometry(QRect(40, 250, 291, 41))
        self.lineEdit_2_n.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    background-color: rgba(255, 255, 255, 220);\n"
"    border: none;\n"
"    color: #003366;\n"
"}\n"
"")
        self.lineEdit_2_n.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_n = QPushButton(self.frame_n)
        self.pushButton_n.setObjectName(u"pushButton_n")
        self.pushButton_n.setGeometry(QRect(80, 340, 211, 51))
        self.pushButton_n.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 52, 101);\n"
"    font: 700 10pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 72, 141); \n"
"}\n"
"")
        self.toolButton_2 = QToolButton(self.frame_n)
        self.toolButton_2.setObjectName(u"toolButton_2")
        self.toolButton_2.setGeometry(QRect(300, 260, 21, 22))
        self.toolButton_2.setStyleSheet(u"QToolButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: rgba(0,0,0,0.1);\n"
"    border-radius: 6px;\n"
"}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u"icons/hide_pss.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toolButton_2.setIcon(icon10)
        self.toolButton_2.setAutoRaise(True)
        self.label_12 = QLabel(self.page_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(1630, 100, 491, 71))
        self.label_12.setStyleSheet(u"font: 900 28pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.frame_6 = QFrame(self.page_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(1050, 50, 371, 461))
        self.frame_6.setStyleSheet(u"    background-color: rgba(255, 255, 255, 30);\n"
"    border-radius: 25px;\n"
"    border: 1px solid rgba(255, 255, 255, 140);")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.lineEdit_5 = QLineEdit(self.frame_6)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(32, 160, 301, 41))
        self.lineEdit_5.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    background-color: rgba(255, 255, 255, 220);\n"
"    border: none;\n"
"    color: #003366;\n"
"}\n"
"")
        self.lineEdit_6 = QLineEdit(self.frame_6)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setGeometry(QRect(30, 250, 301, 41))
        self.lineEdit_6.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    background-color: rgba(255, 255, 255, 220);\n"
"    border: none;\n"
"    color: #003366;\n"
"}\n"
"")
        self.lineEdit_6.setEchoMode(QLineEdit.EchoMode.Password)
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(80, 340, 211, 51))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(0, 52, 101);\n"
"    font: 700 10pt \"Segoe UI\";\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 72, 141); \n"
"}\n"
"")
        self.toolButton = QToolButton(self.frame_6)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(300, 260, 21, 22))
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    padding: 0px;\n"
"}\n"
"\n"
"QToolButton:hover {\n"
"    background-color: rgba(0,0,0,0.1);\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.toolButton.setIcon(icon10)
        self.toolButton.setAutoRaise(True)
        self.label_6_n = QLabel(self.page_2)
        self.label_6_n.setObjectName(u"label_6_n")
        self.label_6_n.setGeometry(QRect(30, 180, 291, 71))
        self.label_6_n.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 11pt \"Segoe UI Semibold\";")
        self.label_4_n = QLabel(self.page_2)
        self.label_4_n.setObjectName(u"label_4_n")
        self.label_4_n.setGeometry(QRect(600, 280, 51, 16))
        self.label_4_n.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1180, 70, 111, 81))
        self.label_8.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255); font-size:25pt;")
        self.label_5_n = QLabel(self.page_2)
        self.label_5_n.setObjectName(u"label_5_n")
        self.label_5_n.setGeometry(QRect(20, 100, 491, 71))
        self.label_5_n.setStyleSheet(u"font: 900 28pt \"Segoe UI Black\";\n"
"color: rgb(255, 255, 255);")
        self.label_11 = QLabel(self.page_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(1080, 280, 49, 16))
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7_n = QLabel(self.page_2)
        self.label_7_n.setObjectName(u"label_7_n")
        self.label_7_n.setGeometry(QRect(660, 450, 191, 21))
        self.label_errn = QLabel(Dialog)
        self.label_errn.setObjectName(u"label")
        self.label_errn.setGeometry(QRect(570, 480, 370, 16))
        self.label_errn.setStyleSheet(u"QLabel {\n"
                                      "    color: rgb(211, 47, 47);  /* error red */\n"
                                      "    font: 600 10pt \"Segoe UI\";\n"
                                      "}\n"
                                      "")
        self.label_errn.hide()
        self.label_3_n = QLabel(self.page_2)
        self.label_3_n.setObjectName(u"label_3_n")
        self.label_3_n.setGeometry(QRect(600, 190, 61, 16))
        self.label_3_n.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(1080, 190, 81, 16))
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_13 = QLabel(self.page_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(1640, 180, 291, 71))
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 600 11pt \"Segoe UI Semibold\";")
        self.label_10 = QLabel(self.page_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(1140, 450, 191, 16))
        self.label_2_n = QLabel(self.page_2)
        self.label_2_n.setObjectName(u"label_2_n")
        self.label_2_n.setGeometry(QRect(640, 90, 221, 44))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(10)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.label_2_n.sizePolicy().hasHeightForWidth())
        self.label_2_n.setSizePolicy(sizePolicy1)
        self.label_2_n.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255,255,255); font-size:25pt;")
        self.label_2_n.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Dialog)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Entered Grades :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"", None))
        self.search_button.setText("")
        self.settings_button.setText("")
        self.exit_button.setText("")
        self.info_button.setText("")
        self.welcome_label.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Total Classes :", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Total Students :", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"", None))
        self.Students_button.setText(QCoreApplication.translate("Dialog", u"     Students", None))
        self.Icon_tool_button.setText(QCoreApplication.translate("Dialog", u"...", None))
        self.Grades_button.setText(QCoreApplication.translate("Dialog", u"        Grades", None))
        self.Attendance_button.setText(QCoreApplication.translate("Dialog", u"   Attendance", None))
        self.Statistics_button.setText(QCoreApplication.translate("Dialog", u"      Statistics", None))
        self.Classes_button.setText(QCoreApplication.translate("Dialog", u"        Classes", None))
        self.label_n.setText("")
        self.pushButton_n.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.toolButton_2.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Welcome back !", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.toolButton.setText("")
        self.label_6_n.setText(QCoreApplication.translate("Dialog", u"Manage students and classes\n"
"simply, efficiently, and securely.", None))
        self.label_4_n.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.label_5_n.setText(QCoreApplication.translate("Dialog", u"Welcome to ClassManager", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"Password", None))
        self.label_7_n.setText(QCoreApplication.translate("Dialog", u"Already have an account? <a href=\"login\">Log in</a>\n"
"", None))
        self.label_3_n.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"Manage students and classes\n"
"simply, efficiently, and securely.", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Don't have an account? <a href=\"create\">Create one</a>\n"
"", None))
        self.label_2_n.setText(QCoreApplication.translate("Dialog", u"Creat account", None))
    # retranslateUi



