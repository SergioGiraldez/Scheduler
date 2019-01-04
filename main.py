import sys, style, menuManager
from PyQt5 import QtWidgets, QtGui, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setFixedSize(240, 320)
        self.initUI()

    def initUI(self):

        #Label declaration
        labelTitle = QtWidgets.QLabel('SCHEDULER',self)

        #Buttons declaration
        button1 = QtWidgets.QPushButton('New Schedule', self)
        button2 = QtWidgets.QPushButton('Task Manager', self)
        button3 = QtWidgets.QPushButton('Send new Task', self)
        button4 = QtWidgets.QPushButton('Load Schedule', self)

        #setting on click handlers
        button1.clicked.connect(self.handleButton1)
        button2.clicked.connect(self.handleButton2)
        button3.clicked.connect(self.handleButton3)
        button4.clicked.connect(self.handleButton4)

        #creates a layout horizontally centered
        vBox = QtWidgets.QVBoxLayout()
        #creates an element that adds space to the top
        vBox.addStretch(1)

        #adds the titleLabel
        vBox.addWidget(labelTitle)

        #add space between the title and the buttons
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

        #setting styles

        #title alignment Centered
        labelTitle.setAlignment(QtCore.Qt.AlignCenter)

        button1.setStyleSheet(style.stylesheetQPushButton)
        button2.setStyleSheet(style.stylesheetQPushButton)
        button3.setStyleSheet(style.stylesheetQPushButton)
        button4.setStyleSheet(style.stylesheetQPushButton)

        self.setObjectName("mainWindow")
        self.setStyleSheet(style.stylesheetQWidget)

        #sets the window title
        self.setWindowTitle("Scheduler")

    def handleButton1(self):
        menuManager.mainMenuRedirectTo(1)
    def handleButton2(self):
        menuManager.mainMenuRedirectTo(2)
    def handleButton3(self):
        menuManager.mainMenuRedirectTo(3)
    def handleButton4(self):
        menuManager.mainMenuRedirectTo(4)


if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	window = Window()
	#allows the widget to use stylesheets
	window.setAttribute(QtCore.Qt.WA_StyledBackground)
	window.show()
	sys.exit(app.exec_())
