# RESOLVIDO
"""Enunciado

Mantenha o estado atual do botão na variável:

    self.button_is_checked

O botão deve iniciar com o mesmo estado armazenado nessa variável.

Ao clicar, atualize self.button_is_checked e imprima seu valor.
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = False

        self.button = QPushButton("Alternar")
        self.button.setCheckable(True)

        # TODO: inicialize o estado do botão usando self.button_is_checked.
        self.button.setChecked(self.button_is_checked)

        self.button.clicked.connect(self.update_button_state)
        self.setCentralWidget(self.button)

    def update_button_state(self, checked):
        # TODO: armazene checked em self.button_is_checked e imprima.
        self.button_is_checked = checked
        print(self.button_is_checked)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
