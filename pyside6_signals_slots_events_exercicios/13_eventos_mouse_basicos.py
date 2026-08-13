# RESOLVIDO
"""Enunciado

Implemente os seguintes eventos:

    mouseMoveEvent
    mousePressEvent
    mouseReleaseEvent
    mouseDoubleClickEvent

Atualize o QLabel para mostrar respectivamente:

    Mouse movido
    Botão pressionado
    Botão liberado
    Clique duplo
"""

import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Interaja com a janela")
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, event):
        # TODO
        self.label.setText('Mouse movido')

    def mousePressEvent(self, event):
        # TODO
        self.label.setText('Botão pressionado')

    def mouseReleaseEvent(self, event):
        # TODO
        self.label.setText('Botão liberado')

    def mouseDoubleClickEvent(self, event):
        # TODO
        self.label.setText('Clique duplo')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
