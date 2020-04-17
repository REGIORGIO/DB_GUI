from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QGridLayout, QTableWidget, QTableWidgetItem, QScrollArea, QVBoxLayout, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import traceback
import secondaryWindow
import startWindow

class addWindow(QWidget):
    def __init__(self, con, string):
        super().__init__()
        self.con = con
        self.string = string
        self.types = {}
        self.setGeometry(600, 250, 400, 300)
        self.setFixedSize(self.size())
        # self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))

        if self.string == 'client':
            self.setWindowTitle('Add a new client')
            l1 = QLabel('Client family name:', self)
            l1.move(30, 40)
            self.FNameEdit = QLineEdit(self)
            self.FNameEdit.move(190, 40)

            l2 = QLabel('Client name:', self)
            l2.move(30, 80)
            self.INameEdit = QLineEdit(self)
            self.INameEdit.move(190, 80)

            l3 = QLabel('Client father name:', self)
            l3.move(30, 120)
            self.ONameEdit = QLineEdit(self)
            self.ONameEdit.move(190, 120)

            l4 = QLabel('Passport seria:', self)
            l4.move(30, 160)
            self.seriaEdit = QLineEdit(self)
            re = QRegExp(r'[0-9]{4}')
            myValidator = QRegExpValidator(re, self.seriaEdit)
            self.seriaEdit.setValidator(myValidator)
            self.seriaEdit.move(190, 160)

            l5 = QLabel('Passport number:', self)
            l5.move(30, 200)
            self.numEdit = QLineEdit(self)
            re = QRegExp(r'[0-9]{6}')
            myValidator2 = QRegExpValidator(re, self.numEdit)
            self.numEdit.setValidator(myValidator2)
            self.numEdit.move(190, 200)
        elif self.string == 'book':
            self.setWindowTitle('Add a new book')
            l1 = QLabel('Book name:', self)
            l1.move(30, 70)
            self.bookNameEdit = QLineEdit(self)
            self.bookNameEdit.move(190, 70)

            l2 = QLabel('Count:', self)
            l2.move(30, 120)
            self.countEdit = QLineEdit(self)
            self.countEdit.setValidator(QIntValidator())
            self.countEdit.move(190,120)

            l3 = QLabel('Type:', self)
            l3.move(30, 170)

            cur = self.con.cursor()
            cur.execute("select id, name from book_types")
            Items = []
            for row in cur:
                self.types[row[1]] = row[0]
                Items.append(row[1])
            self.cb1 = QComboBox(self)
            self.cb1.addItems(Items)
            self.cb1.move(190, 170)
        else:
            self.setWindowTitle('Add a new book type')
            l1 = QLabel('Name:', self)
            l1.move(30, 70)
            self.nameEdit = QLineEdit(self)
            self.nameEdit.move(190, 70)

            l2 = QLabel('Fine:', self)
            l2.move(30, 120)
            self.fineEdit = QLineEdit(self)
            self.fineEdit.setValidator(QIntValidator())
            self.fineEdit.move(190, 120)

            l3 = QLabel('Days:', self)
            l3.move(30, 170)
            self.daysEdit = QLineEdit(self)
            self.daysEdit.setValidator(QIntValidator())
            self.daysEdit.move(190, 170)

        btnOK = QPushButton('Submit', self)
        btnOK.move(150, 250)
        btnOK.clicked.connect(self.OKclicked)

    def OKclicked(self):
        cur = self.con.cursor()
        if self.string == 'client':
            if len(self.FNameEdit.text()) == 0 or len(self.INameEdit.text()) == 0 or len(self.ONameEdit.text()) == 0 or len(self.seriaEdit.text()) == 0 or len(self.numEdit.text()) == 0:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Please fill all the fields!")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
            try:
                query = r"insert into clients (first_name,last_name,father_name,passport_seria,passport_num) values('"+self.INameEdit.text()+"','" + self.FNameEdit.text()+"','"+self.ONameEdit.text()+ "','"+self.seriaEdit.text()+"','"+self.numEdit.text() + "')"
                cur.execute(query)
                self.FNameEdit.setText("")
                self.INameEdit.setText("")
                self.ONameEdit.setText("")
                self.seriaEdit.setText("")
                self.numEdit.setText("")
            except:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("You've probably added client with passport that already in the database.")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
        elif self.string == 'book':
            if len(self.bookNameEdit.text()) == 0 or len(self.countEdit.text()) == 0:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Please fill all the fields!")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
            query = r"insert into books (name, cnt, type_id) values('"+self.bookNameEdit.text()+"', " + self.countEdit.text() + ", " + types[self.foreignCost.text()] + ")"
            cur.execute(query)
            self.bookNameEdit.setText("")
            self.countEdit.setText("")
        else:
            if len(self.nameEdit.text()) == 0 or len(self.fineEdit.text()) == 0 or len(self.daysEdit.text()) == 0:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Please fill all the fields!")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
            query = r"insert into book_types (name, cnt, fine, day_count) values('" + self.nameEdit.text() + "',0," + self.fineEdit.text() + "," + self.daysEdit.text() + ")"
            cur.execute(query)
            self.nameEdit.setText("")
            self.fineEdit.setText("")
            self.daysEdit.setText("")
        self.con.commit()
        self.close()


