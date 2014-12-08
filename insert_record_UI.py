from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
import pdb


class InsertRecord(QMainWindow):
    """The main window that contains the layouts
       for each the method to insert record data
       for each table"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Window")

        #create actions
        self.open_database = QAction("Open Database", self)

        #add menu bar
        self.menu = QMenuBar()
        #add database actions to menu bar
        self.database_menu = self.menu.addMenu("File")
        self.database_menu.addAction(self.open_database)

        #create menu_bar
        self.setMenuBar(self.menu)

        #connections
        self.open_database.triggered.connect(self.open_connection)

        #keyboard shortcuts
        self.open_database.setShortcut('Ctrl+O')

        self.enter_records_layout = QStackedLayout()
        self.enter_records_widget = QWidget()

        self.enter_records_widget.setLayout(self.enter_records_layout)

        self.create_enter_new_location_layout()

        self.setCentralWidget(self.enter_records_widget)

        self.enter_records_layout.setCurrentIndex(0)

    def create_enter_new_location_layout(self):
        self.get_location_name = QLineEdit()
        self.enter_button = QPushButton("Enter")
        self.cancel_button = QPushButton("Cancel")
        self.get_location_name.setPlaceholderText("Location")

        self.enter_new_location_layout = QVBoxLayout()
        self.buttons_layout = QHBoxLayout()

        self.enter_new_location_layout.addWidget(self.get_location_name)

        self.buttons_layout.addWidget(self.enter_button)
        self.buttons_layout.addWidget(self.cancel_button)

        self.buttons_widget = QWidget()
        self.buttons_widget.setLayout(self.buttons_layout)

        self.enter_new_location_layout.addWidget(self.buttons_widget)

        self.enter_location_widget = QWidget()
        self.enter_location_widget.setLayout(self.enter_new_location_layout)

        self.enter_records_layout.addWidget(self.enter_location_widget)

        self.enter_button.clicked.connect(self.validate_entry)

    def validate_entry(self):
        self.location = self.get_location_name.text()

    def open_connection(self):
        path = QFileDialog.getOpenFileName()
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print("Database connection established: {0}".format(ok))
        self.products_menu.setEnabled(True)

    def printing(self):
        printing = Print()
        html = printing.statementHtml()
##        html += ("<h1> Hello this is a test print!</h1>"
##                 "<hr/><p style='font-family:times;color:red;'> {0} This is testing the print functionality"
##                 "of printing something in html from PyQt4.</p>").format(date)
        dialog = QPrintDialog(self.printer, self)
        if dialog.exec_():
            document = QTextDocument()
            document.setHtml(html)
            document.print_(self.printer)
        else:
            print("The print process has failed!")
        print(html)

        
def main_menu_main():
    application = QApplication(sys.argv)
    window = InsertRecord()
    window.show()
    window.raise_()
    application.exec_()

if __name__ == "__main__":
    main_menu_main()
