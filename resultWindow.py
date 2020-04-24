from PyQt5.QtGui import *
from PyQt5.QtWidgets import QTableWidget, QWidget, QPushButton, QMessageBox, QTableWidgetItem


class resultWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(1400, 400, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Результат')
        self.l = ''
        self.text1 = ''
        self.text2 = ''
        self.text3 = ''
        self.third_btn = QPushButton('Записать в файл', self)
        self.third_btn.resize(500, 40)
        self.third_btn.move(200, 450)
        self.third_btn.setFont(QFont('Helvetica', 15))

    def update_table1(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from output_d')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setColumnWidth(0, 250)
            self.table.setColumnWidth(1, 250)
            self.table.setHorizontalHeaderLabels(['Название отдела', 'Среднее время работы (в месяцах)'])
            cur.execute("select * from output_d")

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 2):
                    ##print(ll[i][j])
                    if j == 1 & (str(ll[i][j]) != 'None'):
                        ##print(round(float(ll[i][j]), 1))
                        self.table.setItem(i, j, QTableWidgetItem(str(round(float(ll[i][j]), 1))))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            # third_btn = QPushButton('Записать в файл', self)
            # third_btn.resize(500, 40)
            # third_btn.move(200, 450)
            # third_btn.show()
            self.third_btn.clicked.connect(self.click1)

        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setWindowTitle("Ошибка загрузки данных!\n Повторите попытку позднее")

    def update_table2(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from table_pr5')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setColumnWidth(0, 500)
            print(self.text1)
            self.table.setHorizontalHeaderLabels(
                ["Прибыль с '{}'".format(self.text1 + '/' + (self.text2) + '/' + self.text3)])
            cur.execute("select * from table_pr5")

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 1):
                    self.table.setItem(i, j, QTableWidgetItem(str(round(float(ll[i][j]), 1))))

            self.table.show()
            # third_btn = QPushButton('Записать в файл', self)
            # third_btn.resize(500, 40)
            # third_btn.move(200, 450)
            # third_btn.setFont(QFont('Helvetica', 15))
            # third_btn.show()
            self.third_btn.clicked.connect(self.click2)
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setWindowTitle("Ошибка загрузки данных!\n Повторите попытку позднее")

    def update_table3(self):

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from table_pr3')

            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setHorizontalHeaderLabels(
                ["Самый продолжительный проект отдела №'{}'".format(self.text1), 'Время (в месяцах)'])
            cur.execute("select * from table_pr3")
            self.table.setColumnWidth(0, 320)
            self.table.setColumnWidth(1, 190)

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 2):
                    ##print(ll[i][j])
                    if j == 1 & (str(ll[i][j]) != 'None'):
                        self.table.setItem(i, j, QTableWidgetItem(str(round(float(ll[i][j]), 1))))
                    else:
                        self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()

            # third_btn = QPushButton('Записать в файл', self)
            # third_btn.resize(500, 40)
            # third_btn.move(200, 450)
            # third_btn.setFont(QFont('Helvetica', 15))
            # ##third_btn.clicked.connect()
            # ##third_btn.show()
            self.third_btn.clicked.connect(self.click3)

        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setWindowTitle("Ошибка загрузки данных!\n Повторите попытку позднее")

    def update_table4(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(520, 450)
        self.table.move(185, 0)
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from outp')

            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setHorizontalHeaderLabels(
                ["Совместные проекты служащих №'{}' и №'{}'".format(self.text1, self.text2)])
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
            # third_btn = QPushButton('Записать в файл', self)
            # third_btn.resize(500, 40)
            # third_btn.move(200, 450)
            # third_btn.setFont(QFont('Helvetica', 15))
            # # third_btn.show()
            self.third_btn.clicked.connect(self.click4)
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setWindowTitle("Ошибка загрузки данных!\n Повторите попытку позднее")

    def click1(self):
        f = open('1.txt', 'w')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click2(self):
        f = open('2.txt', 'w')
        f.write("Прибыль с '{}'".format(self.text1 + '/' + (self.text2) + '/' + self.text3))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click3(self):
        f = open('3.txt', 'w')
        f.write("Самый продолжительный проект отдела №'{}'".format(self.text1))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def click4(self):
        f = open('4.txt', 'w')
        f.write("Совместные проекты служащих №'{}' и №'{}'".format(self.text1, self.text2))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()
