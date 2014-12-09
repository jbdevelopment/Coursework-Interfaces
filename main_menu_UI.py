from radio_button_dialog_class import *
from insert_location_widget import *
from insert_item_type_widget import *
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
		self.select_table_dialog_box = RadioButtonWidget("Create New Record", "Please select a table", ("Location","Item-Type","Item", "Customer", "Loan","Loan-Item", "PAT-Test","Item-Test"))
		self.select_table_dialog_box.exec_()
		self.selected_table = self.select_table_dialog_box.selected_button()

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

