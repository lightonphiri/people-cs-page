from PyQt4 import QtGui, QtCore
import random
import sys

class MyWidget(QtGui.QWidget): #Widget Class
    def __init__(self,parent= None): #Constructor
        QtGui.QWidget.__init__(self,parent)
        
        self.setGeometry(300,300,400,300)
        self.setWindowTitle("Guessing Game")
        #Widgets
        self.lblGuesses = QtGui.QLabel("Guesses",self)
        self.lblGuesses.setFont(QtGui.QFont('Courier',14,QtGui.QFont.Bold,False))
        self.lblGuess1 = QtGui.QLabel("Guess 1:",self) 
        self.lblGuess2 = QtGui.QLabel("Guess 2:",self) 
        self.lblGuess3 = QtGui.QLabel("Guess 3:",self)
        
        self.lblGuess_1 = QtGui.QLabel("",self)
        self.lblGuess_2 = QtGui.QLabel("",self)
        self.lblGuess_3 = QtGui.QLabel("",self)
        
        self.lblResult1 = QtGui.QLabel("",self)
        self.lblResult2 = QtGui.QLabel("",self)
        self.lblResult3 = QtGui.QLabel("",self)
    
        self.edtGuess = QtGui.QLineEdit()
        
        self.lblInterface = QtGui.QLabel("Interface:",self) 
        self.lblInterface.setFont(QtGui.QFont('Courier',14,QtGui.QFont.Bold,False))
        
        self.lblPicture = QtGui.QLabel("Picture:",self) 
        self.lblColor = QtGui.QLabel("Color:",self)
        
        self.btnGuess = QtGui.QPushButton("Guess",self)
        self.btnChange = QtGui.QPushButton("Change",self)
        self.btnClose = QtGui.QPushButton("Close",self)
        self.btnNewGame = QtGui.QPushButton("New Game",self)
        
        #Add Items to combobox
        self.cmbPicture = QtGui.QComboBox()
        self.cmbPicture.addItem("Mickey")
        self.cmbPicture.addItem("Pluto")
        
        self.cmbColor = QtGui.QComboBox()
        self.cmbColor.addItem("Red")
        self.cmbColor.addItem("Blue")
        
        
        self.lblImage = QtGui.QLabel(self)
        self.Image = QtGui.QPixmap("mickey.png") #Mickey as Default
        self.lblImage.setPixmap(QtGui.QPixmap(self.Image))
        self.lblImage.setGeometry(0,0,400,400)
        
        self.setPalette(QtGui.QPalette(QtGui.QColor('red'))) # red as Default
        self.setAutoFillBackground(True)
        
        self.theGrid = QtGui.QGridLayout()
        #Add Widgets into a Grid
        self.theGrid.addWidget(self.lblImage,0,0,9,2)
        self.theGrid.addWidget(self.lblGuesses,0,2) #widget,row,cloumn
        self.theGrid.addWidget(self.lblGuess1,1,2)
        self.theGrid.addWidget(self.lblGuess2,2,2)
        self.theGrid.addWidget(self.lblGuess3,3,2)
        
        self.theGrid.addWidget(self.edtGuess,4,3)
        
        self.theGrid.addWidget(self.lblGuess_1,1,3)
        self.theGrid.addWidget(self.lblGuess_2,2,3)
        self.theGrid.addWidget(self.lblGuess_3,3,3)
        
        self.theGrid.addWidget(self.lblResult1,1,4)
        self.theGrid.addWidget(self.lblResult2,2,4)
        self.theGrid.addWidget(self.lblResult3,3,4)
         
        self.theGrid.addWidget(self.lblInterface,5,2)
        self.theGrid.addWidget(self.lblPicture,6,2)
        self.theGrid.addWidget(self.lblColor,7,2)
        self.theGrid.addWidget(self.btnGuess,4,4)
        self.theGrid.addWidget(self.btnChange,7,4)
        self.theGrid.addWidget(self.btnClose,8,2)
        self.theGrid.addWidget(self.btnNewGame,8,3)
        self.theGrid.addWidget(self.cmbPicture,6,3)
        self.theGrid.addWidget(self.cmbColor,7,3)
        
        self.setLayout(self.theGrid)
        self.show()
        QtGui.QMessageBox.information(self,"Instructions","Enter the numbers in the edit as follows : \n a,b,c where a,b and c are your \n numbers separated by a comma")
        
        self.btnChange.clicked.connect(self.Change_Clicked)
        self.btnNewGame.clicked.connect(self.NewGame)        
        self.btnClose.clicked.connect(self.close_)
        self.btnGuess.clicked.connect(self.Guess)   
        
    def image_filepath(self):#Changes the image
        text = self.cmbPicture.currentText()
        if text == "Mickey":
            self.lblImage.setPixmap(QtGui.QPixmap("mickey.png"))
        elif text == "Pluto":
            self.lblImage.setPixmap(QtGui.QPixmap("pluto.png"))

    def background_color(self):#changes background color
        text = self.cmbColor.currentText()
        if text == "Blue":
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
        elif text == "Red":
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        
    def Change_Clicked(self):#Calls methods to change image and background color
        self.image_filepath()
        self.background_color()
            
    def NewGame(self):#Resets the game
        self.lblGuess_1.setText("")
        self.lblGuess_2.setText("")
        self.lblGuess_3.setText("")
        
        self.lblResult1.setText("")
        self.lblResult2.setText("")
        self.lblResult3.setText("")
            
        self.lblGuess_1.setText("")
        self.lblGuess_2.setText("")
        self.lblGuess_3.setText("")  
        self.edtGuess.setText("")
            
    def Guess(self): #Processes the guesses to check if they are Too Small/Correct or Too Large
        string = self.edtGuess.displayText()
        
        guess1 = ''
        guess2 = ''
        guess3 = ''
        
        #Split edit text into separate numbers:
        guess1 = string[0:string.index(',')]
    
        string = string[string.index(",")+1:len(string)]
        guess2 = string[0:string.index(',')]
        
        string = string[string.index(",")+1:len(string)]
        guess3 = string        
            
        
        guess1 = eval(guess1)
        guess2 = eval(guess2)
        guess3 = eval(guess3)
            
        #update guesses:
        self.lblGuess_1.setText(str(guess1))
        self.lblGuess_2.setText(str(guess2))
        self.lblGuess_3.setText(str(guess3))
        
        random_nr = random.randrange(11) #Generates random number from 0 to 9
        
        #evaluate guess 1:
        if guess1<random_nr:
            self.lblResult1.setText("Too small")
        elif guess1==random_nr:
            self.lblResult1.setText("Correct!")
        else:
            self.lblResult1.setText("Too Large")
                                
        #evaluate guess 2:
        if guess2<random_nr:
            self.lblResult2.setText("Too small")
        elif guess2==random_nr:
            self.lblResult2.setText("Correct!")
        elif guess2>random_nr:
            self.lblResult2.setText("Too Large")  
                
        #evaluate guess 3:
        if guess3<random_nr:
            self.lblResult3.setText("Too small")
        elif guess3==random_nr:
            self.lblResult3.setText("Correct!")
        elif guess3>random_nr:
            self.lblResult3.setText("Too Large")
                
    def close_(self):#Closes Application
        self.close()
                             
def main():
    app = QtGui.QApplication(sys.argv)
    widget = MyWidget()#Instance of MyWidget Class
    sys.exit(app.exec_())
    
main()
        
        
