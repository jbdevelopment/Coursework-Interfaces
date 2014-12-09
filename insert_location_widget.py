from PyQt4.QtGui import *
from PyQt4.QtCore import *

from display_entry_error_dialog import *
#from main_menu_UI import *

import sys
import pdb

class InsertLocationWidget(QWidget):
    """The main window that contains the layouts
       for each the method to insert record data
       for each table"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Location")

        self.get_location_name = QLineEdit()
        self.get_location_name.setPlaceholderText("Enter Location")

        self.enter_new_location_layout = QVBoxLayout()

        self.enter_new_location_layout.addWidget(self.get_location_name)

        self.setLayout(self.enter_new_location_layout)

    def get_location(self):
        return self.get_location_name.text()