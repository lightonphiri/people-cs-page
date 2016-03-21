# Dikgang Thapelo
# Point Of Sale system
# 12 March 2016


# Importing necessary modules
import sys
from PyQt4 import QtGui,QtCore
import sqlite3
import datetime

# Connecting python and the database
db = sqlite3.connect('PointOfSaleDBMS.db')

# Creating a class named MainWidget
class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 460, 300)
        self.setWindowTitle('Online Shopping')        
        self.setPalette(QtGui.QPalette(QtGui.QColor('darkcyan')))
        self.setAutoFillBackground(True)      
        
        #Creating Labels
        self.title_label=QtGui.QLabel('SHOP ONLINE')
        self.title_label.setFont(QtGui.QFont('Times',20,2))        
        self.selectItem_label=QtGui.QLabel('Select item: ')
        self.quantity_label=QtGui.QLabel('Quantity: ') 
        self.record_label=QtGui.QLabel('Record: ')
        self.salesReport_label=QtGui.QLabel('Sales report: ')
        self.errorMessage=QtGui.QLabel() 
        
        # Creating a combo that has selective goods
        self.combo = QtGui.QComboBox()
        self.combo.addItem('Fresh tomatoes') 
        self.combo.addItem('Lettuce') 
        self.combo.addItem('White bread') 
        self.combo.addItem('Corn flakes') 
        self.combo.addItem('Dried pinto beans') 
        self.combo.addItem('Vanilla cake mix') 
        self.combo.addItem('Sliced turkey') 
        self.combo.addItem('Cheddar cheese') 
        self.combo.addItem('Chicken breasts') 
        self.combo.addItem('Vanilla ice cream') 
        self.combo.addItem('Grape fruit') 
        
        # Creating an edit box to get the good's quantity
        self.editbox=QtGui.QLineEdit()
        
        # Creating PushButtons
        self.ok_button=QtGui.QPushButton('Ok')
        self.display_button=QtGui.QPushButton('Display')
        self.close_button=QtGui.QPushButton('Close')    
        
        # Creating a grid layout
        self.grid=QtGui.QGridLayout()
        
        # Adding the widgets to the grid layout
        self.grid.addWidget(self.title_label,0,0)
        self.grid.addWidget(self.selectItem_label,1,0)
        self.grid.addWidget(self.quantity_label,2,0)
        self.grid.addWidget(self.record_label,3,0)
        self.grid.addWidget(self.salesReport_label,4,0)
        self.grid.addWidget(self.combo,1,1)
        self.grid.addWidget(self.editbox,2,1)
        self.grid.addWidget(self.ok_button,3,1)
        self.grid.addWidget(self.display_button,4,1)
        self.grid.addWidget(self.errorMessage,5,1)
        self.grid.addWidget(self.close_button,6,2)                
        self.setLayout(self.grid)
        
        # Event handling, connecting signals to their appropriate slots
        self.connect(self.close_button,QtCore.SIGNAL('clicked()'), self.closeButton)
        self.connect(self.ok_button,QtCore.SIGNAL('clicked()'),self.addItem)
        self.connect(self.display_button,QtCore.SIGNAL('clicked()'),self.display)       
        
    def closeButton(self):
        # Closing the window
        self.close()

    def addItem(self):
        # Updating the database based on the inputs 
        self.errorMessage.clear()
        self.text = self.combo.currentText()
        self.RequestedQuantity= self.editbox.displayText()
        self.cursor = db.execute('select * from Stock')
        
        for row in self.cursor:          
            if self.text in row:
                self.QuantityLeft=row[-2]
                self.code=row[1]
            else:
                pass                    
    
        if int(self.RequestedQuantity)>int(self.QuantityLeft):
            self.errorMessage=QtGui.QLabel('Sorry, only '+str(self.QuantityLeft)+' item(s) Left in stock.')
            self.grid.addWidget(self.errorMessage,5,1)
            
        else:
            now=str(datetime.datetime.now())           
            db.execute('insert into Sales values (?,?,?,?)',(int(self.code),int(self.RequestedQuantity),now[11:19],now[:10]))
            db.execute("update Stock set Quantity = ? where Name=?",((int(self.QuantityLeft)-int(self.RequestedQuantity)),self.text))

        self.editbox.clear()
        db.commit()
        
    def display(self):
        # Calling a pop-up window 
        self.dialog = MyPopupDialog()
        self.dialog.show()        

        
# Creating a class named MyPopupDialog
class MyPopupDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(620, 350, 300, 200)
        self.setWindowTitle('report')        
        self.setPalette(QtGui.QPalette(QtGui.QColor('lightgray')))
        self.setAutoFillBackground(True)                  
        
        # Joining necessary fields from Stock and Sales tables
        cursor=db.execute("SELECT Sales.Code,Sales.Quantity_Sold,Stock.Cost_Price,Stock.Sales_Price " + 
                        "FROM Sales " +
                        "JOIN stock "+
                        "on Sales.Code = Stock.Code")
        
        # Calculating total cost,total sales and total profit
        self.totalCost=0
        self.totalSales=0
        self.totalQuantity=0
        for row in cursor:
            self.totalCost+=int(row[2])*int(row[1])
            self.totalSales+=int(row[1]*int(row[3]))
            self.totalQuantity+=int(row[1])
            
        self.totalProfit=round(self.totalSales-self.totalCost,2)
          
        # Creating Labels   
        self.title_label=QtGui.QLabel('REPORT')
        self.title_label.setFont(QtGui.QFont('Times',20,2))        
        self.quantity_label=QtGui.QLabel('Items Sold:')
        self.cost_label=QtGui.QLabel('Total Cost:')
        self.sales_label=QtGui.QLabel('Total Sales:')
        self.profit_label=QtGui.QLabel('Total Profit:')
        self.close_PushButton=QtGui.QPushButton('Close')
        
        self.quantity=QtGui.QLabel(str(self.totalQuantity))
        self.cost=QtGui.QLabel('R '+str(round(self.totalCost,2)))
        self.sales=QtGui.QLabel('R '+str(round(self.totalSales,2)))
        self.profit=QtGui.QLabel('R '+str(round(self.totalProfit,2)))     
        
        # Creating a grid layout
        self.grid=QtGui.QGridLayout()
        
        # Adding widgets to the grid layout
        self.grid.addWidget(self.title_label,0,2)
        self.grid.addWidget(self.quantity_label,1,0)
        self.grid.addWidget(self.cost_label,2,0)
        self.grid.addWidget(self.sales_label,3,0)
        self.grid.addWidget(self.profit_label,4,0)
        self.grid.addWidget(self.quantity,1,2)
        self.grid.addWidget(self.cost,2,2)
        self.grid.addWidget(self.sales,3,2)
        self.grid.addWidget(self.profit,4,2)
        self.grid.addWidget(self.close_PushButton,5,3)
        
        self.setLayout(self.grid)
        db.commit()
        
        # Event handling, connecting a signal and a slot
        self.connect(self.close_PushButton,QtCore.SIGNAL('clicked()'), self.close_button)
        
    def close_button(self):
        self.close()
        
# Defining and calling the Mainwidget Class            
def main():
    app = QtGui.QApplication(sys.argv)
    My_widget = MainWidget()
    My_widget.show()
    sys.exit(app.exec_())

main()