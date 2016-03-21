# Assignment 3
# ASMSAA002 - Saarah Asmal

import sys
from PyQt4 import QtGui, QtCore, QtSql
import sqlite3

class PopUp(QtGui.QWidget):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,450,250)
        self.setWindowTitle("Sale")
        
        l1 = QtGui.QLabel("Select item to be sold:")     # label to select item sold 
        combo = QtGui.QComboBox()
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        combo.addItem("")
        l2 =QtGui.QLabel("Quantity to be sold:")        # label to select quantity
        edit = QtGui.QLineEdit()                        # edit box to input quantity
        sales_rep = QtGui.QPushButton("Sales Report")   # button to bring up a window with sales report
        ok = QtGui.QPushButton("OK")                    # button to record sale input 
        close = QtGui.QPushButton("Close")              # button to close widget
        
        grid = QtGui.QGridLayout()                      # grid layout
        grid.addWidget(l1,0,0)
        grid.addWidget(combo,0,1)
        grid.addWidget(l2,1,0)
        grid.addWidget(edit,1,1)
        grid.addWidget(ok,2,0)
        grid.addWidget(sales_rep,2,2)
        grid.addWidget(close,2,1)
        
        self.setLayout(grid)
        
        # method to check quantity and display error message
        
        # method to add to database
        
        # method to close
        
app = QtGui.QApplication(sys.argv)
myWidget = PopUp()
myWidget.show()
sys.exit(app.exec_())