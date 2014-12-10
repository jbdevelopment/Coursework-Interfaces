<<<<<<< HEAD
from radio_button_dialog_class import *
from insert_location_widget import *
from insert_item_type_widget import *
=======
from display_entry_error_dialog import *
from radio_button_dialog_class import *
>>>>>>> FETCH_HEAD
from printing import *
from SQLController import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb

class MainWindow(QMainWindow):
        """Creates the main menu window where all
        main processes will occure"""

        def __init__(self):
                super().__init__()
                self.setWindowTitle("C3 Media Database Management System")

                self.create_login_dialog()

                self.printer = QPrinter()
                self.printer.setPageSize(QPrinter.Letter)

                self.stacked_layout = QStackedLayout()

                self.central_widget = QWidget()
                self.central_widget.setLayout(self.stacked_layout)

                self.setCentralWidget(self.central_widget)

                self.create_main_menu_layout()

                self.stacked_layout.setCurrentIndex(0)

                QShortcut(QKeySequence("Ctrl+W"), self, self.close)

                self.create_menubar_actions()

        def create_login_dialog(self):
                pass

        def create_menubar_actions(self):
                #actions
                self.open = QAction("Open", self)

                #menubar
                self.menubar = QMenuBar()

                #add menu and actions to menu
                self.file_menu = self.menubar.addMenu("File")
                self.file_menu.addAction(self.open)

                #shortcuts
                self.open.setShortcut('Ctrl+O')

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

        def create_new_record_select_table_dialog(self):
                self.select_table_dialog_box = RadioButtonWidget("Create New Record", "Please select a table", ("Item","Location","Item-Type", "Customer", "Loan","Loan-Item", "PAT-Test","Item-Test"))
                self.select_table_dialog_box.exec_()
                self.selected_table = self.select_table_dialog_box.selected_button()

                if self.selected_table == 1:
                        pass
                elif self.selected_table == 2:
                        self.insert_location_method()
                elif self.selected_table == 3:
                        self.insert_item_type_method()
                elif self.selected_table == 4:
                        self.insert_customer_method()
                elif self.selected_table == 5:
                        pass
                elif self.selected_table == 6:
                        pass
                elif self.selected_table == 7:
                        pass
                elif self.selected_table == 8:
                        pass

        def insert_location_method(self):
                self.get_location_name = QLineEdit()
                self.get_location_name.setPlaceholderText("Enter Location")
                self.cancel_button = QPushButton("Cancel")
                self.confirm_button = QPushButton("Confirm")

                self.enter_location_layout = QVBoxLayout()
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


        def return_location(self):
                self.location = self.get_location_name.text()
                valid_length = False
                if len(self.location) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('a Location')
                        self.error_dialog.exec_()
                elif len(self.location) > 0 :
                        valid = False
                        for char in self.location:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True:
                                print("location: {0}".format(self.location))
                                self.stacked_layout.setCurrentIndex(0)

        def insert_item_type_method(self):
                self.get_item_type = QLineEdit()
                self.get_item_type.setPlaceholderText("Enter Item Type")
                self.cancel_button = QPushButton("Cancel")
                self.confirm_button = QPushButton("Confirm")

                self.enter_item_type_layout = QVBoxLayout()
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
                self.stacked_layout.setCurrentIndex(1)

                self.get_item_type.returnPressed.connect(self.return_item_type)
                self.confirm_button.clicked.connect(self.return_item_type)


        def return_item_type(self):
                self.item_type = self.get_item_type.text()
                valid_length = False
                if len(self.item_type) == 0:
                        valid_length = False
                        self.error_dialog = EntryErrorDialog('an Item Type')
                        self.error_dialog.exec_()
                elif len(self.item_type) > 0 :
                        valid = False
                        for char in self.item_type:
                                if char.isdigit() == True:
                                        valid = False
                                else:
                                        valid = True
                        if valid == False:
                                self.error_dialog = EntryErrorDialog('only letters')
                                self.error_dialog.exec_()
                        elif valid == True:
                                print("Item Type: {0}".format(self.item_type))
                                self.stacked_layout.setCurrentIndex(0)

<<<<<<< HEAD
		if self.selected_table == 1:
			#print("Location")
			self.insert_location_method()
		elif self.selected_table == 2:
			#print("ItemType")
			self.insert_item_type_method()

	def insert_location_method(self):
		self.insert_location_line_edit_widget = InsertLocationWidget()
		self.cancel_button = QPushButton("Cancel")
		self.confirm_button = QPushButton("Confirm")

		self.location_buttons_layout = QHBoxLayout()
		self.location_buttons_layout.addWidget(self.cancel_button)
		self.location_buttons_layout.addWidget(self.confirm_button)

		self.location_buttons_widget = QWidget()
		self.location_buttons_widget.setLayout(self.location_buttons_layout)

		self.new_location_layout = QVBoxLayout()
		self.new_location_layout.addWidget(self.insert_location_line_edit_widget)
		self.new_location_layout.addWidget(self.location_buttons_widget)

		self.insert_location_widget = QWidget()
		self.insert_location_widget.setLayout(self.new_location_layout)

		self.stacked_layout.addWidget(self.insert_location_widget)
		self.stacked_layout.setCurrentIndex(1)

		location = self.insert_location_line_edit_widget.get_location()
		print(location)
		self.confirm_button.clicked.connect(self.back_to_main_menu_layout)

	def back_to_main_menu_layout(self):
		self.stacked_layout.setCurrentIndex(0)

	def insert_item_type_method(self):
		pass
=======
        def insert_customer_method(self):
                self.forename_label = QLabel("Forename")
                self.get_forename = QLineEdit()
                self.surname_label = QLabel("Surname")
                self.get_surname = QLineEdit()
                self.company_label = QLabel("Company")
                self.get_company = QLineEdit()
                self.address_label = QLabel("Address Line 1")
                self.get_address = QLineEdit()
                self.town_label = QLabel("Town")
                self.get_town = QLineEdit()
                self.post_code_label = QLabel("PostCode")
                self.get_post_code = QLineEdit()
                self.mobile_label = QLabel("Mobile")
                self.get_mobile = QLineEdit()
                self.landline_label = QLabel("Landline")
                self.get_landline = QLineEdit()
                self.email_label = QLabel("Email")
                self.get_email = QLineEdit()
                
                self.cancel_button = QPushButton("Cancel")
                self.confirm_button = QPushButton("Confirm")
>>>>>>> FETCH_HEAD

        def return_item(self):
                pass

        
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

