from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import connect
import secondaryWindow
import procWindow
import sys
import procedureWindow
import empWindow
import depWindow
import projWindow
import enterWindow


class StartWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(800, 400, 550, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle('Главное меню')

        self.procWindow = procedureWindow.procWindow(self.con)
        self.projWindow = projWindow.projWindow(self.con)
        self.depWindow = depWindow.depWindow(self.con)
        self.empWindow = empWindow.empWindow(self.con)


        titleLabel = QLabel('Выберите дальнейшнее действие', self)
        titleLabel.move(120, 50)
        titleLabel.setFont(QFont('Helvetica', 20))

        emp_btn = QPushButton('Employees', self)
        emp_btn.setToolTip('Browse all employees')
        emp_btn.move(50, 100)
        emp_btn.resize(120, 35)
        emp_btn.setFont(QFont('Helvetica', 15))
        emp_btn.clicked.connect(self.EmpButtonClicked)

        dep_btn = QPushButton('Departments', self)
        dep_btn.setToolTip('Browse all departments')
        dep_btn.move(220, 100)
        dep_btn.resize(120, 35)
        dep_btn.setFont(QFont('Helvetica', 15))
        dep_btn.clicked.connect(self.DepButtonClicked)

        proj_btn = QPushButton('Projects', self)
        proj_btn.setToolTip('Browse all projects')
        proj_btn.move(390, 100)
        proj_btn.resize(120, 35)
        proj_btn.setFont(QFont('Helvetica', 15))
        proj_btn.clicked.connect(self.ProjButtonClicked)

        proc_btn = QPushButton('Procedures', self)
        proc_btn.setToolTip('Show procedures')
        proc_btn.move(135, 150)
        proc_btn.resize(120, 35)
        proc_btn.setFont(QFont('Helvetica', 15))
        proc_btn.clicked.connect(self.ProcButtonClicked)

        logout_btn = QPushButton('Log out', self)
        logout_btn.setToolTip('Log out')
        logout_btn.resize(100, 100)
        logout_btn.move(305, 150)
        logout_btn.resize(120, 35)
        logout_btn.setFont(QFont('Helvetica', 15))
        logout_btn.clicked.connect(self.LogOutButtonClicked)

        # self.dateEdit = QLineEdit(self)
        # re = QRegExp(r'[0-9]{4}/{1}[0-9]{2}/{1}[0-9]{2}')
        # myValidator = QRegExpValidator(re, self.dateEdit)
        # self.dateEdit.setValidator(myValidator)
        # self.dateEdit.move(290, 240)

        self.show()

    def LogOutButtonClicked(self):
        self.close()
        self.empWindow.close()
        self.depWindow.close()
        self.procWindow.close()
        self.projWindow.close()
        self.enterWindow = enterWindow.EnterWindow()
        connect.shutDownConnection(self.con)
        self.enterWindow.show()

    def ProcButtonClicked(self):
        self.procWindow.show()
        if self.projWindow.isVisible():
            self.projWindow.close()

        if self.empWindow.isVisible():
            self.empWindow.close()

        if self.depWindow.isVisible():
            self.depWindow.close()

    def EmpButtonClicked(self):
        self.empWindow.show()

        if self.projWindow.isVisible():
            self.projWindow.close()

        if self.procWindow.isVisible():
            self.procWindow.close()

        if self.depWindow.isVisible():
            self.depWindow.close()

    def DepButtonClicked(self):
        self.depWindow.show()
        if self.projWindow.isVisible():
            self.projWindow.close()

        if self.empWindow.isVisible():
            self.empWindow.close()

        if self.procWindow.isVisible():
            self.procWindow.close()

    def ProjButtonClicked(self):
        self.projWindow.show()
        if self.procWindow.isVisible():
            self.procWindow.close()

        if self.empWindow.isVisible():
            self.empWindow.close()

        if self.depWindow.isVisible():
            self.depWindow.close()

    #
    # def ClientButtonClicked(self):
    #     self.bookWindow.close()
    #     self.booktypeWindow.close()
    #     self.journalWindow.close()
    #     self.clientWindow.show()
    #
    # def BookButtonClicked(self):
    #     self.booktypeWindow.close()
    #     self.journalWindow.close()
    #     self.clientWindow.close()
    #     self.bookWindow.show()
    #
    # def BookTypeButtonClicked(self):
    #     self.bookWindow.close()
    #     self.journalWindow.close()
    #     self.clientWindow.close()
    #     self.booktypeWindow.show()
    #
    # def JournalButtonClicked(self):
    #     self.bookWindow.close()
    #     self.booktypeWindow.close()
    #     self.clientWindow.close()
    #     self.journalWindow.show()
    #
    # def ProcButtonClicked(self):
    #     self.procWindow.show()
    #
    # def refresh(self):
    #     self.hide()
    #     self.clientWindow.close()
    #     self.bookWindow.close()
    #     self.booktypeWindow.close()
    #     self.journalWindow.close()
    #     self.procWindow.close()
    #     self.initDBEls()
    #
    # def SubmitButtonClicked(self):
    #     if (len(self.dateEdit.text()) != 10):
    #         error_d = QMessageBox()
    #         error_d.setIcon(QMessageBox.Critical)
    #         error_d.setText("Date is not correct!")
    #         error_d.setWindowTitle("Error!")
    #         error_d.exec_()
    #     else:
    #         if self.radio1.isChecked():     # Client wants to take book
    #             book_id = self.books[self.cb2.currentText()]
    #             cur = self.con.cursor()
    #             cur.execute(r"select book_types.day_count from book_types inner join books on book_types.id = books.type_id and books.id = "+str(book_id))
    #             days = cur.fetchone()[0]
    #             try:
    #                 cur.execute(r"insert into journal (book_id,client_id,date_beg,date_end,date_ret) values ("+str(book_id)+","+str(self.names[self.cb1.currentText()])+",to_date('"+self.dateEdit.text()+"','yyyy/mm/dd'),null,to_date('"+self.dateEdit.text()+"','yyyy/mm/dd') + " + str(days) + ")")
    #             except:
    #                 error_d = QMessageBox()
    #                 error_d.setIcon(QMessageBox.Critical)
    #                 error_d.setText("No more than 10 books for a client!")
    #                 error_d.setWindowTitle("Error!")
    #                 error_d.exec_()
    #                 return
    #             self.dateEdit.setText("")
    #         else:                           # Client wants to return book
    #             if len(self.cb2.currentText()) == 0:
    #                 return
    #             else:
    #                 book_id = self.books[self.cb2.currentText()]
    #                 client_id = self.names[self.cb1.currentText()]
    #                 cur = self.con.cursor()
    #                 cur.execute(r"select id from journal where client_id = "+str(client_id)+" and book_id = "+str(book_id)+" and date_end is null")
    #                 id = cur.fetchone()[0]
    #                 try:
    #                     cur.execute(r"update journal set date_end = to_date('" + self.dateEdit.text() + "','yyyy/mm/dd') where id = "+str(id))
    #                 except:
    #                     error_d = QMessageBox()
    #                     error_d.setIcon(QMessageBox.Critical)
    #                     error_d.setText("Date of return is incorrect!")
    #                     error_d.setWindowTitle("Error!")
    #                     error_d.exec_()
    #                     return
    #             self.dateEdit.setText("")
    #         self.con.commit()

