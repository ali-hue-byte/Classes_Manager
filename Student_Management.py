import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from Main_ui import Ui_Dialog
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint


class Main_app(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setFixedSize(990, 564)

        self.widgets_acc = [{"widget":self.ui.frame_n, "pos_off":QPoint(-490,50),"pos_on":QPoint(560,50)},
                       {"widget":self.ui.label_3_n, "pos_off": QPoint(-450,190),"pos_on": QPoint(600,190)},
                       {"widget":self.ui.label_4_n, "pos_off":QPoint(-450,280),"pos_on":QPoint(600,280)},
                       {"widget":self.ui.label_2_n, "pos_off":QPoint(-410,90), "pos_on":QPoint(640,90)},
                       {"widget":self.ui.label_7_n, "pos_off":QPoint(-390,450),"pos_on":QPoint(660,450)},
                       {"widget":self.ui.label_5_n, "pos_off":QPoint(-650,100),"pos_on":QPoint(20,100)},
                       {"widget":self.ui.label_6_n, "pos_off":QPoint(-490,180),"pos_on":QPoint(30,180)},
                       ]

        self.widgets_log = [{"widget":self.ui.label_8, "pos_on":QPoint(180,70),"pos_off":QPoint(1180,70)},
                       {"widget":self.ui.label_9, "pos_on":QPoint(80,190),"pos_off":QPoint(1080,190)},
                       {"widget":self.ui.frame_2, "pos_on":QPoint(50,50),"pos_off":QPoint(1050,50)},
                       {"widget":self.ui.label_10, "pos_on":QPoint(140,450),"pos_off":QPoint(1140,450)},
                       {"widget":self.ui.label_11, "pos_on":QPoint(80,280),"pos_off":QPoint(1080,280)},
                       {"widget":self.ui.label_12, "pos_on":QPoint(630,100),"pos_off":QPoint(1630,100)},
                       {"widget":self.ui.label_13, "pos_on":QPoint(640,180),"pos_off":QPoint(1640,180)}]

        self.ui.label_7_n.linkActivated.connect(lambda: self.creat_acc_animation(self.widgets_acc, self.widgets_log))
        self.ui.label_10.linkActivated.connect(lambda: self.creat_log_animation(self.widgets_log, self.widgets_acc))

        self.animations = []
        self.animations2 = []



    def creat_acc_animation(self, widgets, widgets2):
        for widget in widgets:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_on"])
            anim.setEndValue(QPoint(widget["pos_off"]))
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations.append(anim)
        for widget in widgets2:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_off"])
            anim.setEndValue(QPoint(widget["pos_on"]))
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations.append(anim)

    def creat_log_animation(self, widgets, widgets2):
        for widget in widgets:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_on"])
            anim.setEndValue(widget["pos_off"])
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations2.append(anim)

        for widget in widgets2:
            anim = QPropertyAnimation(widget["widget"], b"pos")
            anim.setDuration(1300)
            anim.setStartValue(widget["pos_off"])
            anim.setEndValue(QPoint(widget["pos_on"]))
            anim.setEasingCurve(QEasingCurve.OutCubic)

            anim.start()
            self.animations2.append(anim)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_app() 
    window.show()
    sys.exit(app.exec())

