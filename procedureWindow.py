from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import secondaryWindow
import procWindow
import sys
import startWindow

class procWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(1500, 400, 900, 500)
        ##self.setGeometry(300, 200, 550, 250)
        self.setFixedSize(self.size())
        self.setWindowTitle('Выберите процедуру')

        first_btn = QPushButton('Отделы и среднее время их работы над проектами', self)
        ##first_btn.setToolTip('Вывести все отделы и вре')
        first_btn.resize(500, 40)
        first_btn.move(200, 10)
        first_btn.setFont(QFont('Helvetica', 15))

        second_btn = QPushButton('Расчет суммы прибыли от завершенных проектов', self)
        second_btn.resize(500, 40)
        second_btn.move(200, 70)
        second_btn.setFont(QFont('Helvetica', 15))

        third_btn = QPushButton('Самый продолжительный проект выбранного отдела', self)
        third_btn.resize(500, 40)
        third_btn.move(200, 130)
        third_btn.setFont(QFont('Helvetica', 15))

        self.l3 = QLabel('Отдел', self)
        self.l3.resize(300, 50)
        self.l3.move(430, 230)
        self.l3.hide()

        self.box3 = QComboBox(self)
        self.box3.resize(200, 160)
        self.box3.move(350, 200)
        self.box3.hide()
        third_btn.clicked.connect(self.proc3)

        last_btn = QPushButton('Проекты двух выбранных служащих', self)
        last_btn.resize(500, 40)
        last_btn.move(200, 190)
        last_btn.setFont(QFont('Helvetica', 15))
        last_btn.clicked.connect(self.proc4)
        self.l1 = QLabel('Первый', self)
        self.l1.resize(200, 160)
        self.l1.move(330, 180)
        self.l1.hide()

        self.l2 = QLabel('Второй', self)
        self.l2.resize(200, 160)
        self.l2.move(520, 180)
        self.l2.hide()

        self.box1 = QComboBox(self)
        self.box1.resize(200, 160)
        self.box1.move(250, 200)
        self.box1.hide()

        self.box2 = QComboBox(self)
        self.box2.resize(200, 160)
        self.box2.move(450, 200)
        self.box2.hide()

        self.btn_show3 = QPushButton('Посмотреть результат', self)
        self.btn_show3.resize(300, 50)
        self.btn_show3.move(300, 330)
        self.btn_show3.setFont(QFont('Helvetica', 15))

        self.btn_show3.hide()

        self.btn_show4 = QPushButton('Посмотреть результат', self)
        self.btn_show4.resize(300, 50)
        self.btn_show4.move(300, 330)
        self.btn_show4.setFont(QFont('Helvetica', 15))

        self.btn_show4.hide()
        ##self.box1.hide()
        ##self.box1.addItems()

        back_btn = QPushButton('Вернуться на главную страницу', self)
        back_btn.resize(300, 50)
        back_btn.move(300, 440)
        back_btn.setFont(QFont('Helvetica', 15))
        back_btn.clicked.connect(self.backToStart)

        self.show()

    def backToStart(self):
        self.procWindow = startWindow.StartWindow(self.con)
        self.close()

    def proc3(self):
        self.btn_show4.hide()
        self.box1.hide()
        self.box2.hide()
        self.l1.hide()
        self.l2.hide()
        self.box3.show()
        self.l3.show()
        self.btn_show3.show()

    def proc4(self):
        self.btn_show3.hide()
        self.box3.hide()
        self.l3.hide()
        self.box1.show()
        self.box2.show()
        self.l1.show()
        self.l2.show()
        self.btn_show4.show()

