# напиши здесь код основного приложения и первого экрана
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(400,500)

text = QLabel('Какой-то текст')
text2 = QLabel('hkdsbfkjhsdfjknfdkshdkjfnsdlf')

Button = QPushButton('Нажми на меня')

v1 = QVBoxLayout()

v1.addWidget(text, alignment = Qt.AlignCenter)
v1.addWidget(text2, alignment = Qt.AlignCenter)
v1.addWidget(Button, alignment = Qt.AlignCenter)

window.setLayout(v1)

def press():
    print('На кнопку нажали')
    text2.setText('Новый текст')

Button.clicked.connect(press)

window.show()
app.exec()