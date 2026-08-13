# RESOLVIDO
"""Enunciado

Use o sinal released do QPushButton.

Como released não fornece o estado checked diretamente ao slot neste exercício,
consulte manualmente o botão com isChecked().

Mostre:
    Estado atual: True
ou:
    Estado atual: False
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Alternar")
        self.button.setCheckable(True)

        # TODO: conecte released a button_released.
        self.button.released.connect(self.button_released)

        self.setCentralWidget(self.button)

    def button_released(self):
        # TODO: consulte o estado atual com isChecked().
        checked = self.button.isChecked()
        print(checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
