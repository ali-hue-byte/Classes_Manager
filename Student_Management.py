import sys
from functools import partial
import os


from PySide6.QtGui import QIcon, QColor, QIntValidator
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QLineEdit,
                               QGraphicsDropShadowEffect,
                               QFrame,
                               QGraphicsOpacityEffect,
                               QTableWidgetItem,
                               QPushButton, QWidget,
                               QAbstractItemView,
                               QTableWidget,
                               QStyledItemDelegate,
                               QItemDelegate, QVBoxLayout, QSizePolicy)
from App import Ui_Dialog, InfoButton
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QPoint, QDate, QRect, QSize
from Functions import (
    hash_password,
    save_data,
    load_data,
    KDF2,
    decrypt_data,
    encrypt_data,

    add_student,
    add_class,
    add_subject,
    add_grade,
    mark_attendance,
select_class,
delete_student,
delete_class,
delete_subject_)
from PySide6.QtCore import Qt
import re
import random

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import sqlite3


conn = sqlite3.connect('data.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS students (
                    student_id INTEGER,
                    user TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    birth_date TEXT,
                    class TEXT,
                    gender TEXT,
                    address TEXT,
                    email TEXT,
                    Number INTEGER,
                    PRIMARY KEY(student_id, user))''')
c.execute('''CREATE TABLE IF NOT EXISTS classes (
                   user TEXT,
                   class_name TEXT,
                   max_students INTEGER,
                   Total_students INTEGER,
                   PRIMARY KEY(class_name, user)
                   )''')
c.execute('''CREATE TABLE IF NOT EXISTS subjects  (
                   user TEXT,
                   subject_name TEXT,
                   coeff INTEGER,
                   PRIMARY KEY(user, subject_name)
                   )''')
c.execute('''CREATE TABLE IF NOT EXISTS grades (
                   user TEXT,
                   student_id INTEGER,
                   subject TEXT,
                   grade INTEGER,
                   PRIMARY KEY (user, student_id, subject)
                   )''')
c.execute('''CREATE TABLE IF NOT EXISTS attendance (
                   user TEXT,
                   student_id INTEGER,
                   date TEXT,
                   status TEXT,
                   PRIMARY KEY (user, student_id, date))''')
conn.commit()

class ReadOnlyDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        return None


class Main_app(QMainWindow):
    def __init__(self):
        super().__init__()


        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.delegue = ReadOnlyDelegate()
        self.current_user = []
        self.current_password = []
        self.wrap_with_shadow(self.ui.frame_5, 90)
        self.wrap_with_shadow(self.ui.frame_4, 90)
        self.wrap_with_shadow(self.ui.frame_3, 90)
        self.wrap_with_shadow(self.ui.frame_2, 20)
        self.wrap_with_shadow(self.ui.frame, 20)


        self.setFixedSize(990, 560)
        self.ui.label_errn.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.icon_show = QIcon("icons/view_pss.png")
        self.icon_hide = QIcon("icons/hide_pss.png")

        self.widgets_to_clear = [
            self.ui.Firstnameline,
            self.ui.lastnameline,
            self.ui.Emailine,
            self.ui.AdressLine,
            self.ui.Numberline,
            self.ui.Classnameline,
            self.ui.maxstudentsline,
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
            self.ui.errclasse,
            self.ui.birtherr

        ]

        self.widget_student_edit = [
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

        ]

        self.widgets_student_view = [
            self.ui.tableWidget,
            self.ui.ClassComboBox2,
            self.ui.class2,
            self.ui.Save_button,
            self.ui.Cancel_button2,
            self.ui.Edit_button,
            self.ui.errlbl

        ]

        self.widgets_home = [
            self.ui.label_5,
            self.ui.label_6,
            self.ui.welcome_label,
            self.ui.frame_4,
            self.ui.frame_5,
            self.ui.frame_3

        ]

        self.widgets_class = [
            self.ui.Classnameline,
            self.ui.classname,
            self.ui.maxstudents,
            self.ui.maxstudentsline,
            self.ui.tableWidget_class,
            self.ui.add_button_class,
            self.ui.cancel_button_class,
            self.ui.requirederrclass,
            self.ui.requirederrmax,
            self.ui.Save_button2,
            self.ui.Cancel_button3,
            self.ui.Edit_button2,
            self.ui.errlbl2

        ]

        self.widgets_grades = [
            self.ui.tableWidget_grades,
            self.ui.ClassComboBox3,
            self.ui.class3,
            self.ui.grades_top_btn,
            self.ui.Subject_top_btn,
            self.ui.tableWidget_subjects,
            self.ui.add_button_subject,
            self.ui.cancel_button_subject,
            self.ui.requirederrsubject,
            self.ui.requirederrcoeff,
            self.ui.subject_name,
            self.ui.subjectline,
            self.ui.coeff,
            self.ui.coeffline,
            self.ui.Edit_button3,
            self.ui.Save_button3,
            self.ui.Cancel_button4,
            self.ui.errlbl3,
            self.ui.Cancel_button5,
            self.ui.Edit_button4,
            self.ui.Save_button4,

        ]

        self.widget_Attendance = [
            self.ui.date,
            self.ui.dateEdit2,
            self.ui.class4,
            self.ui.ClassComboBox4,
            self.ui.tableWidget_att
        ]
        self.error_labels = [
            self.ui.requirederrfirst,
            self.ui.requirederrlast,
            self.ui.requirederrfirst_2,
            self.ui.errlbl,
            self.ui.errlbl2,
            self.ui.errlbl3,
            self.ui.errclasse,
            self.ui.requirederrclass,
            self.ui.requirederrmax,
            self.ui.requirederrfirst_3,
            self.ui.requirederrsubject,
            self.ui.requirederrcoeff,
            self.ui.birtherr,
            self.ui.errscore_lbl

        ]

        self.widgets_statistics = [
            self.ui.performane,
            self.ui.attendancetop,
            self.ui.other,
            self.ui.ranking,
            self.ui.Graph_frame_2,
            self.ui.Graph_frame,
            self.ui.average_class,
            self.ui.subject_avaeges

        ]
        self.widgets_statistics3 = [
            self.ui.Graph_frame_5,
            self.ui.Graph_frame_6,
            self.ui.comboBox2_1,
            self.ui.comboBox2_2,
            self.ui.class2_2,
            self.ui.class2_1,
            self.ui.top_students_3,
            self.ui.top_students
        ]

        self.widgets_statistics_2 = [
            self.ui.Graph_frame_3,
            self.ui.Graph_frame_4,
            self.ui.comboBox2_3,
            self.ui.class2_3,
            self.ui.students_per_class,
            self.ui.malesfemales

        ]
        self.widgets_statistics_4 = [
            self.ui.Graph_frame_7,
            self.ui.Graph_frame_8,
            self.ui.comboBox2_5,
            self.ui.dateEdit5,
            self.ui.comboBox2_6,
            self.ui.comboBox2_7,
            self.ui.attendace_title,
            self.ui.attendace_title2,
            self.ui.year,
            self.ui.classe
        ]

        self.widgets_edit = [
            self.ui.score_settings_lbl,
            self.ui.max_score_lbl,
            self.ui.score_line,
            self.ui.set_btn,
            self.ui.transfe_lbl,
            self.ui.transfer_btn,
            self.ui.from_lbl,
            self.ui.from_combobox,
            self.ui.to_lbl,
            self.ui.to_combobox,
            self.ui.id_lbl2,
            self.ui.id_combobox,
            self.ui.info2
        ]

        self.widgets_acc = [{"widget": self.ui.frame_n, "pos_off": QPoint(-490, 50), "pos_on": QPoint(560, 50)},
                            {"widget": self.ui.label_3_n, "pos_off": QPoint(-450, 190), "pos_on": QPoint(600, 190)},
                            {"widget": self.ui.label_4_n, "pos_off": QPoint(-450, 280), "pos_on": QPoint(600, 280)},
                            {"widget": self.ui.label_2_n, "pos_off": QPoint(-410, 90), "pos_on": QPoint(640, 90)},
                            {"widget": self.ui.label_7_n, "pos_off": QPoint(-390, 450), "pos_on": QPoint(660, 450)},
                            {"widget": self.ui.label_5_n, "pos_off": QPoint(-1000, 100), "pos_on": QPoint(20, 100)},
                            {"widget": self.ui.label_6_n, "pos_off": QPoint(-620, 180), "pos_on": QPoint(30, 180)},
                            {"widget": self.ui.label_errn, "pos_on": QPoint(570, 480), "pos_off": QPoint(50, 480)},
                            ]

        self.widgets_log = [{"widget": self.ui.label_8, "pos_on": QPoint(180, 70), "pos_off": QPoint(1180, 70)},
                            {"widget": self.ui.label_9, "pos_on": QPoint(80, 190), "pos_off": QPoint(1080, 190)},
                            {"widget": self.ui.frame_6, "pos_on": QPoint(50, 50), "pos_off": QPoint(1050, 50)},
                            {"widget": self.ui.label_10, "pos_on": QPoint(140, 450), "pos_off": QPoint(1140, 450)},
                            {"widget": self.ui.label_11, "pos_on": QPoint(80, 280), "pos_off": QPoint(1080, 280)},
                            {"widget": self.ui.label_12, "pos_on": QPoint(630, 100), "pos_off": QPoint(1630, 100)},
                            {"widget": self.ui.label_13, "pos_on": QPoint(640, 180), "pos_off": QPoint(1640, 180)}]
        self.lines = [self.ui.lineEdit_n, self.ui.lineEdit_2_n, self.ui.lineEdit_5, self.ui.lineEdit_6]

        for i in self.widgets_student_add:
            i.hide()
        for i in self.widgets_student_view:
            i.hide()
        for i in self.widget_student_edit:
            i.hide()
        for i in self.widgets_class:
            i.hide()
        for i in self.widgets_grades:
            i.hide()
        for i in self.widget_Attendance:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.hide()
        for i in [self.ui.comboBox2_5, self.ui.comboBox2_6, self.ui.comboBox2_3]:
            i.insertItem(0, "all")
        self.ui.comboBox2_7.insertItem(0, str(QDate.currentDate().year()))
        # ----connecting buttons-----------------------------

        self.ui.pushButton_n.clicked.connect(self.creat_clicked)
        self.ui.pushButton_5.clicked.connect(self.log_clicked)
        self.ui.toolButton_2.clicked.connect(lambda: self.toogle(self.ui.lineEdit_2_n, self.ui.toolButton_2))
        self.ui.toolButton.clicked.connect(lambda: self.toogle(self.ui.lineEdit_6, self.ui.toolButton))
        self.ui.label_7_n.linkActivated.connect(lambda: self.creat_acc_animation(self.widgets_acc, self.widgets_log))
        self.ui.label_10.linkActivated.connect(lambda: self.creat_log_animation(self.widgets_log, self.widgets_acc))
        self.ui.exit_button.clicked.connect(self.exit_clicked)
        self.ui.Students_button.clicked.connect(self.students_clicked)
        self.ui.settings_button.clicked.connect(self.home_clicked)
        self.ui.Add_button.clicked.connect(self.add_btn_clicked)
        self.ui.Cancel_button.clicked.connect(self.cancel_clicked)
        self.ui.View_top_btn.clicked.connect(self.view_top_clicked)
        self.ui.Add_top_btn.clicked.connect(self.Add_top_clicked)
        self.ui.Classes_button.clicked.connect(self.classe_clicked)
        self.ui.add_button_class.clicked.connect(self.Add_class_clicked)
        self.ui.ClassComboBox2.currentTextChanged.connect(
            lambda: self.refresh_view_C(self.current_user[-1], self.current_password[-1]))
        self.ui.cancel_button_class.clicked.connect(self.cancel_clicked)
        self.ui.Edit_button.clicked.connect(self.Edit_btn)
        self.ui.Cancel_button2.clicked.connect(self.Canceled)
        self.ui.Save_button.clicked.connect(self.Save_btn_)
        self.ui.Edit_button2.clicked.connect(self.Edit_btn2)
        self.ui.Cancel_button3.clicked.connect(self.Canceled2)
        self.ui.Save_button2.clicked.connect(self.Save_btn_2)
        self.ui.Grades_button.clicked.connect(self.Grades_clicked)
        self.ui.grades_top_btn.clicked.connect(self.Grades_top)
        self.ui.Subject_top_btn.clicked.connect(self.Subjects)
        self.ui.add_button_subject.clicked.connect(self.add_subject)
        self.ui.cancel_button_subject.clicked.connect(self.cancelsub)
        self.ui.Edit_button3.clicked.connect(self.Edit_btn3)
        self.ui.Cancel_button4.clicked.connect(self.Canceled3)
        self.ui.Save_button3.clicked.connect(self.Save_btn_3)
        self.ui.Edit_button4.clicked.connect(self.Edit_btn_4)
        self.ui.ClassComboBox3.currentTextChanged.connect(
            lambda: self.refresh_grades_C(self.current_user[-1], self.current_password[-1]))
        self.ui.Cancel_button5.clicked.connect(self.Canceled4)
        self.ui.Save_button4.clicked.connect(self.Save_btn_4)
        self.ui.Attendance_button.clicked.connect(self.attendance)
        self.ui.ClassComboBox4.currentTextChanged.connect(
            lambda: self.refresh_attendance_C(self.current_user[-1], self.current_password[-1]))
        self.ui.dateEdit2.dateChanged.connect(
            lambda: self.refresh_attendance_C(self.current_user[-1], self.current_password[-1]))
        self.ui.Statistics_button.clicked.connect(self.statistics)
        self.ui.attendancetop.clicked.connect(self.attendance_top)
        self.ui.performane.clicked.connect(self.performance)
        self.ui.ranking.clicked.connect(self.ranking)
        self.ui.comboBox2_2.currentTextChanged.connect(
            lambda: self.refresh_graph5_C(self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_1.currentTextChanged.connect(
            lambda: self.refresh_graph6_C(self.current_user[-1], self.current_password[-1]))
        self.ui.other.clicked.connect(self.other)
        self.ui.comboBox2_3.currentTextChanged.connect(
            lambda: self.refresh_graph7(self.current_user[-1], self.current_password[-1]))

        self.ui.dateEdit5.dateChanged.connect(
            lambda: self.refresh_graph3(self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_5.currentTextChanged.connect(
            lambda: self.refresh_graph3(self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_6.currentTextChanged.connect(
            lambda: self.refresh_graph4(self.current_user[-1], self.current_password[-1]))
        self.ui.comboBox2_7.currentTextChanged.connect(
            lambda: self.refresh_graph4(self.current_user[-1], self.current_password[-1]))
        self.ui.info_button.clicked.connect(self.edit_page)
        self.ui.from_combobox.currentTextChanged.connect(lambda : self.refresh_combo_id(self.current_user[-1], self.ui.from_combobox.currentText()))
        self.ui.transfer_btn.clicked.connect(self.transfer)
        self.ui.set_btn.clicked.connect(self.set)

        # ------------------------------------------------------------------

        self.salt = None
        self.animations = []
        self.animations2 = []

    def refresh_graph1(self, user, password):
        data = load_data()
        for i in data :
            if i["username"] == user :
                max_score = i["max_score"]
        bars = None

        c.execute("SELECT * FROM students WHERE user=?", (user,))
        students = c.fetchall()
        c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
        classes_rows = c.fetchall()

        c.execute("SELECT * from subjects WHERE user=?", (user,))
        subjects = c.fetchall()

        classes = [x[0] for x in classes_rows]
        coeffs = []
        for z in subjects:
            coeffs.append(int(z[2]))
        data_classes = []
        for i in classes:
            class_average = []

            for j in students:
                student_average = []
                if decrypt_data(j[5],self.kdf) != i:
                    continue
                c.execute("SELECT * FROM grades WHERE user = ? AND student_id = ?",(user,j[0]))
                grades = c.fetchall()
                for k in grades:
                    c.execute("SELECT coeff FROM subjects WHERE user = ? AND subject_name = ?",(user,k[2]))
                    coeff = c.fetchone()[0]
                    student_average.append(float(k[3]) * int(coeff))
                class_average.append(sum(student_average) / sum(coeffs)) if sum(coeffs) !=0 else None
            data_classes.append(sum(class_average) / len(class_average)) if len(
                class_average) > 0 else data_classes.append(0)
        layout = self.ui.Graph_frame.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.Graph_frame)
            self.ui.Graph_frame.setLayout(layout)
        else:

            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()
        fig, ax = plt.subplots(figsize=(5, 3))

        if classes == [] or sum(coeffs) == 0:
            ax.text(0.5, 0.5, "No data available", ha="center", va="center", fontsize=12)
        else:

            bars = ax.bar(classes, data_classes)
            ax.set_ylim(0, int(max_score))
            fig.tight_layout()
            fig.subplots_adjust(bottom=0.2, left=0.15)
            for label in ax.get_xticklabels():
                label.set_rotation(90)
            for bar in bars:
                bar.set_facecolor("#2563EB")
                bar.set_edgecolor("#1E40AF")
        canvas = FigureCanvas(fig)
        canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        canvas.updateGeometry()
        canvas.draw()

        layout.addWidget(canvas)
        if bars is not None:
            self.ui.Graph_frame_2.bars = bars
            self.ui.Graph_frame_2.canvas = canvas
            self.ui.Graph_frame_2.ax = ax

    def refresh_graph2(self, user, password):
        data = load_data()
        for i in data :
            if i["username"] == user :
                max_score = i["max_score"]
        bars = None
        c.execute("SELECT subject_name FROM subjects WHERE user=?", (user,))
        subjects_rows = c.fetchall()
        subjects = [x[0] for x in subjects_rows]

        c.execute("SELECT * FROM students WHERE user=?", (user,))
        students = c.fetchall()
        average_per_subject = []
        for subject in subjects:
            note = []
            for i in students:
                c.execute("SELECT * FROM grades WHERE user=? AND student_id = ?",(user,i[0]))
                grades = c.fetchall()
                for x in grades:
                    if x[2] != subject:
                        continue
                    note.append(float(x[3]))
            average_per_subject.append(sum(note) / len(note)) if len(note) > 0 else average_per_subject.append(0)

        layout = self.ui.Graph_frame_2.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.Graph_frame_2)
            self.ui.Graph_frame_2.setLayout(layout)
        else:

            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        fig, ax = plt.subplots(figsize=(5, 3))
        if subjects == []:
            ax.text(0.5, 0.5, "No data available", ha="center", va="center", fontsize=12)
        else:

            bars = ax.bar(subjects, average_per_subject)
            ax.set_ylim(0, int(max_score))
            fig.tight_layout()
            fig.subplots_adjust(bottom=0.2, left=0.15)
            for label in ax.get_xticklabels():
                label.set_rotation(90)
            for bar in bars:
                bar.set_facecolor("#2563EB")
                bar.set_edgecolor("#1E40AF")

        canvas = FigureCanvas(fig)
        canvas.updateGeometry()
        canvas.draw()
        layout.addWidget(canvas)
        if bars is not None:
            self.ui.Graph_frame.bars = bars
            self.ui.Graph_frame.canvas = canvas
            self.ui.Graph_frame.ax = ax

    def refresh_graph3(self, user, password):

        c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
        classes_rows = c.fetchall()
        classes = [x[0] for x in classes_rows]

        c.execute("SELECT * FROM students WHERE user=?", (user,))
        students_rows = c.fetchall()

        current_class = self.ui.comboBox2_5.currentText()

        if self.ui.comboBox2_5.findText("all") == -1:
            self.ui.comboBox2_5.insertItem(0, "all")
        for i, x in enumerate(classes, start=1):
            if self.ui.comboBox2_5.findText(x) == -1:
                self.ui.comboBox2_5.insertItem(i, x)
        self.ui.comboBox2_5.setCurrentText(current_class)
        classe = self.ui.comboBox2_5.currentText()
        date = self.ui.dateEdit5.date()

        students = 0
        present = 0
        absent = 0
        excused = 0

        for i in students_rows:
            if classe != "all":
                if decrypt_data(i[5], self.kdf) != classe:
                    continue
            c.execute("SELECT * FROM attendance WHERE user=? AND student_id = ?", (user,i[0]))
            attendance = c.fetchall()
            for a in attendance:
                if a[2] != date.toString("yyyy-MM-dd"):
                    continue
                if a[3] == "present":
                    present += 1
                elif a[3] == "absent":
                    absent += 1
                elif a[3] == "excused":
                    excused += 1
            students += 1

        layout = self.ui.Graph_frame_8.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.Graph_frame_8)
            self.ui.Graph_frame_8.setLayout(layout)
        else:

            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        fig, ax = plt.subplots(figsize=(5, 5))
        if students == 0:
            ax.text(0.5, 0.5, "No Data Available",
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=14,
                    transform=ax.transAxes)
            ax.axis('off')
        else:
            attendance_data = [round(present / students * 100),
                               round(absent / students * 100),
                               round(excused / students * 100),
                               round((students - (present + absent + excused)) / students * 100)]
            wedges, texts, autotexts = ax.pie(attendance_data, labels=None, autopct="%1.1f%%", radius=1.55)
            fig.subplots_adjust(bottom=0.3, left=0.15)

            colors = ["#22C55E", "#EF4444", "#F59E0B", "#9CA3AF"]

            for w, ma in zip(wedges, colors):
                w.set_facecolor(ma)

            fig.legend(
                wedges,
                ["Present", "Absent", "Excused", "Not Assigned"],
                loc="lower center",
                bbox_to_anchor=(0.5, -0.05),
                ncol=2,
                frameon=False,
                columnspacing=2,
                handletextpad=0.6
            )

        canvas = FigureCanvas(fig)
        canvas.updateGeometry()
        canvas.draw()

        layout.addWidget(canvas)

    def refresh_graph4(self, user, password):

        c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
        classes_rows = c.fetchall()
        classes = [x[0] for x in classes_rows]

        c.execute("SELECT * FROM students WHERE user=?", (user,))
        students = c.fetchall()

        current_class = self.ui.comboBox2_6.currentText()
        year1 = self.ui.comboBox2_7.currentText()

        if self.ui.comboBox2_6.findText("all") == -1:
            self.ui.comboBox2_6.insertItem(0, "all")
        for i, x in enumerate(classes, start=1):
            if self.ui.comboBox2_6.findText(x) == -1:
                self.ui.comboBox2_6.insertItem(i, x)
        self.ui.comboBox2_6.setCurrentText(current_class)
        classe = self.ui.comboBox2_6.currentText()

        years = []
        for x in students:
            if classe != "all":
                if decrypt_data(x[5], self.kdf) != classe:
                    continue
            c.execute("SELECT * FROM attendance WHERE user =? AND student_id = ?", (user,x[0]))
            attendance = c.fetchall()
            for j in attendance:
                if j[2][:4] not in years:
                    years.append(j[2][:4])
        for a, x in enumerate(years):
            if self.ui.comboBox2_7.findText(x) == -1:
                self.ui.comboBox2_7.insertItem(a, x)
        self.ui.comboBox2_7.setCurrentText(year1)
        attendance = []
        months_data = {
            "01": 0,
            "02": 0,
            "03": 0,
            "04": 0,
            "05": 0,
            "06": 0,
            "07": 0,
            "08": 0,
            "09": 0,
            "10": 0,
            "11": 0,
            "12": 0
        }

        year = self.ui.comboBox2_7.currentText()
        for x in students:
            if classe != "all":
                if decrypt_data(x[5],self.kdf) != classe:
                    continue
            c.execute("SELECT * FROM attendance WHERE user =? AND student_id = ?", (user, x[0]))
            attendance_2 = c.fetchall()
            for qz in attendance_2:

                if qz[2][:4] != year:
                    continue
                if qz[3] == "present":
                    months_data[qz[2][5:7]] = months_data.get(qz[2][5:7], 0) + 1

        d = 0
        for i in students:

            if classe != "all":
                if decrypt_data(i[5],self.kdf) != classe:
                    continue
            c.execute("SELECT * FROM attendance WHERE user =? AND student_id = ?", (user, i[0]))
            attendance_3 = c.fetchall()
            for j in attendance_3:
                if j[2][:4] != year:
                    continue
                d += 1

        layout = self.ui.Graph_frame_7.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.Graph_frame_7)
            self.ui.Graph_frame_7.setLayout(layout)
        else:

            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        fig, ax = plt.subplots(figsize=(5, 5))
        percentages = []
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        if d == 0:
            percentages = [0] * 12
        else:
            percentages = [round(x / d * 100) for x in months_data.values()]
        ax.plot(months, percentages)
        for label in ax.get_xticklabels():
            label.set_rotation(90)
        ax.set_ylim(0, 100)
        fig.subplots_adjust(bottom=0.3, right=0.95, left=0.08)

        canvas = FigureCanvas(fig)
        canvas.updateGeometry()
        canvas.draw()
        layout.addWidget(canvas)

    def refresh_graph5(self, user, password):
        c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
        classes_rows = c.fetchall()

        classes = [x[0] for x in classes_rows]
        c.execute("SELECT * FROM students WHERE user=?", (user,))
        students = c.fetchall()

        c.execute("SELECT * FROM subjects WHERE user=?", (user,))
        subjects = c.fetchall()
        for i in [self.ui.top1_name, self.ui.top1_id, self.ui.top1_grade,
                  self.ui.top2_name, self.ui.top2_id, self.ui.top2_grade,
                  self.ui.top3_name, self.ui.top3_id, self.ui.top3_grade,
                  self.ui.top4_name, self.ui.top4_id, self.ui.top4_grade,
                  self.ui.top5_name, self.ui.top5_id, self.ui.top5_grade]:
            i.setText("")

        current_class = self.ui.comboBox2_2.currentText()
        self.ui.comboBox2_2.clear()
        if self.ui.comboBox2_2.findText("all") == -1:
            self.ui.comboBox2_2.insertItem(0, "all")
        for i, x in enumerate(classes, start=1):
            if self.ui.comboBox2_2.findText(x) == -1:
                self.ui.comboBox2_2.insertItem(i, x)
        self.ui.comboBox2_2.setCurrentText(current_class)
        classe = self.ui.comboBox2_2.currentText()
        top_students = []
        students_averages = {}
        subjects_data = {subject[1]: int(subject[2]) for subject in subjects}
        for i in students:
            if classe != "all":
                if decrypt_data(i[5], self.kdf) != classe:
                    continue
            average = []
            c.execute("SELECT * FROM grades WHERE user=? AND student_id=?", (user, i[0]))
            grades = c.fetchall()
            for x in grades:
                average.append(float(x[3]) * subjects_data[x[2]])
            students_averages[i[0]] = sum(average) / sum(subjects_data.values())

        for z in range(5):
            if students_averages:
                maxi = max(students_averages, key=students_averages.get)
                top_students.append((maxi, round(students_averages[maxi], 2)))
                del students_averages[maxi]

        for i, j in zip(top_students, [(self.ui.top1_name, self.ui.top1_id, self.ui.top1_grade),
                                       (self.ui.top2_name, self.ui.top2_id, self.ui.top2_grade),
                                       (self.ui.top3_name, self.ui.top3_id, self.ui.top3_grade),
                                       (self.ui.top4_name, self.ui.top4_id, self.ui.top4_grade),
                                       (self.ui.top5_name, self.ui.top5_id, self.ui.top5_grade)]):
            c.execute("SELECT first_name FROM students WHERE user=? and student_id=?", (user, i[0]))
            firstname_row = c.fetchone()
            c.execute("SELECT last_name FROM students WHERE user=? and student_id=?", (user, i[0]))
            lastname_row = c.fetchone()
            firstname = decrypt_data(firstname_row[0], self.kdf)
            lastname = decrypt_data(lastname_row[0], self.kdf)
            j[0].setText(f"{firstname} {lastname}")
            j[1].setText(str(i[0]))
            j[2].setText(str(i[1]))

    def refresh_graph5_C(self, user, password):
        c.execute("SELECT class_name FROM classes WHERE user=?",(user,))
        classes_rows = c.fetchall()

        classes = [x[0] for x in classes_rows]
        c.execute("SELECT * FROM students WHERE user=?",(user,))
        students = c.fetchall()

        c.execute("SELECT * FROM subjects WHERE user=?",(user,))
        subjects = c.fetchall()
        for i in [self.ui.top1_name, self.ui.top1_id, self.ui.top1_grade,
                  self.ui.top2_name, self.ui.top2_id, self.ui.top2_grade,
                  self.ui.top3_name, self.ui.top3_id, self.ui.top3_grade,
                  self.ui.top4_name, self.ui.top4_id, self.ui.top4_grade,
                  self.ui.top5_name, self.ui.top5_id, self.ui.top5_grade]:
            i.setText("")

        current_class = self.ui.comboBox2_2.currentText()

        if self.ui.comboBox2_2.findText("all") == -1:
            self.ui.comboBox2_2.insertItem(0, "all")
        for i, x in enumerate(classes, start=1):
            if self.ui.comboBox2_2.findText(x) == -1:
                self.ui.comboBox2_2.insertItem(i, x)
        self.ui.comboBox2_2.setCurrentText(current_class)
        classe = self.ui.comboBox2_2.currentText()
        top_students = []
        students_averages = {}
        subjects_data = {subject[1]: int(subject[2]) for subject in subjects}
        for i in students:
            if classe != "all":
                if decrypt_data(i[5],self.kdf) != classe:
                    continue
            average = []
            c.execute("SELECT * FROM grades WHERE user=? AND student_id=?",(user,i[0]))
            grades = c.fetchall()
            for x in grades:
                average.append(float(x[3]) * subjects_data[x[2]])
            students_averages[i[0]] = sum(average) / sum(subjects_data.values())

        for z in range(5):
            if students_averages:
                maxi = max(students_averages, key=students_averages.get)
                top_students.append((maxi, round(students_averages[maxi], 2)))
                del students_averages[maxi]

        for i, j in zip(top_students, [(self.ui.top1_name, self.ui.top1_id, self.ui.top1_grade),
                                       (self.ui.top2_name, self.ui.top2_id, self.ui.top2_grade),
                                       (self.ui.top3_name, self.ui.top3_id, self.ui.top3_grade),
                                       (self.ui.top4_name, self.ui.top4_id, self.ui.top4_grade),
                                       (self.ui.top5_name, self.ui.top5_id, self.ui.top5_grade)]):
            c.execute("SELECT first_name FROM students WHERE user=? and student_id=?", (user, i[0]))
            firstname_row = c.fetchone()
            c.execute("SELECT last_name FROM students WHERE user=? and student_id=?", (user, i[0]))
            lastname_row = c.fetchone()
            firstname = decrypt_data(firstname_row[0], self.kdf)
            lastname = decrypt_data(lastname_row[0], self.kdf)
            j[0].setText(f"{firstname} {lastname}")
            j[1].setText(str(i[0]))
            j[2].setText(str(i[1]))

    def refresh_graph6_C(self, user, password):

        c.execute("SELECT class_name FROM classes WHERE user=?", (user,))
        classes_rows = c.fetchall()
        classes = [x[0] for x in classes_rows]
        c.execute("SELECT * FROM students WHERE user=?", (user,))
        students = c.fetchall()

        for i in [self.ui.top1_name_2, self.ui.top1_id_2, self.ui.top1_grade_2,
                  self.ui.top2_name_2, self.ui.top2_id_2, self.ui.top2_grade_2,
                  self.ui.top3_name_2, self.ui.top3_id_2, self.ui.top3_grade_2,
                  self.ui.top4_name_2, self.ui.top4_id_2, self.ui.top4_grade_2,
                  self.ui.top5_name_2, self.ui.top5_id_2, self.ui.top5_grade_2]:
            i.setText("")

        current_class = self.ui.comboBox2_1.currentText()


        if self.ui.comboBox2_1.findText("all") == -1:
            self.ui.comboBox2_1.insertItem(0, "all")
        for i, x in enumerate(classes, start=1):
            if self.ui.comboBox2_1.findText(x) == -1:
                self.ui.comboBox2_1.insertItem(i, x)
        self.ui.comboBox2_1.setCurrentText(current_class)
        classe = self.ui.comboBox2_1.currentText()

        top_students = []
        students_data = {}

        for i in students:
            if classe != "all":
                if decrypt_data(i[5], self.kdf) != classe:
                    continue
            present = 0
            c.execute("SELECT status FROM attendance WHERE user=? and student_id=?", (user, i[0]))
            attendance = c.fetchall()
            for k in attendance:
                if k[0] == "present":
                    present += 1
            students_data[i[0]] = round(present / len(attendance) * 100, 2) if len(attendance) != 0 else 0.0

        for i in range(5):
            if students_data:
                maxi = max(students_data, key=students_data.get)
                top_students.append((maxi, students_data[maxi]))
                del students_data[maxi]

        for i, j in zip(top_students, [(self.ui.top1_name_2, self.ui.top1_id_2, self.ui.top1_grade_2),
                                       (self.ui.top2_name_2, self.ui.top2_id_2, self.ui.top2_grade_2),
                                       (self.ui.top3_name_2, self.ui.top3_id_2, self.ui.top3_grade_2),
                                       (self.ui.top4_name_2, self.ui.top4_id_2, self.ui.top4_grade_2),
                                       (self.ui.top5_name_2, self.ui.top5_id_2, self.ui.top5_grade_2)]):
            c.execute("SELECT first_name FROM students WHERE user=? and student_id=?", (user, i[0]))
            firstname_row = c.fetchone()
            c.execute("SELECT last_name FROM students WHERE user=? and student_id=?", (user, i[0]))
            lastname_row = c.fetchone()
            firstname = decrypt_data(firstname_row[0], self.kdf)
            lastname = decrypt_data(lastname_row[0], self.kdf)
            j[0].setText(f"{firstname} {lastname}")
            j[1].setText(str(i[0]))
            j[2].setText(f"{i[1]}%")

    def refresh_graph6(self, user, password):
        c.execute("SELECT class_name FROM classes WHERE user=?",(user,))
        classes_rows =c.fetchall()
        classes = [x[0] for x in classes_rows]
        c.execute("SELECT * FROM students WHERE user=?",(user,))
        students = c.fetchall()

        for i in [self.ui.top1_name_2, self.ui.top1_id_2, self.ui.top1_grade_2,
                  self.ui.top2_name_2, self.ui.top2_id_2, self.ui.top2_grade_2,
                  self.ui.top3_name_2, self.ui.top3_id_2, self.ui.top3_grade_2,
                  self.ui.top4_name_2, self.ui.top4_id_2, self.ui.top4_grade_2,
                  self.ui.top5_name_2, self.ui.top5_id_2, self.ui.top5_grade_2]:
            i.setText("")

        current_class = self.ui.comboBox2_1.currentText()
        self.ui.comboBox2_1.clear()

        if self.ui.comboBox2_1.findText("all") == -1:
            self.ui.comboBox2_1.insertItem(0, "all")
        for i, x in enumerate(classes, start=1):
            if self.ui.comboBox2_1.findText(x) == -1:
                self.ui.comboBox2_1.insertItem(i, x)
        self.ui.comboBox2_1.setCurrentText(current_class)
        classe = self.ui.comboBox2_1.currentText()

        top_students = []
        students_data = {}

        for i in students:
            if classe != "all":
                if decrypt_data(i[5], self.kdf) != classe:
                    continue
            present = 0
            c.execute("SELECT status FROM attendance WHERE user=? and student_id=?",(user,i[0]))
            attendance = c.fetchall()
            for  k in attendance:
                if k[0] == "present":
                    present += 1
            students_data[i[0]] = round(present / len(attendance) * 100, 2) if len(attendance) != 0 else 0.0

        for i in range(5):
            if students_data:
                maxi = max(students_data, key=students_data.get)
                top_students.append((maxi, students_data[maxi]))
                del students_data[maxi]


        for i, j in zip(top_students, [(self.ui.top1_name_2, self.ui.top1_id_2, self.ui.top1_grade_2),
                                       (self.ui.top2_name_2, self.ui.top2_id_2, self.ui.top2_grade_2),
                                       (self.ui.top3_name_2, self.ui.top3_id_2, self.ui.top3_grade_2),
                                       (self.ui.top4_name_2, self.ui.top4_id_2, self.ui.top4_grade_2),
                                       (self.ui.top5_name_2, self.ui.top5_id_2, self.ui.top5_grade_2)]):
            c.execute("SELECT first_name FROM students WHERE user=? and student_id=?",(user,i[0]))
            firstname_row = c.fetchone()
            c.execute("SELECT last_name FROM students WHERE user=? and student_id=?", (user, i[0]))
            lastname_row = c.fetchone()
            firstname = decrypt_data(firstname_row[0],  self.kdf)
            lastname = decrypt_data(lastname_row[0], self.kdf)
            j[0].setText(f"{firstname} {lastname}")
            j[1].setText(str(i[0]))
            j[2].setText(f"{i[1]}%")

    def refresh_graph7(self, user, password):
        wedges = None
        texts = None
        autotexts = None

        current_class = self.ui.comboBox2_3.currentText()
        c.execute("SELECT * FROM students WHERE user = ?", (user,))
        students = c.fetchall()
        c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
        classes_rows = c.fetchall()
        classes=[x[0] for x in classes_rows]

        if self.ui.comboBox2_3.findText("all") == -1:
            self.ui.comboBox2_3.insertItem(0, "all")
        for i, x in enumerate(classes, start=1):
            if self.ui.comboBox2_3.findText(x) == -1:
                self.ui.comboBox2_3.insertItem(i, x)
        self.ui.comboBox2_3.setCurrentText(current_class)
        classe = self.ui.comboBox2_3.currentText()

        males = 0
        females = 0

        for i in students:
            if classe != "all":
                if classe != decrypt_data(i[5], self.kdf):
                    continue
            if decrypt_data(i[6], self.kdf) == "Male":
                males += 1
            else:
                females += 1
        males_percentage = males / len(students) * 100 if len(students) != 0 else 0
        females_percentage = females / len(students) * 100 if len(students) != 0 else 0

        sizes = [males_percentage, females_percentage]
        labels = ["Male", "Female"]

        layout = self.ui.Graph_frame_4.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.Graph_frame_4)
            self.ui.Graph_frame_4.setLayout(layout)
        else:

            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        fig = Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

        try:
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        except (ValueError, ZeroDivisionError):
            ax.text(0.5, 0.5, "No Data Available",
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=14,
                    transform=ax.transAxes)
            ax.axis('off')
        if len(students) == 0:
            ax.text(0.5, 0.5, "No Data Available",
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=14,
                    transform=ax.transAxes)
            ax.axis('off')
        canvas = FigureCanvas(fig)
        canvas.updateGeometry()
        canvas.draw()
        self.ui.Graph_frame_3.wedges = wedges
        self.ui.Graph_frame_3.canvas = canvas
        self.ui.Graph_frame_3.texts = texts
        layout.addWidget(canvas)

    def refresh_graph8(self, user, password):
        c.execute("SELECT * FROM students WHERE user = ?", (user,))
        students = c.fetchall()
        c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
        classes_rows = c.fetchall()
        wedges = None
        texts = None
        autotexts = None
        classes = [x[0] for x in classes_rows]
        classes_data = {}
        for x in classes:
            for i in students:
                if decrypt_data(i[5], self.kdf) == x:
                    classes_data[x] = classes_data.get(x, 0) + 1

        labels = [x for x in classes_data.keys()]
        sizes = [x / len(students) * 100 if len(students) != 0 else 0 for x in
                 classes_data.values()]
        layout = self.ui.Graph_frame_3.layout()
        if layout is None:
            layout = QVBoxLayout(self.ui.Graph_frame_3)
            self.ui.Graph_frame_3.setLayout(layout)
        else:

            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.setParent(None)
                    widget.deleteLater()

        fig = Figure(figsize=(5, 5))
        ax = fig.add_subplot(111)

        try:
            wedges, texts, autotexts = ax.pie(sizes, labels=labels, autopct="%1.1f%%")
        except (ValueError, ZeroDivisionError):
            ax.text(0.5, 0.5, "No Data Available",
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=14,
                    transform=ax.transAxes)
            ax.axis('off')
        if len(students) == 0:
            ax.text(0.5, 0.5, "No Data Available",
                    horizontalalignment='center',
                    verticalalignment='center',
                    fontsize=14,
                    transform=ax.transAxes)
            ax.axis('off')
        canvas = FigureCanvas(fig)
        canvas.updateGeometry()
        canvas.draw()
        layout.addWidget(canvas)

        self.ui.Graph_frame_4.wedges = wedges
        self.ui.Graph_frame_4.canvas = canvas
        self.ui.Graph_frame_4.texts = texts

    def refresh_attendance(self, user, password):
        c.execute("SELECT class_name FROM classes WHERE user = ? ", (user,))
        classes = c.fetchall()

        c.execute("SELECT * FROM students WHERE user = ?", (user,))
        students = c.fetchall()

        desired_class = self.ui.ClassComboBox4.currentText()

        self.ui.ClassComboBox4.clear()
        for i, x in enumerate(classes):
            if self.ui.ClassComboBox4.findText(x[0]) == -1:
                self.ui.ClassComboBox4.insertItem(i, x[0])


        self.ui.ClassComboBox4.setCurrentText(desired_class)
        current_class = self.ui.ClassComboBox4.currentText()
        self.unwrap_shadow(self.ui.tableWidget_att)
        self.ui.tableWidget_att.setRowCount(0)
        x = 860
        y = 170
        h = 20
        w = 60
        for i in students:

            date = self.ui.dateEdit2.date().toString("yyyy-MM-dd")
            c.execute("SELECT status FROM attendance WHERE user = ? AND student_id = ? AND date = ?",
                      (user, i[0], date))
            attendance = c.fetchone()
            status = attendance[0] if attendance else "not assigned"

            def presentt(id=i[0]):
                mark_attendance(user, id, date, "present")

                self.refresh_attendance(user, password)

            def absentt(id=i[0]):
                mark_attendance(user, id, date, "absent")

                self.refresh_attendance(user, password)

            def excusedt(id=i[0]):
                mark_attendance(user, id, date, "excused")

                self.refresh_attendance(user, password)

            if decrypt_data(i[5], self.kdf) != current_class:
                continue
            row = self.ui.tableWidget_att.rowCount()
            self.ui.tableWidget_att.insertRow(row)
            self.ui.tableWidget_att.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.ui.tableWidget_att.setItem(row, 1, QTableWidgetItem(
                decrypt_data(i[2], self.kdf) + " " + decrypt_data(i[3], self.kdf)))

            frame = QFrame()
            frame.setGeometry(QRect(0, 0, 200, 40))

            iconpre = QIcon()
            iconpre.addFile(u"icons/present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            iconabs = QIcon()
            iconabs.addFile(u"icons/absent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            iconex = QIcon()
            iconex.addFile(u"icons/excused.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

            absent = InfoButton(frame,self.ui.page,"Absent",QRect(x,y,w,h))
            absent.setGeometry(QRect(130, 2, 50, 36))
            absent.setIcon(iconabs)

            present = InfoButton(frame,self.ui.page,"Present",QRect(x-120,y,w,h))
            present.setGeometry(QRect(10, 2, 50, 36))
            present.setIcon(iconpre)
            excused = InfoButton(frame,self.ui.page,"Excused",QRect(x-60,y,w,h))
            excused.setGeometry(QRect(70, 2, 50, 36))
            excused.setIcon(iconex)
            y += 40
            for widget in [absent, present, excused]:
                widget.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: #F0F0F0;\n"
                                     "}")
            if status == "present":
                present.setStyleSheet("QPushButton{background-color: #90EE90;\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #4CBB17;\n"
                                      "}")
            else:
                present.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #F0F0F0;\n"
                                      "}")
            if status == "absent":
                absent.setStyleSheet("QPushButton{background-color: #E53935;\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: #C62828;\n"
                                     "}")
            else:
                absent.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: #F0F0F0;\n"
                                     "}")
            if status == "excused":
                excused.setStyleSheet("QPushButton{background-color: #FFEA00;\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #E1C16E;\n"
                                      "}")
            else:
                excused.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #F0F0F0;\n"
                                      "}")
            absent.clicked.connect(partial(absentt))
            present.clicked.connect(partial(presentt))
            excused.clicked.connect(partial(excusedt))

            self.ui.tableWidget_att.setCellWidget(row, 2, frame)
        for row in range(self.ui.tableWidget_att.rowCount()):
            for col in range(self.ui.tableWidget_att.columnCount()):
                item = self.ui.tableWidget_att.item(row, col)
                if item is None:
                    item = QTableWidgetItem("")
                    self.ui.tableWidget_att.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)

        self.wrap_with_shadow2(self.ui.tableWidget_att, 70)

    def refresh_attendance_C(self, user, password):
        c.execute("SELECT class_name FROM classes WHERE user = ? ",(user,))
        classes = c.fetchall()

        c.execute("SELECT * FROM students WHERE user = ?",(user,))
        students = c.fetchall()

        desired_class = self.ui.ClassComboBox4.currentText()

        for i, x in enumerate(classes):
            if self.ui.ClassComboBox4.findText(x[0]) == -1:
                self.ui.ClassComboBox4.insertItem(i, x[0])


        self.ui.ClassComboBox4.setCurrentText(desired_class)
        current_class = self.ui.ClassComboBox4.currentText()
        self.unwrap_shadow(self.ui.tableWidget_att)
        self.ui.tableWidget_att.setRowCount(0)
        for i in students:
            date = self.ui.dateEdit2.date().toString("yyyy-MM-dd")
            c.execute("SELECT status FROM attendance WHERE user = ? AND student_id = ? AND date = ?", (user,i[0],date))
            attendance = c.fetchone()
            status = attendance[0] if attendance else "not assigned"


            def presentt(id=i[0]):
                mark_attendance(user, id, date, "present")

                self.refresh_attendance(user, password)

            def absentt(id=i[0]):
                mark_attendance(user, id, date, "absent")

                self.refresh_attendance(user, password)

            def excusedt(id=i[0]):
                mark_attendance(user, id, date, "excused")

                self.refresh_attendance(user, password)

            if decrypt_data(i[5], self.kdf) != current_class:
                continue
            row = self.ui.tableWidget_att.rowCount()
            self.ui.tableWidget_att.insertRow(row)
            self.ui.tableWidget_att.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.ui.tableWidget_att.setItem(row, 1, QTableWidgetItem(
                decrypt_data(i[2], self.kdf) + " " + decrypt_data(i[3],self.kdf)))

            frame = QFrame()
            frame.setGeometry(QRect(0, 0, 200, 40))

            iconpre = QIcon()
            iconpre.addFile(u"icons/present.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            iconabs = QIcon()
            iconabs.addFile(u"icons/absent.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            iconex = QIcon()
            iconex.addFile(u"icons/excused.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

            absent = QPushButton(frame)
            absent.setGeometry(QRect(130, 2, 50, 36))
            absent.setIcon(iconabs)
            present = QPushButton(frame)
            present.setGeometry(QRect(10, 2, 50, 36))
            present.setIcon(iconpre)
            excused = QPushButton(frame)
            excused.setGeometry(QRect(70, 2, 50, 36))
            excused.setIcon(iconex)
            for widget in [absent, present, excused]:
                widget.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: #F0F0F0;\n"
                                     "}")
            if status == "present":
                present.setStyleSheet("QPushButton{background-color: #90EE90;\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #4CBB17;\n"
                                      "}")
            else:
                present.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #F0F0F0;\n"
                                      "}")
            if status == "absent":
                absent.setStyleSheet("QPushButton{background-color: #E53935;\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: #C62828;\n"
                                     "}")
            else:
                absent.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                     "border-radius: 5px;\n"
                                     "}\n"
                                     "QPushButton:hover{\n"
                                     "background-color: #F0F0F0;\n"
                                     "}")
            if status == "excused":
                excused.setStyleSheet("QPushButton{background-color: #FFEA00;\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #E1C16E;\n"
                                      "}")
            else:
                excused.setStyleSheet("QPushButton{background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 5px;\n"
                                      "}\n"
                                      "QPushButton:hover{\n"
                                      "background-color: #F0F0F0;\n"
                                      "}")
            absent.clicked.connect(partial(absentt))
            present.clicked.connect(partial(presentt))
            excused.clicked.connect(partial(excusedt))

            self.ui.tableWidget_att.setCellWidget(row, 2, frame)
        for row in range(self.ui.tableWidget_att.rowCount()):
            for col in range(self.ui.tableWidget_att.columnCount()):
                item = self.ui.tableWidget_att.item(row, col)
                if item is None:
                    item = QTableWidgetItem("")
                    self.ui.tableWidget_att.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)

        self.wrap_with_shadow2(self.ui.tableWidget_att, 70)

    def refresh_grades(self, user, password):
        data = load_data()
        for i in data :
            if i["username"] == user :
                max_score = i["max_score"]
        self.unwrap_shadow(self.ui.tableWidget_grades)

        current_class1 = self.ui.ClassComboBox3.currentText()
        c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
        classes = c.fetchall()

        c.execute("SELECT subject_name FROM subjects WHERE user = ?", (user,))
        subjects = c.fetchall()
        self.ui.ClassComboBox3.clear()
        for i, x in enumerate(classes):
            if self.ui.ClassComboBox3.findText(x[0]) == -1:
                self.ui.ClassComboBox3.insertItem(i, x[0])
        self.ui.ClassComboBox3.setCurrentText(current_class1)
        current_class = self.ui.ClassComboBox3.currentText()

        self.ui.tableWidget_grades.setRowCount(0)
        c.execute("SELECT * FROM students WHERE user = ?", (user,))
        students = c.fetchall()

        self.ui.tableWidget_grades.setColumnCount(len(subjects) + 3)
        for j, i in enumerate(subjects, start=2):
            self.ui.tableWidget_grades.setHorizontalHeaderItem(j, QTableWidgetItem(i[0]))
        self.ui.tableWidget_grades.setHorizontalHeaderItem(self.ui.tableWidget_grades.columnCount() - 1,
                                                           QTableWidgetItem("Average"))

        for i in students:

            if decrypt_data(i[5], self.kdf) != current_class:
                continue

            grades = []

            row = self.ui.tableWidget_grades.rowCount()
            self.ui.tableWidget_grades.insertRow(row)

            self.ui.tableWidget_grades.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.ui.tableWidget_grades.setItem(row, 1, QTableWidgetItem(
                decrypt_data(i[2], self.kdf) + " " + decrypt_data(i[3], self.kdf)))
            for ix in range(2,self.ui.tableWidget_grades.columnCount()):
                subject = self.ui.tableWidget_grades.horizontalHeaderItem(ix).text()
                c.execute("SELECT grade FROM grades WHERE user = ? AND student_id = ? AND subject=?", (user, i[0],subject))
                showed_grades = c.fetchone()
                c.execute("SELECT coeff FROM subjects WHERE user =? AND subject_name =?", (user, subject))
                rows = c.fetchone()
                coeff = rows[0] if rows else 0
                if showed_grades is None:
                    self.ui.tableWidget_grades.setItem(row, ix, QTableWidgetItem(""))
                else :
                    self.ui.tableWidget_grades.setItem(row, ix, QTableWidgetItem(str(showed_grades[0])))
                    grades.append((int(showed_grades[0]), int(coeff)))



            average = []
            total_coeff = 0
            for mark in grades:
                average.append(mark[0] * mark[1])
                total_coeff += mark[1]
            self.ui.tableWidget_grades.setItem(row, self.ui.tableWidget_grades.columnCount() - 1,
                                               QTableWidgetItem(str(round(sum(average) / total_coeff,
                                                                          2)))) if total_coeff != 0 else QTableWidgetItem(
                "")
            item = self.ui.tableWidget_grades.item(row, self.ui.tableWidget_grades.columnCount() - 1)
            if total_coeff != 0 and sum(average) / total_coeff < (int(max_score)//2):
                if item:
                    item.setBackground(QColor("#FADBD8"))
            else:
                if item:
                    item.setBackground(QColor("#D4EDDA"))

        for row in range(self.ui.tableWidget_grades.rowCount()):
            for col in range(self.ui.tableWidget_grades.columnCount()):
                item = self.ui.tableWidget_grades.item(row, col)
                if item is None:
                    item = QTableWidgetItem("")
                    self.ui.tableWidget.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)

        self.wrap_with_shadow2(self.ui.tableWidget_grades, 70)

    def refresh_grades_C(self, user, password):
        data = load_data()
        for i in data :
            if i["username"] == user :
                max_score = i["max_score"]
        self.unwrap_shadow(self.ui.tableWidget_grades)

        current_class1 = self.ui.ClassComboBox3.currentText()
        c.execute("SELECT class_name FROM classes WHERE user = ?", (user,))
        classes = c.fetchall()

        c.execute("SELECT subject_name FROM subjects WHERE user = ?", (user,))
        subjects = c.fetchall()

        for i, x in enumerate(classes):
            if self.ui.ClassComboBox3.findText(x[0]) == -1:
                self.ui.ClassComboBox3.insertItem(i, x[0])
        self.ui.ClassComboBox3.setCurrentText(current_class1)
        current_class = self.ui.ClassComboBox3.currentText()

        self.ui.tableWidget_grades.setRowCount(0)
        c.execute("SELECT * FROM students WHERE user = ?", (user,))
        students = c.fetchall()

        self.ui.tableWidget_grades.setColumnCount(len(subjects) + 3)
        for j, i in enumerate(subjects, start=2):
            self.ui.tableWidget_grades.setHorizontalHeaderItem(j, QTableWidgetItem(i[0]))
        self.ui.tableWidget_grades.setHorizontalHeaderItem(self.ui.tableWidget_grades.columnCount() - 1,
                                                           QTableWidgetItem("Average"))

        for i in students:

            if decrypt_data(i[5], self.kdf) != current_class:
                continue

            grades = []

            row = self.ui.tableWidget_grades.rowCount()
            self.ui.tableWidget_grades.insertRow(row)

            self.ui.tableWidget_grades.setItem(row, 0, QTableWidgetItem(str(i[0])))
            self.ui.tableWidget_grades.setItem(row, 1, QTableWidgetItem(
                decrypt_data(i[2], self.kdf) + " " + decrypt_data(i[3], self.kdf)))
            for ix in range(2, self.ui.tableWidget_grades.columnCount()):
                subject = self.ui.tableWidget_grades.horizontalHeaderItem(ix).text()
                c.execute("SELECT grade FROM grades WHERE user = ? AND student_id = ? AND subject=?",
                          (user, i[0], subject))
                showed_grades = c.fetchone()
                c.execute("SELECT coeff FROM subjects WHERE user =? AND subject_name =?", (user, subject))
                rows = c.fetchone()
                coeff = rows[0] if rows else 0
                if showed_grades is None:
                    self.ui.tableWidget_grades.setItem(row, ix, QTableWidgetItem(""))
                else:
                    self.ui.tableWidget_grades.setItem(row, ix, QTableWidgetItem(str(showed_grades[0])))
                    grades.append((int(showed_grades[0]), int(coeff)))

            average = []
            total_coeff = 0
            for mark in grades:
                average.append(mark[0] * mark[1])
                total_coeff += mark[1]
            self.ui.tableWidget_grades.setItem(row, self.ui.tableWidget_grades.columnCount() - 1,
                                               QTableWidgetItem(str(round(sum(average) / total_coeff,
                                                                          2)))) if total_coeff != 0 else QTableWidgetItem(
                "")
            item = self.ui.tableWidget_grades.item(row, self.ui.tableWidget_grades.columnCount() - 1)
            if total_coeff != 0 and sum(average) / total_coeff < (int(max_score)//2):
                if item:
                    item.setBackground(QColor("#FADBD8"))
            else:
                if item:
                    item.setBackground(QColor("#D4EDDA"))

        for row in range(self.ui.tableWidget_grades.rowCount()):
            for col in range(self.ui.tableWidget_grades.columnCount()):
                item = self.ui.tableWidget_grades.item(row, col)
                if item is None:
                    item = QTableWidgetItem("")
                    self.ui.tableWidget_grades.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)

        self.wrap_with_shadow2(self.ui.tableWidget_grades, 70)

    def refresh_subject(self, user):
        self.ui.tableWidget_subjects.setRowCount(0)

        self.unwrap_shadow(self.ui.tableWidget_subjects)
        c.execute("SELECT * FROM subjects WHERE user=?",(user,))
        subjects = c.fetchall()

        for i, j in enumerate(subjects):

            def delete_subject(de=j):
                delete_subject_(user,j[1])
                self.refresh_subject(user)

            self.ui.tableWidget_subjects.insertRow(i)
            self.ui.tableWidget_subjects.setItem(i, 0, QTableWidgetItem(j[1]))
            self.ui.tableWidget_subjects.setItem(i, 1, QTableWidgetItem(str(j[2])))
            self.container2 = QWidget()
            self.container2.setGeometry(QRect(0, 0, 200, 40))
            self.delete_btn2 = QPushButton(self.container2)
            icon = QIcon()
            icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.delete_btn2.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                           "color : rgb(255,255,255);\n"
                                           "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                           "border-radius: 15px}\n"
                                           "\n"
                                           "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                           "color: rgb(255,255,255)\n"
                                           "}")
            self.delete_btn2.setIcon(icon)
            self.delete_btn2.setGeometry(QRect(65, 2, 60, 30))
            self.delete_btn2.clicked.connect(partial(delete_subject))
            self.ui.tableWidget_subjects.setCellWidget(i, 2, self.container2)
        for row in range(self.ui.tableWidget_subjects.rowCount()):
            for col in range(self.ui.tableWidget_subjects.columnCount()):
                item = self.ui.tableWidget_subjects.item(row, col)
                if item is None:
                    item = QTableWidgetItem("")
                    self.ui.tableWidget_subjects.setItem(row, col, item)
                item.setTextAlignment(Qt.AlignCenter)

        self.wrap_with_shadow2(self.ui.tableWidget_subjects, 70)

    def refresh_add(self, user, password):

        c.execute("SELECT class_name FROM classes WHERE user = ?",(user,))
        classes = c.fetchall()
        self.ui.ClassComboBox.clear()
        for i, x in enumerate(classes):
            if self.ui.ClassComboBox.findText(x[0]) == -1:
                self.ui.ClassComboBox.insertItem(i, x[0])

    def refresh_view(self, user, password):


        current_class1 = self.ui.ClassComboBox2.currentText()
        self.ui.ClassComboBox2.clear()

        self.unwrap_shadow(self.ui.tableWidget)

        c.execute("SELECT * FROM students WHERE user=?", (user,))
        rows_students = c.fetchall()
        c.execute("SELECT * FROM classes WHERE user=?", (user,))
        rows_class = c.fetchall()

        for i, x in enumerate(rows_class):
            if self.ui.ClassComboBox2.findText(x[1]) == -1:
                self.ui.ClassComboBox2.insertItem(i, x[1])
        self.ui.ClassComboBox2.setCurrentText(current_class1)

        current_class = self.ui.ClassComboBox2.currentText()
        self.ui.tableWidget.setRowCount(0)

        for y in rows_students:
            def delete_btn(student_id=y[0], re=y):

                self.unwrap_shadow(self.ui.tableWidget)
                delete_student(user, student_id)
                classe = select_class(user,decrypt_data(re[5],self.kdf))

                total = classe[3] - 1
                add_class(user, classe[1], classe[2],total)


                self.refresh_view(user, password)
                self.wrap_with_shadow(self.ui.tableWidget, 70)


            if decrypt_data(y[5], self.kdf) != current_class:
                continue

            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)

            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(y[0])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(
                decrypt_data(y[2],  self.kdf) + " " + decrypt_data(y[3], self.kdf)))
            self.ui.tableWidget.setItem(row, 2,
                                        QTableWidgetItem(decrypt_data(y[4],  self.kdf)))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(decrypt_data(y[6], self.kdf)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(decrypt_data(y[7], self.kdf)))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(decrypt_data(y[9], self.kdf)))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(decrypt_data(y[8], self.kdf)))
            self.container = QWidget()
            self.container.setGeometry(QRect(0, 0, 100, 40))
            self.delete_btn = QPushButton(self.container)
            icon = QIcon()
            icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.delete_btn.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                          "color : rgb(255,255,255);\n"
                                          "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                          "border-radius: 15px}\n"
                                          "\n"
                                          "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                          "color: rgb(255,255,255)\n"
                                          "}")
            self.delete_btn.setIcon(icon)
            self.delete_btn.setGeometry(QRect(20, 2, 50, 30))
            self.delete_btn.clicked.connect(partial(delete_btn))
            self.ui.tableWidget.setCellWidget(row, 7, self.container)
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    if item is None:
                        item = QTableWidgetItem("")
                        self.ui.tableWidget.setItem(row, col, item)
                    item.setTextAlignment(Qt.AlignCenter)
        self.wrap_with_shadow2(self.ui.tableWidget, 70)


    def refresh_view_C(self, user, password):

        current_class1 = self.ui.ClassComboBox2.currentText()

        self.unwrap_shadow(self.ui.tableWidget)

        c.execute("SELECT * FROM students WHERE user=?", (user,))
        rows_students = c.fetchall()
        c.execute("SELECT * FROM classes WHERE user=?", (user,))
        rows_class = c.fetchall()

        for i, x in enumerate(rows_class):
            if self.ui.ClassComboBox2.findText(x[1]) == -1:
                self.ui.ClassComboBox2.insertItem(i, x[1])
        self.ui.ClassComboBox2.setCurrentText(current_class1)

        current_class = self.ui.ClassComboBox2.currentText()
        self.ui.tableWidget.setRowCount(0)

        for y in rows_students:
            def delete_btn(student_id=y[0], re=y):

                self.unwrap_shadow(self.ui.tableWidget)
                delete_student(user, student_id)
                classe = select_class(user, decrypt_data(re[5], self.kdf))

                total = classe[3] - 1
                add_class(user, classe[1], classe[2], total)

                self.refresh_view(user, password)
                self.wrap_with_shadow(self.ui.tableWidget, 70)

            if decrypt_data(y[5], self.kdf) != current_class:
                continue

            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)

            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(y[0])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(
                decrypt_data(y[2], self.kdf) + " " + decrypt_data(y[3], self.kdf)))
            self.ui.tableWidget.setItem(row, 2,
                                        QTableWidgetItem(decrypt_data(y[4], self.kdf)))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(decrypt_data(y[6], self.kdf)))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(decrypt_data(y[7], self.kdf)))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(decrypt_data(y[9], self.kdf)))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(decrypt_data(y[8], self.kdf)))
            self.container = QWidget()
            self.container.setGeometry(QRect(0, 0, 100, 40))
            self.delete_btn = QPushButton(self.container)
            icon = QIcon()
            icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.delete_btn.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                          "color : rgb(255,255,255);\n"
                                          "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                          "border-radius: 15px}\n"
                                          "\n"
                                          "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                          "color: rgb(255,255,255)\n"
                                          "}")
            self.delete_btn.setIcon(icon)
            self.delete_btn.setGeometry(QRect(20, 2, 50, 30))
            self.delete_btn.clicked.connect(partial(delete_btn))
            self.ui.tableWidget.setCellWidget(row, 7, self.container)
            for row in range(self.ui.tableWidget.rowCount()):
                for col in range(self.ui.tableWidget.columnCount()):
                    item = self.ui.tableWidget.item(row, col)
                    if item is None:
                        item = QTableWidgetItem("")
                        self.ui.tableWidget.setItem(row, col, item)
                    item.setTextAlignment(Qt.AlignCenter)
        self.wrap_with_shadow2(self.ui.tableWidget, 70)



    def refresh_class(self, user, password):
        self.ui.tableWidget_class.setRowCount(0)

        c.execute("SELECT * FROM classes WHERE user=?", (user,))
        rows_class = c.fetchall()
        c.execute("SELECT * FROM students WHERE user=?", (user,))
        rows_students = c.fetchall()


        for j, x in enumerate(rows_class):
            students_to_delete = []

            def delete_class2(de=x[1]):
                self.unwrap_shadow(self.ui.tableWidget_class)
                delete_class(user,de)
                for  d in rows_students:
                    if decrypt_data(d[5], self.kdf) == de:
                        students_to_delete.append(d[0])
                for i in students_to_delete:
                    delete_student(user,i)


                self.refresh_class(user, password)
                self.refresh_view(user, password)
                self.refresh_add(user, password)
                self.wrap_with_shadow2(self.ui.tableWidget_class, 70)

            self.ui.tableWidget_class.insertRow(j)

            self.ui.tableWidget_class.setItem(j, 0, QTableWidgetItem(x[1]))

            self.ui.tableWidget_class.setItem(j, 1, QTableWidgetItem(str(x[3])))
            self.ui.tableWidget_class.setItem(j, 2, QTableWidgetItem(str(x[2])))
            self.container_ = QWidget()
            self.container_.setGeometry(QRect(0, 0, 100, 40))
            self.delete_btn_ = QPushButton(self.container_)
            self.delete_btn_.setStyleSheet(u"QPushButton{background-color: rgb(37, 99, 235);\n"
                                           "color : rgb(255,255,255);\n"
                                           "font: 700 11pt \"Microsoft PhagsPa\";\n"
                                           "border-radius: 15px}\n"
                                           "\n"
                                           "QPushButton:hover {background-color:  rgb(25, 86, 179);\n"
                                           "color: rgb(255,255,255)\n"
                                           "}")
            self.delete_btn_.setGeometry(QRect(70, 2, 60, 30))
            icon = QIcon()
            icon.addFile(u"icons/delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
            self.delete_btn_.setIcon(icon)
            self.delete_btn_.clicked.connect(partial(delete_class2))
            self.ui.tableWidget_class.setCellWidget(j, 3, self.container_)
        self.wrap_with_shadow2(self.ui.tableWidget_class, 70)

    def Edit_btn(self):
        self.ui.Save_button.show()
        self.ui.Cancel_button2.show()
        self.ui.Cancel_button2.setGeometry(QRect(860, 500, 91, 31))
        self.ui.Save_button.setGeometry(QRect(760, 500, 91, 31))

        self.ui.Edit_button.hide()
        self.unwrap_shadow(self.ui.Edit_button)
        self.wrap_with_shadow(self.ui.Save_button, 70)
        self.wrap_with_shadow(self.ui.Cancel_button2, 70)

        self.ui.tableWidget.setEditTriggers(QTableWidget.AllEditTriggers)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        for i in range(self.ui.tableWidget.rowCount()):
            for j in range(4, 7):
                item = self.ui.tableWidget.item(i, j)
                if item:
                    item.setBackground(QColor("#FFF9C4"))

        for i in range(4):
            self.ui.tableWidget.setItemDelegateForColumn(i, self.delegue)

    def Save_btn_(self):


        new_data = {}
        err = False

        for i in range(self.ui.tableWidget.rowCount()):
            def error(row=i, column=5):
                item = self.ui.tableWidget.item(row, column)
                if item:
                    item.setBackground(QColor("#F8D7DA"))

            def reset(row=i, column=5):
                item = self.ui.tableWidget.item(row, column)
                if item:
                    item.setBackground(QColor("#FFF9C4"))

            ID = self.ui.tableWidget.item(i, 0).text() if self.ui.tableWidget.item(i, 0) else ""
            fullname = (self.ui.tableWidget.item(i, 1).text() if self.ui.tableWidget.item(i, 0) else "").split(" ")
            date = self.ui.tableWidget.item(i, 2).text() if self.ui.tableWidget.item(i, 0) else ""
            gender = self.ui.tableWidget.item(i, 3).text() if self.ui.tableWidget.item(i, 0) else ""
            adress = self.ui.tableWidget.item(i, 4).text() if self.ui.tableWidget.item(i, 0) else ""
            num = self.ui.tableWidget.item(i, 5).text() if self.ui.tableWidget.item(i, 0) else ""
            email = self.ui.tableWidget.item(i, 6).text() if self.ui.tableWidget.item(i, 0) else ""

            if (num != "" and not num.isdigit()):
                error()

                err = True
            else:

                reset()
            if (email != "" and (not email.endswith(".com")or not re.search("@",email))):
                error(i, 6)

                err = True
            else:
                reset(i, 6)

            if (adress != "" and not re.fullmatch(r"[A-Za-z0-9 ]+", adress)):
                error(i, 4)

                err = True
            else:

                reset(i, 4)

            added = {"firstname": encrypt_data(fullname[0], self.kdf),
                     "lastname": encrypt_data(fullname[1], self.kdf),
                     "gender": encrypt_data(gender, self.kdf),
                     "birth_date": encrypt_data(date, self.kdf),
                     "class": encrypt_data(self.ui.ClassComboBox2.currentText(), self.kdf
                                           ),
                     "email": encrypt_data(email, self.kdf),
                     "number": encrypt_data(num,  self.kdf),
                     "address": encrypt_data(adress,  self.kdf),
                     }
            new_data[ID] = added
        if err:
            self.ui.errlbl.show()
            return
        else:
            self.ui.errlbl.hide()

        for i,j in new_data.items():
            add_student(self.current_user[-1],
                        j["firstname"],
                        j["lastname"],
                        i,
                        j["birth_date"],
                        j["class"],
                        j["gender"],
                        j["number"],
                        j["email"],
                        j["address"] )
        self.ui.Edit_button.show()
        self.ui.Edit_button.setGeometry(QRect(810, 500, 91, 31))

        self.wrap_with_shadow(self.ui.Edit_button, 70)
        self.unwrap_shadow(self.ui.Save_button)
        self.unwrap_shadow(self.ui.Cancel_button2)
        self.ui.Save_button.hide()
        self.ui.Cancel_button2.hide()
        self.refresh_view(self.current_user[-1], self.current_password[-1])
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def Canceled(self):
        self.ui.Edit_button.show()
        self.ui.Edit_button.setGeometry(QRect(810, 500, 91, 31))

        self.wrap_with_shadow(self.ui.Edit_button, 70)
        self.unwrap_shadow(self.ui.Save_button)
        self.unwrap_shadow(self.ui.Cancel_button2)
        self.ui.Save_button.hide()
        self.ui.Cancel_button2.hide()
        self.ui.errlbl.hide()

        self.refresh_view(self.current_user[-1], self.current_password[-1])
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)

    def Edit_btn2(self):
        self.ui.Save_button2.show()
        self.ui.Cancel_button3.show()
        self.ui.Cancel_button3.setGeometry(QRect(860, 500, 91, 31))
        self.ui.Save_button2.setGeometry(QRect(760, 500, 91, 31))
        self.ui.Edit_button2.hide()

        self.unwrap_shadow(self.ui.Edit_button2)
        self.wrap_with_shadow(self.ui.Save_button2, 70)
        self.wrap_with_shadow(self.ui.Cancel_button3, 70)

        self.ui.tableWidget_class.setEditTriggers(QTableWidget.AllEditTriggers)
        self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.SingleSelection)

        for i in range(self.ui.tableWidget_class.rowCount()):
            item = self.ui.tableWidget_class.item(i, 2)
            if item:
                item.setBackground(QColor("#FFF9C4"))

        for i in range(2):
            self.ui.tableWidget.setItemDelegateForColumn(i, self.delegue)

    def Canceled2(self):
        self.ui.Edit_button2.show()
        self.ui.Edit_button2.setGeometry(QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button2, 70)
        self.unwrap_shadow(self.ui.Save_button2)
        self.unwrap_shadow(self.ui.Cancel_button3)
        self.ui.Save_button2.hide()
        self.ui.Cancel_button3.hide()
        self.ui.errlbl2.hide()

        self.refresh_class(self.current_user[-1], self.current_password[-1])
        self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)

    def Save_btn_2(self):

        err = False
        new_data = {"Classes": {}}
        for i in range(self.ui.tableWidget_class.rowCount()):
            name = self.ui.tableWidget_class.item(i, 0).text() if self.ui.tableWidget_class.item(i, 0) else ""
            total = self.ui.tableWidget_class.item(i, 1).text() if self.ui.tableWidget_class.item(i, 1) else 0
            max = self.ui.tableWidget_class.item(i, 2).text() if self.ui.tableWidget_class.item(i, 2) else 0

            if not max.isdigit():
                err = True
                item = self.ui.tableWidget_class.item(i, 2)
                if item:
                    item.setBackground(QColor("#F8D7DA"))
            else:
                item = self.ui.tableWidget_class.item(i, 2)
                if item:
                    item.setBackground(QColor("#FFF9C4"))

            new_data["Classes"][name] = {"class_Name": name,
                                         "Max_students": max,
                                         "Total_students": total}

        if err:
            self.ui.errlbl2.show()
            return
        for i,j in new_data["Classes"].items():
            add_class(self.current_user[-1], i,j["Max_students"],j["Total_students"])

        self.ui.errlbl2.hide()

        self.ui.Edit_button2.show()
        self.ui.Edit_button2.setGeometry(QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button2, 70)
        self.unwrap_shadow(self.ui.Save_button2)
        self.unwrap_shadow(self.ui.Cancel_button3)
        self.ui.Save_button2.hide()
        self.ui.Cancel_button3.hide()
        self.refresh_class(self.current_user[-1], self.current_password[-1])
        self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)

    def empty(self, lines):
        for line in lines:
            line.clear()

    def toogle(self, line, tool_btn):
        if line.echoMode() == QLineEdit.EchoMode.Password:
            line.setEchoMode(QLineEdit.EchoMode.Normal)
            tool_btn.setIcon(self.icon_show)
        else:
            line.setEchoMode(QLineEdit.EchoMode.Password)
            tool_btn.setIcon(self.icon_hide)

    def update_line(self, line):
        line.setStyleSheet(u"QLineEdit {\n"
                           "    border-radius: 12px;\n"
                           "    padding: 8px 12px;\n"
                           "    background-color: rgba(255, 255, 255, 220);\n"
                           "    border: 2px solid red;\n"
                           "    color: #003366;\n"
                           "}\n"
                           "")

    def reset_line(self, line):
        line.setStyleSheet(u"QLineEdit {\n"
                           "    border-radius: 12px;\n"
                           "    padding: 8px 12px;\n"
                           "    background-color: rgba(255, 255, 255, 220);\n"
                           "    border: none;\n"
                           "    color: #003366;\n"
                           "}\n"
                           "")

    def update_line2(self, line):
        line.setStyleSheet(u"QLineEdit { border : 2px solid red ;\n"
                           "border-radius : 15px ;\n"
                           "padding : 5px 7px ;\n"
                           "background-color: rgb(255,255,255)\n"
                           "}")

    def reset_line2(self, line):
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

        self.ui.ClassComboBox2.clear()
        self.ui.ClassComboBox.clear()
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

        if re.search(r'[^a-zA-Z0-9_]', username) or len(username) < 3 or len(username) > 15:
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
        if len(password) < 8:
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("The password must be at least 8 characters long.")
            self.update_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.show()
            return
        elif not re.search(r"[A-Z]", password) :
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("The password must include at least one uppercase letter.")
            self.update_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.show()
            return
        elif not re.search(r"[a-z]", password) :
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("The password must include at least one lowercase letter.")
            self.update_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.show()
            return
        elif not re.search(r"[0-9]", password) :
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("The password must include at least one number.")
            self.update_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.show()
            return
        elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            self.reset_line(self.ui.lineEdit_n)
            self.reset_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.setText("The password must include at least one special character.")
            self.update_line(self.ui.lineEdit_2_n)
            self.ui.label_errn.show()
            return
        salt = os.urandom(16)
        new_user = {"username": username, "password": hash_password(password, salt), "salt": salt.hex(),"max_score":20}
        data.append(new_user)
        self.current_user.append(username)
        self.current_password.append(password)
        self.ui.label_errn.hide()
        self.ui.welcome_label.setText(f"Welcome {username}")

        self.animate_page(self.ui.page, 1, 0)
        self.ui.stackedWidget.setCurrentIndex(0)
        save_data(data)

        for i in self.lines:
            i.clear()
            self.reset_line(i)
        self.salt = self.SALT(self.current_user[-1])
        self.kdf = KDF2(self.current_password[-1], self.salt)
        c.execute("SELECT * FROM subjects WHERE user=?",(self.current_user[-1],))
        subjects = len(c.fetchall())
        c.execute("SELECT * FROM students WHERE user=?",(self.current_user[-1],))
        students= len(c.fetchall())
        c.execute("SELECT * FROM classes WHERE user=?",(self.current_user[-1],))
        classes= len(c.fetchall())

        self.ui.label_6.setText(str(subjects))
        self.ui.label_4.setText(str(classes))
        self.ui.label_2.setText(str(students))

    def log_clicked(self):

        self.ui.ClassComboBox2.clear()
        self.ui.ClassComboBox.clear()
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
            if i["username"] == username and i["password"] == hash_password(password, bytes.fromhex(i["salt"])):
                self.reset_line(self.ui.lineEdit_5)
                self.reset_line(self.ui.lineEdit_6)
                self.ui.label_errn.hide()
                self.ui.welcome_label.setText(f"Welcome {username}")
                self.current_user.append(username)
                self.current_password.append(password)

                self.animate_page(self.ui.page, 1, 0)
                self.ui.stackedWidget.setCurrentIndex(0)

                c.execute("SELECT * FROM subjects WHERE user=?", (self.current_user[-1],))
                subjects = len(c.fetchall())
                c.execute("SELECT * FROM students WHERE user=?", (self.current_user[-1],))
                students = len(c.fetchall())
                c.execute("SELECT * FROM classes WHERE user=?", (self.current_user[-1],))
                classes = len(c.fetchall())

                self.ui.label_6.setText(str(subjects))
                self.ui.label_4.setText(str(classes))
                self.ui.label_2.setText(str(students))
                self.salt = self.SALT(self.current_user[-1])
                self.kdf = KDF2(self.current_password[-1], self.salt)
                KDF = self.kdf

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
        self.animate_page(self.ui.page_2, 1, 0)
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


    def animate_page(self, pag, x, y, color="black", b=0, w=990, h=560):

        overlay = QFrame(pag)
        overlay.setGeometry(0, 0, w, h)
        overlay.setStyleSheet(f"background-color: {color};"
                              f"border: 1px solid {color};"
                              f"border-radius: {b}px;")
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


    def animate_btn(self):
        anim = QPropertyAnimation(self.ui.lineEdit_5, b"pos")

    def wrap_with_shadow(self,widget, opacity=120):


        shadow = widget.graphicsEffect()

        if isinstance(shadow, QGraphicsDropShadowEffect):
            shadow.setColor(QColor(0, 0, 0, opacity))
            return

        shadow = QGraphicsDropShadowEffect(widget)
        shadow.setBlurRadius(25)
        shadow.setXOffset(0)
        shadow.setYOffset(6)
        shadow.setColor(QColor(0, 0, 0, opacity))

        widget.setGraphicsEffect(shadow)

    def wrap_with_shadow2(self, frame, x):

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
        self.ui.info.hide()
        self.ui.Add_top_btn.show()
        self.ui.View_top_btn.show()

        self.wrap_with_shadow(self.ui.Add_button, 70)
        self.wrap_with_shadow(self.ui.Cancel_button, 70)

        self.unwrap_shadow(self.ui.tableWidget_subjects)

        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.show()

        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.hide()
            self.unwrap_shadow(i)

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

        self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                              "color :rgb(24, 182, 255);\n"
                                              "border: none;\n"
                                              "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                              "}\n"
                                              "")
        self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                             "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.dateEdit.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
        self.refresh_add(self.current_user[-1], self.current_password[-1])

    def Add_top_clicked(self):
        self.ui.Add_top_btn.show()
        self.ui.View_top_btn.show()

        self.wrap_with_shadow(self.ui.Add_button, 70)
        self.wrap_with_shadow(self.ui.Cancel_button, 70)

        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.show()
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)

        for i in self.widgets_to_clear:
            i.clear()
            self.reset_line2(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
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

        self.ui.Add_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                          "color :rgb(24, 182, 255);\n"
                                          "border: none;\n"
                                          "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                          "}\n"
                                          "")
        self.ui.View_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                           "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.dateEdit.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
        self.refresh_add(self.current_user[-1], self.current_password[-1])

    def home_clicked(self):

        c.execute("SELECT * FROM subjects WHERE user=?", (self.current_user[-1],))
        subjects = len(c.fetchall())
        c.execute("SELECT * FROM students WHERE user=?", (self.current_user[-1],))
        students = len(c.fetchall())
        c.execute("SELECT * FROM classes WHERE user=?", (self.current_user[-1],))
        classes = len(c.fetchall())

        self.ui.label_6.setText(str(subjects))
        self.ui.label_4.setText(str(classes))
        self.ui.label_2.setText(str(students))
        self.ui.info.hide()

        self.wrap_with_shadow(self.ui.frame_5, 90)
        self.wrap_with_shadow(self.ui.frame_4, 90)
        self.wrap_with_shadow(self.ui.frame_3, 90)

        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.show()
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.reset_line2(i)
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.hide()
            self.unwrap_shadow(i)
        self.ui.dateEdit.setDate(QDate.currentDate())

    def add_btn_clicked(self):
        err = False


        self.first_name = self.ui.Firstnameline.text()
        self.last_name = self.ui.lastnameline.text()
        self.gender = self.ui.GenderComboBox.currentText()
        self.date = self.ui.dateEdit.date()
        self.date_str = self.date.toString("yyyy-MM-dd")
        self.classe = self.ui.ClassComboBox.currentText()
        self.email = self.ui.Emailine.text()
        self.number = self.ui.Numberline.text()
        self.address = self.ui.AdressLine.text()

        if self.date > QDate.currentDate():
            err = True
            self.ui.birtherr.show()
            self.ui.dateEdit.setStyleSheet((u"QDateEdit {\n"
                                            "    border-radius: 12px;\n"
                                            "    padding: 8px 12px;\n"
                                            "    background-color: rgba(255, 255, 255, 220);\n"
                                            "    border: 2px solid red;\n"
                                            "    color: #003366;\n"
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
                                            "}"
                                            ))
        else:
            self.ui.birtherr.hide()
            self.ui.dateEdit.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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

        if self.first_name == "":
            self.ui.requirederrfirst.setText("This field is required")
            self.ui.requirederrfirst.show()
            self.update_line2(self.ui.Firstnameline)
            err = True
        elif not re.fullmatch(r"[A-Za-z ]+", self.first_name):
            self.ui.requirederrfirst.setText("Invalid First Name")
            self.ui.requirederrfirst.show()
            self.update_line2(self.ui.Firstnameline)
            err = True
        else:
            self.ui.requirederrfirst.hide()
            self.reset_line2(self.ui.Firstnameline)

        if self.last_name == "":
            self.ui.requirederrlast.setText("This field is required")
            self.ui.requirederrlast.show()
            self.update_line2(self.ui.lastnameline)
            err = True
        elif not re.fullmatch(r"[A-Za-z ]+", self.last_name):
            self.ui.requirederrlast.setText("Invalid Last Name")
            self.ui.requirederrlast.show()
            self.update_line2(self.ui.lastnameline)
            err = True
        else:
            self.ui.requirederrlast.hide()
            self.reset_line2(self.ui.lastnameline)

        if self.email != "":
            if not self.email.endswith(".com") or not re.search("@",self.email):
                self.ui.requirederrfirst_2.show()
                self.update_line2(self.ui.Emailine)
                err = True

            else:
                self.ui.requirederrfirst_2.hide()
                self.reset_line2(self.ui.Emailine)


        else:
            self.ui.requirederrfirst_2.hide()
            self.reset_line2(self.ui.Emailine)

        if self.number != "":
            if self.number.isdigit() and 7 <= len(str(self.number)) <= 15:
                self.ui.requirederrfirst_3.hide()
                self.reset_line2(self.ui.Numberline)


            else:
                self.ui.requirederrfirst_3.show()
                self.update_line2(self.ui.Numberline)
                err = True

        else:
            self.ui.requirederrfirst_3.hide()
            self.reset_line2(self.ui.Numberline)

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
            err = True
        else:
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
        c.execute("SELECT * FROM classes WHERE user=? AND class_name=?", (self.current_user[-1],self.classe))
        rows_classes = c.fetchone()

        if int(rows_classes[3]) == int(rows_classes[2]):
            err = True
            self.ui.errclasse.setText("This Class is full")
            self.ui.errclasse.show()
            self.ui.ClassComboBox.setStyleSheet(u"QComboBox { border : 2px solid red ;\n"
                                                "border-radius : 15px ;\n"
                                                "padding : 5px 7px;  \n"
                                                "background-color: rgb(255,255,255)\n"
                                                "}\n"
                                                "QComboBox:drop-down { width: 0;\n"
                                                "}\n"
                                                )
        else:
            self.ui.errclasse.setText("There are no classes yet")
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

        if err:
            return
        c.execute("SELECT * FROM students WHERE user=?", (self.current_user[-1],))
        rows_students = c.fetchall()
        student_id = random.randint(10000000, 99999999)
        for i in rows_students:
            if i[0] == student_id:
                  student_id = random.randint(10000000, 99999999)
        c.execute("SELECT * FROM subjects WHERE user=?", (self.current_user[-1],))
        rows_subjects = c.fetchall()



        if rows_subjects != []:

            for i in rows_subjects:
                add_grade(self.current_user[-1],student_id,i[1],0)


        add_student(
            self.current_user[-1],

            encrypt_data(self.first_name, self.kdf),
            encrypt_data(self.last_name, self.kdf),
            student_id,
            encrypt_data(self.date_str, self.kdf),
            encrypt_data(self.classe, self.kdf),
            encrypt_data(self.gender, self.kdf),
            encrypt_data(self.number, self.kdf),
            encrypt_data(self.email,  self.kdf),
            encrypt_data(self.address,  self.kdf)
        )
        c.execute("SELECT * FROM classes WHERE user=?", (self.current_user[-1],))
        rows_classes2 = c.fetchall()
        for i in rows_classes2:
            if i[1]==self.classe :
                maxs = i[2]
                tot = i[3]
        add_class(self.current_user[-1],self.classe,maxs,tot+1)

        self.refresh_add(self.current_user[-1], self.current_password[-1])
        for i in self.widgets_to_clear:
            i.clear()

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
        self.ui.dateEdit.setStyleSheet(u"QDateEdit {border-radius: 15px;\n"
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
        for i in self.error_labels:
            i.hide()

    def view_top_clicked(self):
        self.ui.Add_top_btn.show()
        self.ui.View_top_btn.show()

        self.wrap_with_shadow(self.ui.tableWidget, 70)
        self.ui.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.tableWidget.verticalHeader().setHighlightSections(False)

        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.show()
        for i in self.widgets_to_clear:
            i.clear()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()

        self.ui.Edit_button.setGeometry(
            QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button, 70)

        self.ui.Cancel_button2.hide()
        self.ui.Save_button.hide()

        self.ui.View_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                           "color :rgb(24, 182, 255);\n"
                                           "border: none;\n"
                                           "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                           "}\n"
                                           "")
        self.ui.Add_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                          "font: 700 9pt \"Yu Gothic UI\";")
        self.refresh_view(self.current_user[-1], self.current_password[-1])


    def classe_clicked(self):
        self.ui.info.hide()
        for i in self.widgets_class:
            i.show()
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.hide()
            self.unwrap_shadow(i)

        self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                              "color :rgb(24, 182, 255);\n"
                                              "border: none;\n"
                                              "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                              "}\n"
                                              "")
        self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                             "font: 700 9pt \"Yu Gothic UI\";")

        self.wrap_with_shadow(self.ui.tableWidget_class, 70)
        self.wrap_with_shadow(self.ui.add_button_class, 70)
        self.wrap_with_shadow(self.ui.cancel_button_class, 70)
        self.ui.Edit_button2.setGeometry(
            QRect(810, 500, 91, 31))

        self.wrap_with_shadow(self.ui.Edit_button2, 70)

        self.ui.Save_button2.hide()
        self.ui.Cancel_button3.hide()


        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()
        self.refresh_class(self.current_user[-1], self.current_password[-1])

    def Add_class_clicked(self):
        c.execute("SELECT class_name FROM classes WHERE user=?",(self.current_user[-1],))
        classes_rows = c.fetchall()
        classes = [x[0] for x in classes_rows]
        self.class_ = self.ui.Classnameline.text()
        self.MaxxStudents = self.ui.maxstudentsline.text()


        err = False
        if self.class_ == "" or not re.fullmatch(r"[A-Za-z0-9 ]+", self.class_) or len(self.class_) < 2:
            err = True
            self.ui.requirederrclass.setText("Please Enter a Valid Class Name")
            self.update_line2(self.ui.Classnameline)
            self.ui.requirederrclass.show()
        elif self.class_ in classes:
            err = True
            self.update_line2(self.ui.Classnameline)
            self.ui.requirederrclass.setText("Class Already exists")
            self.ui.requirederrclass.show()
        else:
            self.ui.requirederrclass.setText("Please Enter a Valid Class Name")
            self.reset_line2(self.ui.Classnameline)
            self.ui.requirederrclass.hide()
        if self.MaxxStudents == "" or not self.MaxxStudents.isdigit():
            err = True
            self.ui.requirederrmax.setText("Please enter a valid numeric value")
            self.update_line2(self.ui.maxstudentsline)
            self.ui.requirederrmax.show()
        elif int(self.MaxxStudents) < 5:
            err = True
            self.update_line2(self.ui.maxstudentsline)
            self.ui.requirederrmax.setText("That can't be a Class")
            self.ui.requirederrmax.show()
        else:
            self.reset_line2(self.ui.maxstudentsline)
            self.ui.requirederrmax.hide()

        if err == True:
            return


        add_class(self.current_user[-1],self.class_,self.MaxxStudents,0)




        self.ui.Edit_button2.show()
        self.wrap_with_shadow(self.ui.Edit_button2, 70)
        self.unwrap_shadow(self.ui.Save_button2)
        self.unwrap_shadow(self.ui.Cancel_button3)
        self.ui.Save_button2.hide()
        self.ui.Cancel_button3.hide()
        self.ui.tableWidget_class.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_class.setEditTriggers(QTableWidget.NoEditTriggers)
        self.refresh_class(self.current_user[-1], self.current_password[-1])

        for i in self.widgets_to_clear:
            i.clear()

    def cancel_class(self):
        for i in [self.ui.Classnameline, self.ui.maxstudentsline]:
            i.clear()
            self.reset_line2(i)

    def Grades_clicked(self):
        self.ui.info.hide()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
        for i in self.widgets_grades:
            i.show()
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.hide()
            self.unwrap_shadow(i)
        self.ui.Cancel_button5.hide()
        self.ui.Edit_button4.hide()
        self.ui.Save_button4.hide()
        self.ui.Cancel_button4.hide()
        self.ui.Save_button3.hide()

        self.ui.Edit_button3.setGeometry(
            QRect(810, 500, 91, 31))

        self.wrap_with_shadow(self.ui.Edit_button3, 70)
        self.ui.tableWidget_grades.hide()
        self.ui.class3.hide()
        self.ui.ClassComboBox3.hide()
        self.reset_line2(self.ui.subjectline)
        self.reset_line2(self.ui.coeffline)
        self.wrap_with_shadow(self.ui.add_button_subject, 70)
        self.wrap_with_shadow(self.ui.cancel_button_subject, 70)

        self.wrap_with_shadow(self.ui.tableWidget_subjects, 70)

        self.ui.Save_button2.hide()
        self.ui.Cancel_button3.hide()

        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()

        self.refresh_subject(self.current_user[-1])
        self.ui.tableWidget_subjects.setFocusPolicy(Qt.NoFocus)
        self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.subjectline.clear()
        self.ui.coeffline.clear()
        self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                              "color :rgb(24, 182, 255);\n"
                                              "border: none;\n"
                                              "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                              "}\n"
                                              "")
        self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                             "font: 700 9pt \"Yu Gothic UI\";")

    def Subjects(self):
        self.ui.info.hide()
        self.ui.Edit_button4.hide()

        self.ui.Edit_button3.show()
        self.ui.Edit_button3.setGeometry(
            QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button3, 70)
        self.ui.tableWidget_subjects.show()
        self.ui.tableWidget_grades.hide()
        self.ui.add_button_subject.show()
        self.ui.cancel_button_subject.show()
        self.ui.requirederrsubject.hide()
        self.ui.requirederrcoeff.hide()
        self.ui.class3.hide()
        self.ui.subjectline.show()
        self.ui.coeffline.show()
        self.ui.birtherr.hide()
        self.ui.subject_name.show()
        self.ui.coeff.show()
        self.ui.ClassComboBox3.hide()
        self.unwrap_shadow(self.ui.tableWidget_grades)
        self.wrap_with_shadow(self.ui.tableWidget_subjects, 70)
        self.ui.Subject_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                              "color :rgb(24, 182, 255);\n"
                                              "border: none;\n"
                                              "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                              "}\n"
                                              "")
        self.ui.grades_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                             "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.subjectline.clear()
        self.ui.coeffline.clear()
        self.ui.Save_button4.hide()
        self.ui.Cancel_button5.hide()
        self.refresh_subject(self.current_user[-1])

        self.ui.tableWidget_subjects.setFocusPolicy(Qt.NoFocus)
        self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)

    def Grades_top(self):
        self.ui.info.show()
        self.ui.Edit_button4.show()
        self.ui.Edit_button4.setGeometry(
            QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button4, 70)
        self.unwrap_shadow(self.ui.Cancel_button5)
        self.unwrap_shadow(self.ui.Save_button4)
        self.ui.Cancel_button5.hide()

        self.ui.Save_button4.hide()
        self.ui.errlbl3.hide()
        self.reset_line2(self.ui.subjectline)
        self.reset_line2(self.ui.coeffline)
        self.ui.tableWidget_subjects.hide()
        self.ui.tableWidget_grades.show()
        self.ui.add_button_subject.hide()
        self.ui.requirederrsubject.hide()
        self.ui.birtherr.hide()
        self.ui.requirederrcoeff.hide()
        self.ui.cancel_button_subject.hide()
        self.ui.class3.show()
        self.ui.ClassComboBox3.show()
        self.ui.requirederrcoeff.hide()
        self.ui.requirederrsubject.hide()
        self.ui.add_button_subject.hide()
        self.ui.cancel_button_subject.hide()
        self.ui.subjectline.hide()
        self.ui.coeffline.hide()
        self.ui.subject_name.hide()
        self.ui.coeff.hide()
        self.ui.Cancel_button4.hide()
        self.ui.Save_button3.hide()
        self.ui.Edit_button3.hide()
        self.wrap_with_shadow(self.ui.tableWidget_grades, 70)
        self.unwrap_shadow(self.ui.Edit_button3)
        self.unwrap_shadow(self.ui.tableWidget_subjects)
        self.ui.grades_top_btn.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                             "color :rgb(24, 182, 255);\n"
                                             "border: none;\n"
                                             "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                             "}\n"
                                             "")
        self.ui.Subject_top_btn.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                              "font: 700 9pt \"Yu Gothic UI\";")
        self.refresh_grades(self.current_user[-1], self.current_password[-1])

    def add_subject(self):

        err = False
        subject = self.ui.subjectline.text()
        coeff = self.ui.coeffline.text()
        if coeff == "" or not coeff.isdigit():
            self.ui.requirederrcoeff.show()
            self.update_line2(self.ui.coeffline)
            err = True
        else:
            self.ui.requirederrcoeff.hide()
            self.reset_line2(self.ui.coeffline)
        if subject == "" or not re.fullmatch(r"^[a-zA-Z0-9 ]+$", subject):
            self.ui.requirederrsubject.show()
            self.update_line2(self.ui.subjectline)
            err = True
        else:
            self.ui.requirederrsubject.hide()
            self.reset_line2(self.ui.subjectline)

        if err:
            return

        c.execute("SELECT * FROM students WHERE user = ?", (self.current_user[-1],))
        students_rows = c.fetchall()


        for i in students_rows:
            add_grade(self.current_user[-1], i[0],subject,0)


        add_subject(self.current_user[-1], subject, coeff)


        self.refresh_subject(self.current_user[-1])
        for i in [self.ui.subjectline, self.ui.coeffline]:
            i.clear()
            self.reset_line2(i)
        self.ui.requirederrcoeff.hide()
        self.ui.requirederrsubject.hide()

    def cancelsub(self):
        for i in [self.ui.subjectline, self.ui.coeffline]:
            i.clear()
            self.reset_line2(i)
        self.ui.requirederrcoeff.hide()
        self.ui.requirederrsubject.hide()

    def Edit_btn3(self):
        self.ui.Save_button3.show()
        self.ui.Cancel_button4.show()
        self.ui.Save_button3.setGeometry(QRect(760, 500, 91, 31))
        self.ui.Cancel_button4.setGeometry(QRect(860, 500, 91, 31))

        self.ui.Edit_button3.hide()
        self.unwrap_shadow(self.ui.Edit_button3)
        self.wrap_with_shadow(self.ui.Save_button3, 70)
        self.wrap_with_shadow(self.ui.Cancel_button4, 70)

        self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.AllEditTriggers)
        self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.SingleSelection)

        for i in range(self.ui.tableWidget_subjects.rowCount()):
            item = self.ui.tableWidget_subjects.item(i, 1)
            if item:
                item.setBackground(QColor("#FFF9C4"))

        for i in range(1):
            self.ui.tableWidget_subjects.setItemDelegateForColumn(i, self.delegue)

    def Canceled3(self):
        self.ui.Edit_button3.show()
        self.ui.Edit_button3.setGeometry(QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button3, 70)
        self.unwrap_shadow(self.ui.Save_button3)
        self.unwrap_shadow(self.ui.Cancel_button4)
        self.ui.Save_button3.hide()
        self.ui.Cancel_button4.hide()
        self.ui.errlbl3.hide()

        self.refresh_subject(self.current_user[-1])
        self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)

    def Save_btn_3(self):

        err = False
        new_data = {"Subjects": {}}
        for i in range(self.ui.tableWidget_subjects.rowCount()):
            subject = self.ui.tableWidget_subjects.item(i, 0).text()
            coeff = self.ui.tableWidget_subjects.item(i, 1).text()
            if coeff == "" or not coeff.isdigit():
                err = True
                item = self.ui.tableWidget_subjects.item(i, 1)
                if item:
                    item.setBackground(QColor("#F8D7DA"))
            else:
                item = self.ui.tableWidget_subjects.item(i, 1)
                if item:
                    item.setBackground(QColor("#FFF9C4"))

            new_data["Subjects"][subject] = {"subject": subject, "coeff": coeff}

        if err:
            self.ui.errlbl3.show()
            return
        for i,j in new_data["Subjects"].items():
            add_subject(self.current_user[-1], i, j["coeff"])

        self.ui.errlbl3.hide()

        self.ui.Edit_button3.show()
        self.ui.Edit_button3.setGeometry(QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button3, 70)
        self.unwrap_shadow(self.ui.Save_button3)
        self.unwrap_shadow(self.ui.Cancel_button4)
        self.ui.Save_button3.hide()
        self.ui.Cancel_button4.hide()
        self.refresh_subject(self.current_user[-1])
        self.ui.tableWidget_subjects.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_subjects.setEditTriggers(QTableWidget.NoEditTriggers)

    def Edit_btn_4(self):
        self.ui.Edit_button4.hide()
        self.unwrap_shadow(self.ui.Edit_button4)
        self.ui.Save_button4.show()
        self.ui.Cancel_button5.show()
        self.ui.Cancel_button5.setGeometry(QRect(860, 500, 91, 31))
        self.ui.Save_button4.setGeometry(QRect(760, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Save_button4, 70)
        self.wrap_with_shadow(self.ui.Cancel_button5, 70)

        self.ui.tableWidget_grades.setEditTriggers(QTableWidget.AllEditTriggers)
        self.ui.tableWidget_grades.setSelectionMode(QAbstractItemView.SingleSelection)

        for i in range(self.ui.tableWidget_grades.rowCount()):
            for j in range(2, self.ui.tableWidget_grades.columnCount() - 1):
                item = self.ui.tableWidget_grades.item(i, j)
                if item:
                    item.setBackground(QColor("#FFF9C4"))

        for i in range(2):
            self.ui.tableWidget_grades.setItemDelegateForColumn(i, self.delegue)
        self.ui.tableWidget_grades.setItemDelegateForColumn(self.ui.tableWidget_grades.columnCount() - 1, self.delegue)

    def Canceled4(self):
        self.ui.Edit_button4.show()
        self.ui.Edit_button4.setGeometry(QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button4, 70)
        self.unwrap_shadow(self.ui.Save_button4)
        self.unwrap_shadow(self.ui.Cancel_button5)
        self.ui.Save_button4.hide()
        self.ui.Cancel_button4.hide()
        self.ui.errlbl3.hide()

        self.refresh_grades(self.current_user[-1], self.current_password[-1])
        self.ui.tableWidget_grades.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_grades.setEditTriggers(QTableWidget.NoEditTriggers)

    def Save_btn_4(self):
        data = load_data()
        for i in data:
            if i["username"] == self.current_user[-1]:
                max_score = i["max_score"]

        err = False
        entering_data = {}
        for i in range(self.ui.tableWidget_grades.rowCount()):
            new_grades = {}

            id = self.ui.tableWidget_grades.item(i, 0).text()

            for j in range(2, self.ui.tableWidget_grades.columnCount() - 1):
                grades = []

                subject = self.ui.tableWidget_grades.horizontalHeaderItem(j).text()
                marks = self.ui.tableWidget_grades.item(i, j).text().strip()
                marks2 = marks.replace(",", ".")

                if marks2 == "":
                    err = True
                    item = self.ui.tableWidget_grades.item(i, j)
                    item.setBackground(QColor("#F8D7DA"))
                else:
                    item = self.ui.tableWidget_grades.item(i, j)
                    item.setBackground(QColor("#FFF9C4"))

                try:
                    grades = [float(x) for x in marks2.split(" ")]
                    item = self.ui.tableWidget_grades.item(i, j)
                    item.setBackground(QColor("#FFF9C4"))
                except ValueError:
                    err = True
                    item = self.ui.tableWidget_grades.item(i, j)
                    item.setBackground(QColor("#F8D7DA"))

                if round(sum(grades) / len(grades), 2) > int(max_score):
                    err = True
                    item = self.ui.tableWidget_grades.item(i, j)
                    item.setBackground(QColor("#F8D7DA"))
                else:
                    item = self.ui.tableWidget_grades.item(i, j)
                    item.setBackground(QColor("#FFF9C4"))

                new_grades[subject] = round(sum(grades) / len(grades), 2)

            entering_data.update({id: new_grades})

        if err:
            return


        for i,j in entering_data.items():
            for x,y in j.items():
                add_grade(self.current_user[-1], i, x,y)


        self.refresh_grades(self.current_user[-1], self.current_password[-1])

        self.ui.Save_button4.hide()
        self.unwrap_shadow(self.ui.Save_button4)
        self.ui.Cancel_button5.hide()
        self.unwrap_shadow(self.ui.Cancel_button5)
        self.ui.Edit_button4.show()
        self.ui.Edit_button4.setGeometry(QRect(810, 500, 91, 31))
        self.wrap_with_shadow(self.ui.Edit_button4, 70)
        self.ui.tableWidget_grades.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.tableWidget_grades.setEditTriggers(QTableWidget.NoEditTriggers)

    def attendance(self):
        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()
        self.ui.info.hide()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.show()
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.hide()
            self.unwrap_shadow(i)
        self.wrap_with_shadow(self.ui.tableWidget_att, 70)
        self.refresh_attendance(self.current_user[-1], self.current_password[-1])

    def statistics(self):

        self.ui.info.hide()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.show()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.hide()
            self.unwrap_shadow(i)
        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()
        self.ui.performane.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                         "color :rgb(24, 182, 255);\n"
                                         "border: none;\n"
                                         "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                         "}\n"
                                         "")
        self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                      "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                            "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                    "font: 700 9pt \"Yu Gothic UI\";")
        self.refresh_graph1(self.current_user[-1], self.current_password[-1])
        self.refresh_graph2(self.current_user[-1], self.current_password[-1])
        self.animate_page(self.ui.Graph_frame, 1, 0, "white", 15, 351, 321)
        self.animate_page(self.ui.Graph_frame_2, 1, 0, "white", 15, 351, 321)

    def attendance_top(self):
        self.ui.attendancetop.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                            "color :rgb(24, 182, 255);\n"
                                            "border: none;\n"
                                            "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                            "}\n"
                                            "")
        self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                      "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.performane.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                    "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.info.hide()

        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            if i not in [self.ui.attendancetop, self.ui.ranking, self.ui.other, self.ui.performane]:
                i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.show()
        self.refresh_graph3(self.current_user[-1], self.current_password[-1])
        self.refresh_graph4(self.current_user[-1], self.current_password[-1])
        self.animate_page(self.ui.Graph_frame_7, 1, 0, "white", 15, 561, 331)
        self.animate_page(self.ui.Graph_frame_8, 1, 0, "white", 15, 191, 181)

    def performance(self):
        self.ui.info.hide()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.show()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()
        self.ui.performane.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                         "color :rgb(24, 182, 255);\n"
                                         "border: none;\n"
                                         "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                         "}\n"
                                         "")
        self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                      "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                            "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                    "font: 700 9pt \"Yu Gothic UI\";")
        self.refresh_graph1(self.current_user[-1], self.current_password[-1])
        self.refresh_graph2(self.current_user[-1], self.current_password[-1])
        self.animate_page(self.ui.Graph_frame, 1, 0, "white", 15, 351, 321)
        self.animate_page(self.ui.Graph_frame_2, 1, 0, "white", 15, 351, 321)

    def ranking(self):
        self.ui.info.hide()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            if i not in [self.ui.attendancetop, self.ui.ranking, self.ui.other, self.ui.performane]:
                i.hide()
        for i in self.widgets_statistics3:
            i.show()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()

        self.ui.ranking.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                      "color :rgb(24, 182, 255);\n"
                                      "border: none;\n"
                                      "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                      "}\n"
                                      "")
        self.ui.performane.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                            "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.other.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                    "font: 700 9pt \"Yu Gothic UI\";")

        self.refresh_graph5(self.current_user[-1], self.current_password[-1])
        self.refresh_graph6(self.current_user[-1], self.current_password[-1])
        self.animate_page(self.ui.Graph_frame_5, 1, 0, "white", 45, 351, 341)
        self.animate_page(self.ui.Graph_frame_6, 1, 0, "white", 45, 351, 341)

    def other(self):
        self.ui.info.hide()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            if i not in [self.ui.attendancetop, self.ui.ranking, self.ui.other, self.ui.performane]:
                i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.show()
        for i in self.widgets_statistics_4:
            i.hide()


        self.ui.other.setStyleSheet(u"QPushButton {font: 700 9pt \"Yu Gothic UI\";\n"
                                    "color :rgb(24, 182, 255);\n"
                                    "border: none;\n"
                                    "border-bottom: 2px solid rgb(24, 182, 255)\n"
                                    "}\n"
                                    "")
        self.ui.performane.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                         "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.attendancetop.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                            "font: 700 9pt \"Yu Gothic UI\";")
        self.ui.ranking.setStyleSheet(u"color: rgb(101, 119, 152);\n"
                                      "font: 700 9pt \"Yu Gothic UI\";")

        self.refresh_graph7(self.current_user[-1], self.current_password[-1])
        self.refresh_graph8(self.current_user[-1], self.current_password[-1])
        self.animate_page(self.ui.Graph_frame_3, 1, 0, "white", 15, 351, 321)
        self.animate_page(self.ui.Graph_frame_4, 1, 0, "white", 15, 351, 321)

    def SALT(self, user):
        data = load_data()
        for i in data:
            if i["username"] == user:
                salt = i["salt"]
        return bytes.fromhex(salt)

    def edit_page(self):
        self.ui.info.hide()
        for i in self.widgets_class:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_student_add:
            i.hide()
            self.unwrap_shadow(i)
        for j in self.widgets_home:
            j.hide()
            self.unwrap_shadow(j)
        for i in self.widgets_student_view:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widgets_to_clear:
            i.clear()
            self.unwrap_shadow(i)
        for i in self.widgets_grades:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.widget_Attendance:
            i.hide()
            self.unwrap_shadow(i)
        for i in self.error_labels:
            i.hide()
        for i in self.widgets_statistics:
            i.hide()
        for i in self.widgets_statistics3:
            i.hide()
        for i in self.widgets_statistics_2:
            i.hide()
        for i in self.widgets_statistics_4:
            i.hide()
        for i in self.widgets_edit:
            i.show()
        self.ui.Add_top_btn.hide()
        self.ui.View_top_btn.hide()
        data = load_data()
        for i in data:
            if i["username"] == self.current_user[-1] and int(i["max_score"]) == 20 :
                self.ui.info2.hide()
        self.wrap_with_shadow(self.ui.transfer_btn,70)
        self.wrap_with_shadow(self.ui.set_btn,70)

        c.execute("SELECT class_name FROM classes WHERE user = ?",(self.current_user[-1],))
        class_rows = c.fetchall()
        classes = [x[0] for x in class_rows]
        self.reset_line2(self.ui.score_line)



        for i,j in enumerate(classes):
            if self.ui.to_combobox.findText(j) == -1:
                self.ui.to_combobox.insertItem(i, j)
            if self.ui.from_combobox.findText(j) == -1:
                self.ui.from_combobox.insertItem(i, j)
        classe = self.ui.to_combobox.currentText()
        self.refresh_combo_id(self.current_user[-1], classe)


    def refresh_combo_id(self,user,classe):
        c.execute("SELECT student_id,class FROM students WHERE user =? ",(user,))
        students_rows = c.fetchall()
        students = []
        self.ui.id_combobox.clear()
        for i in students_rows:
            if decrypt_data(i[1],self.kdf) == classe :
                students.append(str(i[0]))
        for i,j in enumerate(students):
            if self.ui.id_combobox.findText(j) == -1:
                self.ui.id_combobox.insertItem(i, j)

    def transfer(self):

        to = self.ui.to_combobox.currentText()
        student = self.ui.id_combobox.currentText()
        c.execute("UPDATE students SET class =? WHERE user =? AND student_id = ?",(encrypt_data(to,self.kdf), self.current_user[-1],student))
        conn.commit()

        self.refresh_combo_id(self.current_user[-1], self.ui.from_combobox.currentText())

    def set(self):
        self.ui.info2.hide()
        data = load_data()
        err=False
        c.execute("SELECT grade FROM grades WHERE user =?",(self.current_user[-1],))
        grades = c.fetchall()
        grades2 = [int(x[0]) for x in grades]
        score = self.ui.score_line.text()

        if not re.fullmatch(r"[0-9]+",score):
            self.ui.errscore_lbl.setText("Invalid Score")
            self.ui.errscore_lbl.show()
            self.update_line2(self.ui.score_line)
            return
        for i in grades2 :
            if i> int(score):
                err = True
        if err:
            self.ui.errscore_lbl.setText("Some marks exceed the maximum score you entered.")
            self.update_line2(self.ui.score_line)
            self.ui.errscore_lbl.show()
            return
        self.reset_line2(self.ui.score_line)
        self.ui.errscore_lbl.hide()
        for i in data:
            if i["username"] == self.current_user[-1]:
                i.update({"max_score": score})
        self.ui.score_line.setText("")

        save_data(data)
        self.ui.info2.show() if int(score) != 20 else self.ui.info2.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main_app()
    window.show()
    sys.exit(app.exec())

