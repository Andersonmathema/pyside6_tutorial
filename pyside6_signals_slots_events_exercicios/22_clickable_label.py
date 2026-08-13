"""Enunciado

Crie uma classe ClickableLabel que herda de QLabel.

Ao clicar nela:
    altere seu texto para "O QLabel recebeu o clique"

Depois preserve o comportamento original do QLabel utilizando super().

Também implemente mousePressEvent na janela para imprimir:
    A janela recebeu o clique

Experimente clicar:
1. no QLabel;
2. em uma área vazia;
3. depois, opcionalmente, adicione um QPushButton e compare.
"""

import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class ClickableLabel(QLabel):
    def mousePressEvent(self, event):
        # TODO: altere o texto e preserve o comportamento original.
        pass


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = ClickableLabel("Clique aqui")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        print("A janela recebeu o clique")

        # TODO opcional: preserve também o comportamento da classe base.


app = QApplication(sys.argv)
window = MainWindow()
window.resize(400, 250)
window.show()
app.exec()
