from PySide6.QtCore import Qt # Para alinhar elementos
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QLabel, QPushButton # Botão

app = QApplication() 

font = QFont()
font.setPixelSize(90)

label = QLabel('Deixa um like!')
label.setFont(font)
label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Como alinho ao centro
label.show()

botao = QPushButton('Botão!') # Botão instanciado
botao.setFont(font)
botao.show()

app.exec() 

# Ao executar este código você percebe que ele criar duas janelas a cada show
# Como o Qt só deixa rodar um widget, o segredo é fazer um widget pai com os dois dentro
