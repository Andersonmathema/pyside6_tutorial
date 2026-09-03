from PySide6.QtCore import Qt, QThreadPool, Signal, Slot
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QWidget,
                               QLabel,
                               QPushButton,
                               QVBoxLayout)

import sys
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.count = 0

        self.threadpool = QThreadPool()

        self.setWindowTitle("Threaded example")
        layout = QVBoxLayout()

        self.status_label = QLabel(str(self.count))
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.start_button = QPushButton('Start Demo')

        self.start_button.pressed.connect(self.button_pressed)

        layout.addWidget(self.status_label)
        layout.addWidget(self.start_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)

        self.setCentralWidget(central_widget)


    def button_pressed(self):
        self.threadpool.start(self.run_demo)


    def run_demo(self, length=10):
        for i in range(0, length):
            print(f'Sleeping {self.count}')
            time.sleep(2)
            self.update_count()


    def update_count(self):
        self.count += 1
        self.status_label.setText(str(self.count))


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()




