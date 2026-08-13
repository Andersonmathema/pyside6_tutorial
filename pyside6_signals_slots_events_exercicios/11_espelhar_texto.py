"""Enunciado

Crie um QLineEdit e um QLabel.

Conecte diretamente o sinal textChanged do QLineEdit ao slot setText do QLabel.

O texto digitado deve aparecer imediatamente no QLabel.

Não crie um método intermediário.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input = QLineEdit()
        self.label = QLabel("Digite alguma coisa")

        # TODO: conexão direta entre os widgets.
        # self.input.____________.connect(self.label.________)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
