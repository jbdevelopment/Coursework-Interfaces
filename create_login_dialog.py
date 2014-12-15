from C3_Media_DBMS import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *
    
import sys
import pdb

class LoginWidget(QWidget):
    """Error displayed when login password is incorrect"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.login_label = QLabel("Please enter the Password to access:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        #create layout
        self.login_layout = QVBoxLayout()
        self.login_buttons_layout = QHBoxLayout()
        #add widgets to layout
        self.login_layout.addWidget(self.login_label)
        self.login_layout.addWidget(self.password_entry)
        
        self.setLayout(self.login_layout)

def login_dialog_main():
    application = QApplication(sys.argv)
    window = LoginWidget()
    window.show()
    window.raise_()
    application.exec_()
                
if __name__ == '__main__':
    login_dialog_main()
