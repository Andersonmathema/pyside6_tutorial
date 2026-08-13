"""Enunciado

Identifique qual botão do mouse foi pressionado.

Mostre no QLabel:

    Botão esquerdo
    Botão direito
    Botão do meio

Use Qt.MouseButton.LeftButton, RightButton e MiddleButton.
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Clique com algum botão do mouse")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        # TODO: teste event.button() e altere o texto do QLabel.
        pass


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
