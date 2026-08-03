from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont, QAction
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QWidget, 
    QVBoxLayout, 
    QMainWindow 
)

# Código grande, vamos encapsular
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        base = QWidget() 
        layout = QVBoxLayout() 

        font = QFont()
        font.setPixelSize(90)

        label = QLabel('Deixa um like!')
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter) 

        botao = QPushButton('Botão!')
        botao.setFont(font)

        layout.addWidget(label) 
        layout.addWidget(botao) 

        base.setLayout(layout) 

        self.setCentralWidget(base) 

        menu = self.menuBar() 

        arquivo_menu = menu.addMenu('Arquivo') 
        action = QAction('Print!')
        arquivo_menu.addAction(action) 


app = QApplication() 

janela = Window() # Mudado pra Window que é o nome da classe
# O que estava aqui foi pra classe
janela.show()

app.exec() 


