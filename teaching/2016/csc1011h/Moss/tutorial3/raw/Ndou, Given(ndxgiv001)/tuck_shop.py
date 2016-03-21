import sys
from PyQt4 import QtGui,QtCore
import sqlite3
from datetime import datetime
db = sqlite3.connect('stock.db')
c = db.cursor()

class tuck_shop(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(300,300,300,300)
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))  # set the background colour of the window
        self.setAutoFillBackground(True)
        self.setWindowTitle("Given's tuck shop")  # title window
        self.close_button =QtGui.QPushButton("Quit")
        self.button = QtGui.QPushButton("Ok")
        self.report_button =QtGui.QPushButton("Report")
        self.name_of_item = QtGui.QLabel("Name of Item:")
        self.name_of_quantity = QtGui.QLabel("Enter Quantity:")
        self.label1 = QtGui.QLabel("") # this is a default for printing selected item from the combo box
        self.label2 = QtGui.QLabel("")  # this is the default for values entered by the user
        self.combo = QtGui.QComboBox()  # creating a combo box
        self.combo.addItem("Fish")
        self.combo.addItem("Beans")
        self.combo.addItem("milk")
        self.combo.addItem("sugar")             # adding widgets to the combo box
        self.combo.addItem("salt")
        self.combo.addItem("bread")
        self.combo.addItem("cool drink")
        self.combo.addItem("snacks")
        self.combo.addItem("rice")
        self.combo.addItem("sweets")
        self.amount_entered = "0" # default empty value
        self.text = self.combo.currentText() # accumulates the selected text
        self.edit = QtGui.QLineEdit()
        self.grid = QtGui.QGridLayout()
        self.grid.addWidget(self.name_of_item,0,0)
        self.grid.addWidget(self.combo,0,1)
        self.grid.addWidget(self.name_of_quantity,1,0)
        self.grid.addWidget(self.edit,1,1)
        self.grid.addWidget(self.button,1,2)
        self.grid.addWidget(self.label1,2,0)                 # setting a layout in a gridlayout
        self.grid.addWidget(self.label2,2,1)
        self.grid.addWidget(self.close_button,3,2)
        self.grid.addWidget(self.report_button,3,0)
        self.setLayout(self.grid)
        
        self.button.clicked.connect(self.get_current_text)   # connecting slots and signals of a particular button to a specified function
        self.button.clicked.connect(self.get_entry)
        self.button.clicked.connect(self.go_check_database)
        self.close_button.clicked.connect(self.close_window)
        self.report_button.clicked.connect(self.get_report)
        
        self.grid_2 = QtGui.QGridLayout()                       # the second layout for the report window
        self.number_of_items_sold = QtGui.QLabel("Total number of items sold:")
        self.total_cost_price = QtGui.QLabel("")
        self.total_sales_price = QtGui.QLabel("")
        self.total_profit = QtGui.QLabel("")
        self.value_entry = QtGui.QLabel("")
        self.value_total_cost_price =QtGui.QLabel("")
        self.value_total_sales_price = QtGui.QLabel("")
        self.value_total_profit = QtGui.QLabel("")
        self.grid_2.addWidget(self.number_of_items_sold,0,0)
        self.grid_2.addWidget(self.total_cost_price,1,0)
        self.grid_2.addWidget(self.total_sales_price,2,0)            #adding the widgets to the window
        self.grid_2.addWidget(self.total_profit,3,0)
        self.grid_2.addWidget(self.value_entry,0,1)
        self.grid_2.addWidget(self.value_total_cost_price,1,1)
        self.grid_2.addWidget(self.value_total_sales_price,2,1)
        self.grid_2.addWidget(self.value_total_profit,3,1)
        self.a = QtGui.QWidget()
        self.a.setPalette(QtGui.QPalette(QtGui.QColor('green')))
        self.a.setAutoFillBackground(True)         
        self.a.setLayout(self.grid_2)
        self.value_total= 0           # initialised values
        self.value_total2=0
        self.value_total3=0
        self.get_total_sales_price2=0
     
    def get_current_text(self):
        self.value_taken = self.combo.currentText()   #this variable takes the quantity entered by the user
        self.value_total2+=1                          # this sums the number of items clicked
        self.value_taken = self.value_taken.split(' ')
        
    def get_entry(self):
        x=self.combo.currentText() # takes the combobox selected item
        self.user_entry = self.edit.text()  #takes the quantity of the item taken by the user
        self.user_entry = int(self.user_entry)   # casting a string to an integer
        c.execute('SELECT cost_price FROM stock WHERE name_of_item=?',(x,))   # cost of the price of the item and quantity selected  by the user from a database
        costprice = c.fetchone()[0] # store into a variable
        self.value_total = self.value_total+costprice  # sum up all of them before display when the report button is clicked
        self.get_total_cost_price = float(self.user_entry)*float(costprice)  #total cost price of quantities entered
        self.value_total3+=self.get_total_cost_price            #sum up
        self.value_total_cost_price.setText(str(self.value_total3))   #set the text to the grid layout
        c.execute('SELECT sales_price FROM stock WHERE name_of_item=?',(x,))    # takes the sales price of the item from the database
        salesprice = c.fetchone()[0]
        self.get_total_sales_price = float(self.user_entry)*float(salesprice)    # total sales of the quantity
        self.get_total_sales_price2+=self.get_total_sales_price
        self.value_total_sales_price.setText(str(self.get_total_sales_price2))
        self.get_total_profit = float(self.get_total_sales_price2) - self.value_total3     # addition of the sales price of all items selected by the user
        self.value_total_profit.setText(str(self.get_total_profit))      # profit mae after selling the items  
        
    def close_window(self):            # closes the window when the close button is pressed
        self.close()
        
    def go_check_database(self):    # in general the function takes the item sold and write them to the table in the database and also check if the purchase stock is sufficient or not
        
        x=self.combo.currentText() 
        c.execute('SELECT quantity_in_stock FROM stock WHERE name_of_item=?',(x,))
        value=c.fetchone()[0]
        a = (int(value) - int(self.user_entry))   # variable for getting the remaining values after a purchase
        if int(value) - int(self.user_entry) < 0:
            self.label2.setText('we have insufficient stock')
        else:
            c.execute('SELECT stock_code FROM stock WHERE name_of_item=?',(x,))     #this takes the stock code of the item
            stock_number = c.fetchone()[0]
            purchase_time = datetime.now()
            c.execute('INSERT into sales values(?,?,?,?)',(stock_number,x,self.user_entry,purchase_time))
            db.commit()
            z= [(a,x,)]
            c.executemany('update stock set quantity_in_stock =? where name_of_item=?',z)
            db.commit()
            
    def get_report(self):
        self.total_cost_price.setText("Total cost price:")
        self.total_sales_price.setText("Total sales price:")            # the function deals with setting the layout to the report window and poping up the report window when the report button is pressed
        self.total_profit.setText("Total profit:")
        self.user_entry = str(self.user_entry)
        self.value_entry.setText(str(self.value_total2))        
        self.a.show()
        
def main():
    app = QtGui.QApplication(sys.argv)
    call_tuck_shop = tuck_shop()
    call_tuck_shop.show()
    sys.exit(app.exec_())
main()
        
        
        
    