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
    QToolButton, QWidget,QComboBox, QDateEdit, QTableWidget, QTableWidgetItem)

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
        self.settings_button = QPushButton(self.frame_2)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(870, 30, 31, 26))
        self.settings_button.setStyleSheet(u"QPushButton:hover {\n"
"background-color: rgba(0, 0, 0, 0.1);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"icons/home_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
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
        self.welcome_label.setGeometry(QRect(190, 80, 801, 101))
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
        self.Add_top_btn = QPushButton(self.frame_2)
        self.Add_top_btn.setObjectName(u"Add_top_btn")
        self.Add_top_btn.setGeometry(QRect(480, 40, 81, 31))
        self.Add_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                       "color :rgb(24, 182, 255);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                       "}\n"
                                       "")
        self.Add_top_btn.setFlat(True)
        self.View_top_btn = QPushButton(self.frame_2)
        self.View_top_btn.setObjectName(u"View_top_btn")
        self.View_top_btn.setGeometry(QRect(570, 40, 81, 31))
        self.View_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")
        self.View_top_btn.setFlat(True)
        self.dateEdit = QDateEdit(self.page)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(730, 200, 221, 41))
        self.dateEdit.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
                                    "border: 1px solid grey;\n"
                                    "padding: 6px 8px;\n"
                                    "background-color: rgb(255,255,255)\n"
                                    "}\n"
                                    "\n"
                                    "QDateEdit::up-button {width: 0;}\n"
                                    "QDateEdit::down-button {width: 0;}\n"
                                    "\n"
                                    "QDateEdit:hover {border: 2px solid black;\n"
                                    "padding : 5px 7px;}\n"
                                    "\n"
                                    "QDateEdit:focus {border: 2px solid #0078d7;\n"
                                    "\n"
                                    "}")
        self.dateEdit.setDate(QDate.currentDate())
        self.Firstnameline = QLineEdit(self.page)
        self.Firstnameline.setObjectName(u"Firstnameline")
        self.Firstnameline.setGeometry(QRect(300, 130, 221, 41))
        self.Firstnameline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                         "border-radius : 15px ;\n"
                                         "padding : 6px 8px;\n"
                                         "background-color: rgb(255,255,255)\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:hover{border: 2px solid black;\n"
                                         "padding : 5px 7px;\n"
                                         "}\n"
                                         "\n"
                                         "QLineEdit:focus {\n"
                                         "  border : 2px solid #0078d7;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.GenderComboBox = QComboBox(self.page)
        self.GenderComboBox.addItem("")
        self.GenderComboBox.addItem("")
        self.GenderComboBox.setObjectName(u"GenderComboBox")
        self.GenderComboBox.setGeometry(QRect(300, 200, 221, 41))
        self.GenderComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
                                          "border-radius : 15px ;\n"
                                          "padding : 6px 8px;\n"
                                          "background-color: rgb(255,255,255)\n"
                                          "}\n"
                                          "QComboBox:drop-down { width: 0;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:hover{border: 2px solid black ;\n"
                                          "padding : 5px 7px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:focus {\n"
                                          "  border : 2px solid #0078d7;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.GenderComboBox.setMaxVisibleItems(2)
        self.Firstname = QLabel(self.page)
        self.Firstname.setObjectName(u"Firstname")
        self.Firstname.setGeometry(QRect(170, 140, 111, 16))
        self.Firstname.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                     "font: 600 12pt \"Segoe UI\";")
        self.lastname = QLabel(self.page)
        self.lastname.setObjectName(u"lastname")
        self.lastname.setGeometry(QRect(580, 140, 141, 16))
        self.lastname.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.birth = QLabel(self.page)
        self.birth.setObjectName(u"birth")
        self.birth.setGeometry(QRect(580, 210, 141, 16))
        self.birth.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                 "font: 600 12pt \"Segoe UI\";")
        self.Class1 = QLabel(self.page)
        self.Class1.setObjectName(u"Class1")
        self.Class1.setGeometry(QRect(170, 310, 121, 16))
        self.Class1.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.Gender = QLabel(self.page)
        self.Gender.setObjectName(u"Gender")
        self.Gender.setGeometry(QRect(170, 210, 121, 16))
        self.Gender.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.phone = QLabel(self.page)
        self.phone.setObjectName(u"phone")
        self.phone.setGeometry(QRect(580, 410, 141, 16))
        self.phone.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                 "font: 600 12pt \"Segoe UI\";")
        self.Email = QLabel(self.page)
        self.Email.setObjectName(u"Email")
        self.Email.setGeometry(QRect(170, 410, 121, 16))
        self.Email.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                 "font: 600 12pt \"Segoe UI\";")
        self.Address = QLabel(self.page)
        self.Address.setObjectName(u"Address")
        self.Address.setGeometry(QRect(170, 480, 121, 16))
        self.Address.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                   "font: 600 12pt \"Segoe UI\";")
        self.label_21 = QLabel(self.page)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(180, 85, 201, 31))
        self.label_21.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                    "color: rgb(51, 51, 51);")
        self.lastnameline = QLineEdit(self.page)
        self.lastnameline.setObjectName(u"lastnameline")
        self.lastnameline.setGeometry(QRect(730, 130, 221, 41))
        self.lastnameline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                        "border-radius : 15px ;\n"
                                        "padding : 6px 8px;\n"
                                        "background-color: rgb(255,255,255)\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:hover{border: 2px solid black;\n"
                                        "padding : 5px 7px;\n"
                                        "}\n"
                                        "\n"
                                        "QLineEdit:focus {\n"
                                        "  border : 2px solid #0078d7;\n"
                                        "}\n"
                                        "\n"
                                        "")
        self.label_22 = QLabel(self.page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(180, 255, 251, 31))
        self.label_22.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                    "color: rgb(51, 51, 51);")
        self.ClassComboBox = QComboBox(self.page)
        self.ClassComboBox.setObjectName(u"ClassComboBox")

        self.ClassComboBox.setGeometry(QRect(300, 300, 221, 41))
        self.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
                                         "border-radius : 15px ;\n"
                                         "padding : 6px 8px;  \n"
                                         "background-color: rgb(255,255,255)\n"
                                         "}\n"
                                         "QComboBox:drop-down { width: 0;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox:hover{border: 2px solid black;\n"
                                         "padding : 5px 7px;\n"
                                         "}\n"
                                         "\n"
                                         "QComboBox:focus {\n"
                                         "  border : 2px solid #0078d7;\n"
                                         "}\n"
                                         "\n"
                                         "")
        self.errclasse = QLabel(self.page)
        self.errclasse.setObjectName(u"errclasse")
        self.errclasse.setGeometry(QRect(310, 340, 300, 16))
        self.errclasse.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errclasse.hide()
        self.label_23 = QLabel(self.page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(180, 355, 181, 31))
        self.label_23.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                    "color: rgb(51, 51, 51);")
        self.Emailine = QLineEdit(self.page)
        self.Emailine.setObjectName(u"Emailine")
        self.Emailine.setGeometry(QRect(300, 400, 221, 41))
        self.Emailine.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                    "border-radius : 15px ;\n"
                                    "padding : 6px 8px;\n"
                                    "background-color: rgb(255,255,255)\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:hover{border: 2px solid black;\n"
                                    "padding : 5px 7px;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit:focus {\n"
                                    "  border : 2px solid #0078d7;\n"
                                    "}\n"
                                    "\n"
                                    "")
        self.AdressLine = QLineEdit(self.page)
        self.AdressLine.setObjectName(u"AdressLine")
        self.AdressLine.setGeometry(QRect(300, 470, 221, 41))
        self.AdressLine.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                      "border-radius : 15px ;\n"
                                      "padding : 6px 8px ;\n"
                                      "background-color: rgb(255,255,255)\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{border: 2px solid black;\n"
                                      "padding : 5px 7px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "  border : 2px solid #0078d7;\n"
                                      "}")
        self.Numberline = QLineEdit(self.page)
        self.Numberline.setObjectName(u"Numberline")
        self.Numberline.setGeometry(QRect(730, 400, 221, 41))
        self.Numberline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
                                      "border-radius : 15px ;\n"
                                      "padding : 6px 8px;\n"
                                      "background-color: rgb(255,255,255)\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:hover{border: 2px solid black;\n"
                                      "padding : 5px 7px;\n"
                                      "}\n"
                                      "\n"
                                      "QLineEdit:focus {\n"
                                      "  border : 2px solid #0078d7;\n"
                                      "}\n"
                                      "\n"
                                      "")
        self.label_24 = QLabel(self.page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(160, 60, 221, 41))
        self.label_24.setStyleSheet(u"\n"
                                    "font: 9pt \"Segoe UI\";\n"
                                    "color: rgb(229, 83, 61);")
        self.Add_button = QPushButton(self.page)
        self.Add_button.setObjectName(u"Add_button")
        self.Add_button.setGeometry(QRect(760, 500, 91, 31))
        self.Add_button.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                      "color : rgb(255,255,255);\n"
                                      "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                      "border-radius: 15px}\n"
                                      "\n"
                                      "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                      "color: rgb(255,255,255)\n"
                                      "}")
        self.Cancel_button = QPushButton(self.page)
        self.Cancel_button.setObjectName(u"Cancel_button")
        self.Cancel_button.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_button.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                         "color: rgb(55, 65, 81);\n"
                                         "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                         "border-radius: 15px\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.requirederrfirst = QLabel(self.page)
        self.requirederrfirst.setObjectName(u"requirederrfirst")
        self.requirederrfirst.setGeometry(QRect(310, 170, 111, 16))
        self.requirederrfirst.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.requirederrlast = QLabel(self.page)
        self.requirederrlast.setObjectName(u"requirederrlast")
        self.requirederrlast.setGeometry(QRect(740, 170, 111, 16))
        self.requirederrlast.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.tableWidget = QTableWidget(self.page)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(170, 130, 791, 411))
        self.tableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setStyleSheet(u"QHeaderView::section {\n"
                                       "background-color: rgb(25,86,179);\n"
                                       "color: white;\n"
                                       "font: 600 10pt \"Inter\";"
                                       "padding: 6px\n"
                                       "}\n"
                                       "QHeaderView::section:hover {\n"
                                       "background-color: rgb(20,70,150);\n"
                                       "padding: 6px\n"
                                       "}\n"
                                       "QHeaderView::section:pressed {\n"
                                       "background-color: rgb(15,55,120);\n"
                                       "padding: 6px\n"
                                       "}")
        self.ClassComboBox2 = QComboBox(self.page)
        self.ClassComboBox2.setObjectName(u"ClassComboBox2")
        self.ClassComboBox2.setGeometry(QRect(740, 80, 221, 41))
        self.ClassComboBox2.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
                                          "border-radius : 15px ;\n"
                                          "padding : 6px 8px;  \n"
                                          "background-color: rgb(255,255,255)\n"
                                          "}\n"
                                          "QComboBox:drop-down { width: 0;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:hover{border: 2px solid black;\n"
                                          "padding : 5px 7px;\n"
                                          "}\n"
                                          "\n"
                                          "QComboBox:focus {\n"
                                          "  border : 2px solid #0078d7;\n"
                                          "}\n"
                                          "\n"
                                          "")
        self.class2 = QLabel(self.page)
        self.class2.setObjectName(u"class2")
        self.class2.setGeometry(QRect(680, 90, 41, 16))
        self.class2.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.Edit_Button = QPushButton(self.page)
        self.Edit_Button.setObjectName(u"Edit_Button")
        self.Edit_Button.setGeometry(QRect(760, 500, 91, 31))
        self.Edit_Button.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.requirederrfirst_2 = QLabel(self.page)
        self.requirederrfirst_2.setObjectName(u"requirederrfirst_2")
        self.requirederrfirst_2.setGeometry(QRect(310, 450, 111, 16))
        self.requirederrfirst_2.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.requirederrfirst_3 = QLabel(self.page)
        self.requirederrfirst_3.setObjectName(u"requirederrfirst_3")
        self.requirederrfirst_3.setGeometry(QRect(740, 450, 111, 16))
        self.requirederrfirst_3.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.back_button = QPushButton(self.page)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setGeometry(QRect(860, 500, 91, 31))
        self.back_button.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                       "color: rgb(55, 65, 81);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.stackedWidget.addWidget(self.page)
        self.tableWidget.raise_()
        self.requirederrfirst.raise_()
        self.requirederrlast.raise_()
        self.label_24.raise_()
        self.dateEdit.raise_()
        self.Firstnameline.raise_()
        self.GenderComboBox.raise_()
        self.Firstname.raise_()
        self.lastname.raise_()
        self.birth.raise_()
        self.Class1.raise_()
        self.Gender.raise_()
        self.phone.raise_()
        self.Email.raise_()
        self.Address.raise_()
        self.label_21.raise_()
        self.lastnameline.raise_()
        self.label_22.raise_()
        self.ClassComboBox.raise_()
        self.label_23.raise_()
        self.Emailine.raise_()
        self.AdressLine.raise_()
        self.Numberline.raise_()
        self.Add_button.raise_()
        self.Cancel_button.raise_()
        self.ClassComboBox2.raise_()
        self.class2.raise_()
        self.Edit_Button.raise_()
        self.requirederrfirst_2.raise_()
        self.requirederrfirst_3.raise_()
        self.back_button.raise_()




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






        self.stackedWidget.setCurrentIndex(1)
        self.retranslateUi(Dialog)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Class Manager", None))
        icon = QIcon()
        icon.addFile(u"icons/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Dialog.setWindowIcon(icon)
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Entered Grades :", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"", None))

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

        self.Add_top_btn.setText(QCoreApplication.translate("Dialog", u"Add Student", None))
        self.View_top_btn.setText(QCoreApplication.translate("Dialog", u"View Students", None))
        self.Firstnameline.setText("")
        self.GenderComboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Male", None))
        self.GenderComboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Female", None))
        self.Firstname.setText(QCoreApplication.translate("Dialog", u"First Name*     :", None))
        self.lastname.setText(QCoreApplication.translate("Dialog", u"Last Name*          :", None))
        self.birth.setText(QCoreApplication.translate("Dialog", u"Date Of Birth*      :", None))
        self.Class1.setText(QCoreApplication.translate("Dialog", u"Class*               : ", None))
        self.Gender.setText(QCoreApplication.translate("Dialog", u"Gender*           :", None))
        self.phone.setText(QCoreApplication.translate("Dialog", u"Contact Number  :", None))
        self.Email.setText(QCoreApplication.translate("Dialog", u"Email                :", None))
        self.Address.setText(QCoreApplication.translate("Dialog", u"Home Address :", None))
        self.label_21.setText(QCoreApplication.translate("Dialog", u"Personal info ", None))
        self.lastnameline.setText("")
        self.label_22.setText(QCoreApplication.translate("Dialog", u"Academic info ", None))
        self.label_23.setText(QCoreApplication.translate("Dialog", u"Contact info ", None))
        self.Emailine.setText("")
        self.Emailine.setPlaceholderText(QCoreApplication.translate("Dialog", u"example123@gmail.com", None))
        self.AdressLine.setText("")
        self.Numberline.setText("")
        self.Numberline.setPlaceholderText(QCoreApplication.translate("Dialog", u"", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Fields marked with * are required\n"
                                                                   "", None))
        self.Add_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.Cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.requirederrfirst.setText(QCoreApplication.translate("Dialog", u"This field is required", None))
        self.requirederrlast.setText(QCoreApplication.translate("Dialog", u"This field is required", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Full Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Date of birth", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Gender", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"Contact Number", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Address", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Actions", None));
        self.class2.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.Edit_Button.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.requirederrfirst_2.setText(QCoreApplication.translate("Dialog", u"Invalid Email", None))
        self.errclasse.setText(QCoreApplication.translate("Dialog", u"There are no classes yet", None))
        self.requirederrfirst_3.setText(QCoreApplication.translate("Dialog", u"Invalid Number", None))
        self.back_button.setText(QCoreApplication.translate("Dialog", u"Back", None))
        self.label_n.setText("")
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
        self.label_2_n.setText(QCoreApplication.translate("Dialog", u"Create account", None))
    # retranslateUi




