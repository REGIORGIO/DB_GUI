from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QGridLayout, QTableWidget, QTableWidgetItem, QScrollArea, QVBoxLayout, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import traceback
import datetime
import cx_Oracle

class procWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 200, 450, 600)
        self.setFixedSize(self.size())
        self.setWindowTitle('Procedures')
        self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))
        self.names = {}
        self.books = {}

        issuedLabel = QLabel('Number of issued books', self)
        issuedLabel.move(70, 20)
        issuedLabel.setFont(QFont('SasSerif', 15))

        self.l1 = QLabel('Client name:', self)
        self.l1.move(80, 70)
        cur = self.con.cursor()

        cur.execute("select id,concat(concat(last_name,' '),first_name) from clients")
        Items = []
        for row in cur:
            self.names[row[1]] = row[0]
            Items.append(row[1])
        self.cbClientNB = QComboBox(self)
        self.cbClientNB.addItems(Items)
        self.cbClientNB.move(180, 69)
        self.cbClientNB.currentTextChanged.connect(self.comboClientNBChanged)

        client_id = self.names[self.cbClientNB.currentText()]

        num_of_books = cur.var(cx_Oracle.NUMBER)
        cur.callproc("cnt",[client_id,num_of_books])
        self.labelNB = QLabel("                                                                        ", self)
        self.labelNB.setText(self.formNBLabel(num_of_books.getvalue()))
        self.labelNB.move(80,100)

        borrowLabel = QLabel('Borrow time record', self)
        borrowLabel.move(90, 150)
        borrowLabel.setFont(QFont('SasSerif', 15))

        self.l1 = QLabel('Book name:', self)
        self.l1.move(60, 200)
        cur = self.con.cursor()

        cur.execute("select id,name from books")
        Items = []
        for row in cur:
            self.books[row[1]] = row[0]
            Items.append(row[1])
        self.cbBookMB = QComboBox(self)
        self.cbBookMB.addItems(Items)
        self.cbBookMB.move(160, 199)
        self.cbBookMB.currentTextChanged.connect(self.comboBookMBChanged)

        book_id = self.books[self.cbBookMB.currentText()]

        max_days = cur.var(cx_Oracle.NUMBER)
        max_client_id = cur.var(cx_Oracle.NUMBER)
        cur.callproc("record_borrow",[book_id,max_days,max_client_id])
        self.labelMB = QLabel(self.formMBLabel(max_days.getvalue(),max_client_id.getvalue()), self)
        self.labelMB.move(60,230)

        topThreeLabel = QLabel('Top three books', self)
        topThreeLabel.move(110, 280)
        topThreeLabel.setFont(QFont('SasSerif', 15))

        first = cur.var(cx_Oracle.NUMBER)
        second = cur.var(cx_Oracle.NUMBER)
        third = cur.var(cx_Oracle.NUMBER)
        cur.callproc("top_three_ever",[first,second,third])
        cur.execute(r"select name from books where id = "+str(int(first.getvalue())))
        first = cur.fetchone()[0]
        cur.execute(r"select name from books where id = " + str(int(second.getvalue())))
        second = cur.fetchone()[0]
        cur.execute(r"select name from books where id = " + str(int(third.getvalue())))
        third = cur.fetchone()[0]
        labeltext = "      Top three books borrowed \nthrougout the history of library are:\n\t1. " + first + "\n\t2. " + second + "\n\t3. " + third

        self.labelTT = QLabel(labeltext, self)
        self.labelTT.move(90,330)

        finesLabel = QLabel('Sum of fines', self)
        finesLabel.move(130, 450)
        finesLabel.setFont(QFont('SasSerif', 15))

        self.l2 = QLabel('From:', self)
        self.l2.move(50, 500)
        self.fromEdit = QLineEdit(self)
        re = QRegExp(r'[0-9]{4}/{1}[0-9]{2}/{1}[0-9]{2}')
        fromValidator = QRegExpValidator(re, self.fromEdit)
        self.fromEdit.setValidator(fromValidator)
        self.fromEdit.move(100, 500)

        self.l3 = QLabel('to:', self)
        self.l3.move(50, 540)
        self.toEdit = QLineEdit(self)
        toValidator = QRegExpValidator(re, self.toEdit)
        self.toEdit.setValidator(toValidator)
        self.toEdit.move(100, 540)

        cntBtn = QPushButton('Count', self)
        cntBtn.setToolTip('Count sum of fines')
        cntBtn.move(300, 500)
        cntBtn.clicked.connect(self.CountClicked)

        self.cntLabel = QLabel(' -                    ',self)
        self.cntLabel.move(330,550)


    def formNBLabel(self,num):
        if num == 0:
            return "hasn't got any books right now."
        elif num % 10 == 1:
            return "has " + str(int(num)) + " book right now."
        else:
            return "has " + str(int(num)) + " books right now."

    def formMBLabel(self,days,client):
        if days == 0:
            return "This book hasn't been taken yet."
        else:
            cur = self.con.cursor()
            cur.execute(r"select concat(concat(last_name,' '),first_name) from clients where id = "+str(client))
            name = cur.fetchone()[0]
            if days % 10 == 1:
                return "The record of " + str(int(days)) + " day was set by " + name
            else:
                return "The record of " + str(int(days)) + " days was set by " + name

    def comboClientNBChanged(self):
        client_id = self.names[self.cbClientNB.currentText()]
        cur = self.con.cursor()
        num_of_books = cur.var(cx_Oracle.NUMBER)
        cur.callproc("cnt", [client_id, num_of_books])
        self.labelNB.setText(self.formNBLabel(num_of_books.getvalue()))

    def comboBookMBChanged(self):
        book_id = self.books[self.cbBookMB.currentText()]
        cur = self.con.cursor()
        max_days = cur.var(cx_Oracle.NUMBER)
        max_client_id = cur.var(cx_Oracle.NUMBER)
        cur.callproc("record_borrow", [book_id, max_days, max_client_id])
        self.labelMB.setText(self.formMBLabel(max_days.getvalue(), max_client_id.getvalue()))

    def CountClicked(self):
        fromTime = self.fromEdit.text()
        toTime = self.toEdit.text()
        if len(fromTime) != 10 or len(toTime) != 10:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setText("Date is not correct!")
            error_d.setWindowTitle("Error!")
            error_d.exec_()
        else:
            cur = self.con.cursor()
            year1 = int(fromTime[:4])
            month1 = int(fromTime[5:7])
            day1 = int(fromTime[8:])
            year2 = int(toTime[:4])
            month2 = int(toTime[5:7])
            day2 = int(toTime[8:])
            fromTime = datetime.date(year1,month1,day1)
            toTime = datetime.date(year2, month2, day2)
            if fromTime >= toTime:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Date is not correct!")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
            sum = cur.var(cx_Oracle.NUMBER)
            cur.callproc("fine_sum",[datetime.date(year1,month1,day1),datetime.date(year2,month2,day2),sum])
            self.cntLabel.setText(str(int(sum.getvalue()))+" rub.")
