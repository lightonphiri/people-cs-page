import sys
from PyQt4 import QtGui, QtCore
import sqlite3
import math

class stock(QtGui.QWidget):  #inheritance from Widget      
	def __init__(self, parent=None):		               
		QtGui.QWidget.__init__(self, parent)
		self.sales = 0
		#window dimensions
		self.setGeometry(250, 250, 600, 300) 
		font = QtGui.QFont('Arial',16,QtGui.QFont.Bold,True)
		font2 = QtGui.QFont('Arial',12,QtGui.QFont.Bold,True)

		self.setWindowTitle('Sales') 
	
#code for the labels and pictures in the parent widget
		self.pic_label = QtGui.QLabel()
		self.pic_label.setPixmap(QtGui.QPixmap("clothes-swapping.jpg"))
	
		self.name_label = QtGui.QLabel('AFFORDABLE SPARLIES')
		self.name_label.setFont(font) 
		
		self.select_item_label = QtGui.QLabel('Select Product:')
		self.select_item_label.setStyleSheet('color:cyan')
		self.select_item_label.setFont(font2) 
		self.quantity_label = QtGui.QLabel('Quantity:')
		self.quantity_label.setStyleSheet('color:cyan')
		self.quantity_label.setFont(font2) 
		
		self.products_combo = QtGui.QComboBox()
		self.products_combo.addItem('')
		self.quantity_edit = QtGui.QLineEdit()
		self.quantity_edit.setFixedWidth(60)		
		#add products to the combo box from sql table
		
		self.ok_button = QtGui.QPushButton("OK")
		self.cancel_button = QtGui.QPushButton("Close")
		self.sales_button = QtGui.QPushButton("SALES REPORT")
		
		
		#data base connection
		db = sqlite3.connect('sparlies.db')
		cursor = db.execute('select * from stock')
		for row in cursor:
			self.products_combo.addItem(row[1])
		
		grid = QtGui.QGridLayout()
		grid.addWidget(self.pic_label,1,0,6,6)		
		
		grid.addWidget(self.name_label,0,0)
		grid.addWidget(self.select_item_label,2,1)
		grid.addWidget(self.products_combo,2,2,1,4)
		grid.addWidget(self.quantity_label,3,1)
		grid.addWidget(self.quantity_edit,3,2)
		grid.addWidget(self.ok_button,4,1)
		grid.addWidget(self.cancel_button,4,2)
		grid.addWidget(self.sales_button,5,4)
		
		
		self.setLayout(grid)
		
		self.connect(self.ok_button,QtCore.SIGNAL('clicked()'), self.okClicked)
		self.connect(self.cancel_button,QtCore.SIGNAL('clicked()'), self.cancelClicked)
		self.connect(self.sales_button,QtCore.SIGNAL('clicked()'), self.SRClicked)
		
	def okClicked(self):
		db = sqlite3.connect('sparlies.db')
		currentproduct= self.products_combo.currentText()
		currentquantity= int(self.quantity_edit.displayText())
		qury = db.execute("select quantity_in_stock from stock where name_of_item = ?", (currentproduct,));
		for row in qury:
			q = row[0]
		if currentquantity > q:
			print ("Sorry,stock is less than that!")
		
		else: 
			q = q - currentquantity
			print(q)
			db.execute("update stock set quantity_in_stock = ? where name_of_item = ?", (q,currentproduct))
			print("number of changes",db.total_changes)
			print("its good")
		db.close()	
			
	def cancelClicked(self):
		self.close()
		
	def SRClicked(self):
		self.window= salesWindow()
		self.window.show()
		
		
class salesWindow(QtGui.QWidget):  #inheritance from Widget    
	def __init__(self, parent=None):		               
		QtGui.QWidget.__init__(self, parent)
		self.setGeometry(250, 250, 400, 300) 
		self.setWindowTitle('Sales_Report') 		

		

		
#method to ensure app run successfully
def main():
	app = QtGui.QApplication(sys.argv)
	my_widget = stock()
	my_widget.show()
	sys.exit(app.exec_())

main()		
		
		
		
		
		
			
			
			
	
	
	


		
		

