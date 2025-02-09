from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import QMessageBox, QListWidget, QFileDialog
from time import *

app = QApplication([])
window = QWidget()

window.resize(300, 300)

class New_number:
    def __init__(self, number):
        self.number = number
        self.asd = 1
        self.number_1 = 5
        self.number_5 = 5
        self.number_10 = 5
        self.pass_number = 0
        self.pass_doxod = 0

    def new_number(self):
        self.number = self.number + self.asd
        text.setText(str(self.number))

    def new_1(self):
        if self.number >= 100 and self.number_1 >= 0:
            self.number_1 -= 1
            self.number -= 100
            self.asd += 1
            text.setText(str(self.number))
            butten_1.setText('Прокачка +1 Стоимость 100 \n (остальсь ' + str(self.number_1) + ')')
            butten_number.setText('+' + str(self.asd))
        
    def new_5(self):
        if self.number >= 2500 and self.number_5 > 0:
            self.number_5 -= 1
            self.number -= 2500
            self.asd += 5
            text.setText(str(self.number))
            butten_5.setText('Прокачка +5 Стоимость 2500 \n (остальсь ' + str(self.number_5) + ')')
            butten_number.setText('+' + str(self.asd))
    
    def new_10(self):
        if self.number >= 5000 and self.number_10 > 0:
            self.number_10 -= 1
            self.number -= 5000
            self.asd += 10
            text.setText(str(self.number))
            butten_10.setText('Прокачка +10 Стоимость 5000 \n (остальсь ' + str(self.number_10) + ')')
            butten_number.setText('+' + str(self.asd))

                




            

number = 0


one_numberrr = New_number(number)



hline_home = QHBoxLayout()

vline_one = QVBoxLayout()
vline_to = QVBoxLayout()


text = QLabel(str(number))
text.setAlignment(Qt.AlignCenter)
vline_one.addWidget(text)

butten_number = QPushButton('+1')
butten_number.setStyleSheet('background: rgb(255,0,0);')
vline_one.addWidget(butten_number)


butten_1 = QPushButton('Прокачка +1 Стоимость 100 \n (остальсь 5)')
butten_1.setStyleSheet('background: rgb(0,255,0);')
vline_to.addWidget(butten_1)

butten_5 = QPushButton('Прокачка +5 Стоимость 2500 \n (остальсь 5)')
butten_5.setStyleSheet('background: rgb(0,255,0);')
vline_to.addWidget(butten_5)

butten_10 = QPushButton('Прокачка +10 Стоимость 5000 \n (остальсь 5)')
butten_10.setStyleSheet('background: rgb(0,255,0);')
vline_to.addWidget(butten_10)



hline_home.addLayout(vline_one)
hline_home.addLayout(vline_to)

window.setLayout(hline_home)


butten_number.clicked.connect(one_numberrr.new_number)
butten_1.clicked.connect(one_numberrr.new_1)
butten_5.clicked.connect(one_numberrr.new_5)
butten_10.clicked.connect(one_numberrr.new_10)

window.show()
app.exec_()