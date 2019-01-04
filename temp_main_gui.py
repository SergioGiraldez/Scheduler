import sys, style
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.initUI()

    def initUI(self):

        #Buttons declaration
        button1 = QtWidgets.QPushButton('BUTTON 1', self)
        button2 = QtWidgets.QPushButton('BUTTON 2', self)
        button3 = QtWidgets.QPushButton('BUTTON 3', self)
        button4 = QtWidgets.QPushButton('BUTTON 4', self)

        button1.clicked.connect(self.handleButton1)
        button2.clicked.connect(self.handleButton2)
        button3.clicked.connect(self.handleButton3)
        button4.clicked.connect(self.handleButton4)

        #creates a layout horizontally centered
        vBox = QtWidgets.QVBoxLayout()
        #creates an element that adds space to the top
        vBox.addStretch(1)

        #adds the buttons to the layout
        vBox.addWidget(button1)
        vBox.addWidget(button2)
        vBox.addWidget(button3)
        vBox.addWidget(button4)

        #creates an element that adds space to the bottom
        vBox.addStretch(1)

        #creates a layout vertically centered
        hBox=QtWidgets.QHBoxLayout()
        #creates an element that adds space to the left
        hBox.addStretch(1)
        #adds the layout with the buttons
        hBox.addLayout(vBox)
        #creates an element that adds space to the right
        hBox.addStretch(1)

        #sets the vBox as the main layout
        self.setLayout(hBox)

        #set img as background
        self.setStyleSheet(style.stylesheet)

		#gives an initial size and position to the window
        self.setGeometry(300,300,200,250)
        #sets the window title
        self.setWindowTitle("Testing PyQt GUI")

    def handleButton1(self):
        print ('buton 1 clicked')
    def handleButton2(self):
        print ('buton 2 clicked')
    def handleButton3(self):
	    print ('buton 3 clicked')
    def handleButton4(self):
	    print ('buton 4 clicked')

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	#allows the widget to use stylesheets
	window.setAttribute(QtCore.Qt.WA_StyledBackground)
	window.show()
	sys.exit(app.exec_())
