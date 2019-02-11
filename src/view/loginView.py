from src.controller import loginController

class LoginWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.title_label = None
        self.user_name_edit_text = None
        self.password_edit_text = None
        self.login_button = None
        self.setWindowTitle("Login")
        self.setFixedSize(380, 270)
        self.init_ui()

#----------------------------------------------------------------------------------------
    def __init_ui(self):
        create_ui_elements()
        distribute_elements_in_layout()

        self.setObjectName("logginWindow")
        self.setStyleSheet(style.stylesheetQWidget)
        self.setWindowTitle("Scheduler")

#----------------------------------------------------------------------------------------
    def __create_ui_elements():
        title_label = create_title('SCHEDULER')
        title_label.setAlignment(QtCore.Qt.AlignCenter)
        user_name_edit_text = create_edit_text("YourUser")
        password_edit_text = create_edit_text("********")
        password_edit_text.setEchoMode(QtWidgets.QLineEdit.Password)
        login_button = create_button('Login')

#----------------------------------------------------------------------------------------
    def __distribute_elements_in_layout():
        vertical_block = QtWidgets.QVBoxLayout()
        add_elements_to_vertical_distribution(vertical_block)
        horizontal_block = QtWidgets.QHBoxLayout()
        add_elements_to_horizontal_distribution(horizontal_block)
        self.setLayout(horizontal_block)

#----------------------------------------------------------------------------------------
    def __add_elements_to_vertical_distribution(vertical_block):
        vertical_block.addStretch(1)
        vertical_block.addWidget(title)
        vertical_block.addStretch(1)
        vertical_block.addWidget(user_name_edit_text)
        vertical_block.addWidget(password_edit_text)
        vertical_block.addWidget(login_button)
        vertical_block.addStretch(2)

#----------------------------------------------------------------------------------------
    def __add_elements_to_horizontal_distribution(horizontal_block):
        hBox.addStretch(1)
        hBox.addLayout(vertical_block)
        hBox.addStretch(1)

#----------------------------------------------------------------------------------------
    def __create_title(title):
        font = QtGui.QFont("Arial",18,QtGui.QFont.Bold)
        title_label = QtWidgets.QLabel(title ,self)
        title_label.setFont(font)

#----------------------------------------------------------------------------------------
    def __create_edit_text(place_holder = ""):
        user_name_edit_text = QtWidgets.QLineEdit()
        user_name_edit_text.setPlaceholderText(place_holder)

#----------------------------------------------------------------------------------------
    def __create_button(button_name):
        login_button = QtWidgets.QPushButton(button_name, self)
        login_button.setStyleSheet(style.stylesheetQPushButton)
        login_button.clicked.connect(self.login_button_clicked)

#----------------------------------------------------------------------------------------
    def login_button_clicked(self):
        loginController.check_user_account()

#----------------------------------------------------------------------------------------
    def wrong_user_or_password():
        pass
        #TODO: show error
