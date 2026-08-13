"""Enunciado

Sobrescreva mousePressEvent.

Primeiro:
    imprima "Clique personalizado detectado"

Depois:
    encaminhe o evento para a implementação original de QMainWindow
    utilizando super().

Pergunta para reflexão:
Qual a diferença entre super().mousePressEvent(event) e self.parent()?
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def mousePressEvent(self, event):
        print("Clique personalizado detectado")

        # TODO: encaminhe o evento à implementação da classe base.
        # super().________________(event)


app = QApplication(sys.argv)
window = MainWindow()
window.resize(400, 250)
window.show()
app.exec()
