"""PROJETO FINAL — Painel de eventos

Crie uma aplicação que reúna os conceitos do tutorial.

A janela deve conter:

- QLineEdit
- QLabel para mostrar o texto digitado
- QPushButton alternável
- contador de cliques
- menu de contexto
- exibição das coordenadas do mouse

Requisitos:

1. O texto digitado no campo deve aparecer no QLabel.
2. O botão deve alternar entre "Ativo" e "Inativo".
3. Cada clique esquerdo na janela deve aumentar um contador.
4. O botão direito deve permitir abrir um menu de contexto.
5. O menu deve ter:
       Limpar texto
       Zerar contador
       Alterar título
       Fechar programa
6. Ao mover o mouse, mostre suas coordenadas.
7. Um duplo clique deve restaurar o estado inicial.

Complete os TODOs abaixo.
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMenu,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.click_count = 0

        self.setWindowTitle("Painel de eventos")
        self.resize(500, 300)
        self.setMouseTracking(True)

        self.input = QLineEdit()
        self.output_label = QLabel("Digite um texto")
        self.status_label = QLabel("Cliques: 0")
        self.mouse_label = QLabel("Mouse: X=0, Y=0")
        self.toggle_button = QPushButton("Inativo")

        self.toggle_button.setCheckable(True)

        # TODO 1:
        # conecte textChanged do input a setText do output_label.

        # TODO 2:
        # conecte clicked do toggle_button a toggle_state.

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.output_label)
        layout.addWidget(self.status_label)
        layout.addWidget(self.mouse_label)
        layout.addWidget(self.toggle_button)

        container = QWidget()
        container.setLayout(layout)
        container.setMouseTracking(True)

        self.setCentralWidget(container)

    def toggle_state(self, checked):
        # TODO: altere entre "Ativo" e "Inativo".
        pass

    def mousePressEvent(self, event):
        # TODO:
        # conte somente cliques com botão esquerdo.
        pass

    def mouseMoveEvent(self, event):
        # TODO:
        # mostre coordenadas no mouse_label.
        pass

    def mouseDoubleClickEvent(self, event):
        # TODO:
        # restaure a interface.
        pass

    def contextMenuEvent(self, event):
        # TODO:
        # crie as quatro ações e conecte-as.
        pass

    def reset_counter(self):
        self.click_count = 0
        self.status_label.setText("Cliques: 0")

    def change_title(self):
        self.setWindowTitle("Título alterado")

    def reset_interface(self):
        self.input.clear()
        self.output_label.setText("Digite um texto")
        self.toggle_button.setChecked(False)
        self.toggle_button.setText("Inativo")
        self.reset_counter()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
