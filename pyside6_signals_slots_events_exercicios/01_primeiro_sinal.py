# RESOLVIDO
"""Enunciado

Crie uma janela com um botão "Clique aqui".

Ao clicar no botão, exiba no terminal:
    O botão foi clicado!

Complete a conexão entre o sinal clicked e o método button_clicked.
Depois, como desafio, crie um contador que informe quantas vezes o botão foi clicado.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self, count=0):
        super().__init__()
        self.count = count

        self.setWindowTitle("Exercício 1")

        button = QPushButton("Clique aqui")

        # TODO: conecte o sinal clicked ao método button_clicked.
        # button.________.connect(self.button_clicked)
        button.clicked.connect(self.button_clicked)

        self.setCentralWidget(button)

    def button_clicked(self):
        # TODO: exiba "O botão foi clicado!"
        #print('O botão foi clicado!')
        self.count += 1
        print(f'O botão foi clicado {self.count} vezes!')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
