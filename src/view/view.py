from src import style

class View(QtWidgets.QWidget):

    def __init__(self,window_title):
        QtWidgets.QWidget.__init__(self)
        self.vertical_block = None
        self.horizontal_block = None
        self.setWindowTitle(window_title)

#----------------------------------------------------------------------------------------
    def __create_title(title):
        font = QtGui.QFont("Arial",18,QtGui.QFont.Bold)
        title_label_tmp = QtWidgets.QLabel(title ,self)
        title_label_tmp.setFont(font)
        title_label_tmp.setAlignment(QtCore.Qt.AlignCenter)
        return title_label_tmp

#----------------------------------------------------------------------------------------
    def __create_edit_text(place_holder = ""):
        edit_text = QtWidgets.QLineEdit()
        edit_text.setPlaceholderText(place_holder)
        return edit_text

#----------------------------------------------------------------------------------------
    def __create_button(icon = None, button_name, function_name, button_style):
        button = QtWidgets.QPushButton(icon, button_name, self)
        button.setStyleSheet(button_style)
        button.clicked.connect(function_name)
        return button

#----------------------------------------------------------------------------------------
    def __create_scroll_area(elements_frame, height):
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidget(elements_frame)
        scroll_area.setWidgetResizable(False)
        scroll_area.setFixedHeight(height)
        return scroll_area

#----------------------------------------------------------------------------------------
    def __distribute_elements_in_layout(self):
        self.vertical_block = QtWidgets.QVBoxLayout()
        self.__add_elements_to_vertical_distribution(vertical_block)
        self.horizontal_block = QtWidgets.QHBoxLayout()
        self.__add_elements_to_horizontal_distribution(horizontal_block, vertical_block)
        self.setLayout(horizontal_block)

#----------------------------------------------------------------------------------------
    def __add_elements_to_vertical_distribution(vertical_block):
        vertical_block.addStretch(1)

#----------------------------------------------------------------------------------------
    def __add_elements_to_horizontal_distribution(horizontal_block, vertical_block):
        horizontal_block.addStretch(1)
