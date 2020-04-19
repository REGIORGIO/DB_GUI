from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import secondaryWindow
import procWindow
import sys

class depWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(1500, 400, 700, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Отделы')

