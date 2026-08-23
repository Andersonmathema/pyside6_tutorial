# RESOLVIDO
"""Enunciado

Combine o botão pressionado e a posição do clique.

Exemplos:

    Botão esquerdo em X=80, Y=120
    Botão direito em X=200, Y=60

Use:
    event.button()
    event.position()
"""

import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel("Clique na janela")
        self.setCentralWidget(self.label)

    def mousePressEvent(self, event):
        # TODO: obtenha posição e botão e monte a mensagem.
        x = event.position().x()
        y = event.position().y()
        botao = event.button()
        if botao == Qt.MouseButton.LeftButton:
            self.label.setText(f'Botão esquerdo em X={x}, Y={y}')
        else:
            self.label.setText(f'Botão direito em X={x}, Y={y}')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
