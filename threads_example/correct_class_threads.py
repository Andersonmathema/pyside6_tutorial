from PySide6.QtCore import Qt, QThreadPool, Signal, Slot, QRunnable
from PySide6.QtWidgets import (QApplication,
                               QMainWindow,
                               QWidget,
                               QLabel,
                               QPushButton,
                               QVBoxLayout)

import sys
import time

class MainWindow(QMainWindow):

    progress_signal = Signal(int)


    def __init__(self):
        super().__init__()

        self.count = 0

        self.threadpool = QThreadPool()

        self.progress_signal.connect(self.update_display)

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
        worker = Worker(self.run_demo, 5)
        self.threadpool.start(worker)


    def run_demo(self, length=10):
        for i in range(0, length):
            print(f'Sleeping {self.count}')
            time.sleep(2)
            self.update_count()


    def update_display(self,new_num):
        self.status_label.setText(str(new_num))


    def update_count(self):
        self.count += 1
        self.progress_signal.emit(self.count)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    @Slot() # Qt.QtCore.Slot
    def run(self):
        self.fn(*self.args, **self.kwargs)

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()




