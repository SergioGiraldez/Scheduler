from view import View

class MainWindow(View):

    def __init__(self):
        super().__init__(self,"Scheduler - Main Panel")
        self.title_label = None
        self.setFixedSize(240, 320)
        self.__init_ui()

    def __init_ui(self):

        self.__create_ui_elements()
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

    def __create_ui_elements():
        self.title_label = self.__create_title('SCHEDULER')
        self.scroll_area = self.__create_scroll_area()

    def __create_scroll_area_elements():
        


    def handleButton1(self):
        menuManager.mainMenuRedirectTo(1)
    def handleButton2(self):
        menuManager.mainMenuRedirectTo(2)
    def handleButton3(self):
        menuManager.mainMenuRedirectTo(3)
    def handleButton4(self):
        menuManager.mainMenuRedirectTo(4)
