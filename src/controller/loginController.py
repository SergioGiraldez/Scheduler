from src.model import user
from src.controller import menuController

class loginController:

    def __init__(self):
        self.login_window = None

#----------------------------------------------------------------------------------------
    def start_view():
        self.login_window = LoginWindow()
        self.login_window.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.login_window.switch_window.connect(self.show_menu)
        self.login_window.show()

#----------------------------------------------------------------------------------------
    def show_menu(self):
        menu_controller = menuController()
        menu_controller.start_view()
        self.login_window.close()

#----------------------------------------------------------------------------------------
def check_user_account(user_name, password):
    if user.is_user_registered(user_name, password):
        self.switch_window.emit()
    else
        self.login_window.wrong_user_or_password()
