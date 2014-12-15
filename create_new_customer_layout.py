from added_record_dialog import *

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys
import pdb
import re

class NewCustomerWidget(QWidget):
    """docstring for NewCustomerWidgetQWidget"""
    def __init__(self):
        super().__init__()
        
        self.forename_label = QLabel("Forename")
        self.get_forename = QLineEdit()

        self.surname_label = QLabel("Surname")
        self.get_surname = QLineEdit()

        self.company_label = QLabel("Company")
        self.get_company = QLineEdit()

        self.address_label = QLabel("Address")
        self.get_address = QLineEdit()

        self.town_label = QLabel("Town")
        self.get_town = QLineEdit()

        self.post_code_label = QLabel("Post-Code")
        self.get_post_code = QLineEdit()

        self.mobile_label = QLabel("Mobile")
        self.get_mobile = QLineEdit()

        self.landline_label = QLabel("Landline")
        self.get_landline = QLineEdit()

        self.email_label = QLabel("Email")
        self.get_email = QLineEdit()


        self.new_customer_layout = QVBoxLayout()
        self.new_customer_layout.addWidget(self.forename_label)
        self.new_customer_layout.addWidget(self.get_forename)

        self.new_customer_layout.addWidget(self.surname_label)
        self.new_customer_layout.addWidget(self.get_surname)

        self.new_customer_layout.addWidget(self.company_label)
        self.new_customer_layout.addWidget(self.get_company)

        self.new_customer_layout.addWidget(self.address_label)
        self.new_customer_layout.addWidget(self.get_address)

        self.new_customer_layout.addWidget(self.town_label)
        self.new_customer_layout.addWidget(self.get_town)

        self.new_customer_layout.addWidget(self.post_code_label)
        self.new_customer_layout.addWidget(self.get_post_code)

        self.new_customer_layout.addWidget(self.mobile_label)
        self.new_customer_layout.addWidget(self.get_mobile)

        self.new_customer_layout.addWidget(self.landline_label)
        self.new_customer_layout.addWidget(self.get_landline)

        self.new_customer_layout.addWidget(self.email_label)
        self.new_customer_layout.addWidget(self.get_email)

        
        self.cancel_button = QPushButton("Cancel")
        self.confirm_button = QPushButton("Confirm")

        self.customer_buttons_layout = QHBoxLayout()
        self.customer_buttons_layout.addWidget(self.cancel_button)
        self.customer_buttons_layout.addWidget(self.confirm_button)

        self.customer_buttons_widget = QWidget()
        self.customer_buttons_widget.setLayout(self.customer_buttons_layout)

        self.new_customer_layout.addWidget(self.customer_buttons_widget)

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
                valid = False
                length_regex_validation = re.match('^[a-zA-Z]{1,2}[0-9]{1,2}([A-Z]|[a-z]|[A-Z][a-z])?\s[0-9][a-zA-Z][a-zA-Z]$', self)
                if length_regex_validation:
                    valid = True
                else:
                    valid = False
        else:
                valid_length = False
        if valid_length == True and length_regex_validation == True:
                print("Post-Code: {0}".format(self.post_code))
        else:
                self.error_dialog = EntryErrorDialog('a valid Post-Code')
                self.error_dialog.exec_()


        self.mobile = self.get_mobile.text()
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
                self.added_record_dialog = DisplayCreatedRecordDialog("Customer Record for {0} {1}".format(self.forename,self.surname))
                self.added_record_dialog.exec_()
        else:
                self.error_dialog = EntryErrorDialog('a valid Email Address')
                self.error_dialog.exec_()

        finished = False
        while not finished:
            self.stacked_layout.setCurrentIndex(3)