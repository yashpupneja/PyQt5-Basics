import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Buttons")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
        self.text1=QLabel("MyText",self)
        enterButton=QPushButton("Enter",self)
        exitButton=QPushButton("Exit",self)
        self.text1.move(160,50)
        enterButton.move(100,80)
        exitButton.move(200,80)
        enterButton.clicked.connect(self.enterFunc)
        exitButton.clicked.connect(self.exitFunc)
        self.show()

    def enterFunc(self):
        self.text1.setText("You clicked Enter")
        self.text1.resize(150,20)
    def exitFunc(self):
        self.text1.setText("You clicked Exit")
        self.text1.resize(150, 20)

def main():
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()