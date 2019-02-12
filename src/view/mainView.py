from src.controller import mainController
from src.model import fileReader
from src.view import view
from src import style

class MainWindow(view.View):

    def __init__(self):
        super().__init__(self,"Scheduler - Main Panel")
        self.title_label = None
        self.setFixedSize(240, 320)
        self.__init_ui()

#----------------------------------------------------------------------------------------
    def __init_ui(self):

        self.__create_ui_elements()
        self.__distribute_elements_in_layout(self)
        self.__fill_scroll_panel()
#----------------------------------------------------------------------------------------
    def __create_ui_elements():
        self.title_label = self.__create_title('SCHEDULER')
        scroll_area_innerframe = __create_scroll_area_frame()
        self.scroll_area = self.__create_scroll_area(scroll_area_innerframe, 120)

#----------------------------------------------------------------------------------------
    def __create_scroll_area_frame():
        scroll_content = QtWidgets.QWidget()
        grid_layout_panel = QtWidgets.QGridLayout(scroll_content)

#----------------------------------------------------------------------------------------
    def __fill_scroll_panel():
        categories = fileReader.get_categories()
        y,x = 0
        add_category_button = self.__create_button(icon = QtGui.QIcon("add.jpg"),"New category",self.add_category,style.stylesheetQPushButton)
        self.grid_layout_panel.addWidget(add_category_button),x,y)
        for category in categories:
            #TODO: create button with category data
            self.grid_layout_panel.addWidget(self.__create_button(),x,y)
            if x == 2:
                x = 0
                y += 1
            else:
                x += 1
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
    def __add_elements_to_horizontal_distribution(horizontal_block, vertical_block):
        horizontal_block.addStretch(1)
        horizontal_block.addLayout(vertical_block)
        horizontal_block.addStretch(1)

#----------------------------------------------------------------------------------------
    def add_category():
        pass
        #TODO: call controller
