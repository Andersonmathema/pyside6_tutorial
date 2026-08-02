from PySide6.QtGui import QFont # Import pra mudar fonte
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()

font = QFont() # Instanciando nova fonte (parametro pode ser nome da fonte)
font.setPixelSize(90) # Tamanho da fonte

label = QLabel('Deixa um like!')
label.setFont(font) # Aplicando nova fonte antes do show
label.show()

app.exec() 

