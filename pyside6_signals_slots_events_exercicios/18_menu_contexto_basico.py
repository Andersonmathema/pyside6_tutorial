# RESOLVIDO
"""Enunciado

Crie um menu de contexto com três ações:

    Copiar
    Colar
    Apagar

O menu deve aparecer quando o usuário solicitar o menu de contexto da janela.

Use:
    QMenu
    QAction
    contextMenuEvent
"""

import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Menu de contexto")
        self.resize(400, 250)

    def contextMenuEvent(self, event):
        # TODO: crie o QMenu, adicione três ações e exiba-o.
        menu = QMenu(self)
        menu.addAction(QAction("Copiar", self))
        menu.addAction(QAction("Colar", self))
        menu.addAction(QAction("Apagar", self))
        menu.exec(event.globalPos())        


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
