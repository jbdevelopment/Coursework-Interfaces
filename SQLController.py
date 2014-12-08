try:
    from PyQt4.QtCore import *
    from PyQt4.QtGui import *
    from PyQt4.QtSql import *
except:
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from PyQt5.QtSql import *


import sys
import sqlite3

class SQLConnection():

    def __init__(self,path):
        self.path = path
        self.db = None

    def open_database(self):
        if self.db:
            self.close_database()
            
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(self.path )
        opened_ok = self.db.open()
        return opened_ok

    def close_database(self):
        self.db.close()
        QSqlDatabase.removeDatabase("conn")

    def closeEvent(self,event):
        """closes the database if a close event occures -
           such as close window/quit application"""
        self.close_database()
    
    def find_products_by_number(self,values):
        query = QSqlQuery()
        query.prepare("SELECT * FROM Products WHERE ProductID = ?")
        query.addBindValue(values[0])
        query.exec_()
        return query
