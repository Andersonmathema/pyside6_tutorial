#Continue no https://www.youtube.com/watch?v=5S2paeDKTLk&t=8140s
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
from qdarktheme import load_stylesheet 

# Vamos acionar o botão com função de callback
def callback():
    print('Cliquei no botão!')


def callback2():
    print('Callback 2')


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
        botao.clicked.connect(callback) # Conectando o botão a função
        botao.clicked.connect(callback2) # Conectando o botão a uma segunda função

        layout.addWidget(label) 
        layout.addWidget(botao) 

        base.setLayout(layout) 

        self.setCentralWidget(base) 

        menu = self.menuBar() 

        arquivo_menu = menu.addMenu('Arquivo') 
        action = QAction('Print!')
        action.triggered.connect(callback2)
        arquivo_menu.addAction(action) 


app = QApplication() 
app.setStyleSheet(load_stylesheet('light')) 

janela = Window() 

janela.show()

app.exec() 


