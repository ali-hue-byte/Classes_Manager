import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QLineEdit
from App import Ui_Dialog
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint
from Functions import SALT, hash_password, save_data, load_data, check_strength, check_user
from PySide6.QtCore import Qt






class Main_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(990, 560)
        self.ui.label_errn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_show = QIcon("icons/view_pss.png")
        self.icon_hide = QIcon("icons/hide_pss.png")







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

#----connecting buttons-----------------------------

        self.ui.pushButton_n.clicked.connect(self.creat_clicked)
        self.ui.pushButton_5.clicked.connect(self.log_clicked)
        self.ui.toolButton_2.clicked.connect(lambda: self.toogle(self.ui.lineEdit_2_n,self.ui.toolButton_2))
        self.ui.toolButton.clicked.connect(lambda: self.toogle(self.ui.lineEdit_6,self.ui.toolButton))
        self.ui.label_7_n.linkActivated.connect(lambda: self.creat_acc_animation(self.widgets_acc, self.widgets_log))
        self.ui.label_10.linkActivated.connect(lambda: self.creat_log_animation(self.widgets_log, self.widgets_acc))
        self.ui.exit_button.clicked.connect(self.exit_clicked)
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

        if check_user(username) or len(username) < 3 or len(password) > 15:
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
        self.ui.label_errn.hide()
        self.ui.welcome_label.setText(f"Welcome {username}")
        self.ui.stackedWidget.setCurrentIndex(0)

        save_data(data)
        for i in self.lines:
            i.clear()


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
                self.ui.stackedWidget.setCurrentIndex(0)
                for i in self.lines:
                    i.clear()
                return
        self.update_line(self.ui.lineEdit_5)
        self.update_line(self.ui.lineEdit_6)
        self.ui.label_errn.setText("Invalid username or password")
        self.ui.label_errn.show()
        return

    def exit_clicked(self):
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




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_app()
    window.show()
    sys.exit(app.exec())