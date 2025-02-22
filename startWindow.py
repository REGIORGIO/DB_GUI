from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *
import connect
import procedureWindow
import employeeWindow
import departmentWindow
import projectWindow
import enterWindow
import usersWindow


class StartWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(800, 400, 550, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle('Главное меню')

        self.procWindow = procedureWindow.procWindow(self.con)
        self.projWindow = projectWindow.projWindow(self.con)
        self.depWindow = departmentWindow.depWindow(self.con)
        self.empWindow = employeeWindow.empWindow(self.con)
        self.userWindow = usersWindow.userWindow(self.con)
        titleLabel = QLabel('Выберите дальнейшнее действие', self)
        titleLabel.move(120, 50)
        titleLabel.setFont(QFont('Helvetica', 20))

        emp_btn = QPushButton('Сотрудники', self)
        emp_btn.setToolTip('Browse all employees')
        emp_btn.move(50, 100)
        emp_btn.resize(130, 35)
        emp_btn.setFont(QFont('Helvetica', 15))
        emp_btn.clicked.connect(self.EmpButtonClicked)

        dep_btn = QPushButton('Отделы', self)
        dep_btn.setToolTip('Browse all departments')
        dep_btn.move(210, 100)
        dep_btn.resize(130, 35)
        dep_btn.setFont(QFont('Helvetica', 15))
        dep_btn.clicked.connect(self.DepButtonClicked)

        proj_btn = QPushButton('Проекты', self)
        proj_btn.setToolTip('Browse all projects')
        proj_btn.move(380, 100)
        proj_btn.resize(130, 35)
        proj_btn.setFont(QFont('Helvetica', 15))
        proj_btn.clicked.connect(self.ProjButtonClicked)

        proc_btn = QPushButton('Процедуры', self)
        proc_btn.setToolTip('Show procedures')
        proc_btn.move(50, 150)
        proc_btn.resize(130, 35)
        proc_btn.setFont(QFont('Helvetica', 15))
        proc_btn.clicked.connect(self.ProcButtonClicked)

        user_btn = QPushButton('Пользователи', self)
        user_btn.setToolTip('Show procedures')
        user_btn.move(210, 150)
        user_btn.resize(130, 35)
        user_btn.setFont(QFont('Helvetica', 15))
        user_btn.clicked.connect(self.UserButtonClicked)

        logout_btn = QPushButton('Выход', self)
        logout_btn.setToolTip('Log out')
        logout_btn.resize(100, 100)
        logout_btn.move(380, 150)
        logout_btn.resize(130, 35)
        logout_btn.setFont(QFont('Helvetica', 15))
        logout_btn.clicked.connect(self.LogOutButtonClicked)
        self.show()

    def LogOutButtonClicked(self):
        self.close()
        self.empWindow.close()
        self.depWindow.close()
        self.procWindow.close()
        self.projWindow.close()
        self.userWindow.close()
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

        if self.userWindow.isVisible():
            self.userWindow.close()

    def EmpButtonClicked(self):
        self.empWindow.show()

        if self.projWindow.isVisible():
            self.projWindow.close()

        if self.procWindow.isVisible():
            self.procWindow.close()

        if self.depWindow.isVisible():
            self.depWindow.close()

        if self.userWindow.isVisible():
            self.userWindow.close()

    def DepButtonClicked(self):
        self.depWindow.show()
        if self.projWindow.isVisible():
            self.projWindow.close()

        if self.empWindow.isVisible():
            self.empWindow.close()

        if self.procWindow.isVisible():
            self.procWindow.close()

        if self.userWindow.isVisible():
            self.userWindow.close()

    def ProjButtonClicked(self):
        self.projWindow.show()
        if self.procWindow.isVisible():
            self.procWindow.close()

        if self.empWindow.isVisible():
            self.empWindow.close()

        if self.depWindow.isVisible():
            self.depWindow.close()

        if self.userWindow.isVisible():
            self.userWindow.close()

    def UserButtonClicked(self):
        self.userWindow.show()

        if self.projWindow.isVisible():
            self.projWindow.close()

        if self.procWindow.isVisible():
            self.procWindow.close()

        if self.depWindow.isVisible():
            self.depWindow.close()

