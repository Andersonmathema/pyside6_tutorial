from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont, QAction # Ação para menus
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QWidget, 
    QVBoxLayout, 
    QMainWindow # Tela de menu inicial
)

app = QApplication() 
janela = QMainWindow()
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

# base.show() # Vamos parar de mostrar o base e mostrar a janela

janela.setCentralWidget(base) # A janela central mostrará os widgets de base

menu = janela.menuBar() # Criando o menu

arquivo_menu = menu.addMenu('Arquivo')  # Adicionando um elemento ao menu
action = QAction('Print!') # Uma ação para o menu item criado
arquivo_menu.addAction(action) # Indicando o que fazer ao clicar no menu
 
janela.show()

app.exec() 


