import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(150,250,300,450)
        self.setWindowTitle("Window's Title")

        self.show()

App= QApplication(sys.argv)
window=Window()
sys.exit(App.exec_())