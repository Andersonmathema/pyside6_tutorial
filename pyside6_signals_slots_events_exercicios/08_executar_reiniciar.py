# RESOLVIDO
"""Enunciado

Crie uma interface com dois botões:

    Executar
    Reiniciar

Ao clicar em Executar:
    desabilite o botão Executar.

Ao clicar em Reiniciar:
    habilite novamente o botão Executar.

Use um layout para mostrar os dois botões.
"""

import sys
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.execute_button = QPushButton("Executar")
        self.reset_button = QPushButton("Reiniciar")

        # TODO: conecte os sinais aos métodos.
        self.execute_button.clicked.connect(self.execute)
        self.reset_button.clicked.connect(self.reset)

        layout = QVBoxLayout()
        layout.addWidget(self.execute_button)
        layout.addWidget(self.reset_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def execute(self):
        # TODO: desabilite execute_button.
        self.execute_button.setDisabled(True)

    def reset(self):
        # TODO: habilite execute_button.
        self.execute_button.setDisabled(False)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
