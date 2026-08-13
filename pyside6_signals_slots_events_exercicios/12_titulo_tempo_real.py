# RESOLVIDO
"""Enunciado

Crie um QLineEdit.

Enquanto o usuário digita, o conteúdo deve se tornar automaticamente o título
da janela.

Faça a conexão direta, sem criar um slot intermediário.
"""

import sys
from PySide6.QtWidgets import QApplication, QLineEdit, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input = QLineEdit()

        # TODO:
        self.input.textChanged.connect(self.setWindowTitle)

        self.setCentralWidget(self.input)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
