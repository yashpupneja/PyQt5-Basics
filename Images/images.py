import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50,50,1000,800)
        self.UI()

    def UI(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap('images/Yashu.jpg'))
        self.image.move(220,100)
        self.image.resize(500,500)
        removeButton=QPushButton("Remove",self)
        removeButton.move(380,610)
        removeButton.clicked.connect(self.removeImg)
        showButton=QPushButton("Show",self)
        showButton.move(460,610)
        showButton.clicked.connect(self.showImg)
        self.show()

    def removeImg(self):
        self.image.close()
    def showImg(self):
        self.image.show()

def main():
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()