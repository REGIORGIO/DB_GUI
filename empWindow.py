import PyQt5
from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, \
    QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import secondaryWindow
import procWindow
import sys

class empWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(1500, 400, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Сотрудники')

        self.add_btn = QPushButton('Добавить', self)
        self.add_btn.move(20, 460)
        self.add_btn.resize(150, 30)
        self.add_btn.clicked.connect(self.add_clicked)

        self.modify_btn = QPushButton('Изменить', self)
        self.modify_btn.move(190, 460)
        self.modify_btn.resize(150, 30)
        self.modify_btn.clicked.connect(self.modify_clicked)

        self.delete_btn = QPushButton('Удалить', self)
        self.delete_btn.move(360, 460)
        self.delete_btn.resize(150, 30)
        self.delete_btn.clicked.connect(self.delete_clicked)

        self.title_label = QLabel('', self)
        self.title_label.move(550, 30)
        self.title_label.setFont(QFont('Helvetica', 18))


        self.id_label = QLabel('ID', self)
        self.id_label.move(570, 100)

        self.surname_label = QLabel('Фамилия', self)
        self.surname_label.move(570, 150)

        self.name_label = QLabel('Имя', self)
        self.name_label.move(570, 200)

        self.position_label = QLabel('Должность', self)
        self.position_label.move(570, 250)

        self.salary_label = QLabel('Зарплата', self)
        self.salary_label.move(570, 300)

        self.department_label = QLabel('Отдел', self)
        self.department_label.move(570, 350)



        self.id_combobox = QComboBox(self)
        self.id_combobox.move(675, 100)
        self.id_combobox.resize(163, 20)

        self.surname_edit = QLineEdit(self)
        self.surname_edit.move(680, 150)
        self.surname_edit.resize(150, 20)

        self.name_edit = QLineEdit(self)
        self.name_edit.move(680, 200)
        self.name_edit.resize(150, 20)

        self.position_edit = QLineEdit(self)
        self.position_edit.move(680, 250)
        self.position_edit.resize(150, 20)

        self.salary_edit = QLineEdit(self)
        self.salary_edit.move(680, 300)
        self.salary_edit.resize(150, 20)

        self.department_edit = QLineEdit(self)
        self.department_edit.move(680, 350)
        self.department_edit.resize(150, 20)

        self.commit_btn = QPushButton('Сохранить', self)
        self.commit_btn.move(680, 420)
        self.commit_btn.resize(150, 30)

        self.rollback_btn = QPushButton('Отменить', self)
        self.rollback_btn.move(680, 460)
        self.rollback_btn.resize(150, 30)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.resize(520, 450)
        self.update_table()
        self.update_combobox()
        self.hide_all()

    def update_combobox(self):
        cur = self.con.cursor()
        cur.execute("select id from employees")
        l = cur.fetchall()
        for id in l:
            self.id_combobox.addItem(str(id[0]))

    def update_table(self):
        cur = self.con.cursor()
        cur.execute('select count(*) from employees')
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Фамилия', 'Имя', 'Должность', 'Зарплата'])
        cur.execute("select id, last_name, first_name, position, salary from employees")

        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 5):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

    def add_clicked(self):
        self.hide_all()

        self.title_label.setText('Введите данные нового сотрудника')
        self.title_label.show()

        self.surname_label.show()
        self.name_label.show()
        self.salary_label.show()
        self.position_label.show()

        self.surname_edit.show()
        self.name_edit.show()
        self.salary_edit.show()
        self.position_edit.show()

        self.commit_btn.show()
        self.rollback_btn.show()

    def modify_clicked(self):
        self.hide_all()

        self.title_label.setText('Измените данные сотрудника')
        self.title_label.show()

        self.id_label.show()
        self.surname_label.show()
        self.name_label.show()
        self.salary_label.show()
        self.position_label.show()
        self.department_label.show()

        self.id_combobox.show()
        self.surname_edit.show()
        self.name_edit.show()
        self.salary_edit.show()
        self.position_edit.show()
        self.department_edit.show()

        self.commit_btn.show()
        self.rollback_btn.show()

    def delete_clicked(self):
        self.hide_all()

        self.title_label.setText('Введите ID сотрудника для удаления')
        self.title_label.show()

        self.id_combobox.show()
        self.id_label.show()

        self.commit_btn.show()
        self.rollback_btn.show()

    def hide_all(self):

        self.title_label.setVisible(False)

        self.id_label.setVisible(False)
        self.surname_label.setVisible(False)
        self.name_label.setVisible(False)
        # print(self.name_edit.isVisible())
        self.salary_label.hide()
        self.position_label.hide()
        self.department_label.setHidden(True)

        self.id_combobox.hide()
        self.surname_edit.hide()
        self.name_edit.hide()
        self.salary_edit.hide()
        self.position_edit.hide()
        self.department_edit.setHidden(True)

        self.commit_btn.hide()
        self.rollback_btn.hide()

