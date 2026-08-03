from PySide6.QtWidgets import QApplication, QLabel

app = QApplication() # Vá ao exec lá embaixo

label = QLabel('Deixa um like!')
label.show()

app.exec() # Do app até o exec só pode ser executado 1 widget

