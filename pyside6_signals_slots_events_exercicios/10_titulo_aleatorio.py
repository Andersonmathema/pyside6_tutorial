# RESOLVIDO
"""Enunciado

A cada clique, escolha aleatoriamente um dos títulos abaixo:

    Sistema funcionando
    Processando
    Tudo certo
    Erro crítico

Atualize o título da janela.

Se o novo título for "Erro crítico":
    desabilite o botão.
"""

import sys
from random import choice
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


WINDOW_TITLES = [
    "Sistema funcionando",
    "Processando",
    "Tudo certo",
    "Erro crítico",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Alterar título")
        self.button.clicked.connect(self.change_title)

        # TODO: conecte windowTitleChanged a title_changed.
        self.windowTitleChanged.connect(self.title_changed)

        self.setCentralWidget(self.button)

    def change_title(self):
        # TODO: escolha um título e aplique com setWindowTitle().
        self.setWindowTitle(choice(WINDOW_TITLES))

    def title_changed(self, title):
        # TODO: se title == "Erro crítico", desabilite o botão.
        self.windowTitle = title
        if title == 'Erro crítico':
            self.button.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
