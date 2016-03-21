# Malebo Mahoko
# 11 March 2016
# create tables of stock and sales for a small tuck shop

"""importing all necessary modules to be used"""
import sqlite3
import sys
from PyQt4 import QtGui, QtCore
from datetime import date, datetime

""" class for creating a popup window with sales details """
class Popup(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(500,300,300,150)
        self.setWindowTitle("Sales")
        
        """ labels to appear on the popup window"""
        self.total_items_sold = QtGui.QLabel("Items sold: ")
        self.total_cost = QtGui.QLabel("Total cost price: ")
        self.total_sales = QtGui.QLabel("Total sales price: ")
        self.total_profit = QtGui.QLabel("Total profit: ")
        
        """ cerating empty label space """
        self.emptyLabel1 = QtGui.QLabel('')
        self.emptyLabel2 = QtGui.QLabel('')
        self.emptyLabel3 = QtGui.QLabel('')
        self.emptyLabel4 = QtGui.QLabel('')        
        
        """ placing my objects (labels) on the window"""
        self.grid = QtGui.QGridLayout(self)
        self.grid.addWidget(self.total_sales,0,0)
        self.grid.addWidget(self.total_cost,1,0)
        self.grid.addWidget(self.total_items_sold,2,0)
        self.grid.addWidget(self.total_profit,3,0)
        
        """ placing empty spaces on popup window """
        self.grid.addWidget(self.emptyLabel1,0,1)
        self.grid.addWidget(self.emptyLabel2,1,1)
        self.grid.addWidget(self.emptyLabel3,2,1)
        self.grid.addWidget(self.emptyLabel4,3,1)

""" main window where interaction with user will take place """
class StockSales(QtGui.QWidget):
    
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent= None)
        self.setGeometry(250, 250, 300, 200)
        self.setWindowTitle("Quard's Shop")
        
        self.choiceBox = QtGui.QComboBox(self)                          
        """ combo box and items to choose from """
        self.choiceBox.addItem("Pie")
        self.choiceBox.addItem("Coke")
        self.choiceBox.addItem("Lays")
        self.choiceBox.addItem("Tennis Biscuit")
        self.choiceBox.addItem("Romany Creams")
        self.choiceBox.addItem("Dairy Milk")
        self.choiceBox.addItem("Maynards")
        self.choiceBox.addItem("Doritos")
        self.choiceBox.addItem("Tropica")
        self.choiceBox.addItem("Jumping Jack")
        
        self.edit = QtGui.QLineEdit(self)                                           # creating a line edit  
        
        self.ok = QtGui.QPushButton("Ok")                                            # ok push button the =n connecting it to a method           
        self.connect(self.ok,QtCore.SIGNAL('clicked()'), self.okClicked)
        
        self.sales_report = QtGui.QPushButton("Sales Report")                        # sales report button and connection to its method   
        self.connect(self.sales_report,QtCore.SIGNAL('clicked()'), self.salesClicked)
        
        self.close_button = QtGui.QPushButton("Close")                               # close button and connection to its method
        self.connect(self.close_button,QtCore.SIGNAL('clicked()'), self.closeClicked)

        """ making my layout to be grid and adding all my widgets to it """               
        self.grid = QtGui.QGridLayout(self)	
        self.grid.addWidget(self.choiceBox,0,0)
        self.grid.addWidget(self.edit,0,1)
        self.grid.addWidget(self.ok,1,0)
        self.grid.addWidget(self.close_button,1,1)
        self.grid.addWidget(self.sales_report,1,2)

        """ count varianles in order to sum costs,sales and items sold"""
        self.cost = 0
        self.sales = 0
        self.items_sold = 0
        
        """ creating my databases with the stock and sales table """
        #def CreateTable():
            #stock_var = sqlite3.connect("stock_table.db")
            #sales_var = sqlite3.connect("sales_table.db")
            #stock_var.execute("create table if not exists Stock (StockCode int, Name text, Description text, Cost real, Sales real, Quantity int)")
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (2161, "Pie", "Unique and health especially in combination with a coke", 13,15, 25))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (4162, "Coke", "Its the real thing, taste the feeling", 7,9, 48))   
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (6163, "Lays", "125g Cruchy taste", 15,17, 48))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (8164, "Tennis Biscuit", " Original ", 18,22, 12))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (10165, "Romany Creams", " Mint flavoured", 19,22, 18))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (12166, "Dairy Milk", "Biscuit flavoured bar", 10,14, 12))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (14167, "Maynards", "Wine gums flavoured, sweets", 5,9, 24))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (16168, "Doritos", " 125g Snacks", 15,17, 96))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (18169, "Tropica", " 100% fruit juice", 9,11, 12))
            #stock_var.execute("insert into Stock values (?,?,?,?,?,?)", (201610, "Jumping Jack", "Pop corns", 12,16.5, 48))
            #sales_var.execute("create table if not exists Sales (StockCode int, ItemSold text, Quantity int, Date text, Time text)")   
            #stock_var.commit()
            #sales_var.commit()
        #CreateTable()
            

    def okClicked(self):                        # method connected with the ok button

        stock_var = sqlite3.connect("stock_table.db")       # connecting stock table and storing in a variable
        stock_var.commit()
        
        sales_var = sqlite3.connect("sales_table.db")           # connecting sles table then storing in a variable
        sales_var.commit()

        
        self.text = self.edit.displayText()                     # getting the input(number of items to buy) from the user
        self.text_combo = self.choiceBox.currentText()                  # getting the current combo text    
        
        """ if statement to ensure that something has been entered on the edit line"""
        if self.text == '':
            print("Please enter number of items to purchase...")
        
        self.edit.clear()            # clearing the edit line after ok is clicked
        
        quantity = stock_var.execute("select Quantity from stock where Name = ('"+self.text_combo+"')")  # getting the quantity as a cursor

        for row in quantity:                    # looping through the cursor in order to get the real value
            m = row[0]
            
        if m < int(self.text):                  # if the quantity obtained from table is less than the one entered 
            print("Apparently we have insufficient quantity",self.text_combo+"!")
            
        elif m >= int(self.text):               # if quantity obtained from table is greater than the one entered
            
            sales_var = sqlite3.connect("Sales_table.db")           #connecting
            
            """ summing up number of items sold"""
            self.items_sold += int(self.text)            
            
            date_time = datetime.now()                      # using datetime method to get current date and time
            current_time = str(date_time)[11:19]            # slicing current date time to get time only
            current_date = str(date_time)[:11]              # slicing current date time to get date only
            
            stock_code = stock_var.execute("select StockCode from stock where Name = ('"+self.text_combo+"')")              # getting stock code as cursor from table
            
            for row in stock_code:          #looping through cursor to get the real stock code for item
                code_tup = row[0]
            
            """ inserting stock code, name of item, number of item bought, current date and cuurent time on sales table """
            sales_var.execute("insert into Sales values (?,?,?,?,?)", (str(code_tup),self.text_combo,int(self.text),str(current_date),str(current_time)))
            
            update_quantity = int(m) - int(self.text)     # updated number of items
            
            stock_var.execute("update stock set Quantity = '"+str(update_quantity)+"' where Name = ('"+self.text_combo+"') ")           # updating quantity on stock table
            
            """ getting cost for each and every item sold"""
            cost_item = stock_var.execute("select    Cost from stock where Name = ('"+self.text_combo+"')")                 # getting cost from table as cursor
            
            for row in cost_item:               # looping through cursor to get cost as real value
                cost = row[0]

                
            cost_for_each_item = int(self.text) * int(cost)
            self.cost += cost_for_each_item            # summing costs for each item
            
            """getting sales for each and every item sold"""
            
            sales_item = stock_var.execute("select Sales from stock where Name = ('"+self.text_combo+"')")              # getting sales as cursor
            
            for item in sales_item:             # looping thrugh sales cursor to get sales as real value
                sale = item[0]
                
            sales_for_each_item = int(self.text) * int(sale)    
            self.sales += sales_for_each_item                           # summing sales for each purchase made
            
            self.profit = self.sales - self.cost                # calculating the profit for each purchase made
            
            stock_var.commit()
            sales_var.commit()
            """ if quantity from table is less than number of items entered get into this statement"""
        else:
            print("We out of stock!")   
            
    def salesClicked(self):      # when sales button clicked 
        self.dialog = Popup()           # assign object self.dialog to class popup
        
        """ printing sales,costs, item sold and profit on popup window where theres empty labels"""
        self.dialog.emptyLabel1.setText("R"+str(self.sales))
        self.dialog.emptyLabel2.setText("R"+str(self.cost))
        self.dialog.emptyLabel3.setText(str(self.items_sold))
        self.dialog.emptyLabel4.setText("R"+str(self.profit))
        self.dialog.show()
        
             
    def closeClicked(self):
        sys.exit()

def main():
    app = QtGui.QApplication(sys.argv)
    shop = StockSales()
    shop.show()
    sys.exit(app.exec_())
    
main()