class modifyWindow(QWidget):
    def __init__(self, con, string):
        super().__init__()
        self.con = con
        self.string = string
        self.types = {}
        self.setGeometry(600, 250, 400, 300)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))

        if self.string == 'client':
            self.setWindowTitle('Modify client data')
            l0 = QLabel('Client ID:', self)
            l0.move(30, 20)
            cur = self.con.cursor()
            cur.execute("select id from clients")
            Items = []
            for row in cur:
                Items.append(str(row[0]))
            self.cb1 = QComboBox(self)
            self.cb1.addItems(Items)
            self.cb1.currentTextChanged.connect(self.comboChanged)
            self.cb1.move(190, 20)

            l1 = QLabel('New family name:', self)
            l1.move(30, 60)
            self.FNameEdit = QLineEdit(self)
            self.FNameEdit.move(190, 60)

            l2 = QLabel('New name:', self)
            l2.move(30, 100)
            self.INameEdit = QLineEdit(self)
            self.INameEdit.move(190, 100)

            l3 = QLabel('New father name:', self)
            l3.move(30, 140)
            self.ONameEdit = QLineEdit(self)
            self.ONameEdit.move(190, 140)

            l4 = QLabel('New passport seria:', self)
            l4.move(30, 180)
            self.seriaEdit = QLineEdit(self)
            re = QRegExp(r'[0-9]{4}')
            myValidator = QRegExpValidator(re, self.seriaEdit)
            self.seriaEdit.setValidator(myValidator)
            self.seriaEdit.move(190, 180)

            l5 = QLabel('New passport number:', self)
            l5.move(30, 220)
            self.numEdit = QLineEdit(self)
            re = QRegExp(r'[0-9]{6}')
            myValidator2 = QRegExpValidator(re, self.numEdit)
            self.numEdit.setValidator(myValidator2)
            self.numEdit.move(190, 220)

        elif self.string == 'book':
            self.setWindowTitle('Modify book')
            l0 = QLabel('Book ID:', self)
            l0.move(30, 20)
            cur = self.con.cursor()
            cur.execute("select id from books")
            Items = []
            for row in cur:
                Items.append(str(row[0]))
            self.cb1 = QComboBox(self)
            self.cb1.addItems(Items)
            self.cb1.currentTextChanged.connect(self.comboChanged)
            self.cb1.move(190, 20)

            l1 = QLabel('New book name:', self)
            l1.move(30, 70)
            self.bookNameEdit = QLineEdit(self)
            self.bookNameEdit.move(190, 70)

            l2 = QLabel('New count:', self)
            l2.move(30, 120)
            self.countEdit = QLineEdit(self)
            self.countEdit.setValidator(QIntValidator())
            self.countEdit.move(190, 120)

            l3 = QLabel('New type:', self)
            l3.move(30, 170)

            cur = self.con.cursor()
            cur.execute("select id, name from book_types")
            Items = []
            for row in cur:
                self.types[row[1]] = row[0]
                Items.append(row[1])
            self.cb2 = QComboBox(self)
            self.cb2.addItems(Items)
            self.cb2.move(190, 170)

        else:
            self.setWindowTitle('Modify book type')
            l0 = QLabel('Type ID:', self)
            l0.move(30, 20)
            cur = self.con.cursor()
            cur.execute("select id from book_types")
            Items = []
            for row in cur:
                Items.append(str(row[0]))
            self.cb1 = QComboBox(self)
            self.cb1.addItems(Items)
            self.cb1.currentTextChanged.connect(self.comboChanged)
            self.cb1.move(190, 20)

            l1 = QLabel('New name:', self)
            l1.move(60, 100)
            self.nameEdit = QLineEdit(self)
            self.nameEdit.move(190, 100)

        btnOK = QPushButton('Submit', self)
        btnOK.move(150, 260)
        btnOK.clicked.connect(self.OKclicked)
        self.comboChanged()

    def comboChanged(self):
        if self.string == 'client':
            cur = self.con.cursor()
            cur.execute(r"select * from clients where id = " + self.cb1.currentText())
            line = cur.fetchone()
            self.FNameEdit.setText(line[2])
            self.INameEdit.setText(line[1])
            self.ONameEdit.setText(line[3])
            self.seriaEdit.setText(line[4])
            self.numEdit.setText(line[5])
        elif self.string == 'book':
            cur = self.con.cursor()
            cur.execute(r"select books.name, books.cnt, book_types.name from books inner join book_types on books.type_id = book_types.id and books.id = " + self.cb1.currentText())
            line = cur.fetchone()
            self.bookNameEdit.setText(line[0])
            self.countEdit.setText(str(line[1]))
            index = self.cb2.findText(line[2])
            if index >= 0:
                self.cb2.setCurrentIndex(index)
        else:
            cur = self.con.cursor()
            cur.execute(r"select name from book_types where id = " + self.cb1.currentText())
            line = cur.fetchone()
            self.nameEdit.setText(line[0])

    def OKclicked(self):
        cur = self.con.cursor()
        if self.string == 'client':
            if len(self.FNameEdit.text()) == 0 or len(self.INameEdit.text()) == 0 or len(self.ONameEdit.text()) == 0 or len(self.seriaEdit.text()) == 0 or len(self.numEdit.text()) == 0:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Please fill all the fields!")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
            cur.execute(r"update clients set first_name = '"+self.INameEdit.text()+"',last_name = '"+self.FNameEdit.text()+"',father_name = '"+self.ONameEdit.text()+"',passport_seria = '"+self.seriaEdit.text()+"',passport_num ='"+self.numEdit.text()+"' where id = "+self.cb1.currentText())
            self.FNameEdit.setText("")
            self.INameEdit.setText("")
            self.ONameEdit.setText("")
            self.seriaEdit.setText("")
            self.numEdit.setText("")
        elif self.string == 'book':
            if len(self.bookNameEdit.text()) == 0 or len(self.countEdit.text()) == 0:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Please fill all the fields!")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
            cur.execute(r"update books set name = '"+self.bookNameEdit.text()+"', cnt = " + self.countEdit.text() + ", type_id = " + str(self.types[self.cb2.currentText()]) + " where id = "+self.cb1.currentText())
            self.bookNameEdit.setText("")
            self.countEdit.setText("")
        else:
            if len(self.nameEdit.text()) == 0:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Please fill all the fields!")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
            cur.execute(r"update book_types set name = '"+self.nameEdit.text()+"' where id = "+ self.cb1.currentText())
            self.nameEdit.setText("")
        self.con.commit()
        self.close()


