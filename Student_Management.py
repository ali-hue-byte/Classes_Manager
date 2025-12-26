import sys

from PySide6.QtGui import QIcon, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit , QGraphicsDropShadowEffect, QFrame, QGraphicsOpacityEffect
from App import Ui_Dialog
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QDate
from Functions import SALT, hash_password, save_data, load_data, check_strength, KDF, decrypt_data,encrypt_data, load,save
from PySide6.QtCore import Qt
import re
import time


class Main_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.current_user = []
        self.current_password = []
        self.wrap_with_shadow(self.ui.frame_5,90)
        self.wrap_with_shadow(self.ui.frame_4,90)
        self.wrap_with_shadow(self.ui.frame_3,90)
        self.wrap_with_shadow(self.ui.frame_2,20)
        self.wrap_with_shadow(self.ui.frame ,20)
        self.salt = SALT()

        self.setFixedSize(990, 560)
        self.ui.label_errn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_show = QIcon("icons/view_pss.png")
        self.icon_hide = QIcon("icons/hide_pss.png")

        self.widgets_to_clear = [
            self.ui.Firstnameline,
            self.ui.lastnameline,
            self.ui.Emailine,
            self.ui.AdressLine,
            self.ui.Numberline
        ]

        self.widgets_student_add = [

            self.ui.dateEdit,
            self.ui.Firstnameline,
            self.ui.GenderComboBox,
            self.ui.Firstname,
            self.ui.lastname,
            self.ui.birth,
            self.ui.Class1,
            self.ui.Gender,
            self.ui.phone,
            self.ui.Email,
            self.ui.Address,
            self.ui.label_21,
            self.ui.lastnameline,
            self.ui.label_22,
            self.ui.ClassComboBox,
            self.ui.label_23,
            self.ui.Emailine,
            self.ui.AdressLine,
            self.ui.Numberline,
            self.ui.label_24,
            self.ui.Add_button,
            self.ui.Cancel_button,
            self.ui.requirederrfirst,
            self.ui.requirederrlast,
            self.ui.ClassComboBox2,
            self.ui.class2,
            self.ui.requirederrfirst_2,
            self.ui.requirederrfirst_3,
            self.ui.errclasse

        ]

        self.widget_student_edit =[
            self.ui.Add_top_btn,
            self.ui.View_top_btn,
            self.ui.dateEdit,
            self.ui.Firstnameline,
            self.ui.GenderComboBox,
            self.ui.Firstname,
            self.ui.lastname,
            self.ui.birth,
            self.ui.Class1,
            self.ui.Gender,
            self.ui.phone,
            self.ui.Email,
            self.ui.Address,
            self.ui.label_21,
            self.ui.lastnameline,
            self.ui.label_22,
            self.ui.ClassComboBox,
            self.ui.label_23,
            self.ui.Emailine,
            self.ui.AdressLine,
            self.ui.Numberline,
            self.ui.label_24,
            self.ui.ClassComboBox2,
            self.ui.class2,
            self.ui.requirederrfirst_2,
            self.ui.requirederrfirst_3,
            self.ui.back_button,
            self.ui.Edit_Button
        ]

        self.widgets_student_view =[
            self.ui.tableWidget,
            self.ui.ClassComboBox2,
            self.ui.class2
        ]

        self.widgets_home = [
            self.ui.label_5,
            self.ui.label_6,
            self.ui.welcome_label,
            self.ui.frame_4,

        ]

        self.widgets_acc = [{"widget":self.ui.frame_n, "pos_off":QPoint(-490,50),"pos_on":QPoint(560,50)},
                       {"widget":self.ui.label_3_n, "pos_off": QPoint(-450,190),"pos_on": QPoint(600,190)},
                       {"widget":self.ui.label_4_n, "pos_off":QPoint(-450,280),"pos_on":QPoint(600,280)},
                       {"widget":self.ui.label_2_n, "pos_off":QPoint(-410,90), "pos_on":QPoint(640,90)},
                       {"widget":self.ui.label_7_n, "pos_off":QPoint(-390,450),"pos_on":QPoint(660,450)},
                       {"widget":self.ui.label_5_n, "pos_off":QPoint(-1000,100),"pos_on":QPoint(20,100)},
                       {"widget":self.ui.label_6_n, "pos_off":QPoint(-620,180),"pos_on":QPoint(30,180)},
                       {"widget":self.ui.label_errn, "pos_on":QPoint(570,480),"pos_off":QPoint(50,480)},
                       ]

        self.widgets_log = [{"widget":self.ui.label_8, "pos_on":QPoint(180,70),"pos_off":QPoint(1180,70)},
                       {"widget":self.ui.label_9, "pos_on":QPoint(80,190),"pos_off":QPoint(1080,190)},
                       {"widget":self.ui.frame_6, "pos_on":QPoint(50,50),"pos_off":QPoint(1050,50)},
                       {"widget":self.ui.label_10, "pos_on":QPoint(140,450),"pos_off":QPoint(1140,450)},
                       {"widget":self.ui.label_11, "pos_on":QPoint(80,280),"pos_off":QPoint(1080,280)},
                       {"widget":self.ui.label_12, "pos_on":QPoint(630,100),"pos_off":QPoint(1630,100)},
                       {"widget":self.ui.label_13, "pos_on":QPoint(640,180),"pos_off":QPoint(1640,180)}]
        self.lines = [self.ui.lineEdit_n, self.ui.lineEdit_2_n, self.ui.lineEdit_5, self.ui.lineEdit_6]

        for i in self.widgets_student_add:
            i.hide()
        for i in self.widgets_student_view:
            i.hide()
        for i in self.widget_student_edit:
            i.hide()

