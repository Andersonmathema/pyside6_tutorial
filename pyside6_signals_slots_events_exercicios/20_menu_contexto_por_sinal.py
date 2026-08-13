"""Enunciado

Implemente um menu de contexto usando:

    Qt.ContextMenuPolicy.CustomContextMenu
    customContextMenuRequested

Não sobrescreva contextMenuEvent neste exercício.

O menu deve possuir:
    Opção 1
    Opção 2

Converta a posição recebida para coordenadas globais com mapToGlobal().
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # TODO:
        # self.setContextMenuPolicy(...)
        # self.customContextMenuRequested.connect(...)

        self.resize(400, 250)

    def open_context_menu(self, position):
        # TODO: crie o menu, converta position e chame exec().
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
