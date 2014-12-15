from create_login_dialog import *
from login_error_dialog import *
from change_password_dialog import *
from password_reset import *


from create_main_layout import *
from create_new_item_type_layout import *
from create_new_location_layout import *
from create_new_customer_layout import *

from display_entry_error_dialog import *
from added_record_dialog import *
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
        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle("C3 Media Database Management System")

        self.password = read_password()

        self.printer = QPrinter()
        self.printer.setPageSize(QPrinter.Letter)

        self.stacked_layout = QStackedLayout()

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.stacked_layout)

        self.setCentralWidget(self.central_widget)

        self.create_main_menu_layout()
        self.create_new_location_layout()
        self.create_new_item_type_layout()
        self.create_new_customer_layout()

        self.stacked_layout.setCurrentIndex(0)


        QShortcut(QKeySequence("Ctrl+W"), self, self.close)

        self.create_menubar_actions()

    def create_menubar_actions(self):
        #file actions
        self.open = QAction("Open", self)
        self.new = QAction("New", self)
        self.save = QAction("Save", self)
        self.save_as = QAction("Save As...", self)
        self.Print = QAction("Print", self)
        self.close_window = QAction("Close Window...", self)

        #edit actions
        self.cut = QAction("Cut", self)
        self.copy = QAction("Copy", self)
        self.paste = QAction("Paste...", self)
        self.select_all = QAction("Select All", self)

        #window actions
        self.view_main_window = QAction("Main Menu", self)

        #menubar
        self.menubar = QMenuBar()

        #add file menu and add actions to file menu
        self.file_menu = self.menubar.addMenu("File")
        self.file_menu.addAction(self.open)
        self.file_menu.addAction(self.new)
        self.file_menu.addAction(self.save)
        self.file_menu.addAction(self.save_as)
        self.file_menu.addAction(self.Print)
        self.file_menu.addAction(self.close_window)

        #file menu shortcuts
        self.open.setShortcut('Ctrl+O')
        self.new.setShortcut('Ctrl+N')
        self.save.setShortcut('Ctrl+S')
        self.save_as.setShortcut('Ctrl+Shift+S')
        self.Print.setShortcut('Ctrl+P')
        self.close_window.setShortcut('Ctrl+W')

        #add edit menu and add actions to edit menu
        self.edit_menu = self.menubar.addMenu("Edit")
        self.edit_menu.addAction(self.cut)
        self.edit_menu.addAction(self.copy)
        self.edit_menu.addAction(self.paste)
        self.edit_menu.addAction(self.select_all)

        #edit menu shortcuts
        self.cut.setShortcut('Ctrl+X')
        self.copy.setShortcut('Ctrl+C')
        self.paste.setShortcut('Ctrl+V')
        self.select_all.setShortcut('Ctrl+A')
        self.close_window.setShortcut('Ctrl+W')

        #add window menu and actions to window menu
        self.window_menu = self.menubar.addMenu("Window")
        self.window_menu.addAction(self.view_main_window)

        #window menu shortcuts

        #create menubar
        self.setMenuBar(self.menubar)

        #connections
        self.open.triggered.connect(self.open_connection)
        self.close_window.triggered.connect(self.close)

        self.view_main_window.triggered.connect(self.create_main_menu_layout)

    def create_new_record_select_table_dialog(self):
        self.select_table_dialog_box = RadioButtonWidget("Create New Record", "Please select a table", ("Item","Location","Item-Type", "Customer", "Loan","Loan-Item", "PAT-Test","Item-Test"))
        self.select_table_dialog_box.exec_()
        self.selected_table = self.select_table_dialog_box.selected_button()

        if self.selected_table == 1:
            pass
        elif self.selected_table == 2:
            if hasattr(self, 'create_new_location_layout'):
                self.new_location_widget.get_location_name.clear()
                self.stacked_layout.setCurrentIndex(1)
            else:
                self.create_new_location_layout()
        elif self.selected_table == 3:
            if hasattr(self, 'create_new_item_type_layout'):
                self.new_item_type_widget.get_item_type.clear()
                self.stacked_layout.setCurrentIndex(2)
            else:
                self.create_new_item_type_layout()
        elif self.selected_table == 4:
            if hasattr(self, 'create_new_customer_layout'):
                self.new_customer_widget.get_forename.clear() 
                self.new_customer_widget.get_surname.clear()
                self.new_customer_widget.get_company.clear()
                self.new_customer_widget.get_address.clear()
                self.new_customer_widget.get_town.clear()
                self.new_customer_widget.get_post_code.clear()
                self.new_customer_widget.get_mobile.clear()
                self.new_customer_widget.get_landline.clear()
                self.new_customer_widget.get_email.clear()
                self.new_customer_widget.get_forename.setFocus()
                self.stacked_layout.setCurrentIndex(3)
            else:
                self.create_new_customer_layout()
        elif self.selected_table == 5:
             pass
        elif self.selected_table == 6:
             pass
        elif self.selected_table == 7:
             pass
        elif self.selected_table == 8:
             pass

    def create_main_menu_layout(self):
        self.main_menu_widget = MainMenuLayout()
        self.main_menu_widget.setLayout(self.main_menu_widget.main_menu_layout)

        #connections
        self.main_menu_widget.new_record_button.clicked.connect(self.create_new_record_select_table_dialog)
        self.main_menu_widget.logout_button.clicked.connect(self.logout)
        self.main_menu_widget.change_password_button.clicked.connect(self.change_password_method)

        self.stacked_layout.addWidget(self.main_menu_widget)

    def create_new_location_layout(self):
        self.new_location_widget = NewLocationWidget()
        self.new_location_widget.setLayout(self.new_location_widget.new_location_layout)

        #connections
        self.new_location_widget.get_location_name.returnPressed.connect(self.return_location)
        self.new_location_widget.confirm_button.clicked.connect(self.return_location)
        self.new_location_widget.cancel_button.clicked.connect(self.cancel)

        self.stacked_layout.addWidget(self.new_location_widget)

    def return_location(self):
        self.location = self.new_location_widget.get_location_name.text()
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
                self.added_record_dialog = DisplayCreatedRecordDialog("Location Record for {0}".format(self.location))
                self.added_record_dialog.exec_()
        self.stacked_layout.setCurrentIndex(0)

    def create_new_item_type_layout(self):
        self.new_item_type_widget = NewItemTypeWidget()
        self.new_item_type_widget.setLayout(self.new_item_type_widget.new_item_type_layout)

        self.new_item_type_widget.get_item_type.returnPressed.connect(self.return_item_type)
        self.new_item_type_widget.confirm_button.clicked.connect(self.return_item_type)
        self.new_item_type_widget.cancel_button.clicked.connect(self.cancel)

        self.stacked_layout.addWidget(self.new_item_type_widget)

    def return_item_type(self):
        self.item_type = self.new_item_type_widget.get_item_type.text()
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
                self.added_record_dialog = DisplayCreatedRecordDialog("Item Type Record for {0}".format(self.item_type))
                self.added_record_dialog.exec_()
        self.stacked_layout.setCurrentIndex(0)

    def create_new_customer_layout(self):
        self.new_customer_widget = NewCustomerWidget()
        self.new_customer_widget.setLayout(self.new_customer_widget.new_customer_layout)

        self.new_customer_widget.get_forename.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_surname.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_company.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_address.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_town.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_post_code.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_mobile.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_landline.returnPressed.connect(self.return_customer)
        self.new_customer_widget.get_email.returnPressed.connect(self.return_customer)
        self.new_customer_widget.confirm_button.clicked.connect(self.return_customer)
        self.new_customer_widget.cancel_button.clicked.connect(self.cancel)

        self.stacked_layout.addWidget(self.new_customer_widget)

    def return_customer(self):
        self.forename = self.new_customer_widget.get_forename.text()
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


        self.surname = self.new_customer_widget.get_surname.text()
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


        self.company = self.new_customer_widget.get_company.text()
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


        self.street = self.new_customer_widget.get_address.text()
        valid_length = False
        if len(self.street) > 0:
            valid_length = True
            print("Address: {0}".format(self.street))
            self.stacked_layout.setCurrentIndex(0)
        else:
            valid_length = False
            self.error_dialog = EntryErrorDialog('a valid Address')
            self.error_dialog.exec_()
                

        self.town = self.new_customer_widget.get_town.text()
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


        self.post_code = self.new_customer_widget.get_post_code.text()
        valid_length = False
        if len(self.post_code) == 8 or len(self.post_code) == 7:
            valid_length = True
            valid = False
            length_regex_validation = re.match('^(GIR 0AA)|((([A-Z-[QVX]][0-9][0-9]?)|(([A-Z-[QVX]][A-Z-[IJZ]][0-9][0-9]?)|(([A-Z-[QVX]][0-9][A-HJKSTUW])|([A-Z-[QVX]][A-Z-[IJZ]][0-9][ABEHMNPRVWXY])))) [0-9][A-Z-[CIKMOV]]{2})$', self.post_code)
            if length_regex_validation:
                valid = True
            else:
                valid = False
        else:
            valid_length = False
        if valid_length == True and valid == True:
            print("Post-Code: {0}".format(self.post_code))
        else:
            self.error_dialog = EntryErrorDialog('a valid Post-Code')
            self.error_dialog.exec_()


        self.mobile = self.new_customer_widget.get_mobile.text()
        valid_length = False
        if len(self.mobile) == 11:
            valid_length = True
            valid = False
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


        self.landline = self.new_customer_widget.get_landline.text()
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


        self.email = self.new_customer_widget.get_email.text()
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
            self.added_record_dialog = DisplayCreatedRecordDialog("Customer Record for {0} {1}".format(self.forename,self.surname))
            self.added_record_dialog.exec_()
        else:
            self.error_dialog = EntryErrorDialog('a valid Email Address')
            self.error_dialog.exec_()
        
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

    def cancel(self):
        self.stacked_layout.setCurrentIndex(0)

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print("Database connection established: {0}".format(ok))

def main_menu_main():
    application = QApplication(sys.argv)
    application.setQuitOnLastWindowClosed(False)
    window = MainWindow()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
        main_menu_main()
