from PyQt4.QtGui import *
from PyQt4.QtCore import *

from display_entry_error_dialog import *
#from main_menu_UI import *

import sys
import pdb

class Insertitem_typeWidget(QWidget):
    """The main window that contains the layouts
       for each the method to insert record data
       for each table"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert item_type")

        self.get_item_type_name = QLineEdit()
        self.get_item_type_name.setPlaceholderText("Enter Item Type")

        self.enter_new_item_type_layout = QVBoxLayout()

        self.enter_new_item_type_layout.addWidget(self.get_item_type_name)

        self.setLayout(self.enter_new_item_type_layout)

    def get_item_type(self):
        self.item_type_name = self.get_item_type_name.text()
        valid = False
        if len(self.item_type_name) >0:
            valid = True
        return self.get_item_type_name.text()