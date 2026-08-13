# RESOLVIDO
"""Enunciado

Conecte o mesmo botão a dois slots:

1. mostrar_mensagem()
2. contar_clique()

A cada clique, o terminal deve mostrar algo semelhante a:

    Botão pressionado
    Total: 1

    Botão pressionado
    Total: 2
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.numero_de_cliques = 0

        button = QPushButton("Pressione")

        # TODO: conecte clicked aos dois métodos.
        # button.clicked.connect(________________)
        # button.clicked.connect(________________)

        button.clicked.connect(self.mostrar_mensagem)
        button.clicked.connect(self.contar_clique)

        self.setCentralWidget(button)

    def mostrar_mensagem(self):
        print("Botão pressionado")

    def contar_clique(self):
        self.numero_de_cliques += 1
        print(self.numero_de_cliques)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
