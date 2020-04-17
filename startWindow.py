from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import connect
import secondaryWindow
import procWindow
import sys


class StartWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(300, 200, 550, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle('Главное меню')

        # # self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))
        # self.names = {}
        # self.books = {}
        titleLabel = QLabel('Выберите дальнейшнее действие', self)
        titleLabel.move(120, 50)
        titleLabel.setFont(QFont('Helvetica', 20))
        #
        emp_btn = QPushButton('Employees', self)
        emp_btn.setToolTip('Browse all employees')
        emp_btn.move(50, 100)
        emp_btn.resize(120, 35)
        emp_btn.setFont(QFont('Helvetica', 15))
        # emp_btn.clicked.connect(self.ClientButtonClicked)
        #

        dep_btn = QPushButton('Departments', self)
        dep_btn.setToolTip('Browse all departments')
        dep_btn.move(220, 100)
        dep_btn.resize(120, 35)
        dep_btn.setFont(QFont('Helvetica', 15))
        # bookBtn.clicked.connect(self.BookButtonClicked)
        #
        proj_btn = QPushButton('Projects', self)
        proj_btn.setToolTip('Browse all projects')
        proj_btn.move(390, 100)
        proj_btn.resize(120, 35)
        proj_btn.setFont(QFont('Helvetica', 15))
        # booktypesBtn.clicked.connect(self.BookTypeButtonClicked)
        #
        # journalBtn = QPushButton('Journal', self)
        # journalBtn.setToolTip('Browse library journal')
        # journalBtn.move(580, 120

        # journalBtn.clicked.connect(self.JournalButtonClicked)
        #
        # createWorkLabel = QLabel('Modify Journal record', self)
        # createWorkLabel.move(260, 180)
        # createWorkLabel.setFont(QFont('Helvetica', 15))
        #
        # l1 = QLabel('Date (YYYY/MM/DD):', self)
        # l1.move(60, 240)
        # l1.setFont(QFont('Helvetica', 10))
        # l2 = QLabel('Client:', self)
        # l2.move(60, 280)
        # l2.setFont(QFont('Helvetica', 10))
        # l3 = QLabel('Wants to:', self)
        # l3.move(60, 320)
        # l3.setFont(QFont('Helvetica', 10))
        # l4 = QLabel('Book:', self)
        # l4.move(60, 360)
        # l4.setFont(QFont('Helvetica', 10))

        # self.submitBtn = QPushButton('Issue', self)
        # self.submitBtn.setToolTip('Issue the book to client')
        # self.submitBtn.move(150, 430)
        # self.submitBtn.action = 'Issue'
        # self.submitBtn.clicked.connect(self.SubmitButtonClicked)
        #
        # refreshBtn = QPushButton('Refresh', self)
        # refreshBtn.setToolTip('Refresh all tables')
        # refreshBtn.move(650, 20)
        # # refreshBtn.clicked.connect(self.refresh)
        #
        proc_btn = QPushButton('Procedures', self)
        proc_btn.setToolTip('Show procedures')
        proc_btn.move(135, 150)
        proc_btn.resize(120, 35)
        proc_btn.setFont(QFont('Helvetica', 15))
        # statBtn.clicked.connect(self.ProcButtonClicked)
        #
        # # #!!!!!!!!!!!!!!
        # # testBtn = QPushButton('Test', self)
        # # testBtn.move(650, 400)
        # # testBtn.clicked.connect(self.test)
        # #!!!!!!!!!!!!!!
        #
        exit_btn = QPushButton('Exit', self)
        exit_btn.setToolTip('Exit the Program')
        exit_btn.resize(100, 100)
        exit_btn.move(305, 150)
        exit_btn.resize(120, 35)
        exit_btn.setFont(QFont('Helvetica', 15))
        exit_btn.clicked.connect(self.ExitButtonClicked)

        # self.dateEdit = QLineEdit(self)
        # re = QRegExp(r'[0-9]{4}/{1}[0-9]{2}/{1}[0-9]{2}')
        # myValidator = QRegExpValidator(re, self.dateEdit)
        # self.dateEdit.setValidator(myValidator)
        # self.dateEdit.move(290, 240)

        self.show()
        # self.initDBEls()

    # def initDBEls(self):
    #     cur = self.con.cursor()
    #
    #     cur.execute("select id, concat(concat(concat(last_name,' '),concat(first_name,' ')),father_name) from clients")
    #     Items = []
    #     for row in cur:
    #         Items.append(row[1])
    #         self.names[row[1]] = row[0]
    #     self.cb1 = QComboBox(self)
    #     self.cb1.addItems(Items)
    #     self.cb1.move(290, 280)
    #     self.cb1.currentTextChanged.connect(self.comboChanged)
    #
    #     cur.execute('select id, name from books')
    #     Items = []
    #     for row in cur:
    #         Items.append(row[1])
    #         self.books[row[1]] = row[0]
    #     self.cb2 = QComboBox(self)
    #     self.cb2.addItems(Items)
    #     self.cb2.move(290, 360)
    #
    #     self.radio1 = QRadioButton("take a book",self)
    #     self.radio1.setChecked(True)
    #     self.radio1.move(290, 320)
    #     self.radio1.toggled.connect(self.takeChosen)
    #
    #     self.radio2 = QRadioButton("return a book",self)
    #     self.radio2.move(450, 320)
    #     self.radio2.toggled.connect(self.returnChosen)
    #
    #     self.clientWindow = secondaryWindow.ClientWindow(self.con)
    #     self.bookWindow = secondaryWindow.BookWindow(self.con)
    #     self.booktypeWindow = secondaryWindow.BooktypeWindow(self.con)
    #     self.journalWindow = secondaryWindow.JournalWindow(self.con)
    #     self.procWindow = procWindow.procWindow(self.con)
    #     self.show()
    #
    # def takeChosen(self):
    #     self.submitBtn.setText('Issue')
    #     self.submitBtn.action = 'Issue'
    #     self.submitBtn.setToolTip('Issue the book to client')
    #     self.change_books_list("take")
    #
    # def returnChosen(self):
    #     self.submitBtn.setText('Take')
    #     self.submitBtn.action = 'Take'
    #     self.submitBtn.setToolTip('Take the book from client')
    #     self.change_books_list("return")
    #
    # def comboChanged(self):
    #     if self.radio1.isChecked():
    #         self.change_books_list("take")
    #     else:
    #         self.change_books_list("return")
    #
    # def change_books_list(self, act):
    #     cur = self.con.cursor()
    #     if act == "return":
    #         cur.execute('select distinct books.name from journal inner join books on books.id = journal.book_id and date_end is null and client_id = ' + str(self.names[self.cb1.currentText()]))
    #     else:
    #         cur.execute('select name from books where cnt <> 0')
    #     Items = []
    #     for row in cur:
    #         Items.append(row[0])
    #     self.cb2.clear()
    #     self.cb2.addItems(Items)
    #
    def ExitButtonClicked(self):
        sys.exit(0)
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

    def test(self):
        cur = self.con.cursor()
        #cur.execute(r"select book_types.day_count from books inner join book_types on books.type_id = books_types.id and books.id = 14")

        cur.execute(r"select id from journal where date_beg < to_date('2019/06/03','yyyy/mm/dd') and id = 262")
        print(cur.fetchone())
        #con.commit()

# if __name__ == '__main__':
#     con = connect.getDBconnection()
#     app = QApplication(sys.argv)
#     startWindow = StartWindow(con)
#     sys.exit(app.exec_())