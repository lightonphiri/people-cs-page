
import sys, random
from PyQt4 import QtGui, QtCore

class GuessingGame(QtGui.QWidget):
    
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 200, 150)
        self.setWindowTitle('Gussing Game')
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        
        #set buttons
        guessbutton  = QtGui.QPushButton('Guess')
        closebutton = QtGui.QPushButton('Close')
        changebutton = QtGui.QPushButton('Change')
        newgamebutton = QtGui.QPushButton('New Game') 
        editbutton = QtGui.QLineEdit(self)
        text = editbutton.displayText()
        guessbutton.setMinimumSize(80,20)
        guessbutton.setMaximumSize(100,25)
        closebutton.setMinimumSize(80,20)
        closebutton.setMaximumSize(100,25)
        changebutton.setMinimumSize(80,20)
        changebutton.setMaximumSize(100,25)
        newgamebutton.setMinimumSize(80,20)
        newgamebutton.setMaximumSize(100,25)
        editbutton.setMinimumSize(80,20)
        editbutton.setMaximumSize(100,25)          
                
        guess = QtGui.QLabel('Guesses:',self)
        guess.setFont(QtGui.QFont('Times',20,2))        
        guess1 = QtGui.QLabel('Guess1:',self)
        guess2 = QtGui.QLabel('Guess2:',self)
        guess3 = QtGui.QLabel('Guess3:',self)
        empty1 = QtGui.QLabel('')
        empty2 = QtGui.QLabel('')
        empty3 = QtGui.QLabel('')
        empty4 = QtGui.QLabel('')
        empty5 = QtGui.QLabel('')
        empty6 = QtGui.QLabel('')
        interface = QtGui.QLabel('Interface:',self)
        interface.setFont(QtGui.QFont('Times',20,2))
        picture = QtGui.QLabel('Picture:',self)
        colour = QtGui.QLabel('Colour:',self)
        
        self.pixmap = QtGui.QPixmap('mickey.gif') # constructor
        self.pic_label = QtGui.QLabel(self) # QLabel to hold pixmap
        self.pic_label.setPixmap(self.pixmap)   # 
        
        self.pixmap1 = QtGui.QPixmap('pluto.gif') # constructor
        self.pic_label1 = QtGui.QLabel(self) # QLabel to hold pixmap
        self.pic_label1.setPixmap(self.pixmap1)        
        
        combo = QtGui.QComboBox(self) # constructor
        combo.addItem('red')
        combo.addItem('blue')
        text = combo.currentText() # gets selected text	
        
        combo2 = QtGui.QComboBox(self) # constructor
        combo2.addItem('mickey')
        combo2.addItem('pluto')
        text = combo2.currentText() # gets selected text	        
        
        grid = QtGui.QGridLayout() 
        grid.addWidget(self.pic_label,0,1,9,1)
        grid.addWidget(guess,0,2)
        grid.addWidget(guess1,1,2)
        grid.addWidget(guess2,2,2)
        grid.addWidget(guess3,3,2)
        grid.addWidget(editbutton,4,3)
        grid.addWidget(empty1,1,3)
        grid.addWidget(empty2,2,3)
        grid.addWidget(empty3,3,3)
        grid.addWidget(empty4,1,4)
        grid.addWidget(empty5,2,4)
        grid.addWidget(empty6,3,4)                            
        grid.addWidget(guessbutton,4,4)
        grid.addWidget(interface,5,2)
        grid.addWidget(picture,6,2)
        grid.addWidget(colour,7,2)
        grid.addWidget(combo,7,3)
        grid.addWidget(combo2,6,3)
        grid.addWidget(changebutton,7,4)
        grid.addWidget(closebutton,8,2)
        grid.addWidget(newgamebutton,8,3)
        self.setLayout(grid)
        
        
        
def main():
    app = QtGui.QApplication(sys.argv)
    guessing_game = GuessingGame()
    guessing_game.show()
    sys.exit(app.exec_())
    
main()
    
    
        
        


        
        
        
                
        
        
        
        
        

        
        
        
        
        
        
        
        



