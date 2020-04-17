from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QGridLayout, QTableWidget, QTableWidgetItem, QScrollArea, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import startWindow
import actionsWindow
import sys

class ClientWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.initUI()

    def initUI(self):
        self.setGeometry(1150, 200, 700, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Clients')
        self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))

        btnAdd = QPushButton('Add a new client', self)
        btnAdd.clicked.connect(self.addNewClient)
        btnMofidy = QPushButton('Modify table', self)
        btnMofidy.clicked.connect(self.modifyClient)
        btnDelete = QPushButton('Delete a client', self)
        btnDelete.clicked.connect(self.deleteClient)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)

        cur = self.con.cursor()
        cur.execute('select count(*) from clients')
        N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Family Name', 'Name', 'Father Name', 'Passport'])
        cur.execute("select id, last_name, first_name, father_name, concat(passport_seria,concat(' ',passport_num)) from clients")
        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, N_ROWS):
            for j in range(0, 5):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))
        self.table.resizeColumnsToContents()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        scroll = QScrollArea()
        scroll.setWidget(self.table)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        layout.addWidget(btnAdd)
        layout.addWidget(btnMofidy)
        layout.addWidget(btnDelete)
        self.setLayout(layout)

        self.newC = actionsWindow.addWindow(self.con, 'client')
        self.modC = actionsWindow.modifyWindow(self.con, 'client')
        self.delC = actionsWindow.deleteWindow(self.con, 'client')

    def addNewClient(self):
        self.modC.close()
        self.delC.close()
        self.newC.show()

    def modifyClient(self):
        self.delC.close()
        self.newC.close()
        self.modC.show()

    def deleteClient(self):
        self.newC.close()
        self.modC.close()
        self.delC.show()


class BookWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.initUI()

    def initUI(self):
        self.setGeometry(1150, 200, 700, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Books')
        self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))

        btnAdd = QPushButton('Add new book', self)
        btnAdd.clicked.connect(self.addNewBook)
        btnMofidy = QPushButton('Modify table', self)
        btnMofidy.clicked.connect(self.modifyBook)
        btnDelete = QPushButton('Delete book', self)
        btnDelete.clicked.connect(self.deleteBook)

        self.table = QTableWidget(self)
        self.table.setColumnCount(4)

        cur = self.con.cursor()
        cur.execute('select count(*) from books')
        N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Count', 'Type'])
        cur.execute('select books.id, books.name, books.cnt, book_types.name from books inner join book_types on books.type_id = book_types.id')
        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, N_ROWS):
            for j in range(0, 4):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))
        self.table.resizeColumnsToContents()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        scroll = QScrollArea()
        scroll.setWidget(self.table)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        layout.addWidget(btnAdd)
        layout.addWidget(btnMofidy)
        layout.addWidget(btnDelete)
        self.setLayout(layout)

        self.newB = actionsWindow.addWindow(self.con, 'book')
        self.modB = actionsWindow.modifyWindow(self.con, 'book')
        self.delB = actionsWindow.deleteWindow(self.con, 'book')

    def addNewBook(self):
        self.modB.close()
        self.delB.close()
        self.newB.show()

    def modifyBook(self):
        self.delB.close()
        self.newB.close()
        self.modB.show()

    def deleteBook(self):
        self.modB.close()
        self.newB.close()
        self.delB.show()

class BooktypeWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.initUI()

    def initUI(self):
        self.setGeometry(1150, 200, 700, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Book types')
        self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))

        btnAdd = QPushButton('Add new book type', self)
        btnAdd.clicked.connect(self.addNewType)
        btnMofidy = QPushButton('Modify table', self)
        btnMofidy.clicked.connect(self.modifyType)
        btnDelete = QPushButton('Delete book type', self)
        btnDelete.clicked.connect(self.deleteType)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)

        cur = self.con.cursor()
        cur.execute('select count(*) from book_types')
        N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Count', 'Fine', 'Days'])
        cur.execute('select * from book_types')
        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, N_ROWS):
            for j in range(0, 5):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))
        self.table.resizeColumnsToContents()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        scroll = QScrollArea()
        scroll.setWidget(self.table)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        layout.addWidget(btnAdd)
        layout.addWidget(btnMofidy)
        layout.addWidget(btnDelete)
        self.setLayout(layout)

        self.newT = actionsWindow.addWindow(self.con, 'type')
        self.modT = actionsWindow.modifyWindow(self.con, 'type')
        self.delT = actionsWindow.deleteWindow(self.con, 'type')

    def addNewType(self):
        self.modT.close()
        self.delT.close()
        self.newT.show()

    def modifyType(self):
        self.delT.close()
        self.newT.close()
        self.modT.show()

    def deleteType(self):
        self.modT.close()
        self.newT.close()
        self.delT.show()


class JournalWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.initUI()

    def initUI(self):
        self.setGeometry(1150, 200, 700, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Library Journal')
        self.setWindowIcon(QIcon(r'C:\Users\Kirill\PycharmProjects\LibraryBD\logo.png'))

        self.table = QTableWidget(self)
        self.table.setColumnCount(6)

        cur = self.con.cursor()
        cur.execute('select count(*) from journal')
        N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Book', 'Client', 'Date begin', 'Date end', 'Date return'])
        cur.execute("select journal.id, books.name, concat(last_name, concat(' ',first_name)), date_beg, date_end, date_ret from journal inner join books on journal.book_id = books.id inner join clients on clients.id = journal.client_id")
        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, N_ROWS):
            for j in range(0, 6):
                string = str(ll[i][j])
                if j > 2:
                    string = string[:10]
                self.table.setItem(i, j, QTableWidgetItem(string))
        self.table.resizeColumnsToContents()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        scroll = QScrollArea()
        scroll.setWidget(self.table)
        scroll.setWidgetResizable(True)
        layout.addWidget(scroll)
        self.setLayout(layout)