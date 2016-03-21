import sys 
import sqlite3
import time

from PyQt4 import QtGui,QtCore

class MyStore(QtGui.QWidget):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(90,150,350,150)
        #(1050,150,350,150)
        self.setWindowTitle("Mondlolo Super Market")
        self.setPalette(QtGui.QPalette(QtGui.QColor("Yellow")))

        
        '''Create Buttons'''
        ok = QtGui.QPushButton("OK")
        close = QtGui.QPushButton("Close")
        report = QtGui.QPushButton("Report")
        report.setMaximumSize(150,25)
       
        '''create labels'''
        errorLabel = QtGui.QLabel()
        heading = QtGui.QLabel("Sales Records Table")
        heading.setFont(QtGui.QFont('Times',20,2))
        selectItem = QtGui.QLabel("Select Item: ")
        enterQuantity = QtGui.QLabel("Enter Quantity: ")
        self.errorMessage = QtGui.QLabel("error message area!")
        #resultLabel = QtGui.QLabel("Select results to be displayed: ")
        
        '''Create Line edit'''
        
        self.selectQuantity = QtGui.QLineEdit()
        

        '''Create combo box'''
        self.stockCombo = QtGui.QComboBox()
        #self.resultCombo = QtGui.QComboBox()
    
        
        '''Add Items to the stock combo'''
        self.stockCombo.addItem("Tastic")
        self.stockCombo.addItem("Jive")
        self.stockCombo.addItem("Oreo")
        self.stockCombo.addItem("Bokomo")  
        self.stockCombo.addItem("King Korn")
        self.stockCombo.addItem("Amazimba")
        self.stockCombo.addItem("Inkomasi")
        self.stockCombo.addItem("Danoon")
        self.stockCombo.addItem("Amajoya")
        self.stockCombo.addItem("Simba")
        
        #'''Add Items to the stock combo'''
        #self.resultCombo.addItem("Tastic")
        #self.resultCombo.addItem("Jive")
        #self.resultCombo.addItem("Oreo")
        #self.resultCombo.addItem("Bokomo")  
        #self.resultCombo.addItem("King Korn")
        #self.resultCombo.addItem("Amazimba")
        #self.resultCombo.addItem("Inkomasi")
        #self.resultCombo.addItem("Danoon")
        #self.resultCombo.addItem("Amajoya")
        #self.resultCombo.addItem("Simba")        
    
        '''Create layout grid'''
        
        grid = QtGui.QGridLayout()
        
        '''Adding elements to the grid layout'''
        
        grid.addWidget(heading,0,0)
        grid.addWidget(selectItem,1,0)
        grid.addWidget(self.stockCombo,1,1)
        grid.addWidget(enterQuantity,2,0)
        grid.addWidget(self.selectQuantity,2,1)
    
        #grid.addWidget(resultLabel,3,0)
        
        grid.addWidget(report,4,1)
        grid.addWidget(close,4,2)
        #grid.addWidget(self.resultCombo,3,1)
        grid.addWidget(ok,2,2)
        
        self.selectKey = ""
        self.tryOut = ""
        self.currentDateTime =  time.strftime("%c")
        
        '''Set the layout of the window to grid'''
        self.setLayout(grid)
        
        '''Connections to buttons'''
        close.clicked.connect(self.closeButton)
        ok.clicked.connect(self.okButton)
        report.clicked.connect(self.reportButton)
        
        '''Access Data base'''
        self.stockData = sqlite3.connect("myexample.db")
        #self.stockCode = ""
        
    def closeButton(self):
        self.close()
        
    def okButton(self):
        
        self.tryOut = self.stockCombo.currentText()
        self.selectKey = self.stockData.execute("select quantityInStock from Stock where nameOfItem = '"+self.tryOut+"'")
         
        a = None
        code = None
        stockCode = None
        for i in self.selectKey:
            a = i[0]
             
            
        difference = (int(a)-int(self.selectQuantity.displayText()))
        frmTxt = int(self.selectQuantity.displayText())
        if a ==0:
            print(self.tryOut+" is Out of Stock.")
        elif difference >=0:
            b =(int(a)-int(self.selectQuantity.displayText()))
            self.stockData.execute("update Stock set quantityInStock ='"+str(b)+"' where nameOfItem = '"+self.tryOut+"'")
            stockCode = self.stockData.execute("select stockCode from Stock where nameOfItem = '"+self.tryOut+"'") #
            for k in stockCode:
                code = k[0]
              
            self.stockData.commit()
            self.stockData.execute("insert into Sales values(?,?,?)",(code,frmTxt,self.currentDateTime))
            self.stockData.commit()
            
           
        elif difference < 0:
            if a ==1:
                self.errorMessage.setText("There is only "+str(a)+" "+self.tryOut+" remainig in stock.")
            elif a>1:
                self.errorMessage.setText("There are "+str(a)+" "+self.tryOut+"s remainig in stock.")
            
                '''Create Pop Out Widget forerror'''
                
                errorWidget = QtGui.QWidget()
                errorWidget.setWindowTitle("Error Maessage")
                errorWidget.setGeometry(400,150,200,100)
                errorWidget.setPalette(QtGui.QPalette(QtGui.QColor("red")))
                
                '''Create grid layout'''
                grider = QtGui.QGridLayout()
                
                '''create labels'''
                errorLabel= QtGui.QLabel(self.errorMessage)
                
                grider.addWidget(self.errorMessage,0,0)
                errorWidget.setLayout(grider)
                
                errorWidget.show()
                sys.exit(errorWidget.exec_())            
                
        #print(code)

    def reportButton(self):
                tempSale = self.stockData.cursor() #execute("select*from Sales")
                tempStock = tempSale.execute("select*from Stock")
                tempStockData = tempStock.fetchall()
                tempSaleData = tempSale.execute("select*from Sales")
                #tempSaleData = tempSale.fetchall()
                #tempSale.cursor()
                profit = 0
                totalCp = 0
                totalSp = 0
                l =0
                totalItems = 0
                tempSaleData = tempSaleData.fetchall()
                k =0
                for i in tempSaleData:
                    totalItems =totalItems+i[1]
                    for k in tempStockData:
                        if i[0] == k[0]:
                            totalCp +=int(i[1])*k[3]
                            totalSp += int(i[1])*k[4]
                            profit += int(i[1])*(k[4]-k[3])
                    
                
                    
                #print("print total number of people = "+str(totalItems)+" ",tempStockData)
                #print(totalItems)
                #print(tempSaleData)
                #print(totalItems)
                #print(tempSaleData)
                #print(tempStockData)
                #print(l)
                #print(profit)
                #print(totalSp)
                
                
                '''Create Pop Out Widget for report'''
                
                reportWidget = QtGui.QWidget()
                reportWidget.setWindowTitle("Mondlolo Super Market Sales Report")
                reportWidget.setGeometry(400,150,300,200)
                reportWidget.setPalette(QtGui.QPalette(QtGui.QColor("green")))
                
                
                '''Create grid layout'''
                grid = QtGui.QGridLayout()
                
                """Push button for closing window"""
                clik = QtGui.QPushButton("Close")
                def clikButton():
                    reportWidget.close()
                
                '''create labels'''
                tabHeading = QtGui.QLabel("Sales Report")
                tabHeading.setFont(QtGui.QFont('Aerial',20,2))
                totSales = QtGui.QLabel("Total Sales Price: ")
                totCost = QtGui.QLabel("Total Cost Price")
                totQuantity = QtGui.QLabel("Total Number Of Items Sold: ")
                totProfit = QtGui.QLabel("Total Profit: ")
                
                sale_label = QtGui.QLabel()
                sale_label.setText("R"+str(totalSp))
                cost_label = QtGui.QLabel()
                cost_label.setText("R"+str(totalCp))
                quantity_label = QtGui.QLabel()
                quantity_label.setText(str(totalItems))
                profit_label =  QtGui.QLabel()
                profit_label.setText("R"+str(profit))
                
                grid.addWidget(tabHeading,0,0)
                grid.addWidget(totSales,1,0)
                grid.addWidget(totCost,2,0)
                grid.addWidget(totQuantity,3,0)
                grid.addWidget(totProfit,4,0)
                
                grid.addWidget(sale_label,1,1)
                grid.addWidget(cost_label,2,1)
                grid.addWidget(quantity_label,3,1)
                grid.addWidget(profit_label,4,1)
                grid.addWidget(clik,5,1)
                #grid.addWidget()
                #grid.addWidget()
                reportWidget.setLayout(grid)
                clik.clicked.connect(clikButton)
                
                reportWidget.show()
                sys.exit(reportWidget.exec_())
                
                
               
                        

def main():
        
    app = QtGui.QApplication(sys.argv)
    spaza = MyStore()
    spaza.show()
    sys.exit(app.exec_())
main()