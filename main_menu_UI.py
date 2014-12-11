from login_dialog import *
from login_error_dialog import *
from change_password_dialog import *
from password_reset import *


from display_entry_error_dialog import *
from radio_button_dialog_class import *
from printing import *
from SQLController import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re

class MainWindow(QMainWindow):
        """Creates the main menu window where all
        main processes will occure"""

        def __init__(self):
                super().__init__()
                self.setGeometry(300, 300, 500, 100)
                self.setWindowTitle("C3 Media Database Management System")

                self.password = read_password()

                self.printer = QPrinter()
                self.printer.setPageSize(QPrinter.Letter)

                self.stacked_layout = QStackedLayout()

                self.central_widget = QWidget()
                self.central_widget.setLayout(self.stacked_layout)

                self.setCentralWidget(self.central_widget)

                #self.create_login_dialog()
                self.create_main_menu_layout()
                self.insert_location_method()
                self.insert_item_type_method()
                self.insert_customer_method()

                self.stacked_layout.setCurrentIndex(0)


                QShortcut(QKeySequence("Ctrl+W"), self, self.close)

                self.create_menubar_actions()

        def create_login_dialog(self):
                #components
                self.login_interface_widget = LoginWidget()
                self.quit_button = QPushButton("Quit")
                self.login_button = QPushButton("Login")

                self.quit_button.setAutoDefault(False)
                self.login_button.setAutoDefault(True)

                self.login_buttons_layout = QHBoxLayout()
                self.login_buttons_layout.addWidget(self.quit_button)
                self.login_buttons_layout.addWidget(self.login_button)

                self.login_buttons_widget = QWidget()
                self.login_buttons_widget.setLayout(self.login_buttons_layout)

                self.login_layout = QVBoxLayout()
                self.login_layout.addWidget(self.login_interface_widget)
                self.login_layout.addWidget(self.login_buttons_widget)

                self.login_widget = QWidget()
                self.login_widget.setLayout(self.login_layout)

                self.stacked_layout.addWidget(self.login_widget)

                self.login_interface_widget.password_entry.returnPressed.connect(self.login)
                self.login_button.clicked.connect(self.login)
                self.quit_button.clicked.connect(self.close)

        def login(self):
                name = self.login_interface_widget.password_entry.text()
                if name == self.password:
                    allow_access = True
                    self.stacked_layout.setCurrentIndex(1)
                else:
                    allow_access = False
                    login_error = LoginErrorDialog()
                    login_error.exec_()

        def logout(self):
                self.stacked_layout.setCurrentIndex(0)
                self.password_entry.clear()
                self.password = read_password()

        def change_password_method(self):
                change_password_dialog = ChangePasswordDialog(self.password)
                change_password_dialog.exec_()
                self.new_password = change_password_dialog.change_password()
                if self.new_password != self.password:
                    self.password = self.new_password
                    update_password(self.password)      

        def create_menubar_actions(self):
                #file actions
                self.open = QAction("Open", self)
                self.close_window = QAction("Close Window...", self)

                #edit actions
                self.cut = QAction("Cut", self)
                self.copy = QAction("Copy", self)
                self.paste = QAction("Paste...", self)
                self.select_all = QAction("Select All", self)

                #menubar
                self.menubar = QMenuBar()

                #add file menu and add actions to file menu
                self.file_menu = self.menubar.addMenu("File")
                self.file_menu.addAction(self.open)
                self.file_menu.addAction(self.close_window)

                #file menu shortcuts
                self.open.setShortcut('Ctrl+O')

                #add edit menu and add actions to edit menu
                self.edit_menu = self.menubar.addMenu("Edit")
                self.edit_menu.addAction(self.cut)
                self.edit_menu.addAction(self.copy)
                self.edit_menu.addAction(self.paste)
                self.edit_menu.addAction(self.select_all)

                #edit menu shortcuts
                self.cut.setShortcut('Ctrl+X')
                self.copy.setShortcut('Ctrl+C')
                self.paste.setShortcut('Ctrl+P')
                self.select_all.setShortcut('Ctrl+A')

                #create menubar
                self.setMenuBar(self.menubar)

                #connections
                self.open.triggered.connect(self.open_connection)

        def create_main_menu_layout(self):
                #components
                self.new_record_button = QPushButton("New Record")
                self.display_records_button = QPushButton("Display Table Records")
                self.edit_record_button = QPushButton("Edit Records")
                self.delete_record_button = QPushButton("Delete Record")
                self.logout_button = QPushButton("Logout")
                self.change_password_button = QPushButton("Change Password")

                #create layout
                self.main_menu_screen_layout = QGridLayout()

                #add components to layout
                self.main_menu_screen_layout.addWidget(self.new_record_button,0,0)
                self.main_menu_screen_layout.addWidget(self.display_records_button,0,1)
                self.main_menu_screen_layout.addWidget(self.edit_record_button,1,0)
                self.main_menu_screen_layout.addWidget(self.delete_record_button,1,1)
                self.main_menu_screen_layout.addWidget(self.logout_button,3,0)
                self.main_menu_screen_layout.addWidget(self.change_password_button,3,1)

                #create widget to hold layout
                self.main_menu_initial_widget = QWidget()

                #add layout to widget
                self.main_menu_initial_widget.setLayout(self.main_menu_screen_layout)

                #add widget to stacked layout
                self.stacked_layout.addWidget(self.main_menu_initial_widget)

                #connections
                self.new_record_button.clicked.connect(self.create_new_record_select_table_dialog)
                self.logout_button.clicked.connect(self.logout)
                self.change_password_button.clicked.connect(self.change_password_method)

        def create_new_record_select_table_dialog(self):
                self.select_table_dialog_box = RadioButtonWidget("Create New Record", "Please select a table", ("Item","Location","Item-Type", "Customer", "Loan","Loan-Item", "PAT-Test","Item-Test"))
                self.select_table_dialog_box.exec_()
                self.selected_table = self.select_table_dialog_box.selected_button()

                if self.selected_table == 1:
                        pass
                elif self.selected_table == 2:
                        if hasattr(self, 'insert_location_widget'):
                                self.get_location_name.clear()
                                self.stacked_layout.setCurrentIndex(1)
                        else:
                                self.insert_location_method()
                elif self.selected_table == 3:
                        if hasattr(self, 'insert_item_type_widget'):
                                self.get_item_type.clear()
                                self.stacked_layout.setCurrentIndex(2)
                        else:
                                self.insert_item_type_method()
                elif self.selected_table == 4:
                        if hasattr(self, 'insert_customer_widget'):
                                self.get_forename.clear()
                                self.get_surname.clear()
                                self.get_company.clear()
                                self.get_address.clear()
                                self.get_town.clear()
                                self.get_post_code.clear()
                                self.get_mobile.clear()
                                self.get_landline.clear()
                                self.get_email.clear()
                                self.stacked_layout.setCurrentIndex(3)
                        else:
                                self.insert_customer_method()
                                while hasattr(self, 'error_dialog'):
                                    pass
                                else:
                                    self.stacked_layout.setCurrentIndex(0)
                elif self.selected_table == 5:
                        pass
                elif self.selected_table == 6:
                        pass
                elif self.selected_table == 7:
                        pass
                elif self.selected_table == 8:
                        pass

        def insert_location_method(self):
                self.location_label = QLabel("Location")
                self.get_location_name = QLineEdit()
                self.get_location_name.clear()
                self.get_location_name.setPlaceholderText("Enter Location")
                self.cancel_button = QPushButton("Cancel")
                self.confirm_button = QPushButton("Confirm")

                self.enter_location_layout = QVBoxLayout()
                self.enter_location_layout.addWidget(self.location_label)
                self.enter_location_layout.addWidget(self.get_location_name)
                self.enter_location_widget = QWidget()
                self.enter_location_widget.setLayout(self.enter_location_layout)

                self.location_buttons_layout = QHBoxLayout()
                self.location_buttons_layout.addWidget(self.cancel_button)
                self.location_buttons_layout.addWidget(self.confirm_button)

                self.location_buttons_widget = QWidget()
                self.location_buttons_widget.setLayout(self.location_buttons_layout)

                self.new_location_layout = QVBoxLayout()
                self.new_location_layout.addWidget(self.enter_location_widget)
                self.new_location_layout.addWidget(self.location_buttons_widget)

                
                self.insert_location_widget = QWidget()
                self.insert_location_widget.setLayout(self.new_location_layout)

                self.stacked_layout.addWidget(self.insert_location_widget)
                self.stacked_layout.setCurrentIndex(1)

                self.get_location_name.returnPressed.connect(self.return_location)
                self.confirm_button.clicked.connect(self.return_location)
                self.cancel_button.clicked.connect(self.cancel)


        def return_location(self):
                self.location = self.get_location_name.text()
                valid_length = False
                if len(self.location) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('a Location')
                        self.error_dialog.exec_()
                elif len(self.location) > 0 :
                        valid_length = True
                        valid = False
                        for char in self.location:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True and valid_length == True:
                                print("location: {0}".format(self.location))
                                self.stacked_layout.setCurrentIndex(0)

        def insert_item_type_method(self):
                self.item_type_label = QLabel("Item Type")
                self.get_item_type = QLineEdit()
                self.get_item_type.clear()
                self.get_item_type.setPlaceholderText("Enter Item Type")
                self.cancel_button = QPushButton("Cancel")
                self.confirm_button = QPushButton("Confirm")

                self.enter_item_type_layout = QVBoxLayout()
                self.enter_item_type_layout.addWidget(self.item_type_label)
                self.enter_item_type_layout.addWidget(self.get_item_type)
                self.enter_item_type_widget = QWidget()
                self.enter_item_type_widget.setLayout(self.enter_item_type_layout)

                self.item_type_buttons_layout = QHBoxLayout()
                self.item_type_buttons_layout.addWidget(self.cancel_button)
                self.item_type_buttons_layout.addWidget(self.confirm_button)

                self.item_type_buttons_widget = QWidget()
                self.item_type_buttons_widget.setLayout(self.item_type_buttons_layout)

                self.new_item_type_layout = QVBoxLayout()
                self.new_item_type_layout.addWidget(self.enter_item_type_widget)
                self.new_item_type_layout.addWidget(self.item_type_buttons_widget)

                self.insert_item_type_widget = QWidget()
                self.insert_item_type_widget.setLayout(self.new_item_type_layout)

                self.stacked_layout.addWidget(self.insert_item_type_widget)
                self.stacked_layout.setCurrentIndex(2)

                self.get_item_type.returnPressed.connect(self.return_item_type)
                self.confirm_button.clicked.connect(self.return_item_type)
                self.cancel_button.clicked.connect(self.cancel)



        def return_item_type(self):
                self.item_type = self.get_item_type.text()
                valid_length = False
                if len(self.item_type) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('an Item Type')
                        self.error_dialog.exec_()
                elif len(self.item_type) > 0 :
                        valid_length = True
                        valid = False
                        for char in self.item_type:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True and valid_length == True:
                                print("Item Type: {0}".format(self.item_type))
                                self.stacked_layout.setCurrentIndex(0)

        def insert_customer_method(self):
                self.forename_label = QLabel("Forename")
                self.get_forename = QLineEdit()
                self.get_forename.clear()

                self.surname_label = QLabel("Surname")
                self.get_surname = QLineEdit()
                self.get_surname.clear()

                self.company_label = QLabel("Company")
                self.get_company = QLineEdit()
                self.get_company.clear()

                self.address_label = QLabel("Address")
                self.get_address = QLineEdit()
                self.get_address.clear()

                self.town_label = QLabel("Town")
                self.get_town = QLineEdit()
                self.get_town.clear()

                self.post_code_label = QLabel("Post-Code")
                self.get_post_code = QLineEdit()
                self.get_post_code.clear()

                self.mobile_label = QLabel("Mobile")
                self.get_mobile = QLineEdit()
                self.get_mobile.clear()

                self.landline_label = QLabel("Landline")
                self.get_landline = QLineEdit()
                self.get_landline.clear()

                self.email_label = QLabel("Email")
                self.get_email = QLineEdit()
                self.get_email.clear()


                self.customer_layout = QVBoxLayout()
                self.customer_layout.addWidget(self.forename_label)
                self.customer_layout.addWidget(self.get_forename)

                self.customer_layout.addWidget(self.surname_label)
                self.customer_layout.addWidget(self.get_surname)

                self.customer_layout.addWidget(self.company_label)
                self.customer_layout.addWidget(self.get_company)

                self.customer_layout.addWidget(self.address_label)
                self.customer_layout.addWidget(self.get_address)

                self.customer_layout.addWidget(self.town_label)
                self.customer_layout.addWidget(self.get_town)

                self.customer_layout.addWidget(self.post_code_label)
                self.customer_layout.addWidget(self.get_post_code)

                self.customer_layout.addWidget(self.mobile_label)
                self.customer_layout.addWidget(self.get_mobile)

                self.customer_layout.addWidget(self.landline_label)
                self.customer_layout.addWidget(self.get_landline)

                self.customer_layout.addWidget(self.email_label)
                self.customer_layout.addWidget(self.get_email)

                
                self.cancel_button = QPushButton("Cancel")
                self.confirm_button = QPushButton("Confirm")

                self.customer_buttons_layout = QHBoxLayout()
                self.customer_buttons_layout.addWidget(self.cancel_button)
                self.customer_buttons_layout.addWidget(self.confirm_button)

                self.customer_buttons_widget = QWidget()
                self.customer_buttons_widget.setLayout(self.customer_buttons_layout)

                self.customer_layout.addWidget(self.customer_buttons_widget)

                self.insert_customer_widget = QWidget()
                self.insert_customer_widget.setLayout(self.customer_layout)

                self.stacked_layout.addWidget(self.insert_customer_widget)
                self.stacked_layout.setCurrentIndex(3)


                self.get_forename.returnPressed.connect(self.return_customer)
                self.get_surname.returnPressed.connect(self.return_customer)
                self.get_company.returnPressed.connect(self.return_customer)
                self.get_address.returnPressed.connect(self.return_customer)
                self.get_town.returnPressed.connect(self.return_customer)
                self.get_post_code.returnPressed.connect(self.return_customer)
                self.get_mobile.returnPressed.connect(self.return_customer)
                self.get_landline.returnPressed.connect(self.return_customer)
                self.get_email.returnPressed.connect(self.return_customer)
                self.confirm_button.clicked.connect(self.return_customer)
                self.cancel_button.clicked.connect(self.cancel)

        def return_customer(self):
                self.forename = self.get_forename.text()
                valid_length = False
                if len(self.forename) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('a valid Forename')
                        self.error_dialog.exec_()
                elif len(self.forename) > 0 :
                        valid_length = True
                        valid = False
                        for char in self.forename:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True and valid_length == True:
                                print("Forename: {0}".format(self.forename))


                self.surname = self.get_surname.text()
                valid_length = False
                if len(self.surname) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('a valid Surname')
                        self.error_dialog.exec_()
                elif len(self.surname) > 0 :
                        valid_length = True
                        valid = False
                        for char in self.surname:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True and valid_length == True:
                                print("Surname: {0}".format(self.surname))


                self.company = self.get_company.text()
                valid_length = False
                if len(self.company) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('a valid Company')
                        self.error_dialog.exec_()
                elif len(self.company) > 0 :
                        valid_length = True
                        valid = False
                        for char in self.company:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True and valid_length == True:
                                print("Company: {0}".format(self.company))


                self.street = self.get_address.text()
                valid_length = False
                if len(self.street) > 0:
                        valid_length = True
                        print("Address: {0}".format(self.street))
                        self.stacked_layout.setCurrentIndex(0)
                else:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('a valid Address')
                        self.error_dialog.exec_()
                        

                self.town = self.get_town.text()
                valid_length = False
                if len(self.town) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('a Town')
                        self.error_dialog.exec_()
                elif len(self.town) > 0 :
                        valid_length = True
                        valid = False
                        for char in self.town:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True and valid_length == True:
                                print("Town: {0}".format(self.town))


                self.post_code = self.get_post_code.text()
                valid_length = False
                if len(self.post_code) == 8 or len(self.post_code) == 7:
                        valid_length = True
                else:
                        valid_length = False
                if valid_length == True:
                        print("Post-Code: {0}".format(self.post_code))
                else:
                        self.error_dialog = EntryErrorDialog('a valid Post-Code')
                        self.error_dialog.exec_()


                self.mobile = self.get_mobile.text()
                valid_length = False
                if len(self.mobile) == 11:
                        valid_length = True
                        valid = False
                        for char in self.mobile:
                                no_letters = re.search('^[a-z],[A-z]*$', self.mobile)
                                valid_mobile = re.search('^(07\d{8,12}|447\d{7,11})$', self.mobile)
                                if not no_letters and valid_mobile:
                                        valid = True
                                else:
                                        valid = False
                else:
                        valid_length = False
                if valid_length == True and valid == True:
                        print("Mobile: {0}".format(self.mobile))
                else:
                        self.error_dialog = EntryErrorDialog('a valid Mobile Number')
                        self.error_dialog.exec_()


                self.landline = self.get_landline.text()
                valid_length = False
                if len(self.landline) == 11:
                        valid_length = True
                        valid = False
                        for char in self.landline:
                                no_letters = re.search('^[a-z],[A-z]*$',self.landline)
                                valid_landline = re.search('^\s*\(?(020[78]?\)? ?[1-9][0-9]{2,3} ?[0-9]{4})$|^(0[1-8][0-9]{3}\)? ?[1-9][0-9]{2} ?[0-9]{3})\s*$', self.landline)
                                if not no_letters and valid_landline:
                                        valid = True
                                else:
                                        valid = False
                else:
                        valid_length = False
                if valid_length == True and valid == True:
                        print("Landline: {0}".format(self.landline))
                else:
                        self.error_dialog = EntryErrorDialog('a valid Landline Number')
                        self.error_dialog.exec_()


                self.email = self.get_email.text()
                valid_length = False
                if len(self.email) > 0:
                        valid_length = True
                        valid = False
                        valid_email = re.match("^[a-zA-Z0-9._%-+]+@[a-zA-Z0-9._%-]+.[a-z]{2,3}(\.[a-z]{2,3})$", self.email)
                        if valid_email:
                                valid = True
                        else:
                                valid = False
                else:
                        valid_length = False
                if valid_length == True and valid == True:
                        print("Email: {0}".format(self.email))
                else:
                        self.error_dialog = EntryErrorDialog('a valid Email Address')
                        self.error_dialog.exec_()


        def cancel(self):
                self.stacked_layout.setCurrentIndex(0)

        def open_connection(self):
                path = QFileDialog.getOpenFileName()
                self.connection = SQLConnection(path)
                ok = self.connection.open_database()
                print("Database connection established: {0}".format(ok))

def main_menu_main():
        application = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        window.raise_()
        application.exec_()

if __name__ == "__main__":
        main_menu_main()

