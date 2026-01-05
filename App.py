# -*- coding: utf-8 -*-
#from PyQt6.QtWidgets.QMainWindow import enterEvent
################################################################################
## Form generated from reading UI file 'App.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from Functions import animate_title

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QPropertyAnimation, QEasingCurve, QTimer)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLabel,
                               QLineEdit, QPushButton, QSizePolicy, QStackedWidget,
                               QToolButton, QWidget, QComboBox, QDateEdit, QTableWidget, QTableWidgetItem, QHeaderView,
                               QAbstractItemView, QScrollArea, QGraphicsDropShadowEffect)


class InfoButton(QPushButton):
    def __init__(self, parent=None,page=None,text=None,pos=None):
        super().__init__(parent)
        self.label = QLabel(page)
        self.label.setText(text)
        self.label.setGeometry(pos)


        self.label.setStyleSheet(u"QLabel{\n"
                                 "background-color: #E6EBF2;\n"
                                 "border : 1px solid #CBD5E1;\n"
                                 "color: #1F2A44;\n"
                                 "border-radius: 5px;\n"
                                 "font-size: 12px;\n"
                                 "}")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.hide()
    def enterEvent(self, event):
        self.label.show()
        self.label.raise_()
    def leaveEvent(self, event):
        self.label.hide()

class HoverButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setDuration(100)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)
        self.original_rect = None


    def enterEvent(self, event):
        self.anim.stop()
        if self.original_rect == None:
              self.original_rect = self.geometry()

        self.anim.setStartValue(self.geometry())
        target = QRect(
            self.original_rect.x() - 3,
            self.original_rect.y() - 3,
            self.original_rect.width() + 6,
            self.original_rect.height() + 6
        )
        self.anim.setEndValue(target)
        self.anim.start()

        super().enterEvent(event)

    def leaveEvent(self, event):
        if self.original_rect:
            self.anim.stop()
            self.anim.setStartValue(self.geometry())


            self.anim.setEndValue(self.original_rect)
            self.anim.start()
        super().leaveEvent(event)




