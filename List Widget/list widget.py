import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

font=QFont("Times",14)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using List Widget")
        self.setGeometry(50,50,500,500)
        self.UI()

    def UI(self):
        self.addRecord=QLineEdit(self)
        self.addRecord.move(100,50)
        self.listWidget=QListWidget(self)
        self.listWidget.move(100,80)
        list1=["Batman","Superman","Spiderman"]
        self.listWidget.addItems(list1)
        self.listWidget.addItem("Heman")
        btnAdd=QPushButton("Add",self)
        btnAdd.move(360,80)
        btnAdd.clicked.connect(self.funcAdd)
        btnDelete=QPushButton("Delete",self)
        btnDelete.move(360,110)
        btnDelete.clicked.connect(self.funcDelete)
        btnGet=QPushButton("Get",self)
        btnGet.move(360,140)
        btnGet.clicked.connect(self.funcGet)
        btnDelAll=QPushButton("Delete All",self)
        btnDelAll.move(360,170)
        btnDelAll.clicked.connect(self.funcDelAll)
        #for number in range(5,11):
         #   self.listWidget.addItem(str(number))

        self.show()
    def funcDelAll(self):
        self.listWidget.clear()
    def funcGet(self):
        val=self.listWidget.currentItem().text()
        print(val)
    def funcAdd(self):
        val=self.addRecord.text()
        self.listWidget.addItem(val)
        self.addRecord.setText("")
    def funcDelete(self):
        id=self.listWidget.currentRow()
        print(id)
        self.listWidget.takeItem(id)
def main():
    App= QApplication(sys.argv)
    window=Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()