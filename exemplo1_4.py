from PySide6.QtCore import Qt 
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QPushButton,
    QWidget, # Widget que englobará
    QVBoxLayout, # Widget de layout vertical
) 


app = QApplication() 
base = QWidget() # Instanciando o widget base
layout = QVBoxLayout() # Instanciando o layout base

font = QFont()
font.setPixelSize(90)

label = QLabel('Deixa um like!')
label.setFont(font)
label.setAlignment(Qt.AlignmentFlag.AlignCenter) 
#label.show() # Para não criar novas janelas removemos isto

botao = QPushButton('Botão!')
botao.setFont(font)
#botao.show() # Para não criar novas janelas removemos isto


layout.addWidget(label) # Adicionando o label ao layout
layout.addWidget(botao) # Adicionando o botao ao layout

base.setLayout(layout) # Aplicando o layout a base

base.show() # Mostrando o novo widget
app.exec() 


