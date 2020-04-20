from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, \
    QMessageBox
from PyQt5.QtGui import *
from datetime import datetime, date


class projWindow(QWidget):
    def __init__(self, con):
        super().__init__()

        self.setWindowTitle('Проекты')

        self.con = con
        self.setGeometry(1500, 400, 1000, 500)
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
        self.title_label.move(670, 20)
        self.title_label.setFont(QFont('Helvetica', 18))

        self.id_label = QLabel('ID', self)
        self.id_label.move(670, 60)

        self.name_label = QLabel('Название', self)
        self.name_label.move(670, 110)

        self.cost_label = QLabel('Cтоимость', self)
        self.cost_label.move(670, 160)

        self.dep_label = QLabel('Отдел', self)
        self.dep_label.move(670, 210)

        self.date_beg_label = QLabel('Дата начала', self)
        self.date_beg_label.move(670, 260)

        self.date_end_label = QLabel('Дата завершения', self)
        self.date_end_label.move(670, 310)

        self.date_end_real_label = QLabel('Дата завершения итог', self)
        self.date_end_real_label.move(670, 360)

        # self.department_label = QLabel('Отдел', self)
        # self.department_label.move(570, 350)

        self.id_combobox = QComboBox(self)
        self.id_combobox.move(835, 60)
        self.id_combobox.resize(163, 20)
        self.id_combobox.currentIndexChanged.connect(self.id_changed)

        self.name_edit = QLineEdit(self)
        self.name_edit.move(840, 110)
        self.name_edit.resize(150, 20)

        self.cost_edit = QLineEdit(self)
        self.cost_edit.move(840, 160)
        self.cost_edit.resize(150, 20)

        self.dep_edit = QLineEdit(self)
        self.dep_edit.move(840, 210)
        self.dep_edit.resize(150, 20)

        self.date_beg_edit = QLineEdit(self)
        self.date_beg_edit.move(840, 260)
        self.date_beg_edit.resize(150, 20)

        self.date_end_edit = QLineEdit(self)
        self.date_end_edit.move(840, 310)
        self.date_end_edit.resize(150, 20)

        self.date_end_real_edit = QLineEdit(self)
        self.date_end_real_edit.move(840, 360)
        self.date_end_real_edit.resize(150, 20)

        # self.department_edit = QLineEdit(self)
        # self.department_edit.move(680, 350)
        # self.department_edit.resize(150, 20)

        self.apply_btn = QPushButton('Сохранить', self)
        self.apply_btn.move(840, 420)
        self.apply_btn.resize(150, 30)
        self.apply_btn.clicked.connect(self.apply_clicked)

        self.commit_btn = QPushButton('Сохранить', self)
        self.commit_btn.move(670, 460)
        self.commit_btn.resize(150, 30)
        self.commit_btn.clicked.connect(self.commit_clicked)

        self.rollback_btn = QPushButton('Отменить', self)
        self.rollback_btn.move(840, 460)
        self.rollback_btn.resize(150, 30)
        self.rollback_btn.clicked.connect(self.rollback_clicked)

        self.table = QTableWidget(self)
        self.table.setColumnCount(6)
        self.table.resize(630, 450)

        # self.table.setDisabled(True)
        self.update_table()
        self.update_combobox()
        self.hide_all()

    def add_proj(self):
        if self.name_edit.text() and self.cost_edit.text() and self.date_beg_edit.text() and self.date_end_edit.text():
                # and self.cost_edit.text().isnumeric() and self.dep_edit.text().isdecimal():

            cur = self.con.cursor()
            date_beg = datetime.strptime(self.date_beg_edit.text(), "%Y-%m-%d %H:%M:%S")
            date_end = datetime.strptime(self.date_end_edit.text(), "%Y-%m-%d %H:%M:%S")
            print(date_beg)
            query = r"INSERT INTO projects(NAME, COST, Department_ID, Date_beg, Date_end, Date_end_real) " \
                    r"VALUES ('{}', {}, {}, {}, {})".format(self.name_edit.text(),
                                                            int(self.cost_edit.text()),
                                                            int(self.dep_edit.text()),
                                                            date_beg,
                                                            date_end)
            cur.execute(query)
            # self.con.commit()
            self.update_table()
        else:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setText("Заполните все поля!")
            error_d.setWindowTitle("Ошибка!")
            error_d.exec_()
        print('Добавлено')

    def delete_proj(self):
        try:
            cur = self.con.cursor()
            query = r"DELETE from projects where ID = {}".format(int(self.id_combobox.currentText()))
            cur.execute(query)
            # self.con.commit()
            self.update_table()
            self.update_combobox()
            self.update_table()
        except:
            print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Неизвестная ошибка!")

    def update_proj(self):

        # try:
        cur = self.con.cursor()
        # r"Date_beg = TO_DATE('{}', 'YYYY-MM-DD HH24:MI:SS') " \
        # query = r"Update projects set name = '{}', " \
        #         r"cost = {} " \
        #         r"where id = {}".format('Проект', int(self.cost_edit.text()), int(self.id_combobox.currentText()))
        #                         # int(self.cost_edit.text()),
        #                         # int(self.dep_edit.text()),
        #                         # int(self.id_combobox.currentText()))

        query = r"Update projects set name = '{}', " \
                r"Cost = '{}', " \
                r" Department_id = {} " \
                r" where id = {}".format(self.name_edit.text(),
                                         int(self.cost_edit.text()),
                                         int(self.dep_edit.text()),
                                         int(self.id_combobox.currentText()))
        print(query)
        cur.execute(query)
        # except:
        #     error_d = QMessageBox()
        #     error_d.setIcon(QMessageBox.Critical)
        #     error_d.setText("Хз че случилось!")
        #     error_d.setWindowTitle("Ошибка!")
        #     error_d.exec_()
        # if self.date_end_real_edit.text() is not 'None':
        #     try:
        #         date_end_real = datetime.strptime(self.date_end_real_edit.text(), "%d-%m-%Y %H:%M:%S")
        #     except:
        #         error_d = QMessageBox()
        #         error_d.setIcon(QMessageBox.Critical)
        #         error_d.setText("Неправильный формат даты!")
        #         error_d.setWindowTitle("Ошибка!")
        #         error_d.exec_()
        # else:
        #     date_end_real = 'None'



        self.update_combobox()
        self.update_table()
        self.clear_all()
        self.update_edits()

    def update_combobox(self):
        cur = self.con.cursor()
        self.id_combobox.clear()
        cur.execute("select id from projects")
        l = cur.fetchall()
        for id in l:
            self.id_combobox.addItem(str(id[0]))

        self.id_combobox.setCurrentIndex(0)

    def update_table(self):
        curs = self.con.cursor()
        curs.execute('select count(*) from projects')
        self.N_ROWS = curs.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(
            ['ID', 'Название', 'Стоимость', 'Дата начала', 'Дата завершения', 'Реальная дата завершения'])
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
        cur.execute('select * from projects')
        l = cur.fetchall()

        self.name_edit.setText(str(l[int(self.id_combobox.currentIndex())][1]))
        self.cost_edit.setText(str(l[int(self.id_combobox.currentIndex())][2]))
        self.dep_edit.setText(str(l[(int(self.id_combobox.currentIndex()))][3]))
        self.date_beg_edit.setText(str(l[int(self.id_combobox.currentIndex())][4]))
        self.date_end_edit.setText(str(l[int(self.id_combobox.currentIndex())][5]))
        self.date_end_real_edit.setText(str((l[int(self.id_combobox.currentIndex())][6])))

    def id_changed(self):
        print(self.id_combobox.currentText())
        self.update_edits()

    def add_clicked(self):
        # self.add_btn.setDisabled(True)
        self.hide_all()
        self.clear_all()
        self.title_label.setText('Введите данные нового проекта')
        self.title_label.show()

        self.dep_label.show()
        self.name_label.show()
        self.cost_label.show()
        self.date_end_label.show()
        self.date_beg_label.show()
        self.date_end_real_label.show()

        self.name_edit.show()
        self.cost_edit.show()
        self.dep_edit.show()
        self.date_end_edit.show()
        self.date_beg_edit.show()
        self.date_end_real_edit.show()

        self.apply_btn.setText('Добавить')
        self.rollback_btn.setText('Отменить')
        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def modify_clicked(self):
        self.hide_all()

        self.title_label.setText('Измените данные проекта')
        self.title_label.show()

        self.id_label.show()
        self.dep_label.show()
        self.cost_label.show()
        self.name_label.show()
        self.date_end_label.show()
        self.date_beg_label.show()
        self.date_end_real_label.show()
        # self.department_label.show()

        self.id_combobox.show()
        self.name_edit.show()
        self.cost_edit.show()
        self.dep_edit.show()
        self.date_end_edit.show()
        self.date_beg_edit.show()
        self.date_end_real_edit.show()
        # self.department_edit.show()

        self.apply_btn.setText('Изменить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def delete_clicked(self):
        self.hide_all()

        self.title_label.setText('Введите ID проекта для удаления')
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
            self.add_proj()
        elif self.apply_btn.text() == 'Удалить':
            self.delete_proj()
        elif self.apply_btn.text() == 'Изменить':
            self.update_proj()

        # self.clear_all()

    def commit_clicked(self):
        self.con.commit()
        self.clear_all()
        self.hide_all()

    def rollback_clicked(self):
        self.con.rollback()
        self.update_table()
        self.update_combobox()
        self.clear_all()
        self.hide_all()

    def hide_all(self):
        self.title_label.setVisible(False)

        self.id_label.hide()
        self.dep_label.hide()
        self.cost_label.hide()
        self.name_label.hide()
        self.date_end_label.hide()
        self.date_beg_label.hide()
        self.date_end_real_label.hide()
        # self.department_label.setHidden(True)

        self.id_combobox.hide()
        self.name_edit.hide()
        self.cost_edit.hide()
        self.dep_edit.hide()
        self.date_end_edit.hide()
        self.date_beg_edit.hide()
        self.date_end_real_edit.hide()
        # self.department_edit.setHidden(True)

        self.apply_btn.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()

    def clear_all(self):
        self.name_edit.clear()
        self.cost_edit.clear()
        self.dep_edit.clear()
        self.date_end_edit.clear()
        self.date_beg_edit.clear()
        self.date_end_real_edit.clear()
        # self.department_edit.clear()
