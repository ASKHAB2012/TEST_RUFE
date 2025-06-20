from PyQt5.QtCore import QtCore
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QHBoxLayout, QVBoxLayout,
    QGroupBox, QRadioButton,
    QPushButton, QLabel, QListWidget, QLineEdit)



from instr import *
from second_win import *

class MainWin(QWidget):
     def __init__(self):
         super().__init__()
         self.initUI()
         self.connects()
         self.set_appear
         self.show


     def initUI(self):
         self.btn_next = QPushButton(txt_next, self)
         self.hello_text = QLabel(txt_hello)
         self.instruction


        self.layout_line = QVBoxLayout()
        self.layout_line.addWidget(self.hello_text, alignment = Qt.Alignleft)
        self.layout_line.addWidget(self.instruction, alignment = Qt.Alignleft)
        self.layout_line.addWidget(self.btn_next, alignment = Qt.Alignleft)
        self.setLayout(self.layout_line)


    def next_clisk(self):
        self.tw = TestWin()
        self.hide()

    def connects(self):
        self.btn_next.clicked.connects(self.next_clisk)


    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)


app =   QApplication([])
mw = MainWin()
app.exec_()