class HoverFrame(QFrame):
    def __init__(self, parent=None,
                 frame=None,
                 start=None,
                 end=None,
                 start2=None,
                 end2=None,
                 title=None,
                 start3=None,
                 end3=None,
                 title2=None,
                 start4=None,
                 end4=None,
                 bars=None,
                 canvas=None,
                 ax=None,
                 combo1=None,
                 com1s=None,
                 com1e = None,

                 lbl=None,
                 lbls=None,
                 lble=None,
                 wedges=None,
                 texts=None):
        super().__init__(parent)
        self.anim = QPropertyAnimation(self, b"geometry")


        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.Type.InOutQuad)


        self.frame = frame

        self.start = start
        self.end = end
        self.start2 = start2
        self.end2 = end2
        self.title = title
        self.start3 = start3
        self.end3 = end3
        self.title2 = title2
        self.start4 = start4
        self.end4 = end4
        self.bars = bars
        self.canvas = canvas
        self.ax = ax
        self.combo1 = combo1
        self.texts = texts

        self.lbl = lbl

        self.com1s = com1s
        self.com1e = com1e



        self.lbls = lbls
        self.lble = lble

        self.wedges = wedges
        self.saved_colors = None



        self.anim2 = QPropertyAnimation(self.frame, b"geometry")
        self.anim2.setDuration(200)

    def enterEvent(self, event):
        self.saved_colors = None
        self.anim2.stop()
        self.anim.stop()
        self.anim.setStartValue(self.start)
        self.anim.setEndValue(self.end)
        self.anim.start()


        self.anim2.setStartValue(self.start2)
        self.anim2.setEndValue(self.end2)
        self.anim2.start()

        if self.title:
            animate_title(self.title,self.start3,self.end3)

        if self.title2:
            animate_title(self.title2,self.start4,self.end4)

        if self.bars and self.canvas :
            for bar in self.bars:
                bar.set_facecolor("#9e9e9e")
                bar.set_edgecolor("#616161")
            self.ax.tick_params(axis="x", colors="#9e9e9e")
            self.ax.tick_params(axis="y", colors="#9e9e9e")
            for spine in self.ax.spines.values():
                spine.set_edgecolor("#9e9e9e")
            self.canvas.draw()
        if self.frame :
            self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid grey;")
        if self.title :
            self.title2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                         "color: #808080;")
        if self.combo1 and self.lbl :
            animate_title(self.combo1,self.com1s,self.com1e)

            animate_title(self.lbl,self.lbls,self.lble)



        if self.wedges :
            if self.saved_colors == None:
                self.saved_colors = [wedge.get_facecolor() for wedge in self.wedges]
            for widget in self.wedges:
                widget.set_facecolor("#9e9e9e")
            for t in self.texts:
                t.set_color("#9e9e9e")

            self.canvas.draw()





        super().enterEvent(event)
    def leaveEvent(self, event):

        self.anim.stop()
        self.anim.setStartValue(self.end)

        self.anim.setEndValue(self.start)
        self.anim.start()

        self.anim2.stop()
        self.anim2.setStartValue(self.end2)
        self.anim2.setEndValue(self.start2)
        self.anim2.start()

        if self.title:
            animate_title(self.title,self.end3,self.start3)

        if self.title2:
            animate_title(self.title2,self.end4,self.start4)

        if self.bars and self.canvas :
            for bar in self.bars:
                bar.set_facecolor("#2563EB")
                bar.set_edgecolor("#124187")
            self.ax.tick_params(axis="x", colors="#000000")
            self.ax.tick_params(axis="y", colors="#000000")
            for spine in self.ax.spines.values():
                spine.set_edgecolor("#000000")

            self.canvas.draw()
        if self.frame :
            self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")
        if self.title :
            self.title2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                 "color: rgb(34, 34, 34);")
        if self.combo1 and self.lbl :
            animate_title(self.combo1,self.com1e,self.com1s)

            animate_title(self.lbl,self.lble,self.lbls)

        if self.wedges :
            for wedge,color in zip(self.wedges,self.saved_colors):
                wedge.set_facecolor(color)
            for t in self.texts:
                t.set_color("#000000")
            self.canvas.draw()

        super().leaveEvent(event)

            




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
        self.Students_button.setGeometry(QRect(0, 200, 151, 61))
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
        self.Classes_button.setGeometry(QRect(0, 140, 151, 61))
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
                                    "}\n"
                                    "QDateEdit::drop-down {\n"
                                    "subcontrol-origin: padding;\n"
                                    "subcontrol-position: right center;\n"
                                    "width: 30px;\n"          
                                    "border-top-right-radius: 15px;\n"    
                                    "border-bottom-right-radius: 15px;\n" 
                                      "}\n"
                                    "QDateEdit::down-arrow {\n"
                                    "image: url(icons/calendar.png);\n"
                                    "width: 15px;\n"
                                    "height: 15px;\n"
                                    "}")
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setCalendarPopup(True)
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
        self.Add_button = HoverButton(self.page)
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
        self.Cancel_button = HoverButton(self.page)
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

        self.birtherr = QLabel(self.page)
        self.birtherr.setObjectName(u"birtherr")
        self.birtherr.setGeometry(QRect(730, 240, 221, 41))
        self.birtherr.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.tableWidget = QTableWidget(self.page)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
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
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(160, 130, 820, 340))
        self.tableWidget.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(40)
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
                                       "}\n"
                                       "QTableWidget {"
                                       "border: none;\n}"
                                       "QTableWidget QLineEdit {\n"
                                       "background-color: rgb(255,255,255);"
                                       "border-bottom: 4px;"
                                       "}\n"
                                       "QScrollBar::vertical {\n"
                                       "background-color: rgb(224,224,224);\n"
                                       "border: none;\n"
                                       "width: 12px;\n"
                                       "border-radius: 5px;\n"
                                       "}"
                                       "QScrollBar::handle:vertical {\n"
                                       "background: rgb(25,86,179);\n"
                                       "min-width: 20px;\n"
                                       "border-radius: 6px;\n"
                                       "}\n"
                                       "QScrollBar::handle:vertical:hover {\n"
                                       "background: rgb(20,70,150);\n"
                                       "}\n"
                                       "QScrollBar::add-line:vertical,\n"
                                       "QScrollBar::sub-line:vertical {\n"
                                       "border: none;\n"
                                       "background: none;\n"
                                       "width: 0px;\n"
                                       "}\n"
                                       "QScrollBar::add-page:vertical,\n"
                                       "QScrollBar::sub-page:vertical {\n"
                                       "background: none;\n"
                                       "}\n"
                                       )

        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.setColumnWidth(0, 80)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 50)
        self.tableWidget.setColumnWidth(4, 100)
        self.tableWidget.setColumnWidth(5, 100)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setColumnWidth(7, 70)
        self.Save_button = HoverButton(self.page)
        self.Save_button.setObjectName(u"Edit_button")
        self.Save_button.setGeometry(QRect(760, 500, 91, 31))

        self.Save_button.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                      "color : rgb(255,255,255);\n"
                                      "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                      "border-radius: 15px}\n"
                                      "\n"
                                      "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                      "color: rgb(255,255,255)\n"
                                      "}")
        self.Edit_button = HoverButton(self.page)
        self.Edit_button.setObjectName(u"Edit_button")
        self.Edit_button.setGeometry(QRect(810, 500, 91, 31))

        self.Edit_button.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.Cancel_button2 = HoverButton(self.page)
        self.Cancel_button2.setObjectName(u"Cancel_button2")
        self.Cancel_button2.setGeometry(QRect(860, 500, 91, 31))

        self.Cancel_button2.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                         "color: rgb(55, 65, 81);\n"
                                         "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                         "border-radius: 15px\n"
                                         "}\n"
                                         "\n"
                                         "QPushButton:hover {background-color: rgb(156,163,175)}")

        self.errlbl = QLabel(self.page)
        self.errlbl.setObjectName(u"requirederrfirst_2")
        self.errlbl.setGeometry(QRect(180, 80, 270, 16))
        self.errlbl.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errlbl.hide()

        self.errlbl2 = QLabel(self.page)
        self.errlbl2.setObjectName(u"requirederrfirst_22")
        self.errlbl2.setGeometry(QRect(180, 160, 270, 16))
        self.errlbl2.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errlbl2.hide()

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

        self.requirederrfirst_2 = QLabel(self.page)
        self.requirederrfirst_2.setObjectName(u"requirederrfirst_2")
        self.requirederrfirst_2.setGeometry(QRect(310, 450, 111, 16))
        self.requirederrfirst_2.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.requirederrfirst_3 = QLabel(self.page)
        self.requirederrfirst_3.setObjectName(u"requirederrfirst_3")
        self.requirederrfirst_3.setGeometry(QRect(740, 450, 111, 16))
        self.requirederrfirst_3.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.Classnameline = QLineEdit(self.page)
        self.Classnameline.setObjectName(u"Classnameline")
        self.Classnameline.setGeometry(QRect(290, 90, 221, 41))
        self.Classnameline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.requirederrclass = QLabel(self.page)
        self.requirederrclass.setObjectName(u"requirederrclass")
        self.requirederrclass.setGeometry(QRect(290, 135, 200, 16))
        self.requirederrclass.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.classname = QLabel(self.page)
        self.classname.setObjectName(u"classname")
        self.classname.setGeometry(QRect(170, 100, 101, 16))
        self.classname.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                     "font: 600 12pt \"Segoe UI\";")
        self.maxstudents = QLabel(self.page)
        self.maxstudents.setObjectName(u"maxstudents")
        self.maxstudents.setGeometry(QRect(590, 100, 141, 16))
        self.maxstudents.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                       "font: 600 12pt \"Segoe UI\";")
        self.maxstudentsline = QLineEdit(self.page)
        self.maxstudentsline.setObjectName(u"maxstudentsline")
        self.maxstudentsline.setGeometry(QRect(730, 90, 221, 41))
        self.maxstudentsline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.requirederrmax = QLabel(self.page)
        self.requirederrmax.setObjectName(u"requirederrmax")
        self.requirederrmax.setGeometry(QRect(730, 135, 200, 16))
        self.requirederrmax.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.tableWidget_class = QTableWidget(self.page)
        if (self.tableWidget_class.columnCount() < 4):
            self.tableWidget_class.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_class.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_class.setObjectName(u"tableWidget_class")
        self.tableWidget_class.setGeometry(QRect(170, 200, 801, 280))
        self.tableWidget_class.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget_class.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_class.verticalHeader().setStretchLastSection(False)
        self.tableWidget_class.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_class.setShowGrid(True)
        self.tableWidget_class.setStyleSheet(u"QHeaderView::section {\n"
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
                                       "}\n"
                                       "QTableWidget {border: none}\n"
                                       "QTableWidget QLineEdit {\n"
                                       "background-color: rgb(255,255,255);"
                                       "}\n"
                                       "QScrollBar::vertical {\n"
                                             "background-color: rgb(224,224,224);\n"
                                             "border: none;\n"
                                             "width: 12px;\n"
                                             "border-radius: 5px;\n"
                                             "}"
                                       "QScrollBar::handle:vertical {\n"
                                             "background: rgb(25,86,179);\n"
                                             "min-width: 20px;\n"
                                             "border-radius: 6px;\n"
                                             "}\n"
                                       "QScrollBar::handle:vertical:hover {\n"
                                             "background: rgb(20,70,150);\n"
                                             "}\n"
                                       "QScrollBar::add-line:vertical,\n"
                                       "QScrollBar::sub-line:vertical {\n"
                                             "border: none;\n"
                                             "background: none;\n"
                                             "width: 0px;\n"
                                             "}\n"
                                       "QScrollBar::add-page:vertical,\n"
                                       "QScrollBar::sub-page:vertical {\n"
                                             "background: none;\n"
                                             "}\n"
                                             )
        self.tableWidget_class.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_class.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_class.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_class.verticalHeader().setHighlightSections(False)

        self.Save_button2 = HoverButton(self.page)
        self.Save_button2.setObjectName(u"Edit_button")
        self.Save_button2.setGeometry(QRect(760, 500, 91, 31))
        self.Save_button2.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.Edit_button2 = HoverButton(self.page)
        self.Edit_button2.setObjectName(u"Edit_button")
        self.Edit_button2.setGeometry(QRect(810, 500, 91, 31))
        self.Edit_button2.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.Cancel_button3 = HoverButton(self.page)
        self.Cancel_button3.setObjectName(u"Cancel_button2")
        self.Cancel_button3.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_button3.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                          "color: rgb(55, 65, 81);\n"
                                          "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                          "border-radius: 15px\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: rgb(156,163,175)}")


        self.add_button_class = HoverButton(self.page)
        self.add_button_class.setObjectName(u"add_button_class")
        self.add_button_class.setGeometry(QRect(470, 160, 101, 31))
        self.add_button_class.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                            "color : rgb(255,255,255);\n"
                                            "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                            "border-radius: 15px}\n"
                                            "\n"
                                            "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                            "color: rgb(255,255,255)\n"
                                            "}")
        self.cancel_button_class = HoverButton(self.page)
        self.cancel_button_class.setObjectName(u"cancel_button_class")
        self.cancel_button_class.setGeometry(QRect(580, 160, 101, 31))
        self.cancel_button_class.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                               "color: rgb(55, 65, 81);\n"
                                               "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                               "border-radius: 15px\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.ClassComboBox3 = QComboBox(self.page)
        self.ClassComboBox3.setObjectName(u"ClassComboBox3")
        self.ClassComboBox3.setGeometry(QRect(740, 80, 221, 41))
        self.ClassComboBox3.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.class3 = QLabel(self.page)
        self.class3.setObjectName(u"class3")
        self.class3.setGeometry(QRect(680, 90, 41, 16))
        self.class3.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")

        self.tableWidget_grades = QTableWidget(self.page)
        self.tableWidget_grades.setColumnCount(2)
        __qtablewidgetitemg = QTableWidgetItem()
        self.tableWidget_grades.setHorizontalHeaderItem(0, __qtablewidgetitemg)
        __qtablewidgetitem1g = QTableWidgetItem()
        self.tableWidget_grades.setHorizontalHeaderItem(1, __qtablewidgetitem1g)


        self.tableWidget_grades.setObjectName(u"tableWidget")
        self.tableWidget_grades.setGeometry(QRect(160, 130, 820, 340))
        self.tableWidget_grades.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.ArrowCursor))
        self.tableWidget_grades.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget_grades.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_grades.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_grades.setShowGrid(True)
        self.tableWidget_grades.setStyleSheet(u"QHeaderView::section {\n"
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
                                       "}\n"
                                       "QTableWidget {"
                                       "border: none;\n}"
                                       "QTableWidget QLineEdit {\n"
                                       "background-color: rgb(255,255,255);"
                                       "border-bottom: 4px;"
                                       "}\n"
                                       "QScrollBar::horizontal {\n"
                                              "background-color: rgb(224,224,224);\n"
                                              "border: none;\n"
                                              "height: 15px;\n"
                                              "border-radius: 5px;\n"
                                              "}"
                                       "QScrollBar::handle:horizontal {\n"
                                              "background: rgb(25,86,179);\n"
                                              "min-width: 15px;\n"
                                              "border-radius: 6px;\n"
                                              "height: 15px;\n"
                                              "}\n"
                                       "QScrollBar::handle:horizontal:hover {\n"
                                              "background: rgb(20,70,150);\n"
                                              "height: 20px;\n"
                                              "}\n"
                                       "QScrollBar::add-line:horizontal,\n"
                                        "QScrollBar::sub-line:horizontal {\n"
                                                   "border: none;\n"
                                                  " background: none;\n"
                                                   "width: 0px;\n"
                                               "}\n"
                                        "QScrollBar::add-page:horizontal,\n"
                                        "QScrollBar::sub-page:horizontal {\n"
                                                    "background: none;\n"
                                                "}\n"
                                        "QScrollBar::vertical {\n"
                                              "background-color: rgb(224,224,224);\n"
                                              "border: none;\n"
                                              "width: 12px;\n"
                                              "border-radius: 5px;\n"
                                              "}"
                                        "QScrollBar::handle:vertical {\n"
                                              "background: rgb(25,86,179);\n"
                                              "min-width: 20px;\n"
                                              "border-radius: 6px;\n"
                                              "}\n"
                                        "QScrollBar::handle:vertical:hover {\n"
                                              "background: rgb(20,70,150);\n"
                                              "}\n"
                                        "QScrollBar::add-line:vertical,\n"
                                        "QScrollBar::sub-line:vertical {\n"
                                              "border: none;\n"
                                              "background: none;\n"
                                              "width: 0px;\n"
                                              "}\n"
                                        "QScrollBar::add-page:vertical,\n"
                                        "QScrollBar::sub-page:vertical {\n"
                                              "background: none;\n"
                                              "}\n"
                                              )

        self.tableWidget_grades.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_grades.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_grades.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_grades.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_grades.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)

        self.Subject_top_btn = QPushButton(self.frame_2)
        self.Subject_top_btn.setObjectName(u"Add_top_btn")
        self.Subject_top_btn.setGeometry(QRect(480, 40, 81, 31))
        self.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                       "color :rgb(24, 182, 255);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                       "}\n"
                                       "")
        self.Subject_top_btn.setFlat(True)
        self.grades_top_btn = QPushButton(self.frame_2)
        self.grades_top_btn.setObjectName(u"View_top_btn")
        self.grades_top_btn.setGeometry(QRect(570, 40, 81, 31))
        self.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")
        self.grades_top_btn.setFlat(True)

        self.tableWidget_subjects = QTableWidget(self.page)

        if (self.tableWidget_subjects.columnCount() < 3):
            self.tableWidget_subjects.setColumnCount(3)
        __qtablewidgetitems = QTableWidgetItem()
        self.tableWidget_subjects.setHorizontalHeaderItem(0, __qtablewidgetitems)
        __qtablewidgetitem1s = QTableWidgetItem()
        self.tableWidget_subjects.setHorizontalHeaderItem(1, __qtablewidgetitem1s)
        __qtablewidgetitem2s = QTableWidgetItem()
        self.tableWidget_subjects.setHorizontalHeaderItem(2, __qtablewidgetitem2s)
        __qtablewidgetitem3s = QTableWidgetItem()


        self.tableWidget_subjects.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_subjects.setObjectName(u"tableWidget_class")
        self.tableWidget_subjects.setGeometry(QRect(270, 220, 610, 270))
        self.tableWidget_subjects.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget_subjects.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_subjects.verticalHeader().setStretchLastSection(False)
        self.tableWidget_subjects.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_subjects.setShowGrid(True)
        self.tableWidget_subjects.setStyleSheet(u"QHeaderView::section {\n"
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
                                       "}\n"
                                       "QTableWidget {border: none}\n"
                                       "QTableWidget QLineEdit {\n"
                                       "background-color: rgb(255,255,255);"
                                       "}\n"
                                       "QScrollBar::vertical {\n"
                                                "background-color: rgb(224,224,224);\n"
                                                "border: none;\n"
                                                "width: 12px;\n"
                                                "border-radius: 5px;\n"
                                                "}"
                                       "QScrollBar::handle:vertical {\n"
                                                "background: rgb(25,86,179);\n"
                                                "min-width: 20px;\n"
                                                "border-radius: 6px;\n"
                                                "}\n"
                                       "QScrollBar::handle:vertical:hover {\n"
                                                "background: rgb(20,70,150);\n"
                                                "}\n"
                                       "QScrollBar::add-line:vertical,\n"
                                       "QScrollBar::sub-line:vertical {\n"
                                                "border: none;\n"
                                                "background: none;\n"
                                                "width: 0px;\n"
                                                "}\n"
                                       "QScrollBar::add-page:vertical,\n"
                                       "QScrollBar::sub-page:vertical {\n"
                                                "background: none;\n"
                                                "}\n"
                                                )
        self.tableWidget_subjects.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_subjects.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_subjects.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_subjects.verticalHeader().setHighlightSections(False)
        self.tableWidget_subjects.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.add_button_subject = HoverButton(self.page)
        self.add_button_subject.setObjectName(u"add_button_class")
        self.add_button_subject.setGeometry(QRect(470, 160, 101, 31))
        self.add_button_subject.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                              "color : rgb(255,255,255);\n"
                                              "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                              "border-radius: 15px}\n"
                                              "\n"
                                              "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                              "color: rgb(255,255,255)\n"
                                              "}")
        self.cancel_button_subject = HoverButton(self.page)
        self.cancel_button_subject.setObjectName(u"cancel_button_class")
        self.cancel_button_subject.setGeometry(QRect(580, 160, 101, 31))
        self.cancel_button_subject.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                               "color: rgb(55, 65, 81);\n"
                                               "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                               "border-radius: 15px\n"
                                               "}\n"
                                               "\n"
                                               "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.subjectline = QLineEdit(self.page)
        self.subjectline.setObjectName(u"Classnameline")
        self.subjectline.setGeometry(QRect(290, 90, 221, 41))
        self.subjectline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.requirederrsubject = QLabel(self.page)
        self.requirederrsubject.setObjectName(u"requirederrclass")
        self.requirederrsubject.setGeometry(QRect(290, 135, 200, 16))
        self.requirederrsubject.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.subject_name = QLabel(self.page)
        self.subject_name.setObjectName(u"classname")
        self.subject_name.setGeometry(QRect(170, 100, 101, 16))
        self.subject_name.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                     "font: 600 12pt \"Segoe UI\";")
        self.coeff = QLabel(self.page)
        self.coeff.setObjectName(u"maxstudents")
        self.coeff.setGeometry(QRect(590, 100, 141, 16))
        self.coeff.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                       "font: 600 12pt \"Segoe UI\";")
        self.coeffline = QLineEdit(self.page)
        self.coeffline.setObjectName(u"maxstudentsline")
        self.coeffline.setGeometry(QRect(730, 90, 221, 41))
        self.coeffline.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.requirederrcoeff = QLabel(self.page)
        self.requirederrcoeff.setObjectName(u"requirederrmax")
        self.requirederrcoeff.setGeometry(QRect(730, 135, 200, 16))
        self.requirederrcoeff.setStyleSheet(u"color: rgb(220, 38, 38);")

        self.Save_button3 = HoverButton(self.page)
        self.Save_button3.setObjectName(u"Edit_button")
        self.Save_button3.setGeometry(QRect(760, 500, 91, 31))
        self.Save_button3.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                        "color : rgb(255,255,255);\n"
                                        "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                        "border-radius: 15px}\n"
                                        "\n"
                                        "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                        "color: rgb(255,255,255)\n"
                                        "}")
        self.Edit_button3 = HoverButton(self.page)
        self.Edit_button3.setObjectName(u"Edit_button")
        self.Edit_button3.setGeometry(QRect(810, 500, 91, 31))
        self.Edit_button3.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                        "color : rgb(255,255,255);\n"
                                        "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                        "border-radius: 15px}\n"
                                        "\n"
                                        "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                        "color: rgb(255,255,255)\n"
                                        "}")
        self.Cancel_button4 = HoverButton(self.page)
        self.Cancel_button4.setObjectName(u"Cancel_button2")
        self.Cancel_button4.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_button4.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                          "color: rgb(55, 65, 81);\n"
                                          "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                          "border-radius: 15px\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: rgb(156,163,175)}")
        self.Save_button4 = QPushButton(self.page)
        self.Save_button4.setObjectName(u"Edit_button")
        self.Save_button4.setGeometry(QRect(760, 500, 91, 31))
        self.Save_button4.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.Edit_button4 = HoverButton(self.page)
        self.Edit_button4.setObjectName(u"Edit_button")
        self.Edit_button4.setGeometry(QRect(810, 500, 91, 31))
        self.Edit_button4.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                       "color : rgb(255,255,255);\n"
                                       "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                       "border-radius: 15px}\n"
                                       "\n"
                                       "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                       "color: rgb(255,255,255)\n"
                                       "}")
        self.Cancel_button5 = HoverButton(self.page)
        self.Cancel_button5.setObjectName(u"Cancel_button2")
        self.Cancel_button5.setGeometry(QRect(860, 500, 91, 31))
        self.Cancel_button5.setStyleSheet(u"QPushButton {background-color: rgb(209, 213, 219);\n"
                                          "color: rgb(55, 65, 81);\n"
                                          "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                          "border-radius: 15px\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {background-color: rgb(156,163,175)}")

        self.errlbl3 = QLabel(self.page)
        self.errlbl3.setObjectName(u"requirederrfirst_22")
        self.errlbl3.setGeometry(QRect(180, 160, 270, 16))
        self.errlbl3.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.errlbl3.hide()

        self.info = QLabel(self.page)
        self.info.setObjectName(u"requirederrfirst_22")
        self.info.setGeometry(QRect(170, 80, 430, 16))
        self.info.setStyleSheet(u"color: #2196F3;")
        self.info.hide()

        self.dateEdit2 = QDateEdit(self.page)
        self.dateEdit2.setObjectName(u"dateEdit")
        self.dateEdit2.setGeometry(QRect(260, 80, 221, 41))
        self.dateEdit2.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
                                    "}\n"
                                    "QDateEdit::drop-down {\n"
                                    "subcontrol-origin: padding;\n"
                                    "subcontrol-position: right center;\n"
                                    "width: 30px;\n"
                                    "border-top-right-radius: 15px;\n"
                                    "border-bottom-right-radius: 15px;\n"
                                    "}\n"
                                    "QDateEdit::down-arrow {\n"
                                    "image: url(icons/calendar.png);\n"
                                    "width: 15px;\n"
                                    "height: 15px;\n"
                                    "}")
        self.dateEdit2.setDate(QDate.currentDate())
        self.dateEdit2.setCalendarPopup(True)

        self.ClassComboBox4 = QComboBox(self.page)
        self.ClassComboBox4.setObjectName(u"ClassComboBox3")
        self.ClassComboBox4.setGeometry(QRect(740, 80, 221, 41))
        self.ClassComboBox4.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

        self.class4 = QLabel(self.page)
        self.class4.setObjectName(u"class3")
        self.class4.setGeometry(QRect(680, 90, 41, 16))
        self.class4.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.date = QLabel(self.page)
        self.date.setObjectName(u"class3")
        self.date.setGeometry(QRect(200, 90, 41, 16))
        self.date.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")

        self.tableWidget_att = QTableWidget(self.page)

        if (self.tableWidget_att.columnCount() < 3):
            self.tableWidget_att.setColumnCount(3)
        __qtablewidgetitema = QTableWidgetItem()
        self.tableWidget_att.setHorizontalHeaderItem(0, __qtablewidgetitema)
        __qtablewidgetitem1a = QTableWidgetItem()
        self.tableWidget_att.setHorizontalHeaderItem(1, __qtablewidgetitem1a)
        __qtablewidgetitem2a = QTableWidgetItem()
        self.tableWidget_att.setHorizontalHeaderItem(2, __qtablewidgetitem2a)
        __qtablewidgetitem3s = QTableWidgetItem()

        self.tableWidget_att.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_att.setObjectName(u"tableWidget_class")
        self.tableWidget_att.setGeometry(QRect(270, 150, 610, 340))
        self.tableWidget_att.horizontalHeader().setDefaultSectionSize(190)
        self.tableWidget_att.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_att.verticalHeader().setStretchLastSection(False)
        self.tableWidget_att.verticalHeader().setDefaultSectionSize(40)
        self.tableWidget_att.setShowGrid(True)
        self.tableWidget_att.setStyleSheet(u"QHeaderView::section {\n"
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
                                                "}\n"
                                                "QTableWidget {border: none}\n"
                                                "QTableWidget QLineEdit {\n"
                                                "background-color: rgb(255,255,255);"
                                                "}\n"
                                                "QScrollBar::vertical {\n"
                                                "background-color: rgb(224,224,224);\n"
                                                "border: none;\n"
                                                "width: 12px;\n"
                                                "border-radius: 5px;\n"
                                                "}"
                                                "QScrollBar::handle:vertical {\n"
                                                "background: rgb(25,86,179);\n"
                                                "min-width: 20px;\n"
                                                "border-radius: 6px;\n"
                                                "}\n"
                                                "QScrollBar::handle:vertical:hover {\n"
                                                "background: rgb(20,70,150);\n"
                                                "}\n"
                                                "QScrollBar::add-line:vertical,\n"
                                                "QScrollBar::sub-line:vertical {\n"
                                                "border: none;\n"
                                                "background: none;\n"
                                                "width: 0px;\n"
                                                "}\n"
                                                "QScrollBar::add-page:vertical,\n"
                                                "QScrollBar::sub-page:vertical {\n"
                                                "background: none;\n"
                                                "}\n"
                                                )
        self.tableWidget_att.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_att.setSelectionMode(QAbstractItemView.NoSelection)
        self.tableWidget_att.setEditTriggers(QTableWidget.NoEditTriggers)
        header = self.tableWidget_att.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        vheader = self.tableWidget_att.verticalHeader()
        vheader.setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget_att.verticalHeader().setHighlightSections(False)
        self.tableWidget_att.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.performane = QPushButton(self.frame_2)
        self.performane.setObjectName(u"performane")
        self.performane.setGeometry(QRect(410, 40, 81, 31))
        self.performane.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                      "color :rgb(24, 182, 255);\n"
                                      "border: none;\n"
                                      "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                      "}\n"
                                      "")
        self.performane.setFlat(True)
        self.ranking = QPushButton(self.frame_2)
        self.ranking.setObjectName(u"ranking")
        self.ranking.setGeometry(QRect(570, 40, 81, 31))
        self.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                   "font: 700 9pt \"Yu Gothic UI\";")
        self.ranking.setFlat(True)
        self.attendancetop = QPushButton(self.frame_2)
        self.attendancetop.setObjectName(u"attendancetop")
        self.attendancetop.setGeometry(QRect(490, 40, 81, 31))
        self.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")
        self.attendancetop.setFlat(True)
        self.other = QPushButton(self.frame_2)
        self.other.setObjectName(u"other")
        self.other.setGeometry(QRect(650, 40, 81, 31))
        self.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                 "font: 700 9pt \"Yu Gothic UI\";")
        self.other.setFlat(True)
        self.Graph_frame_2 = HoverFrame(self.page,start=QRect(590, 140, 351, 321),end=QRect(555, 105, 421, 391),start2=QRect(200, 140, 351, 321),end2=QRect(235, 175, 281, 251))
        self.Graph_frame_2.setObjectName(u"scrollArea_2")
        self.Graph_frame_2.setGeometry(QRect(590, 140, 351, 321))
        self.Graph_frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 15px;\n"
                                       "border: 2px solid black;")



        self.Graph_frame = HoverFrame(self.page,frame=self.Graph_frame_2,start=QRect(200, 140, 351, 321),end=QRect(165, 105, 421, 391),start2=QRect(590, 140, 351, 321),end2=QRect(625, 175, 281, 251))
        self.Graph_frame_2.frame = self.Graph_frame
        self.Graph_frame_2.anim2 = QPropertyAnimation(self.Graph_frame, b"geometry")
        self.Graph_frame.setObjectName(u"scrollArea_3")
        self.Graph_frame.setGeometry(QRect(200, 140, 351, 321))
        self.Graph_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                        "border-radius: 15px;\n"
                                       "border: 2px solid black;")

        self.Graph_frame_5 = QFrame(self.page)
        self.Graph_frame_5.setObjectName(u"Graph_frame_5")
        self.Graph_frame_5.setGeometry(QRect(200, 140, 351, 341))
        self.Graph_frame_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 40px;\n"
                                         "border: 1px solid rgb(25, 86, 179),")
        self.Graph_frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Graph_frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.top1_name = QLabel(self.Graph_frame_5)
        self.top1_name.setObjectName(u"top1_name")
        self.top1_name.setGeometry(QRect(0, 40, 131, 61))
        self.top1_name.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                     "\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "font: 600 11pt \"Segoe UI\";\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top1_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_name = QLabel(self.Graph_frame_5)
        self.top2_name.setObjectName(u"top2_name")
        self.top2_name.setGeometry(QRect(0, 100, 131, 61))
        self.top2_name.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #F8F8F8;\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top2_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_name = QLabel(self.Graph_frame_5)
        self.top4_name.setObjectName(u"top4_name")
        self.top4_name.setGeometry(QRect(0, 220, 131, 61))
        self.top4_name.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #F0F0F0;\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top4_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_name = QLabel(self.Graph_frame_5)
        self.top3_name.setObjectName(u"top3_name")
        self.top3_name.setGeometry(QRect(0, 160, 131, 61))
        self.top3_name.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #F5F5F5;\n"
                                     "border: none;\n"
                                     "border-left: 1px solid rgb(25, 86, 179)")
        self.top3_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_name = QLabel(self.Graph_frame_5)
        self.top5_name.setObjectName(u"top5_name")
        self.top5_name.setGeometry(QRect(0, 280, 131, 61))
        self.top5_name.setStyleSheet(u"border:none;\n"
                                     "border-left :1px solid rgb(25, 86, 179);\n"
                                     "border-bottom :1px solid rgb(25, 86, 179);\n"
                                     "border-top-left-radius: 0px;\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 40px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "font: 600 11pt \"Segoe UI\";\n"
                                     "background-color: #E8E8E8")
        self.top5_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_id = QLabel(self.Graph_frame_5)
        self.top2_id.setObjectName(u"top2_id")
        self.top2_id.setGeometry(QRect(130, 100, 111, 61))
        self.top2_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color : #F8F8F8;\n"
                                   "border: none")
        self.top2_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_id = QLabel(self.Graph_frame_5)
        self.top4_id.setObjectName(u"top4_id")
        self.top4_id.setGeometry(QRect(130, 220, 111, 61))
        self.top4_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color: #F0F0F0;\n"
                                   "border: none")
        self.top4_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_id = QLabel(self.Graph_frame_5)
        self.top5_id.setObjectName(u"top5_id")
        self.top5_id.setGeometry(QRect(130, 280, 111, 61))
        self.top5_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color: #E8E8E8;\n"
                                   "border: none;\n"
                                   "border-bottom :1px solid rgb(25, 86, 179);\n"
                                   "")
        self.top5_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_id = QLabel(self.Graph_frame_5)
        self.top3_id.setObjectName(u"top3_id")
        self.top3_id.setGeometry(QRect(130, 160, 111, 61))
        self.top3_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "background-color: #F5F5F5;\n"
                                   "border: none")
        self.top3_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_id = QLabel(self.Graph_frame_5)
        self.top1_id.setObjectName(u"top1_id")
        self.top1_id.setGeometry(QRect(130, 40, 111, 61))
        self.top1_id.setStyleSheet(u"color: #6B7280;\n"
                                   "font: 10pt \"Segoe UI\";\n"
                                   "border: none")
        self.top1_id.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_grade = QLabel(self.Graph_frame_5)
        self.top1_grade.setObjectName(u"top1_grade")
        self.top1_grade.setGeometry(QRect(240, 40, 111, 61))
        self.top1_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "border: none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)\n"
                                      "")
        self.top1_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_grade = QLabel(self.Graph_frame_5)
        self.top2_grade.setObjectName(u"top2_grade")
        self.top2_grade.setGeometry(QRect(240, 100, 111, 61))
        self.top2_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color : #F8F8F8;\n"
                                      "border: none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)")
        self.top2_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_grade = QLabel(self.Graph_frame_5)
        self.top5_grade.setObjectName(u"top5_grade")
        self.top5_grade.setGeometry(QRect(240, 280, 111, 61))
        self.top5_grade.setStyleSheet(u"border: none;\n"
                                      "border-right :1px solid rgb(25, 86, 179);\n"
                                      "border-bottom :1px solid rgb(25, 86, 179);\n"
                                      "border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 40px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color: #E8E8E8")
        self.top5_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_grade = QLabel(self.Graph_frame_5)
        self.top4_grade.setObjectName(u"top4_grade")
        self.top4_grade.setGeometry(QRect(240, 220, 111, 61))
        self.top4_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color: #F0F0F0;\n"
                                      "border:none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)")
        self.top4_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_grade = QLabel(self.Graph_frame_5)
        self.top3_grade.setObjectName(u"top3_grade")
        self.top3_grade.setGeometry(QRect(240, 160, 111, 61))
        self.top3_grade.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                      "font: 600 11pt \"Segoe UI\";\n"
                                      "border-top-right-radius: 0px;\n"
                                      "border-bottom-left-radius: 0px;\n"
                                      "border-bottom-right-radius: 0px;\n"
                                      "color: rgb(33, 130, 12);\n"
                                      "background-color: #F5F5F5;\n"
                                      "border: none;\n"
                                      "border-right: 1px solid rgb(25, 86, 179)")
        self.top3_grade.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.full_name = QLabel(self.Graph_frame_5)
        self.full_name.setObjectName(u"full_name")
        self.full_name.setGeometry(QRect(0, 0, 131, 41))
        self.full_name.setStyleSheet(u"border-top-left-radius: 40px;\n"
                                     "font: 600 13pt \"Sitka\";\n"
                                     "color: #F9FAFB;\n"
                                     "border-top-right-radius: 0px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "background-color: rgb(25, 86, 179)")
        self.full_name.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grade_lbl = QLabel(self.Graph_frame_5)
        self.grade_lbl.setObjectName(u"grade_lbl")
        self.grade_lbl.setGeometry(QRect(240, 0, 111, 41))
        self.grade_lbl.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                     "font: 600 13pt \"Sitka\";\n"
                                     "color: #F9FAFB;\n"
                                     "border-top-right-radius: 40px;\n"
                                     "border-bottom-left-radius: 0px;\n"
                                     "border-bottom-right-radius: 0px;\n"
                                     "background-color: rgb(25, 86, 179)")
        self.grade_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.id_lbl = QLabel(self.Graph_frame_5)
        self.id_lbl.setObjectName(u"id_lbl")
        self.id_lbl.setGeometry(QRect(130, 0, 111, 41))
        self.id_lbl.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                  "font: 600 13pt \"Sitka\";\n"
                                  "color: #F9FAFB;\n"
                                  "border-top-right-radius: 0px;\n"
                                  "border-bottom-left-radius: 0px;\n"
                                  "border-bottom-right-radius: 0px;\n"
                                  "background-color: rgb(25, 86, 179)")
        self.id_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_16 = QLabel(self.page)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(290, 100, 49, 16))
        self.comboBox2_1 = QComboBox(self.page)
        self.comboBox2_1.setObjectName(u"comboBox2_1")
        self.comboBox2_1.setGeometry(QRect(680, 500, 231, 41))
        self.comboBox2_1.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.class2_1 = QLabel(self.page)
        self.class2_1.setObjectName(u"class2")
        self.class2_1.setGeometry(QRect(620, 510, 41, 16))
        self.class2_1.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.class2_2 = QLabel(self.page)
        self.class2_2.setObjectName(u"class2_2")
        self.class2_2.setGeometry(QRect(230, 510, 41, 16))
        self.class2_2.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.comboBox2_2 = QComboBox(self.page)
        self.comboBox2_2.setObjectName(u"comboBox2_2")
        self.comboBox2_2.setGeometry(QRect(290, 500, 231, 41))
        self.comboBox2_2.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.average_class = QLabel(self.page)
        self.average_class.setObjectName(u"average_class")
        self.average_class.setGeometry(QRect(200, 100, 351, 31))
        self.average_class.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                         "color: rgb(34, 34, 34);")
        self.average_class.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame.title = self.average_class
        self.Graph_frame.start3 = QPoint(200, 100)
        self.Graph_frame.end3 = QPoint(200, 65)
        self.Graph_frame_2.title2 = self.average_class
        self.Graph_frame_2.start4 = QPoint(200, 100)
        self.Graph_frame_2.end4 = QPoint(200, 135)
        self.top_students = QLabel(self.page)
        self.top_students.setObjectName(u"top_students")
        self.top_students.setGeometry(QRect(200, 100, 351, 31))
        self.top_students.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                        "color: rgb(34, 34, 34);")
        self.top_students.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.subject_avaeges = QLabel(self.page)
        self.subject_avaeges.setObjectName(u"subject_avaeges")
        self.subject_avaeges.setGeometry(QRect(590, 100, 351, 31))
        self.subject_avaeges.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                           "color: rgb(34, 34, 34);")
        self.subject_avaeges.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame.title2 = self.subject_avaeges
        self.Graph_frame.start4 = QPoint(590, 100)
        self.Graph_frame.end4 = QPoint(590, 135)
        self.Graph_frame_2.title = self.subject_avaeges
        self.Graph_frame_2.start3 = QPoint(590, 100)
        self.Graph_frame_2.end3 = QPoint(590, 65)
        self.top_students_3 = QLabel(self.page)
        self.top_students_3.setObjectName(u"top_students_3")
        self.top_students_3.setGeometry(QRect(590, 100, 351, 31))
        self.top_students_3.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                          "color: rgb(34, 34, 34);")
        self.top_students_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Graph_frame_6 = QFrame(self.page)
        self.Graph_frame_6.setObjectName(u"Graph_frame_6")
        self.Graph_frame_6.setGeometry(QRect(590, 140, 351, 341))
        self.Graph_frame_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 40px;\n"
                                         "border: 1px solid rgb(25, 86, 179),")
        self.Graph_frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.Graph_frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.top1_name_2 = QLabel(self.Graph_frame_6)
        self.top1_name_2.setObjectName(u"top1_name_2")
        self.top1_name_2.setGeometry(QRect(0, 40, 131, 61))
        self.top1_name_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                       "\n"
                                       "border-top-right-radius: 0px;\n"
                                       "border-bottom-left-radius: 0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "font: 600 11pt \"Segoe UI\";\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top1_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_name_2 = QLabel(self.Graph_frame_6)
        self.top2_name_2.setObjectName(u"top2_name_2")
        self.top2_name_2.setGeometry(QRect(0, 100, 131, 61))
        self.top2_name_2.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #F8F8F8;\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top2_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_name_2 = QLabel(self.Graph_frame_6)
        self.top4_name_2.setObjectName(u"top4_name_2")
        self.top4_name_2.setGeometry(QRect(0, 220, 131, 61))
        self.top4_name_2.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #F0F0F0;\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top4_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_name_2 = QLabel(self.Graph_frame_6)
        self.top3_name_2.setObjectName(u"top3_name_2")
        self.top3_name_2.setGeometry(QRect(0, 160, 131, 61))
        self.top3_name_2.setStyleSheet(u"font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #F5F5F5;\n"
                                       "border: none;\n"
                                       "border-left: 1px solid rgb(25, 86, 179)")
        self.top3_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_name_2 = QLabel(self.Graph_frame_6)
        self.top5_name_2.setObjectName(u"top5_name_2")
        self.top5_name_2.setGeometry(QRect(0, 280, 131, 61))
        self.top5_name_2.setStyleSheet(u"border:none;\n"
                                       "border-left :1px solid rgb(25, 86, 179);\n"
                                       "border-bottom :1px solid rgb(25, 86, 179);\n"
                                       "border-top-left-radius: 0px;\n"
                                       "border-top-right-radius: 0px;\n"
                                       "border-bottom-left-radius: 40px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "font: 600 11pt \"Segoe UI\";\n"
                                       "background-color: #E8E8E8")
        self.top5_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_id_2 = QLabel(self.Graph_frame_6)
        self.top2_id_2.setObjectName(u"top2_id_2")
        self.top2_id_2.setGeometry(QRect(130, 100, 111, 61))
        self.top2_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color : #F8F8F8;\n"
                                     "border: none")
        self.top2_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_id_2 = QLabel(self.Graph_frame_6)
        self.top4_id_2.setObjectName(u"top4_id_2")
        self.top4_id_2.setGeometry(QRect(130, 220, 111, 61))
        self.top4_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color: #F0F0F0;\n"
                                     "border: none")
        self.top4_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_id_2 = QLabel(self.Graph_frame_6)
        self.top5_id_2.setObjectName(u"top5_id_2")
        self.top5_id_2.setGeometry(QRect(130, 280, 111, 61))
        self.top5_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color: #E8E8E8;\n"
                                     "border: none;\n"
                                     "border-bottom :1px solid rgb(25, 86, 179);\n"
                                     "")
        self.top5_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_id_2 = QLabel(self.Graph_frame_6)
        self.top3_id_2.setObjectName(u"top3_id_2")
        self.top3_id_2.setGeometry(QRect(130, 160, 111, 61))
        self.top3_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "background-color: #F5F5F5;\n"
                                     "border: none")
        self.top3_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_id_2 = QLabel(self.Graph_frame_6)
        self.top1_id_2.setObjectName(u"top1_id_2")
        self.top1_id_2.setGeometry(QRect(130, 40, 111, 61))
        self.top1_id_2.setStyleSheet(u"color: #6B7280;\n"
                                     "font: 10pt \"Segoe UI\";\n"
                                     "border: none")
        self.top1_id_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top1_grade_2 = QLabel(self.Graph_frame_6)
        self.top1_grade_2.setObjectName(u"top1_grade_2")
        self.top1_grade_2.setGeometry(QRect(240, 40, 111, 61))
        self.top1_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "border: none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)\n"
                                        "")
        self.top1_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top2_grade_2 = QLabel(self.Graph_frame_6)
        self.top2_grade_2.setObjectName(u"top2_grade_2")
        self.top2_grade_2.setGeometry(QRect(240, 100, 111, 61))
        self.top2_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color : #F8F8F8;\n"
                                        "border: none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)")
        self.top2_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top5_grade_2 = QLabel(self.Graph_frame_6)
        self.top5_grade_2.setObjectName(u"top5_grade_2")
        self.top5_grade_2.setGeometry(QRect(240, 280, 111, 61))
        self.top5_grade_2.setStyleSheet(u"border: none;\n"
                                        "border-right :1px solid rgb(25, 86, 179);\n"
                                        "border-bottom :1px solid rgb(25, 86, 179);\n"
                                        "border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 40px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color: #E8E8E8")
        self.top5_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top4_grade_2 = QLabel(self.Graph_frame_6)
        self.top4_grade_2.setObjectName(u"top4_grade_2")
        self.top4_grade_2.setGeometry(QRect(240, 220, 111, 61))
        self.top4_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color: #F0F0F0;\n"
                                        "border:none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)")
        self.top4_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.top3_grade_2 = QLabel(self.Graph_frame_6)
        self.top3_grade_2.setObjectName(u"top3_grade_2")
        self.top3_grade_2.setGeometry(QRect(240, 160, 111, 61))
        self.top3_grade_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                        "font: 600 11pt \"Segoe UI\";\n"
                                        "border-top-right-radius: 0px;\n"
                                        "border-bottom-left-radius: 0px;\n"
                                        "border-bottom-right-radius: 0px;\n"
                                        "color: rgb(33, 130, 12);\n"
                                        "background-color: #F5F5F5;\n"
                                        "border: none;\n"
                                        "border-right: 1px solid rgb(25, 86, 179)")
        self.top3_grade_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.full_name_2 = QLabel(self.Graph_frame_6)
        self.full_name_2.setObjectName(u"full_name_2")
        self.full_name_2.setGeometry(QRect(0, 0, 131, 41))
        self.full_name_2.setStyleSheet(u"border-top-left-radius: 40px;\n"
                                       "font: 600 13pt \"Sitka\";\n"
                                       "color: #F9FAFB;\n"
                                       "border-top-right-radius: 0px;\n"
                                       "border-bottom-left-radius: 0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "background-color: rgb(25, 86, 179)")
        self.full_name_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.grade_lbl_2 = QLabel(self.Graph_frame_6)
        self.grade_lbl_2.setObjectName(u"grade_lbl_2")
        self.grade_lbl_2.setGeometry(QRect(240, 0, 111, 41))
        self.grade_lbl_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                       "font: 600 13pt \"Sitka\";\n"
                                       "color: #F9FAFB;\n"
                                       "border-top-right-radius: 40px;\n"
                                       "border-bottom-left-radius: 0px;\n"
                                       "border-bottom-right-radius: 0px;\n"
                                       "background-color: rgb(25, 86, 179)")
        self.grade_lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.id_lbl_2 = QLabel(self.Graph_frame_6)
        self.id_lbl_2.setObjectName(u"id_lbl_2")
        self.id_lbl_2.setGeometry(QRect(130, 0, 111, 41))
        self.id_lbl_2.setStyleSheet(u"border-top-left-radius: 0px;\n"
                                    "font: 600 13pt \"Sitka\";\n"
                                    "color: #F9FAFB;\n"
                                    "border-top-right-radius: 0px;\n"
                                    "border-bottom-left-radius: 0px;\n"
                                    "border-bottom-right-radius: 0px;\n"
                                    "background-color: rgb(25, 86, 179)")
        self.id_lbl_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame_3 = HoverFrame(self.page, start=QRect(590, 140, 351, 321), end=QRect(555, 105, 421, 391),
                                        start2=QRect(200, 140, 351, 321), end2=QRect(235, 175, 281, 251))
        self.Graph_frame_3.setObjectName(u"scrollArea_2")
        self.Graph_frame_3.setGeometry(QRect(590, 140, 351, 321))
        self.Graph_frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.Graph_frame_4 = HoverFrame(self.page, frame=self.Graph_frame_3, start=QRect(200, 140, 351, 321),
                                      end=QRect(165, 105, 421, 391), start2=QRect(590, 140, 351, 321),
                                      end2=QRect(625, 175, 281, 251))
        self.Graph_frame_3.frame = self.Graph_frame_4
        self.Graph_frame_3.anim2 = QPropertyAnimation(self.Graph_frame_4, b"geometry")
        self.Graph_frame_4.setObjectName(u"scrollArea_3")
        self.Graph_frame_4.setGeometry(QRect(200, 140, 351, 321))
        self.Graph_frame_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                       "border-radius: 15px;\n"
                                       "border: 2px solid black;")



        self.class2_3 = QLabel(self.page)
        self.class2_3.setObjectName(u"class2_2")
        self.class2_3.setGeometry(QRect(230, 480, 41, 16))
        self.class2_3.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.comboBox2_3 = QComboBox(self.page)
        self.comboBox2_3.setObjectName(u"comboBox2_2")
        self.comboBox2_3.setGeometry(QRect(290, 470, 231, 41))
        self.comboBox2_3.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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


        self.Graph_frame_3.combo1 = self.comboBox2_3

        self.Graph_frame_3.lbl = self.class2_3

        self.Graph_frame_3.com1s = QPoint(290, 470)
        self.Graph_frame_3.com1e = QPoint(290, 435)

        self.Graph_frame_3.lbls = QPoint(230, 480)
        self.Graph_frame_3.lble = QPoint(230, 445)


        self.Graph_frame_4.combo1 = self.comboBox2_3

        self.Graph_frame_4.lbl = self.class2_3
        self.Graph_frame_4.com1s = QPoint(290, 470)
        self.Graph_frame_4.com1e = QPoint(290, 505)

        self.Graph_frame_4.lbls = QPoint(230, 480)
        self.Graph_frame_4.lble = QPoint(230, 515)

        self.malesfemales = QLabel(self.page)
        self.malesfemales.setObjectName(u"average_class")
        self.malesfemales.setGeometry(QRect(200, 100, 351, 31))
        self.malesfemales.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                         "color: rgb(34, 34, 34);")
        self.malesfemales.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.students_per_class = QLabel(self.page)
        self.students_per_class.setObjectName(u"subject_avaeges")
        self.students_per_class.setGeometry(QRect(590, 100, 351, 31))
        self.students_per_class.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                           "color: rgb(34, 34, 34);")
        self.students_per_class.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.Graph_frame_4.title = self.malesfemales
        self.Graph_frame_4.start3 = QPoint(200, 100)
        self.Graph_frame_4.end3 = QPoint(200, 65)
        self.Graph_frame_3.title2 = self.malesfemales
        self.Graph_frame_3.start4 = QPoint(200, 100)
        self.Graph_frame_3.end4 = QPoint(200, 135)

        self.Graph_frame_4.title2 = self.students_per_class
        self.Graph_frame_4.start4 = QPoint(590, 100)
        self.Graph_frame_4.end4 = QPoint(590, 135)
        self.Graph_frame_3.title = self.students_per_class
        self.Graph_frame_3.start3 = QPoint(590, 100)
        self.Graph_frame_3.end3 = QPoint(590, 65)

        self.Graph_frame_7 = QFrame(self.page)
        self.Graph_frame_7.setObjectName(u"scrollArea_2")
        self.Graph_frame_7.setGeometry(QRect(170, 140, 511, 331))
        self.Graph_frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.Graph_frame_8 = QFrame(self.page)
        self.Graph_frame_8.setObjectName(u"scrollArea_2")
        self.Graph_frame_8.setGeometry(QRect(700, 140, 271, 221))
        self.Graph_frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
                                         "border-radius: 15px;\n"
                                         "border: 2px solid black;")

        self.comboBox2_5 = QComboBox(self.page)
        self.comboBox2_5.setObjectName(u"comboBox2_2")
        self.comboBox2_5.setGeometry(QRect(740, 370, 191, 41))
        self.comboBox2_5.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.dateEdit5 = QDateEdit(self.page)
        self.dateEdit5.setObjectName(u"dateEdit")
        self.dateEdit5.setGeometry(QRect(740, 420, 191, 41))
        self.dateEdit5.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
                                     "}\n"
                                     "QDateEdit::drop-down {\n"
                                     "subcontrol-origin: padding;\n"
                                     "subcontrol-position: right center;\n"
                                     "width: 30px;\n"
                                     "border-top-right-radius: 15px;\n"
                                     "border-bottom-right-radius: 15px;\n"
                                     "}\n"
                                     "QDateEdit::down-arrow {\n"
                                     "image: url(icons/calendar.png);\n"
                                     "width: 15px;\n"
                                     "height: 15px;\n"
                                     "}")
        self.dateEdit5.setDate(QDate.currentDate())
        self.dateEdit5.setCalendarPopup(True)

        self.comboBox2_6 = QComboBox(self.page)
        self.comboBox2_6.setObjectName(u"comboBox2_2")
        self.comboBox2_6.setGeometry(QRect(240, 490, 181, 41))
        self.comboBox2_6.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.comboBox2_7 = QComboBox(self.page)
        self.comboBox2_7.setObjectName(u"comboBox2_2")
        self.comboBox2_7.setGeometry(QRect(500, 490, 181, 41))
        self.comboBox2_7.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

        self.attendace_title = QLabel(self.page)
        self.attendace_title.setObjectName(u"average_class")
        self.attendace_title.setGeometry(QRect(170, 100, 511, 31))
        self.attendace_title.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                         "color: rgb(34, 34, 34);")
        self.attendace_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.attendace_title2 = QLabel(self.page)
        self.attendace_title2.setObjectName(u"average_class")
        self.attendace_title2.setGeometry(QRect(680, 100, 311, 31))
        self.attendace_title2.setStyleSheet(u"font: 700 14pt \"Arial\";\n"
                                         "color: rgb(34, 34, 34);")
        self.attendace_title2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.classe = QLabel(self.page)
        self.classe.setObjectName(u"average_class")
        self.classe.setGeometry(QRect(160, 495, 100, 31))
        self.classe.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.classe.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.year = QLabel(self.page)
        self.year.setObjectName(u"average_class")
        self.year.setGeometry(QRect(420, 495, 100, 31))
        self.year.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.year.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.transfer_btn = HoverButton(self.page)
        self.transfer_btn.setObjectName(u"transfer_btn")
        self.transfer_btn.setGeometry(QRect(520, 510, 91, 31))
        self.transfer_btn.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                        "color : rgb(255,255,255);\n"
                                        "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                        "border-radius: 15px}\n"
                                        "\n"
                                        "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                        "color: rgb(255,255,255)\n"
                                        "}")
        self.score_settings_lbl = QLabel(self.page)
        self.score_settings_lbl.setObjectName(u"score_settings_lbl")
        self.score_settings_lbl.setGeometry(QRect(180, 105, 241, 41))
        self.score_settings_lbl.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                              "color: rgb(51, 51, 51);")
        self.info2 = QLabel(self.page)
        self.info2.setObjectName(u"requirederrfirst_22")
        self.info2.setGeometry(QRect(340, 220, 180, 16))
        self.info2.setStyleSheet(u"color: #6B7280;\n"
                                 u"font-size: 11px;")


        self.score_line = QLineEdit(self.page)
        self.score_line.setObjectName(u"score_line")
        self.score_line.setGeometry(QRect(340, 170, 221, 41))
        self.score_line.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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
        self.transfe_lbl = QLabel(self.page)
        self.transfe_lbl.setObjectName(u"transfe_lbl")
        self.transfe_lbl.setGeometry(QRect(180, 320, 251, 31))
        self.transfe_lbl.setStyleSheet(u"font: 700 20pt \"Segoe UI Variable\";\n"
                                       "color: rgb(51, 51, 51);")
        self.to_combobox = QComboBox(self.page)
        self.to_combobox.setObjectName(u"to_combobox")
        self.to_combobox.setGeometry(QRect(680, 440, 221, 41))
        self.to_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.errscore_lbl = QLabel(self.page)
        self.errscore_lbl.setObjectName(u"errscore_lbl")
        self.errscore_lbl.setGeometry(QRect(340, 220, 300, 16))
        self.errscore_lbl.setStyleSheet(u"color: rgb(220, 38, 38);")
        self.max_score_lbl = QLabel(self.page)
        self.max_score_lbl.setObjectName(u"max_score_lbl")
        self.max_score_lbl.setGeometry(QRect(170, 180, 161, 16))
        self.max_score_lbl.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                         "font: 600 12pt \"Segoe UI\";")
        self.to_lbl = QLabel(self.page)
        self.to_lbl.setObjectName(u"to_lbl")
        self.to_lbl.setGeometry(QRect(630, 450, 21, 16))
        self.to_lbl.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")
        self.from_combobox = QComboBox(self.page)
        self.from_combobox.setObjectName(u"from_combobox")
        self.from_combobox.setGeometry(QRect(300, 440, 221, 41))
        self.from_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.set_btn = HoverButton(self.page)
        self.set_btn.setObjectName(u"set_btn")
        self.set_btn.setGeometry(QRect(520, 260, 91, 31))
        self.set_btn.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                   "color : rgb(255,255,255);\n"
                                   "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                   "border-radius: 15px}\n"
                                   "\n"
                                   "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                   "color: rgb(255,255,255)\n"
                                   "}")
        self.id_combobox = QComboBox(self.page)
        self.id_combobox.setObjectName(u"id_combobox")
        self.id_combobox.setGeometry(QRect(490, 370, 241, 41))
        self.id_combobox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.from_lbl = QLabel(self.page)
        self.from_lbl.setObjectName(u"from_lbl")
        self.from_lbl.setGeometry(QRect(230, 450, 51, 16))
        self.from_lbl.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                    "font: 600 12pt \"Segoe UI\";")
        self.id_lbl2 = QLabel(self.page)
        self.id_lbl2.setObjectName(u"id_lbl")
        self.id_lbl2.setGeometry(QRect(390, 380, 100, 16))
        self.id_lbl2.setStyleSheet(u"color: rgb(46, 58, 89);\n"
                                  "font: 600 12pt \"Segoe UI\";")












        self.stackedWidget.addWidget(self.page)
        self.tableWidget_class.lower()
        self.tableWidget.lower()
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

        self.requirederrfirst_2.raise_()
        self.requirederrfirst_3.raise_()

        self.maxstudents.raise_()








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
        self.pushButton_n = HoverButton(self.frame_n)
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
        self.pushButton_5 = HoverButton(self.frame_6)
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
        self.label_2_n.setGeometry(QRect(630, 90, 250, 44))
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
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Total Subjects :", None))
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
        self.Subject_top_btn.setText(QCoreApplication.translate("Dialog", u"Subjects", None))
        self.grades_top_btn.setText(QCoreApplication.translate("Dialog", u"Grades", None))
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
        self.attendace_title.setText(QCoreApplication.translate("Dialog", u"Monthly Attendance Rate (%) ", None))
        self.attendace_title2.setText(QCoreApplication.translate("Dialog", u"Attendance Status Distribution ", None))
        self.classe.setText(QCoreApplication.translate("Dialog", u"Class ", None))
        self.year.setText(QCoreApplication.translate("Dialog", u"Year ", None))
        self.Emailine.setText("")
        self.Emailine.setPlaceholderText(QCoreApplication.translate("Dialog", u"example123@gmail.com", None))
        self.AdressLine.setText("")
        self.Numberline.setText("")
        self.Numberline.setPlaceholderText(QCoreApplication.translate("Dialog", u"", None))
        self.label_24.setText(QCoreApplication.translate("Dialog", u"Fields marked with * are required\n"
                                                                   "", None))
        self.Add_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.Cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Edit_button.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Cancel_button3.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Edit_button2.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button2.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Cancel_button2.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Edit_button3.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button3.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Cancel_button4.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.Edit_button4.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.Save_button4.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.Cancel_button5.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.requirederrfirst.setText(QCoreApplication.translate("Dialog", u"This field is required", None))
        self.requirederrlast.setText(QCoreApplication.translate("Dialog", u"This field is required", None))
        self.transfer_btn.setText(QCoreApplication.translate("Dialog", u"Transfer", None))
        self.score_settings_lbl.setText(QCoreApplication.translate("Dialog", u"Score Settings", None))

        self.score_line.setPlaceholderText("20")

        self.transfe_lbl.setText(QCoreApplication.translate("Dialog", u"Transfer Student", None))
        self.errscore_lbl.setText(QCoreApplication.translate("Dialog", u"", None))
        self.max_score_lbl.setText(QCoreApplication.translate("Dialog", u"Set Maximum Score", None))
        self.to_lbl.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.set_btn.setText(QCoreApplication.translate("Dialog", u"Set", None))
        self.from_lbl.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.id_lbl2.setText(QCoreApplication.translate("Dialog", u"Student ID", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dialog", u"Full Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dialog", u"Date of Birth", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dialog", u"M/F", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dialog", u"Address", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dialog", u"Number", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dialog", u"Email", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dialog", u"Delete", None));

        ___qtablewidgetitemg = self.tableWidget_grades.horizontalHeaderItem(0)
        ___qtablewidgetitemg.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1g = self.tableWidget_grades.horizontalHeaderItem(1)
        ___qtablewidgetitem1g.setText(QCoreApplication.translate("Dialog", u"Full Name", None));

        self.class2.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.class2_3.setText(QCoreApplication.translate("Dialog", u"Class     ", None))

        self.class3.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.class4.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.date.setText(QCoreApplication.translate("Dialog", u"Date     ", None))
        self.requirederrfirst_2.setText(QCoreApplication.translate("Dialog", u"Invalid Email", None))
        self.errlbl2.setText(
            QCoreApplication.translate("Dialog", u"Please ensure all entered information is correct", None))
        self.errlbl3.setText(
            QCoreApplication.translate("Dialog", u"Please ensure all entered information is correct", None))
        self.errlbl.setText(QCoreApplication.translate("Dialog", u"Please ensure all entered information is correct", None))
        self.info.setText(
            QCoreApplication.translate("Dialog", u"You can enter multiple marks separated by spaces (for multiple exams)", None))
        self.info2.setText(
            QCoreApplication.translate("Dialog",u"Default value: 20", None))

        self.errclasse.setText(QCoreApplication.translate("Dialog", u"There are no classes yet", None))
        self.requirederrclass.setText(QCoreApplication.translate("Dialog", u"Please Enter a Valid Class Name", None))
        self.requirederrmax.setText(QCoreApplication.translate("Dialog", u"Please enter a valid numeric value", None))
        self.requirederrfirst_3.setText(QCoreApplication.translate("Dialog", u"Invalid Number", None))
        self.Classnameline.setText("")
        self.add_button_subject.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.cancel_button_subject.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.classname.setText(QCoreApplication.translate("Dialog", u"Class Name   :", None))
        self.maxstudents.setText(QCoreApplication.translate("Dialog", u"Max Students    :", None))
        self.maxstudentsline.setText("")
        self.subject_name.setText(QCoreApplication.translate("Dialog", u"Subject :", None))
        self.coeff.setText(QCoreApplication.translate("Dialog", u"Coefficient :", None))
        self.requirederrsubject.setText(QCoreApplication.translate("Dialog", u"Invalid Subject", None))
        self.requirederrcoeff.setText(QCoreApplication.translate("Dialog", u"Invalid Coefficient", None))
        ___qtablewidgetitem = self.tableWidget_class.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dialog", u"Class name", None));
        ___qtablewidgetitem1c = self.tableWidget_class.horizontalHeaderItem(1)
        ___qtablewidgetitem1c.setText(QCoreApplication.translate("Dialog", u"Total Students", None));
        ___qtablewidgetitem2c = self.tableWidget_class.horizontalHeaderItem(2)
        ___qtablewidgetitem2c.setText(QCoreApplication.translate("Dialog", u"Max Students", None));
        ___qtablewidgetitem3c = self.tableWidget_class.horizontalHeaderItem(3)
        ___qtablewidgetitem3c.setText(QCoreApplication.translate("Dialog", u"Delete", None));
        self.add_button_class.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.cancel_button_class.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        ___qtablewidgetitems = self.tableWidget_subjects.horizontalHeaderItem(0)
        ___qtablewidgetitems.setText(QCoreApplication.translate("Dialog", u"Subject", None));
        ___qtablewidgetitem1cs = self.tableWidget_subjects.horizontalHeaderItem(1)
        ___qtablewidgetitem1cs.setText(QCoreApplication.translate("Dialog", u"Coefficient", None));
        ___qtablewidgetitem2cs = self.tableWidget_subjects.horizontalHeaderItem(2)
        ___qtablewidgetitem2cs.setText(QCoreApplication.translate("Dialog", u"Delete", None));

        self.label_n.setText("")
        self.label_n.setText("")
        self.pushButton_n.setText(QCoreApplication.translate("Dialog", u"Sign up", None))
        self.toolButton_2.setText("")
        self.label_12.setText(QCoreApplication.translate("Dialog", u"Welcome back !", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"LOG IN", None))
        self.toolButton.setText("")
        self.top1_name.setText("")
        self.top2_name.setText("")
        self.top4_name.setText("")
        self.top3_name.setText("")
        self.top5_name.setText("")
        self.top2_id.setText("")
        self.top4_id.setText("")
        self.top5_id.setText("")
        self.top3_id.setText("")
        self.top1_id.setText("")
        self.top1_grade.setText("")
        self.top2_grade.setText("")
        self.top5_grade.setText("")
        self.top4_grade.setText("")
        self.top3_grade.setText("")
        self.full_name.setText(QCoreApplication.translate("Dialog", u"Full Name", None))
        self.grade_lbl.setText(QCoreApplication.translate("Dialog", u"Grade", None))
        self.id_lbl.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_16.setText("")
        self.class2_1.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.class2_2.setText(QCoreApplication.translate("Dialog", u"Class     ", None))
        self.average_class.setText(QCoreApplication.translate("Dialog", u"Class Average Scores", None))
        self.top_students.setText(QCoreApplication.translate("Dialog", u"Top 5 Students by Grade", None))
        self.malesfemales.setText(QCoreApplication.translate("Dialog", u"Gender Distribution", None))
        self.students_per_class.setText(QCoreApplication.translate("Dialog", u"Students per Class", None))
        self.subject_avaeges.setText(QCoreApplication.translate("Dialog", u"Subject Average Scores", None))
        self.top_students_3.setText(QCoreApplication.translate("Dialog", u"Top 5 Students by Attendance", None))
        self.top1_name_2.setText("")
        self.birtherr.setText(QCoreApplication.translate("Dialog", u"Is the student’s birth date in the future?", None))
        self.top2_name_2.setText("")
        self.top4_name_2.setText("")
        self.top3_name_2.setText("")
        self.top5_name_2.setText("")
        self.top2_id_2.setText("")
        self.top4_id_2.setText("")
        self.top5_id_2.setText("")
        self.top3_id_2.setText("")
        self.top1_id_2.setText("")
        self.top1_grade_2.setText("")
        self.top2_grade_2.setText("")
        self.top5_grade_2.setText("")
        self.top4_grade_2.setText("")
        self.top3_grade_2.setText("")
        self.full_name_2.setText(QCoreApplication.translate("Dialog", u"Full Name", None))
        self.grade_lbl_2.setText(QCoreApplication.translate("Dialog", u"Presence", None))
        self.id_lbl_2.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.performane.setText(QCoreApplication.translate("Dialog", u"Performance", None))
        self.ranking.setText(QCoreApplication.translate("Dialog", u"Ranking", None))
        self.attendancetop.setText(QCoreApplication.translate("Dialog", u"Attendance", None))
        self.other.setText(QCoreApplication.translate("Dialog", u"Other", None))
        ___qtablewidgetitema = self.tableWidget_att.horizontalHeaderItem(0)
        ___qtablewidgetitema.setText(QCoreApplication.translate("Dialog", u"ID", None));
        ___qtablewidgetitem1a = self.tableWidget_att.horizontalHeaderItem(1)
        ___qtablewidgetitem1a.setText(QCoreApplication.translate("Dialog", u"Full Name", None));
        ___qtablewidgetitem2a = self.tableWidget_att.horizontalHeaderItem(2)
        ___qtablewidgetitem2a.setText(QCoreApplication.translate("Dialog", u"Status", None));

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

