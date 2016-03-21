import sqlite3
import sys
from PyQt4 import QtGui
import datetime

class MyPOS(QtGui.QWidget):
    def __init__(self, parent=None):  	
        QtGui.QWidget.__init__(self, parent)	        # create window
        self.setGeometry(300, 300, 200, 150)       	
        self.setWindowTitle('Point of Sale (POS)')
        self.db = sqlite3.connect('POSsystem.db')
        
        
        self.title_label = QtGui.QLabel('POINT OF SALE',self)
        self.title_label.setFont(QtGui.QFont('Times',24,3))     # change the font of the title
        self.items_label = QtGui.QLabel('Items:',self)
        self.items_label.setFont(QtGui.QFont('Arial',12,2))      # change the label font
        self.quantity_label = QtGui.QLabel('Quantity:',self)
        self.quantity_label.setFont(QtGui.QFont('Arial',12,2))   
        self.item_edit = QtGui.QLineEdit(self)                      # open line edit
        self.ok_button = QtGui.QPushButton("OK",self)
        self.ok_button.clicked.connect(self.ok_buttonFX)            # connect ok button to ok_buttonFX function
        self.stock_report_button = QtGui.QPushButton("Stock Report",self)
        self.stock_report_button.clicked.connect(self.stock_button)  # connect stock_report_button to stock_report function
        self.close_button = QtGui.QPushButton("Close",self)
        self.close_button.clicked.connect(self.close)            # connect close_button to close function
        self.stock_report = QtGui.QLabel("(Press the stock report button to view sales report.)",self)
        
        self.items_combo = QtGui.QComboBox(self)     # open comboBox for items and add all items using add method
        self.items_combo.addItem('Select item')
        self.items_combo.addItem('Laundry bag')
        self.items_combo.addItem('Laundry busket')
        self.items_combo.addItem('Shower cap') 
        self.items_combo.addItem('Showering slippers') 
        self.items_combo.addItem('Bath Towel') 
        self.items_combo.addItem('Face Towel') 
        self.items_combo.addItem('Body scrubbing gloves') 
        self.items_combo.addItem('Hand towel') 
        self.items_combo.addItem('Scrubbing body lotion')
        self.items_combo.addItem('Bath oil') 
        self.item_text = self.items_combo.currentText() # set currentText from comboBox
        
        self.setPalette(QtGui.QPalette(QtGui.QColor('pink'))) #set colour
        self.pixmap = QtGui.QPixmap("toiletries.jpg")
        self.pic_label = QtGui.QLabel(self)                          
        self.pic_label.setPixmap(self.pixmap)            
        
        grid = QtGui.QGridLayout()               # set grid
        grid.addWidget(self.title_label,0,0,1,2)
        grid.addWidget(self.items_combo,1,2)
        grid.addWidget(self.pic_label,4,2)
        grid.addWidget(self.items_label,1,0)
        grid.addWidget(self.quantity_label,2,0)
        grid.addWidget(self.item_edit,2,1)
        grid.addWidget(self.ok_button,2,2)
        grid.addWidget(self.stock_report_button,3,0)
        grid.addWidget(self.stock_report,5,0,8,2)
        grid.addWidget(self.close_button,8,2)
        self.setLayout(grid)                            
         
    def close(self):                                   
        sys.exit()
        
    def ok_buttonFX(self):
        self.db = sqlite3.connect('POSsystem.db')    # connect to sqlite3 to get database
        self.cur = self.db.cursor()            
        self.quantity = self.item_edit.displayText()    # get quantity from the user
        self.item_text = self.items_combo.currentText()  # take item currently clicked in the comboBox 
        self.column = self.cur.execute("select* from Stock where ItemName = ?",(self.item_text,)); # select everything in the colunm corresponding to the given item
        self.id_exists = self.column.fetchone() # fetchone column from the table stock       
        self.column = list(self.id_exists)  # change the tuple to a list
        self.db.commit()       # commit
        
        if int(self.quantity) > self.column[5]: # compare the quantity given by user with the quantity from Stock if its greater than
            self.message = QtGui.QMessageBox.information(self,'Point of Sale (POS)',"Available stock is less than the quantity you want.",QtGui.QMessageBox.Cancel) # pop up message error
            if self.message == QtGui.QMessageBox.Cancel:
                pass
            
        elif int(self.quantity) <= self.column[5]:  # if less or equal to available stock. do the purchasing method
            self.t = datetime.date.today()
            self.today = str(self.t)
            self.ti = datetime.datetime.time(datetime.datetime.now())
            self.time = str(self.ti)
            self.db.execute("insert into Sales values (?,?,?,?)",(self.column[0],int(self.quantity),self.today,self.time)); # insert into table the information needed
            self.db.commit()
            self.items_left = self.column[5] - int(self.quantity)
            self.db.execute("update Stock set InStock = ? where StockCode = ?",(self.items_left,self.column[0])); # update the stock table in the quantity
            self.db.commit()  
            
        else:
            self.column[5] <= 0 # if quantity in Stock is less or equal 0
            self.message1 = QtGui.QMessageBox.information(self,'Point of Sale (POS)',"This item is out of stock.",QtGui.QMessageBox.Cancel) # pop up message error
            if self.message1 == QtGui.QMessageBox.Cancel:
                pass
        self.db.close()
        
    def stock_button(self):
        self.db = sqlite3.connect('POSsystem.db')
        self.cur = self.db.cursor()            
        self.cost_price = self.cur.execute('select sum(CostPrice) from Stock'); # calculate sum in sqlite
        self.cp = self.cost_price.fetchone() # fetchone column of the sum
        self.cp1 = list(self.cp)
        self.db.commit()
        
        self.sales_price = self.cur.execute('select sum(SalesPrice) from Stock');
        self.sp = self.sales_price.fetchone()
        self.sp1 = list(self.sp)
        self.db.commit()
        
        self.in_stock = self.cur.execute('select sum(InStock) from Stock');
        self.ins = self.in_stock.fetchone()
        self.ins1 = list(self.ins)
        self.db.commit()
        
        self.quantity_sold = self.cur.execute('select sum(QuantitySold) from Sales');
        self.qs = self.quantity_sold.fetchone()
        self.qs1 = list(self.qs)
        self.db.commit()
        self.db.close()
       
        myWidget = QtGui.QWidget()                                        # creating my own wimdow for sales report
        myWidget.setGeometry(400, 400, 200, 150)       	
        myWidget.setWindowTitle('Sales Report')
        myWidget.report_label = QtGui.QLabel('SALES REPORT',myWidget)
        myWidget.report_label.setFont(QtGui.QFont('Times',18))                      
        myWidget.total_items_sold_label = QtGui.QLabel('Total number of items sold:',myWidget)
        myWidget.total_items_sold_label.setFont(QtGui.QFont('Arial',10,2))
        myWidget.total_cost_price_label = QtGui.QLabel('Total cost price:',myWidget)
        myWidget.total_cost_price_label.setFont(QtGui.QFont('Arial',10,2))
        myWidget.total_sales_price_label = QtGui.QLabel('Total sales price:',myWidget)
        myWidget.total_sales_price_label.setFont(QtGui.QFont('Arial',10,2))
        myWidget.total_profit_label = QtGui.QLabel('Total profit made:',myWidget)
        myWidget.total_profit_label.setFont(QtGui.QFont('Arial',10,2))
        myWidget.label1 = QtGui.QLabel('')
        myWidget.label2 = QtGui.QLabel('')
        myWidget.label3 = QtGui.QLabel('')
        myWidget.label4 = QtGui.QLabel('')
        
        self.total_items_sold = self.qs1[0]
        myWidget.label1.setText(str(self.total_items_sold))
        self.total_cost_price = round(self.cp1[0],0)
        myWidget.label2.setText('R'+ str(self.total_cost_price))
        self.total_sales_price = round(self.sp1[0],0)
        myWidget.label3.setText('R'+ str(self.total_sales_price))
        self.total_profit = round(self.sp1[0],0) - round(self.cp1[0],0)
        myWidget.label4.setText('R'+ str(self.total_profit))        
    
        grid = QtGui.QGridLayout()
        grid.addWidget(myWidget.report_label,0,0,1,1)
        grid.addWidget(myWidget.total_items_sold_label,1,0)
        grid.addWidget(myWidget.total_cost_price_label,2,0)
        grid.addWidget(myWidget.total_sales_price_label,3,0)
        grid.addWidget(myWidget.total_profit_label,4,0)
        grid.addWidget(myWidget.label1,1,1)
        grid.addWidget(myWidget.label2,2,1)
        grid.addWidget(myWidget.label3,3,1)
        grid.addWidget(myWidget.label4,4,1)
        myWidget.setLayout(grid)
        
        myWidget.show()
        sys.exit(app.exec_())
                                
def main():
    app = QtGui.QApplication(sys.argv)
    abs_widget = MyPOS()
    abs_widget.show()
    sys.exit(app.exec_())

main()
