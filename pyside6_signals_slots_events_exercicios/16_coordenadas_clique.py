"""Enunciado

Quando o usuário clicar na janela, mostre no QLabel a posição local do clique:

    Clique em X=120, Y=75

Use event.position().

Observação:
position() retorna QPointF, portanto X e Y podem ser valores decimais.
Você pode convertê-los para int se desejar.
"""

import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Clique na janela")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        # TODO:
        # position = event.________()
        # x = ...
        # y = ...
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
