"""Enunciado

Ative o rastreamento do mouse para que mouseMoveEvent seja disparado sem a
necessidade de manter um botão pressionado.

Ative setMouseTracking(True):

1. na janela;
2. no QLabel central.

Mostre as coordenadas do mouse no QLabel.
"""

import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # TODO: ative mouse tracking na janela.

        self.label = QLabel("Mova o mouse")

        # TODO: ative mouse tracking no label.

        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        # TODO: mostre X e Y.
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
