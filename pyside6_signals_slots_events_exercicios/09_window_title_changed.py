# RESOLVIDO
"""Enunciado

Detecte alterações no título da janela usando windowTitleChanged.

Ao clicar em "Alterar título":
    altere o título para "Novo título".

Quando o título mudar, imprima:
    O novo título é: Novo título
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Título inicial")

        self.button = QPushButton("Alterar título")
        self.button.clicked.connect(self.change_title)

        # TODO: conecte windowTitleChanged ao método title_changed.
        self.windowTitleChanged.connect(self.title_changed)

        self.setCentralWidget(self.button)

    def change_title(self):
        self.setWindowTitle("Novo título")

    def title_changed(self, title: str):
        # TODO: mostre o título recebido.
        self.title = title
        self.windowTitle = title
        print(f'O novo título é: {self.title}')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
