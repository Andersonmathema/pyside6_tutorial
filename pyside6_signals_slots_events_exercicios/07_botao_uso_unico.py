# RESOLVIDO
"""Enunciado

Crie um botão "Executar tarefa".

Após o primeiro clique:

1. Mude o texto do botão para "Concluído".
2. Desabilite o botão.
3. Mude o título da janela para "Tarefa concluída".
"""

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tarefa pendente")

        self.button = QPushButton("Executar tarefa")
        self.button.clicked.connect(self.complete_task)

        self.setCentralWidget(self.button)

    def complete_task(self):
        # TODO: implemente os três comportamentos pedidos.
        self.button.setText('Concluído')
        self.button.setDisabled(True)
        self.setWindowTitle('Tarefa concluída')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
