from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader

def callback():
    print(window.email_input.text())
    print('Callback login!')


# Use no terminal pyside6-designer
app = QApplication()

loader = QUiLoader()
window = loader.load('login.ui')
window.login_button.clicked.connect(callback) # Observe que a variável não foi inicializada mas veio da UI
window.show()

app.exec()

# Transformar UI em py
# pyuic5 <arquivo>.ui -o <output>.py
# Voltar ao video no 1h45


