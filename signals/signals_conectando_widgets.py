import sys

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Widget label
        self.label = QLabel()

        #Widget lineEdit (input)
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        # Criando layout para conectar os dois widgets criados
        layout = QVBoxLayout()
        layout.addWidget(self.input) # Adicionando os widgets
        layout.addWidget(self.label)

        # Empacotando tudo como um único widget
        container = QWidget()
        container.setLayout(layout)

        # Centralizando na tela
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
