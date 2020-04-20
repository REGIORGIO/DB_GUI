from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, \
    QMessageBox
from PyQt5.QtGui import *


class projWindow(QWidget):
    def __init__(self, con):
        super().__init__()

        self.setWindowTitle('Проекты')

        self.con = con
        self.setGeometry(1500, 400, 900, 500)
        self.setFixedSize(self.size())

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

        # self.department_label = QLabel('Отдел', self)
        # self.department_label.move(570, 350)



        self.id_combobox = QComboBox(self)
        self.id_combobox.move(675, 100)
        self.id_combobox.resize(163, 20)
        self.id_combobox.currentIndexChanged.connect(self.id_changed)

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

        # self.department_edit = QLineEdit(self)
        # self.department_edit.move(680, 350)
        # self.department_edit.resize(150, 20)

        self.apply_btn = QPushButton('Сохранить', self)
        self.apply_btn.move(740, 420)
        self.apply_btn.resize(150, 30)
        self.apply_btn.clicked.connect(self.apply_clicked)

        self.commit_btn = QPushButton('Сохранить', self)
        self.commit_btn.move(570, 460)
        self.commit_btn.resize(150, 30)
        self.commit_btn.clicked.connect(self.commit_clicked)

        self.rollback_btn = QPushButton('Отменить', self)
        self.rollback_btn.move(740, 460)
        self.rollback_btn.resize(150, 30)
        self.rollback_btn.clicked.connect(self.rollback_clicked)

        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.resize(660, 450)

        # self.table.setDisabled(True)
        self.update_table()
        self.update_combobox()
        self.hide_all()

    def add_emp(self):

        if self.name_edit.text() and  self.surname_edit.text() and self.position_edit.text() and self.salary_edit.text():

            cur = self.con.cursor()

            query =r"INSERT INTO EMPLOYEES(FIRST_NAME, LAST_NAME, POSITION, SALARY) VALUES ('{}', '{}', '{}', {})".format(self.name_edit.text(), self.surname_edit.text(), self.position_edit.text(), float(self.salary_edit.text()))
            cur.execute(query)
            # self.con.commit()
            self.update_table()
        else:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setText("Заполните все поля!")
            error_d.setWindowTitle("Ошибка!")
            error_d.exec_()
        # print('Добавлено')

    def delete_emp(self):
        try:
            cur = self.con.cursor()
            query = r"DELETE from employees where ID = {}".format(int(self.id_combobox.currentText()))
            cur.execute(query)
            # self.con.commit()
            self.update_table()
            self.update_combobox()
            self.update_table()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setText("Заполните все поля!")
            error_d.setWindowTitle("Ошибка!")
            error_d.exec_()

    def update_emp(self):
        cur = self.con.cursor()
        query = r"Update employees set First_name = '{}', " \
                r"Last_name = '{}', " \
                r"Position = '{}', " \
                r"Salary = {}" \
                r" where id = {}".format(self.name_edit.text(),
                                         self.surname_edit.text(),
                                         self.position_edit.text(),
                                         self.salary_edit.text(),
                                         int(self.id_combobox.currentText()))
        cur.execute(query)

        self.update_combobox()
        self.update_table()
        self.clear_all()
        self.update_edits()

    def update_combobox(self):
        cur = self.con.cursor()
        self.id_combobox.clear()
        cur.execute("select id from employees")
        l = cur.fetchall()
        for id in l:
            self.id_combobox.addItem(str(id[0]))

        self.id_combobox.setCurrentIndex(0)

    def update_table(self):
        curs = self.con.cursor()
        curs.execute('select count(*) from projects')
        self.N_ROWS = curs.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Название', 'Стоимость', 'Дата начала', 'Дата завершения', 'Реальная дата завершения'])
        curs.execute("select id, name, cost, date_beg, date_end, date_end_real from projects order by id")

        l = curs.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 6):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

    def update_edits(self):
        cur = self.con.cursor()
        cur.execute('select * from employees')
        l = cur.fetchall()
        self.surname_edit.setText(l[int(self.id_combobox.currentIndex())][3])
        self.name_edit.setText(l[int(self.id_combobox.currentIndex())][1])
        self.position_edit.setText(l[int(self.id_combobox.currentIndex())][4])
        self.salary_edit.setText(str(l[int(self.id_combobox.currentIndex())][5]))
        # self.surname_edit.setText(l[int(self.id_combobox.currentIndex())][3])

    def id_changed(self):
        print(self.id_combobox.currentText())
        self.update_edits()

    def add_clicked(self):
        # self.add_btn.setDisabled(True)
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

        self.apply_btn.setText('Добавить')
        self.rollback_btn.setText('Отменить')
        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def modify_clicked(self):
        self.hide_all()

        self.title_label.setText('Измените данные сотрудника')
        self.title_label.show()

        self.id_label.show()
        self.surname_label.show()
        self.name_label.show()
        self.salary_label.show()
        self.position_label.show()
        # self.department_label.show()

        self.id_combobox.show()
        self.surname_edit.show()
        self.name_edit.show()
        self.salary_edit.show()
        self.position_edit.show()
        # self.department_edit.show()

        self.apply_btn.setText('Изменить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def delete_clicked(self):
        self.hide_all()

        self.title_label.setText('Введите ID сотрудника для удаления')
        self.title_label.show()

        self.id_combobox.show()
        self.id_label.show()

        self.apply_btn.setText('Удалить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def apply_clicked(self):
        # print('Commit clicked')
        if self.apply_btn.text() == 'Добавить':
            self.add_emp()
        elif self.apply_btn.text() == 'Удалить':
            self.delete_emp()
        elif self.apply_btn.text() == 'Изменить':
            self.update_emp()

        # self.clear_all()

    def commit_clicked(self):
        self.con.commit()

    def rollback_clicked(self):
        self.con.rollback()
        self.update_table()
        self.update_combobox()

    def hide_all(self):
        self.title_label.setVisible(False)

        self.id_label.setVisible(False)
        self.surname_label.setVisible(False)
        self.name_label.setVisible(False)
        # print(self.name_edit.isVisible())
        self.salary_label.hide()
        self.position_label.hide()
        # self.department_label.setHidden(True)

        self.id_combobox.hide()
        self.surname_edit.hide()
        self.name_edit.hide()
        self.salary_edit.hide()
        self.position_edit.hide()
        # self.department_edit.setHidden(True)

        self.apply_btn.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()

    def clear_all(self):
        self.surname_edit.clear()
        self.name_edit.clear()
        self.salary_edit.clear()
        self.position_edit.clear()
        # self.department_edit.clear()
