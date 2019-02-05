import sys, style, menuManager
from PyQt5 import QtWidgets, QtGui, QtCore

class LoginWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("Login")
        self.setFixedSize(380, 270)
        self.initUI()

    def initUI(self):

        #Label declaration
        font = QtGui.QFont("Arial",18,QtGui.QFont.Bold)
        labelTitle = QtWidgets.QLabel('SCHEDULER',self)
        labelTitle.setFont(font)

        #Edit text declaration
        eTxtUser= QtWidgets.QLineEdit()
        eTxtPass= QtWidgets.QLineEdit()
        eTxtPass.setEchoMode(QtWidgets.QLineEdit.Password)

        #setting placeholders
        eTxtUser.setPlaceholderText("YourUser")
        eTxtPass.setPlaceholderText("********")

        #Buttons declaration
        button1 = QtWidgets.QPushButton('Login', self)

        #setting on click handlers
        button1.clicked.connect(self.handleButton1)

        #creates a layout horizontally centered
        vBox = QtWidgets.QVBoxLayout()
        #creates an element that adds space to the top
        vBox.addStretch(1)

        #adds the titleLabel
        vBox.addWidget(labelTitle)

        #add space between the title and the buttons
        vBox.addStretch(1)

        #adds the text input & buttons to the layout
        vBox.addWidget(eTxtUser)
        vBox.addWidget(eTxtPass)
        vBox.addWidget(button1)

        #creates an element that adds space to the bottom
        vBox.addStretch(2)

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

        self.setObjectName("logginWindow")
        self.setStyleSheet(style.stylesheetQWidget)

        #sets the window title
        self.setWindowTitle("Scheduler")

    def handleButton1(self):

        self.switch_window.emit() # se pueden añadir parametros a pasar


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle("TITLE")
        self.setFixedSize(240, 320)
        self.initUI()

    def initUI(self):

        #Buttons declaration
        button1 = QtWidgets.QPushButton(QtGui.QIcon("add.svg"), 'New Category', self)
        button2 = QtWidgets.QPushButton(QtGui.QIcon("file.png"), 'Manager', self)
        button3 = QtWidgets.QPushButton(QtGui.QIcon("addTask.png"), 'New Task', self)
        button4 = QtWidgets.QPushButton(QtGui.QIcon("user.png"), 'User Settings', self)

        #setting on click handlers
        button1.clicked.connect(self.handleButton1)
        button2.clicked.connect(self.handleButton2)
        button3.clicked.connect(self.handleButton3)
        button4.clicked.connect(self.handleButton4)

        #creates a layout horizontally centered
        vBox1 = QtWidgets.QVBoxLayout()
        vBox2 = QtWidgets.QVBoxLayout()

        #creates an element that adds space to the top
        vBox1.addStretch(1)
        vBox2.addStretch(1)

        #adds the buttons to the layout
        vBox1.addWidget(button1)
        vBox1.addWidget(button2)
        vBox2.addWidget(button3)
        vBox2.addWidget(button4)

        #creates an element that adds space to the bottom
        vBox1.addStretch(1)
        vBox2.addStretch(1)

        #creates a layout vertically centered
        hBox=QtWidgets.QHBoxLayout()
        #creates an element that adds space to the left
        hBox.addStretch(1)
        #adds the layout with the buttons
        hBox.addLayout(vBox1)
        hBox.addLayout(vBox2)
        #creates an element that adds space to the right
        hBox.addStretch(1)

        #sets the vBox as the main layout
        self.setLayout(hBox)

        #setting styles
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

class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.loginWindow = LoginWindow()
        self.loginWindow.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.loginWindow.switch_window.connect(self.show_main)
        self.loginWindow.show()

    def show_main(self):
        self.mainWindow = MainWindow()
        self.loginWindow.close()
        self.mainWindow.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
