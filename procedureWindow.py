from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import secondaryWindow
import procWindow
import sys
import startWindow
import resultWindow
import cx_Oracle
import datetime
import time

class procWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.resWindow = resultWindow.resultWindow(self.con)
        self.setGeometry(1500, 400, 900, 500)
        ##self.setGeometry(300, 200, 550, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle('Выберите процедуру')

        first_btn = QPushButton('Отделы и среднее время их работы над проектами', self)
        ##first_btn.setToolTip('Вывести все отделы и вре')
        first_btn.resize(500, 40)
        first_btn.move(200, 10)
        first_btn.setFont(QFont('Helvetica', 15))
        first_btn.clicked.connect(self.proc1)

        second_btn = QPushButton('Расчет суммы прибыли от завершенных проектов', self)
        second_btn.resize(500, 40)
        second_btn.move(200, 70)
        second_btn.setFont(QFont('Helvetica', 15))
        second_btn.clicked.connect(self.proc2)

        self.l4 = QLabel('Введите начальную дату периода', self)
        self.l4.resize(310, 100)
        self.l4.move(320, 220)
        self.l4.setFont(QFont('Helvetica', 16))
        self.l5 = QLabel('(Формат DD/MM/YYYY)', self)
        self.l5.resize(310, 100)
        self.l5.move(380, 240)
        self.l5.setFont(QFont('Helvetica', 13))
        self.l4.hide()
        self.l5.hide()


        self.text = QLineEdit(self)
        self.text.resize(110, 50)
        self.text.move(390, 310)
        self.text.hide()


        third_btn = QPushButton('Самый продолжительный проект выбранного отдела', self)
        third_btn.resize(500, 40)
        third_btn.move(200, 130)
        third_btn.setFont(QFont('Helvetica', 15))

        self.l3 = QLabel('Отдел', self)
        self.l3.resize(300, 50)
        self.l3.move(430, 230)
        self.l3.hide()

        self.box3 = QComboBox(self)
        self.box3.resize(200, 160)
        self.box3.move(350, 200)
        self.box3.hide()
        third_btn.clicked.connect(self.proc3)

        last_btn = QPushButton('Проекты двух выбранных служащих', self)
        last_btn.resize(500, 40)
        last_btn.move(200, 190)
        last_btn.setFont(QFont('Helvetica', 15))
        last_btn.clicked.connect(self.proc4)
        self.l1 = QLabel('Первый', self)
        self.l1.resize(200, 160)
        self.l1.move(330, 180)
        self.l1.hide()

        self.l2 = QLabel('Второй', self)
        self.l2.resize(200, 160)
        self.l2.move(520, 180)
        self.l2.hide()

        self.box1 = QComboBox(self)
        self.box1.resize(200, 160)
        self.box1.move(250, 200)
        self.box1.hide()

        self.box2 = QComboBox(self)
        self.box2.resize(200, 160)
        self.box2.move(450, 200)
        self.box2.hide()

        self.btn_show2 = QPushButton('Посмотреть результат', self)
        self.btn_show2.resize(300, 50)
        self.btn_show2.move(300, 375)
        self.btn_show2.setFont(QFont('Helvetica', 15))

        self.btn_show3 = QPushButton('Посмотреть результат', self)
        self.btn_show3.resize(300, 50)
        self.btn_show3.move(300, 330)
        self.btn_show3.setFont(QFont('Helvetica', 15))

        self.btn_show3.hide()
        self.btn_show2.hide()

        self.btn_show4 = QPushButton('Посмотреть результат', self)
        self.btn_show4.resize(300, 50)
        self.btn_show4.move(300, 330)
        self.btn_show4.setFont(QFont('Helvetica', 15))

        self.btn_show4.hide()
        ##self.box1.hide()
        ##self.box1.addItems()

        back_btn = QPushButton('Вернуться на главную страницу', self)
        back_btn.resize(300, 50)
        back_btn.move(300, 440)
        back_btn.setFont(QFont('Helvetica', 15))
        back_btn.clicked.connect(self.backToStart)

        ##self.show()

    def backToStart(self):
        self.procWindow = startWindow.StartWindow(self.con)
        self.close()

    def proc1(self):
        self.l4.hide()
        self.l5.hide()
        self.text.hide()
        self.btn_show2.hide()
        self.btn_show3.hide()
        self.box3.hide()
        self.l3.hide()
        self.box1.hide()
        self.box2.hide()
        self.l1.hide()
        self.l2.hide()
        self.btn_show4.hide()
        self.showRes1()


    def proc2(self):
        self.btn_show3.hide()
        self.box3.hide()
        self.l3.hide()
        self.box1.hide()
        self.box2.hide()
        self.l1.hide()
        self.l2.hide()
        self.btn_show4.hide()
        ##self.showRes2()
        self.l4.show()
        self.l5.show()
        self.text.show()
        self.btn_show2.show()
        self.btn_show2.clicked.connect(self.showRes2)

    def proc3(self):
        self.l4.hide()
        self.l5.hide()
        self.text.hide()
        self.btn_show2.hide()
        self.btn_show4.hide()
        self.box1.hide()
        self.box2.hide()
        self.l1.hide()
        self.l2.hide()
        self.box3.show()
        self.l3.show()
        self.btn_show3.show()
        self.init_box3()
        self.btn_show3.clicked.connect(self.showRes3)

    def proc4(self):
        self.l4.hide()
        self.l5.hide()
        self.text.hide()
        self.btn_show2.hide()
        self.btn_show3.hide()
        self.box3.hide()
        self.l3.hide()
        self.box1.show()
        self.box2.show()
        self.l1.show()
        self.l2.show()
        self.btn_show4.show()
        self.init_box1()
        self.init_box2()
        self.btn_show4.clicked.connect(self.showRes4)

    def init_box1(self):
        cur = self.con.cursor()
        self.box1.clear()
        cur.execute("select id from employees")
        l = cur.fetchall()
        for id in l:
            self.box1.addItem(str(id[0]))

        self.box1.setCurrentIndex(0)

    def init_box2(self):
        cur = self.con.cursor()
        self.box2.clear()
        cur.execute("select id from employees")
        l = cur.fetchall()
        for id in l:
            self.box2.addItem(str(id[0]))

        self.box2.setCurrentIndex(0)

    def init_box3(self):
        cur = self.con.cursor()
        self.box3.clear()
        cur.execute("select id from departments")
        l = cur.fetchall()
        for id in l:
            self.box3.addItem(str(id[0]))

        self.box3.setCurrentIndex(0)

    def showRes1(self):
        self.resWindow.show()
        cur = self.con.cursor()
        cur.callproc('output_dep')
        # cur2 = self.con.cursor()
        # cur2.execute('select * from output_d')
        # l = cur2.fetchall()
        # for id in l:
        #     print(id)

        self.resWindow.update_table1()

    def showRes2(self):
        self.resWindow.show()

        cur = self.con.cursor()
        ##rep_date = datetime.date(1,1,2019)
        date = datetime.date(2019,1,1)
        date = str(date.strftime('%d.%m.%Y'))
        print(date)
        cur_val = cur.var(cx_Oracle.NUMBER)
        cur.callproc('pr_5', ['01.01.19'])

        cur2 = self.con.cursor()
        cur2.execute('select * from table_pr5')
        l = cur2.fetchall()
        for id in l:
            print(id)
        # cur.execute('''v_date DATE:= '01/01/2019;''')
        # cur.execute('''profit NUMBER;''')
        # cur.execute('''pr_5(v_date, profit);''')

    def showRes3(self):
        self.resWindow.show()
        self.resWindow.show()
        cur = self.con.cursor()
        cur.callproc('pr_3', [int(self.box3.currentText())])

        # cur2 = self.con.cursor()
        # cur2.execute('select * from table_pr3')
        # l = cur2.fetchall()
        # for id in l:
        #     print(id)
        self.resWindow.update_table3()

    def showRes4(self):
        self.resWindow.show()
        cur = self.con.cursor()
        cur.callproc('proj2', [int(self.box1.currentText()), int(self.box2.currentText())])

        # cur2 = self.con.cursor()
        # cur2.execute('select * from outp')
        # l = cur2.fetchall()
        # for id in l:
        #     print(id)
        self.resWindow.update_table4()


