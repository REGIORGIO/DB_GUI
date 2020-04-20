from PyQt5 import QtCore
from PyQt5.QtWidgets import QTableWidget, QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import secondaryWindow
import procWindow
import sys
import startWindow
import pdfrw

class resultWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(1500, 400, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Результат')
        self.l = '';

    def update_table1(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        cur.execute('select count(*) from output_d')
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setColumnWidth(0, 250)
        self.table.setColumnWidth(1,250)
        self.table.setHorizontalHeaderLabels(['Название отдела', 'Среднее время работы над проектами'])
        cur.execute("select * from output_d")

        self.l = cur.fetchall()
        ll = []
        for el in self.l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 2):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

        self.table.show()
        third_btn = QPushButton('Записать в файл', self)
        third_btn.resize(500, 40)
        third_btn.move(200, 450)
        third_btn.setFont(QFont('Helvetica', 15))
        ##third_btn.clicked.connect()
        third_btn.show()
        # f = open('1.txt', 'w')
        # for id in l:
        #     f.writelines(str(id))
        #     f.write('\n')
        third_btn.clicked.connect(self.click1)

    def update_table2(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        cur.execute('select count(*) from outp')
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['Название'])
        cur.execute("select * from outp")

        self.l = cur.fetchall()
        ll = []
        for el in self.l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 1):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

        self.table.show()
        third_btn = QPushButton('Записать в файл', self)
        third_btn.resize(500, 40)
        third_btn.move(200, 450)
        third_btn.setFont(QFont('Helvetica', 15))
        ##third_btn.clicked.connect()
        third_btn.show()
        third_btn.clicked.connect(self.click2)

    def update_table3(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        cur.execute('select count(*) from table_pr3')

        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['Название проекта', 'Время'])
        cur.execute("select * from table_pr3")
        self.table.setColumnWidth(0, 300)
        self.table.setColumnWidth(1, 200)

        self.l = cur.fetchall()
        ll = []
        for el in self.l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 2):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

        self.table.show()

        third_btn = QPushButton('Записать в файл', self)
        third_btn.resize(500, 40)
        third_btn.move(200, 450)
        third_btn.setFont(QFont('Helvetica', 15))
        ##third_btn.clicked.connect()
        third_btn.show()
        third_btn.clicked.connect(self.click3)

    def update_table4(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        cur.execute('select count(*) from outp')

        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['Название'])
        cur.execute("select * from outp")
        self.table.setColumnWidth(0, 500)

        self.l = cur.fetchall()
        ll = []
        for el in self.l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 1):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

        self.table.show()
        third_btn = QPushButton('Записать в файл', self)
        third_btn.resize(500, 40)
        third_btn.move(200, 450)
        third_btn.setFont(QFont('Helvetica', 15))
        ##third_btn.clicked.connect()
        third_btn.show()
        third_btn.clicked.connect(self.click4)

    def click1(self):
        f = open('1.txt', 'w')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click2(self):
        f = open('2.txt', 'w')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click3(self):
        f = open('3.txt', 'w')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click4(self):
        f = open('4.txt', 'w')
        for id in self.l:
            f.writelines(id)
            f.write('\n')
        f.close()
