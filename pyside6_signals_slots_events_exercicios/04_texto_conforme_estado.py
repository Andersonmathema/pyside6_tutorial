# RESOLVIDO
"""Enunciado

Crie um botão alternável.

Quando estiver marcado:
    texto = "Ligado"

Quando estiver desmarcado:
    texto = "Desligado"

Guarde o botão como atributo self.button para acessá-lo no slot.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Desligado")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_toggled)

        self.setCentralWidget(self.button)

    def button_toggled(self, checked):
        if checked == True:
            self.button.setText('Ligado')
        else:
            self.button.setText('Desligado')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
