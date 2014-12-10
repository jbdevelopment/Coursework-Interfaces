from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb

class EntryErrorDialog(QDialog):
    """Error displayed when nothing is entered"""
<<<<<<< HEAD
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Entry Error")
        self.login_error_label = QLabel("Error, please enter a location")
=======
    def __init__(self,field):
        super().__init__()
        self.setWindowTitle("Entry Error")
        self.login_error_label = QLabel("Error, please enter {0}".format(field))
>>>>>>> FETCH_HEAD
        self.close_button = QPushButton("Close")

        self.login_error_layout = QGridLayout()
        self.close_layout = QHBoxLayout()
        self.close_layout.addWidget(self.close_button)

        self.close_widget = QWidget()
        self.close_widget.setLayout(self.close_layout)

        self.login_error_layout.addWidget(self.login_error_label,0,0)
        self.login_error_layout.addWidget(self.close_widget,1,1)


        self.setLayout(self.login_error_layout)

<<<<<<< HEAD
        self.close_button.clicked.connect(self.close)
        #self.returnPressed.connect(self.close)
=======
        self.close_button.clicked.connect(self.close_window)

    def close_window(self):
        self.close()
>>>>>>> FETCH_HEAD