class deleteWindow(QWidget):
    def __init__(self, con, string):
        super().__init__()
        self.con = con
        self.string = string
        self.setGeometry(600, 250, 300, 200)
        self.setFixedSize(self.size())
        self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))

        if self.string == 'client':
            self.setWindowTitle('Delete client data from database')
            l1 = QLabel('Client ID:', self)
            l1.move(50, 62)
            cur = self.con.cursor()
            cur.execute("select id from clients")
            Items = []
            for row in cur:
                Items.append(str(row[0]))
            self.cb1 = QComboBox(self)
            self.cb1.addItems(Items)
            self.cb1.move(170, 60)
        elif self.string == 'book':
            self.setWindowTitle('Delete book from database')
            l1 = QLabel('Book ID:', self)
            l1.move(50, 62)
            cur = self.con.cursor()
            cur.execute("select id from books")
            Items = []
            for row in cur:
                Items.append(str(row[0]))
            self.cb1 = QComboBox(self)
            self.cb1.addItems(Items)
            self.cb1.move(170, 60)
        else:
            self.setWindowTitle('Delete book type from database')
            l1 = QLabel('Type ID:', self)
            l1.move(50, 62)
            cur = self.con.cursor()
            cur.execute("select id from book_types")
            Items = []
            for row in cur:
                Items.append(str(row[0]))
            self.cb1 = QComboBox(self)
            self.cb1.addItems(Items)
            self.cb1.move(170, 60)

        btnOK = QPushButton('Submit', self)
        btnOK.move(80, 130)
        btnOK.clicked.connect(self.OKclicked)

    def OKclicked(self):
        cur = self.con.cursor()
        if self.string == 'client':
            try:
                cur.execute(r"delete from clients where id = "+self.cb1.currentText())
            except:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("This client has some records in library journal.")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return

        elif self.string == 'book':
            try:
                cur.execute(r"delete from books where id = "+self.cb1.currentText())
            except:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("This book has some records in library journal.")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
        else:
            try:
                cur.execute(r"delete from book_types where id = "+self.cb1.currentText())
            except:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("There are some books of this type in the library.")
                error_d.setWindowTitle("Error!")
                error_d.exec_()
                return
        self.con.commit()
        self.close()
