#I followed this video to make this file: https://www.youtube.com/watch?v=Vde5SH8e1OQ&t=501s
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()
    
    def initUI(self):
        #Label
        self.label=QtWidgets.QLabel(self)
        self.label.setText("My first label!")
        self.label.move(50,50)

        #Button
        self.b1=QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(clicked)

    def clicked(self):
        self.label.setText("You pressed the button")

def window():
    app = QApplication(sys.argv)
    win=QMainWindow()
    #win.setGeometry(xpos, ypos, width, height)
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("My first PyQt file")    

    win.show()
    sys.exit(app.exec_())

window()