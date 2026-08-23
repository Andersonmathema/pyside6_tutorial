"""Enunciado

Crie uma janela com um QLineEdit e um menu de contexto.

O menu deve possuir:

    Limpar texto
    Desabilitar campo
    Alterar título
    Fechar

Conecte cada QAction ao comportamento correspondente.

Dica:
    self.input.clear
    self.close
    self.setWindowTitle(...)
"""

import sys
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input = QLineEdit()
        self.input.setPlaceholderText("Digite algo...")
        self.setCentralWidget(self.input)

    def contextMenuEvent(self, event):
        # TODO: crie e conecte as quatro ações.
        context = QMenu(self)
        context.addAction(QAction("Limpar texto", self.clear_line))
        context.addAction(QAction("Desabilitar campo", self.disable_input))
        context.addAction(QAction("Alterar título", self.change_title))
        context.addAction(QAction("Fechar", self.close))
        context.exec(event.globalPos())


    def clear_line(self):
        self.input.clear()

    def disable_input(self):
        # TODO
        self.input.setDisabled(True)

    def change_title(self):
        # TODO
        self.setWindowTitle("Novo título")

    def close_window(self):
        self.close(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
