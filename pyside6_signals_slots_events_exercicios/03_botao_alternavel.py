# RESOLVIDO
"""Enunciado

Crie um QPushButton alternável utilizando setCheckable.

A cada clique, mostre no terminal:

    Ativado: True
    Ativado: False

O valor deve vir do argumento recebido pelo slot conectado ao sinal clicked.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        button = QPushButton("Ativar")

        # TODO: torne o botão checkable.
        button.setCheckable(True)

        button.clicked.connect(self.button_toggled)

        self.setCentralWidget(button)

    def button_toggled(self, checked):
        print(f'Botão: {checked}')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
