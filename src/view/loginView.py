from src.controller import loginController
from src.view import view
from src import style

class LoginWindow(view.View):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__(self,"Scheduler - Login Panel")
        self.title_label = None
        self.user_name_edit_text = None
        self.password_edit_text = None
        self.login_button = None
        self.setFixedSize(380, 270)
        self.__init_ui()

#----------------------------------------------------------------------------------------
    def __init_ui(self):
        self.__create_ui_elements()
        self.__distribute_elements_in_layout(self)

        self.setObjectName("logginWindow")
        self.setStyleSheet(style.stylesheetQWidget)

#----------------------------------------------------------------------------------------
    def __create_ui_elements(self):
        self.title_label = self.__create_title('LOGIN PANEL')
        self.user_name_edit_text = self.__create_edit_text("YourUser")
        self.password_edit_text = self.__create_edit_text("********")
        self.password_edit_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_button = self.__create_button('Login',self.login_button_clicked,style.stylesheetQPushButton)

#----------------------------------------------------------------------------------------
    def __add_elements_to_vertical_distribution(self, vertical_block):
        self.vertical_block.addStretch(1)
        self.vertical_block.addWidget(title)
        self.vertical_block.addStretch(1)
        self.vertical_block.addWidget(user_name_edit_text)
        self.vertical_block.addWidget(password_edit_text)
        self.vertical_block.addWidget(login_button)
        self.vertical_block.addStretch(2)

#----------------------------------------------------------------------------------------
    def __add_elements_to_horizontal_distribution(self, horizontal_block, vertical_block):
        self.horizontal_block.addStretch(1)
        self.horizontal_block.addLayout(vertical_block)
        self.horizontal_block.addStretch(1)

#----------------------------------------------------------------------------------------
    def login_button_clicked(self):
        loginController.check_user_account()

#----------------------------------------------------------------------------------------
    def wrong_user_or_password():
        pass
        #TODO: show error
