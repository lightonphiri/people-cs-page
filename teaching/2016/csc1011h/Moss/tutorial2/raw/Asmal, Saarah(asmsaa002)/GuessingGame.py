# Question 1 - Assignment 2
# ASMSAA002 - Saarah Asmal

import random # imports standard Python random module 
import sys # imports standard Python sys module
from PyQt4 import QtGui, QtCore # imports PyQt4 QtGui module
from RandomGameClass import RandomGameClass

class GuessingGame(QtGui.QWidget):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(200,200,600,300)
        self.setWindowTitle("Guessing Game")
        
        # Labels
        L1 = QtGui.QLabel("Guesses:")
        L1.setFont(QtGui.QFont("Arial",25,2)) # resizing Guesses label
        L2 = QtGui.QLabel("Guess 1:") 
        L3 = QtGui.QLabel("Guess 2:")
        L4 = QtGui.QLabel("Guess 3:")
        L5 = QtGui.QLabel("Interface:")
        L5.setFont(QtGui.QFont("Arial",25,2)) # resizing Interface label
        L6 = QtGui.QLabel("Picture:") 
        L7 = QtGui.QLabel("Colour:")
        pic_label = QtGui.QLabel() # blank label for picture
        
        # (6 more labels; 3 for actual guesses and 3 for comments; too big, too small, correct)
        L8 = QtGui.QLabel()
        L9 = QtGui.QLabel()
        L10 = QtGui.QLabel()
        L11 = QtGui.QLabel()
        L12 = QtGui.QLabel()
        L13 = QtGui.QLabel()
        
        # Textbox, buttons and comboboxes 
        edit = QtGui.QLineEdit() # text box to input guesses
        guessButton = QtGui.QPushButton("Guess") # button to click after inputting guess
        combo_p = QtGui.QComboBox() # picture combo box constructor
        combo_p.addItem("mickey")
        combo_p.addItem("pluto")
        #pixmap = QtGui.QPixmap("mickey.gif") # constructor of mickey picture
        pixmap = QtGui.QPixmap("pluto.gif") # constructor of pluto picture
        pic_label.setPixmap(pixmap)
        self.combo_c = QtGui.QComboBox() # colour combo box constructor
        self.combo_c.addItem("red")
        self.combo_c.addItem("blue")
        change = QtGui.QPushButton("Change") # button to click after changing colour and pic
        close = QtGui.QPushButton("Close") # button to close app
        NewGame = QtGui.QPushButton("New Game") # button to start a new game
        
        
        # Create grid layout
        grid = QtGui.QGridLayout()
        
        # positioning labels
        grid.addWidget(L1,0,2)  # guesses label
        grid.addWidget(L2,1,2)  # guess 1 
        grid.addWidget(L3,2,2)  # guess 2
        grid.addWidget(L4,3,2)  # guess 3
        grid.addWidget(L5,5,2)  # interface        
        grid.addWidget(L6,6,2)  # picture        
        grid.addWidget(L7,7,2)  # colour
        
        # postioning text guess box
        grid.addWidget(edit,4,3)        

        #poisitioning combo boxes
        grid.addWidget(combo_p,6,3)
        grid.addWidget(self.combo_c,7,3)

        # positioning buttons
        grid.addWidget(guessButton,4,4)
        grid.addWidget(change,7,4)
        grid.addWidget(close,8,2)
        grid.addWidget(NewGame,8,3)
        
        # positioning picture
        grid.addWidget(pic_label,0,1)
        
        # positioning guesses and comments
        grid.addWidget(L8,1,3) # first guess 
        grid.addWidget(L9,2,3) # second guess
        grid.addWidget(L10,3,3) # third guess
        grid.addWidget(L11,1,4) # comment on first guess
        grid.addWidget(L12,2,4) # comment on second guess
        grid.addWidget(L13,3,4) # comment on third guess
        
        self.setLayout(grid) # set grid layout as widget layout
        
        # signals to link buttons 
        self.connect(close,QtCore.SIGNAL('clicked()'),self.closeClicked) 
        self.connect(change,QtCore.SIGNAL('clicked()'),self.CandP_Change)
        #self.connect(guess,QtCore.SIGNAL('clicked()'),self.)
        #
        
    def closeClicked(self): # method allows close button to close window
        self.close()

    def CandP_Change(self): # method to change window background colour and picture
        comboColour = self.combo_c.currentText()
        self.setPalette(QtGui.QPalette(QtGui.QColor(comboColour)))
        self.setAutoFillBackground(True) 
        picChange = self.combo_p.currentText()
        pic_label.setPixmap(picChange)
        
    #def Game(self): # method to link RandomGameClass with Widget
    
    #def newGame(self): # method allows user to select new game button and start a new game         
        
app = QtGui.QApplication(sys.argv)
MyWidget = GuessingGame()   # create GuessingGame object
MyWidget.show()             # makes the widget pop up 
sys.exit(app.exec_())