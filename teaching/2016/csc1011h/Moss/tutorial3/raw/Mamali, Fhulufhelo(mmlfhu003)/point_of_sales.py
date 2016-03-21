import sqlite3
import sys
from PyQt4 import QtGui
import math
database1=sqlite3.connect("STOCK.db") # opeaning stock database
pen1=database1.cursor() # pen to write on the data stock base
database2=sqlite3.connect("SALe.db") # opeaning a sale data base
pen2=database2.cursor() #pen to write on the sale data
app=QtGui.QApplication(sys.argv)

from datetime import datetime 
class My_wid(QtGui.QWidget): # My_wid inherits from QtGui.QWidget
    
    def __init__(self,parent=None): 
        
        QtGui.QWidget.__init__(self,parent) # initialazing the QtGui.QWidget variable 
        pixmap = QtGui.QPixmap('f.jpg') # constructor
        pic_label = QtGui.QLabel(self) # QLabel to hold pixmap
        pic_label.setPixmap(pixmap)   # add pixmap to label
        self.setWindowTitle("UCT TUCK SHOP") # Main window Title
        self.setMaximumSize(600,400) # The maximum window size
        self.setMinimumSize(600,400) # The minimum window size
        self.setPalette(QtGui.QPalette(QtGui.QColor('yellow'))) # Background colour 
        self.setAutoFillBackground(True)
        self.edit=QtGui.QLineEdit(self) # Creating an edit box
        self.edit.setGeometry(100,150,200,30) # positioning and resizing the edit box
        ok=QtGui.QPushButton("OK",self) # Creating the Ok button
        cancel=QtGui.QPushButton("Close",self) # Modifying the window by creating close button
        cancel.clicked.connect(self.close)
        self.report=QtGui.QPushButton("Report",self)
        self.report.setGeometry(100,325,200,30)
        self.report.clicked.connect(self.Report) # Connecting the report button to the method called Report
        self.combo=QtGui.QComboBox(self)
        cancel.setGeometry(100,250,200,30)
        self.combo.setGeometry(350,150,200,30)
        """ADDING ITEMS INTO THE COMBO BOX"""
        self.combo.addItem("Rice")
        self.combo.addItem("Beef")
        self.combo.addItem("White Sugar")
        self.combo.addItem("Cooking oil")
        self.combo.addItem("Chicken pieces")
        self.combo.addItem("Apples")
        self.combo.addItem("Brown Sugar")
        self.combo.addItem("Onion")
        self.combo.addItem("Spinach")
        self.combo.addItem("Cabbage")
        #Positioning the ok box
        ok.setGeometry(350,250,200,30)
        message=QtGui.QLabel("Quantity",self)
        message.setFont(QtGui.QFont('Arial',15))
        message.move(0,150)
        ok.clicked.connect(self.check_stock)
        #Empty field to write Error message if the store is out of quantity 
        self.label=QtGui.QLabel("",self)
        self.label.setFont(QtGui.QFont('Arial',10))
        self.label.setGeometry(100,200,600,30)
        self.pixmap = QtGui.QPixmap('qw.jng')
        self.pic_label = QtGui.QLabel() 
        self.pic_label.setPixmap(self.pixmap) 
        
    #Closing the Window
    def close(self):
        pen1.close()
        pen2.close()            
        sys.exit()
    def Report(self):
        pen2.execute("SELECT * FROM sale") # highliting everything from sale table 
        pen1.execute("SELECT * FROM stock") # highliting everything from stock table 
        dat=pen1.fetchall() # Fetching all the items from the stock table
        data=pen2.fetchall() # Fetching all the items from sale table
        stock_code=[] # List to save the stock code
        total_number_of_items=0 # variable to save the number of items
        
        for i in data:
            total_number_of_items+=int(i[1]) # selecting the quantity from the stock table
            stock_code.append(i[0]) #  selecting the stock code from the stock table
        price=[] #list to save the total cost price
        price2=[] # list to save the total sale price
        for i in dat: # loo[ing throught the stock table
            if i[0] in stock_code: # if the stock code from stock table is also in sale table 
                price.append(i[3]) # Selecting the cost price from sale table and add it into the list
                price2.append(i[4]) # Adding the sale price from the sale table and add it into the list
        cost_price=0
        for i in price: #looping through cost price
            cost_price+=eval(i[1:])
        sale_price=0 # variable to save the total sale price
        for i in price2:
            sale_price+=eval(i[1:]) # Rmoving "R" and sum up the sale price
        profit=round((sale_price-cost_price),0)# calculating the profit
        self.pic_label.setPixmap(self.pixmap) 
        self.pic_label.resize(200,300)
        self.pic_label.setGeometry(200,200,200,300)
        """WRITING MY ANSWERS INTO MY REPORT"""
            
        Report_Heading=QtGui.QLabel("THE FINAL REPORT",self.pic_label)
        Report_Heading.setFont(QtGui.QFont('Arial',15))
        Report_Heading.move(50,0)
        profit="4. The profit=R"+str(profit)
        costprice="2. The cost Price is = R "+str(cost_price)
        saleprice="3. The Sale Price is = R "+str(sale_price)
        numberofitems="1. The total number of items sold= "+str(total_number_of_items)
        Items_field=QtGui.QLabel(numberofitems,self.pic_label)
        Items_field.move(0,40) 
        Items_field.setFont(QtGui.QFont('Arial',15))
        Cost_price_field=QtGui.QLabel(costprice,self.pic_label)
        Cost_price_field.setFont(QtGui.QFont('Arial',15))
        Cost_price_field.move(0,60)
        Sale_price_field=QtGui.QLabel(saleprice,self.pic_label)
        Sale_price_field.setFont(QtGui.QFont('Arial',15))
        Sale_price_field.move(0,80)
        Profit_field=QtGui.QLabel(profit,self.pic_label)
        Profit_field.setFont(QtGui.QFont('Arial',15))
        Profit_field.move(0,100)         
        self.pic_label.setMaximumSize(300,200)
        self.pic_label.setMinimumSize(350,200) 
        
        
        self.pic_label.setPalette(QtGui.QPalette(QtGui.QColor('magenta')))
        self.pic_label.setAutoFillBackground(True) 
        self.pic_label.setWindowTitle("Sale Report")
        self.pic_label.show()                 
    def check_stock(self):
        selection=self.combo.currentText() # Taking the Text from the combo box
        selection=self.combo.currentText() # collecting the number of items from the edit box
        quntity=self.edit.displayText()
        quntity=self.edit.displayText()
        pen1.execute('SELECT * FROM stock WHERE Name=?',(selection,)) # Highlighting everything from stock table        
        data=pen1.fetchone() # fetching only one row
        number=data[-1] # selecting the Quantity number from my row
        date= datetime.now() # Taking the current time at which the oblect was sold
        date_time=str(date)[0:-10]
        if int(number)>=int(quntity):
            self.label.clear()
            pen2.execute("INSERT INTO sale(Stock,Quantity,DateandTime) VaLUES(?,?,?)",(data[0],int(quntity),date_time)) # Recordind the stock code,date and time as well as the quantity number into sale table
            remain=int(number)-int(quntity) # Calculating the remaining Quantity
            pen1.execute("UPDATE stock SET Quantity=(?) WHERE Name=(?)",(remain,selection,)) # updating the Quantity number from the stock table
            print("Recorded")
            self.edit.clear()
        else:
            message=("SORRY WE HAVE INSUFFICIENT QUANTITY OF {}".format(selection.upper())) # Error message if there is insuficiant quantity
            self.label.setText(message)
            self.edit.clear()
            print("Not Recorded")
        database2.commit()
        database1.commit()
window=My_wid()
window.show()

sys.exit(app.exec_())
        