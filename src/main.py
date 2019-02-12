import sys, style, menuManager
from PyQt5 import QtWidgets, QtGui, QtCore

def main():
    app = QtWidgets.QApplication(sys.argv)
    login_controller = loginController()
    login_controller.start_view()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
