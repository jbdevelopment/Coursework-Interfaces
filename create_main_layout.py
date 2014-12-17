from added_record_dialog import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re

class MainMenuLayout(QWidget):
    """docstring for Main Menu Layout"""
    def __init__(self):
        super().__init__()

        #components
        self.new_record_button = QPushButton("New Record")
        self.display_records_button = QPushButton("Display Table Records")
        self.edit_record_button = QPushButton("Edit Records")
        self.delete_record_button = QPushButton("Delete Record")
        self.logout_button = QPushButton("Logout")
        self.change_password_button = QPushButton("Change Password")

        #create layout
        self.main_menu_layout = QGridLayout()

        #add components to layout
        #self.main_menu_layout.addWidget(self.new_record_button,0,0)
        #self.main_menu_layout.addWidget(self.display_records_button,0,1)
        #self.main_menu_layout.addWidget(self.edit_record_button,1,0)
        #self.main_menu_layout.addWidget(self.delete_record_button,1,1)
        #self.main_menu_layout.addWidget(self.logout_button,3,0)
        #self.main_menu_layout.addWidget(self.change_password_button,3,1)