#----connecting buttons-----------------------------

        self.ui.pushButton_n.clicked.connect(self.creat_clicked)
        self.ui.pushButton_5.clicked.connect(self.log_clicked)
        self.ui.toolButton_2.clicked.connect(lambda: self.toogle(self.ui.lineEdit_2_n,self.ui.toolButton_2))
        self.ui.toolButton.clicked.connect(lambda: self.toogle(self.ui.lineEdit_6,self.ui.toolButton))
        self.ui.label_7_n.linkActivated.connect(lambda: self.creat_acc_animation(self.widgets_acc, self.widgets_log))
        self.ui.label_10.linkActivated.connect(lambda: self.creat_log_animation(self.widgets_log, self.widgets_acc))
        self.ui.exit_button.clicked.connect(self.exit_clicked)
        self.ui.Students_button.clicked.connect(self.students_clicked)
        self.ui.settings_button.clicked.connect(self.home_clicked)
        self.ui.Add_button.clicked.connect(self.add_btn_clicked)
        self.ui.Cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.View_top_btn.clicked.connect(self.view_top_clicked)
        self.ui.Add_top_btn.clicked.connect(self.Add_top_clicked)

#------------------------------------------------------------------


        self.animations = []
        self.animations2 = []

    def empty(self,lines):
        for line in lines:
            line.clear()

    def toogle(self,line,tool_btn):
        if line.echoMode() == QLineEdit.EchoMode.Password :
            line.setEchoMode(QLineEdit.EchoMode.Normal)
            tool_btn.setIcon(self.icon_show)
        else :
            line.setEchoMode(QLineEdit.EchoMode.Password)
            tool_btn.setIcon(self.icon_hide)

    def update_line(self,line):
        line.setStyleSheet(u"QLineEdit {\n"
                                               "    border-radius: 12px;\n"
                                               "    padding: 8px 12px;\n"
                                               "    background-color: rgba(255, 255, 255, 220);\n"
                                               "    border: 2px solid red;\n"
                                               "    color: #003366;\n"
                                               "}\n"
                                               "")
    def reset_line(self,line):
        line.setStyleSheet(u"QLineEdit {\n"
"    border-radius: 12px;\n"
"    padding: 8px 12px;\n"
"    background-color: rgba(255, 255, 255, 220);\n"
"    border: none;\n"
"    color: #003366;\n"
"}\n"
"")
    def update_line2(self,line):
        line.setStyleSheet(u"QLineEdit { border : 2px solid red ;\n"
                                      "border-radius : 15px ;\n"
                                      "padding : 5px 7px ;\n"
                                      "background-color: rgb(255,255,255)\n"
                                      "}")

    def reset_line2(self,line):
        line.setStyleSheet(u"QLineEdit { border : 1px solid grey ;\n"
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


    def creat_clicked(self):
        username = str(self.ui.lineEdit_n.text())
        password = str(self.ui.lineEdit_2_n.text())
        data = load_data()

        if username == "" or password == "":
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("Please enter both username and password")
            self.ui.label_errn.show()
            self.update_line(self.ui.lineEdit_n)
            self.update_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.repaint()
            return

        if  re.search(r'[^a-zA-Z0-9_]',username) or len(username) < 3 or len(username) > 15:
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("Username is invalid")
            self.update_line(self.ui.lineEdit_n)
            self.ui.label_errn.show()
            return


        for i in data:
            if username == i["username"]:
                self.reset_line(self.ui.lineEdit_n)
                self.reset_line(self.ui.lineEdit_2_n)
                self.ui.label_errn.setText("Username already exists")
                self.update_line(self.ui.lineEdit_n)
                self.ui.label_errn.show()
                return
        if not check_strength(password):
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("Your password is too weak. Please choose a stronger one.")
            self.update_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.show()
            return

        new_user = {"username":username, "password":hash_password(password,SALT())}
        data.append(new_user)
        self.current_user.append(username)
        self.current_password.append(password)
        self.ui.label_errn.hide()
        self.ui.welcome_label.setText(f"Welcome {username}")

        self.animate_page(self.ui.page, 1, 0)
        self.ui.stackedWidget.setCurrentIndex(0)
        save_data(data)
        loaded2 = load()
        loaded2.update({username: {}})
        save(loaded2)
        for i in self.lines:
            i.clear()
            self.reset_line(i)

    def log_clicked(self):
        username = str(self.ui.lineEdit_5.text())
        password = str(self.ui.lineEdit_6.text())
        data = load_data()

        if username == "" or password == "":
            self.reset_line(self.ui.lineEdit_5)
            self.reset_line(self.ui.lineEdit_6)
            self.ui.label_errn.setText("Please enter both username and password")
            self.ui.label_errn.show()
            self.update_line(self.ui.lineEdit_5)
            self.update_line(self.ui.lineEdit_6)
            self.ui.label_errn.repaint()
            return
        for i in data:
            if i["username"] == username and i["password"] == hash_password(password, SALT()):
                self.reset_line(self.ui.lineEdit_5)
                self.reset_line(self.ui.lineEdit_6)
                self.ui.label_errn.hide()
                self.ui.welcome_label.setText(f"Welcome {username}")
                self.current_user.append(username)
                self.current_password.append(password)

                self.animate_page(self.ui.page, 1, 0)
                self.ui.stackedWidget.setCurrentIndex(0)
                for i in self.lines:
                    i.clear()
                    self.reset_line(i)
                return
        self.update_line(self.ui.lineEdit_5)
        self.update_line(self.ui.lineEdit_6)
        self.ui.label_errn.setText("Invalid username or password")
        self.ui.label_errn.show()
        return

    def exit_clicked(self):
        self.animate_page(self.ui.page_2,1,0)
        self.home_clicked()
        self.ui.stackedWidget.setCurrentIndex(1)

        return


    def creat_acc_animation(self, widgets, widgets2):
        self.ui.label_errn.hide()
        for i in self.lines:
            self.reset_line(i)
        for widget in widgets:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_on"])
            anim.setEndValue(QPoint(widget["pos_off"]))
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations.append(anim)
            self.empty(self.lines)

        for widget in widgets2:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_off"])
            anim.setEndValue(QPoint(widget["pos_on"]))
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations.append(anim)
            self.empty(self.lines)

    def creat_log_animation(self, widgets, widgets2):
        self.ui.label_errn.hide()
        for i in self.lines:
            self.reset_line(i)
        for widget in widgets:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_on"])
            anim.setEndValue(widget["pos_off"])
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations2.append(anim)
            self.empty(self.lines)


        for widget in widgets2:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_off"])
            anim.setEndValue(QPoint(widget["pos_on"]))
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations2.append(anim)
            self.empty(self.lines)

    def animate_page(self, pag, x, y):

        overlay = QFrame(pag)
        overlay.setGeometry(0, 0, 990, 560)
        overlay.setStyleSheet("background-color: black;")
        overlay.show()

        effect = QGraphicsOpacityEffect(overlay)
        overlay.setGraphicsEffect(effect)
        effect.setOpacity(x)

        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(1000)
        anim.setStartValue(x)
        anim.setEndValue(y)
        anim.setEasingCurve(QEasingCurve.OutQuad)
        anim.start()
        self.animations.append(anim)


        def on_finished():
            overlay.hide()
            overlay.deleteLater()

        anim.finished.connect(on_finished)

    def wrap_with_shadow(self, frame, x):

        wrapper = getattr(frame, "_shadow_wrapper", None)

        if wrapper:
            try:
                _ = wrapper.graphicsEffect()
                shadow = wrapper.graphicsEffect()
                if shadow:
                    shadow.setColor(QColor(0, 0, 0, x))
                return
            except RuntimeError:
                wrapper = None

        parent = frame.parentWidget()

        wrapper = QFrame(parent)
        wrapper.setGeometry(
            frame.x() - 10,
            frame.y() - 10,
            frame.width() + 20,
            frame.height() + 20
        )
        wrapper.setStyleSheet("background: transparent;")

        frame.setParent(wrapper)
        frame.move(10, 10)

        shadow = QGraphicsDropShadowEffect(wrapper)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(6)
        shadow.setColor(QColor(0, 0, 0, x))
        wrapper.setGraphicsEffect(shadow)

        wrapper.show()

        frame._shadow_wrapper = wrapper

    def unwrap_shadow(self, frame):
        wrapper = getattr(frame, "_shadow_wrapper", None)
        if not wrapper:
            return
        original_parent = wrapper.parentWidget()
        if not original_parent:
            return
        global_pos = wrapper.pos() + frame.pos()
        frame.setParent(original_parent)
        frame.move(global_pos)
        wrapper.setGraphicsEffect(None)
        wrapper.deleteLater()
        frame._shadow_wrapper = None

    def students_clicked(self):
        self.ui.Add_top_btn.show()
        self.ui.View_top_btn.show()
        self.unwrap_shadow(self.ui.frame_5)
        self.unwrap_shadow(self.ui.frame_4)
        self.unwrap_shadow(self.ui.frame_3)

        for i in self.widgets_student_add:
            i.show()
        for j in self.widgets_home:
            j.hide()
        for i in self.widgets_student_view:
            i.hide()
        for i in self.widgets_to_clear:
            i.clear()

        self.ui.requirederrfirst.hide()
        self.ui.requirederrlast.hide()
        self.ui.requirederrfirst_2.hide()
        self.ui.requirederrfirst_3.hide()
        self.ui.errclasse.hide()
        for i in [self.ui.lastnameline, self.ui.Firstnameline]:
            self.reset_line2(i)
        self.ui.Add_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                           "color :rgb(24, 182, 255);\n"
                                           "border: none;\n"
                                           "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                           "}\n"
                                           "")
        self.ui.View_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                          "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

    def Add_top_clicked(self):
        self.ui.Add_top_btn.show()
        self.ui.View_top_btn.show()

        for i in self.widgets_student_add:
            i.show()
        for j in self.widgets_home:
            j.hide()
        for i in self.widgets_student_view:
            i.hide()
        for i in self.widgets_to_clear:
            i.clear()

        for i in self.widgets_to_clear:
            i.clear()
            self.reset_line2(i)
        self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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

        self.ui.requirederrfirst.hide()
        self.ui.requirederrlast.hide()
        self.ui.requirederrfirst_2.hide()
        self.ui.requirederrfirst_3.hide()
        self.ui.errclasse.hide()
        self.ui.Add_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                           "color :rgb(24, 182, 255);\n"
                                           "border: none;\n"
                                           "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                           "}\n"
                                           "")
        self.ui.View_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                          "font: 700 9pt \"Yu Gothic UI\";")



    def home_clicked(self):

        self.wrap_with_shadow(self.ui.frame_5, 90)
        self.wrap_with_shadow(self.ui.frame_4, 90)
        self.wrap_with_shadow(self.ui.frame_3, 90)
        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()
        for i in self.widgets_student_add:
            i.hide()
        for j in self.widgets_home:
            j.show()
        for i in self.widgets_student_view:
            i.hide()
        for i in self.widgets_to_clear:
            i.clear()
            self.reset_line2(i)
        self.ui.dateEdit.setDate(QDate.currentDate())

    def add_btn_clicked(self):
        err = False
        data = load()
        self.first_name = self.ui.Firstnameline.text()
        self.last_name = self.ui.lastnameline.text()
        self.gender = self.ui.GenderComboBox.currentText()
        self.date = self.ui.dateEdit.date()
        self.date_str = self.date.toString("yyyy-MM-dd")
        self.classe = self.ui.ClassComboBox.currentText()
        self.email = self.ui.Emailine.text()
        self.number = self.ui.Numberline.text()
        self.address = self.ui.AdressLine.text()

        if self.first_name == "" :
            self.ui.requirederrfirst.setText("This field is required")
            self.ui.requirederrfirst.show()
            self.update_line2(self.ui.Firstnameline)
            err = err or True
        elif not re.fullmatch(r"[A-Za-z]+", self.first_name):
            self.ui.requirederrfirst.setText("Invalid First Name")
            self.ui.requirederrfirst.show()
            self.update_line2(self.ui.Firstnameline)
            err = err or True
        else:
            self.ui.requirederrfirst.hide()
            self.reset_line2(self.ui.Firstnameline)
            err = err or False

        if self.last_name == "":
            self.ui.requirederrlast.setText("This field is required")
            self.ui.requirederrlast.show()
            self.update_line2(self.ui.lastnameline)
            err = err or True
        elif not re.fullmatch(r"[A-Za-z ]+", self.last_name):
            self.ui.requirederrlast.setText("Invalid Last Name")
            self.ui.requirederrlast.show()
            self.update_line2(self.ui.lastnameline)
            err = err or True
        else :
            self.ui.requirederrlast.hide()
            self.reset_line2(self.ui.lastnameline)
            err = err or False

        if self.email != "":
             if not self.email.endswith("@gmail.com") :
                 self.ui.requirederrfirst_2.show()
                 self.update_line2(self.ui.Emailine)
                 err = err or True

             else:
                 self.ui.requirederrfirst_2.hide()
                 self.reset_line2(self.ui.Emailine)
                 err = err or False

        else:
             self.ui.requirederrfirst_2.hide()
             self.reset_line2(self.ui.Emailine)
             err = err or False

        if self.number != "":
            if self.number.isdigit() and 7 <= len(str(self.number)) <= 15:
                self.ui.requirederrfirst_3.hide()
                self.reset_line2(self.ui.Numberline)
                err = err or False

            else:
                self.ui.requirederrfirst_3.show()
                self.update_line2(self.ui.Numberline)
                err = err or True

        else:
            self.ui.requirederrfirst_3.hide()
            self.reset_line2(self.ui.Numberline)
            err = err or False

        if self.classe == "":
            self.ui.errclasse.show()
            self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 2px solid red ;\n"
                                         "border-radius : 15px ;\n"
                                         "padding : 5px 7px;  \n"
                                         "background-color: rgb(255,255,255)\n"
                                         "}\n"
                                         "QComboBox:drop-down { width: 0;\n"
                                         "}\n"
                                         )
            err = err or True
        else :
            self.ui.errclasse.hide()
            self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
            err = err or False

        if err :
           return

        student = {"firstname":encrypt_data(self.first_name, self.current_password[-1], KDF, self.salt),
                   "lastname":encrypt_data(self.last_name, self.current_password[-1], KDF, self.salt),
                   "gender":encrypt_data(self.gender, self.current_password[-1], KDF, self.salt),
                   "birth_date":encrypt_data(self.date_str, self.current_password[-1], KDF, self.salt),
                   "class":encrypt_data(self.classe, self.current_password[-1], KDF, self.salt),
                   "email":encrypt_data(self.email, self.current_password[-1], KDF, self.salt),
                   "number":encrypt_data(self.number, self.current_password[-1], KDF, self.salt),
                   "address":encrypt_data(self.address, self.current_password[-1], KDF, self.salt)
                  }

        data[self.current_user[-1]]["students"] = data[self.current_user[-1]].get("students", []) + [student]
        save(data)

    def cancel_clicked(self):
        for i in self.widgets_to_clear:
            i.clear()
            self.reset_line2(i)
        self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 1px solid grey ;\n"
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
        self.ui.errclasse.hide()
        self.ui.requirederrfirst.hide()
        self.ui.requirederrlast.hide()
        self.ui.requirederrfirst_2.hide()
        self.ui.requirederrfirst_3.hide()

    def view_top_clicked(self):
        self.ui.Add_top_btn.show()
        self.ui.View_top_btn.show()



        for i in self.widgets_student_add:
            i.hide()
        for j in self.widgets_home:
            j.hide()
        for i in self.widgets_student_view:
            i.show()
        for i in self.widgets_to_clear:
            i.clear()

        self.ui.requirederrfirst.hide()
        self.ui.requirederrlast.hide()
        self.ui.requirederrfirst_2.hide()
        self.ui.requirederrfirst_3.hide()
        self.ui.errclasse.hide()
        self.ui.View_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                       "color :rgb(24, 182, 255);\n"
                                       "border: none;\n"
                                       "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                       "}\n"
                                       "")
        self.ui.Add_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                        "font: 700 9pt \"Yu Gothic UI\";")









if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_app()
    window.show()
    sys.exit(app.exec())
