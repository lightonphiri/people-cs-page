"""05/03/2016
           Guessing game program by
                     Rachel Ramonyai"""

import sys
from PyQt4 import QtGui, QtCore
import random

class GuessingGame(QtGui.QWidget):  #inheritance from Widget      
	def __init__(self, parent=None):  
		QtGui.QWidget.__init__(self, parent)
		self.Guesses = 0
		#window dimensions
		self.setGeometry(250, 250, 600, 300) 
		font = QtGui.QFont('Arial',16,QtGui.QFont.Bold,True)
		#generating random numbers to be guessed
		self.randomNumber = random.randrange(1,11) 
		#background colours
		colours = ["white","red","green","blue","black","cyan","magenta","yellow","grey"] 
		 
		self.setWindowTitle('Guessing Game') 
		
	#code for the labels and pictures in the parent widget
		self.pic_label = QtGui.QLabel()
		self.pic_label.setPixmap(QtGui.QPixmap("mickey.gif"))

		self.guesses_label = QtGui.QLabel('Guesses:')
		self.guesses_label.setFont(font) 
		
		self.guess1_label = QtGui.QLabel('Guess 1:')
		self.guess2_label = QtGui.QLabel('Guess 2:')
		self.guess3_label = QtGui.QLabel('Guess 3:')
		
		self.guess1Ans_label = QtGui.QLabel('')
		self.guess2Ans_label = QtGui.QLabel('')
		self.guess3Ans_label = QtGui.QLabel('')
		
		self.guess1Is_label = QtGui.QLabel('')
		self.guess2Is_label = QtGui.QLabel('')
		self.guess3Is_label = QtGui.QLabel('')
		
		self.guessbox_edit = QtGui.QLineEdit()
		self.guessbox_edit.setFixedWidth(100)
		self.guess_button = QtGui.QPushButton("Guess")
		
		self.interface_label = QtGui.QLabel('Interface:')
		self.interface_label.setFont(font)
		
		self.picture_label = QtGui.QLabel('Picture:')
		self.picture_combo = QtGui.QComboBox()
		self.picture_combo.addItem('mickey')
		self.picture_combo.addItem('pluto')
		
		self.colour_label = QtGui.QLabel('Picture:')
		self.colour_combo = QtGui.QComboBox()
		
	#loop to ensure that colours can change
		for colour in colours:
			self.colour_combo.addItem(colour)

		self.change_button = QtGui.QPushButton("Change")
		self.close_button = QtGui.QPushButton("Close")
		
		self.newGame_button = QtGui.QPushButton("New Game")
		
	#code using the gridlayout to add widgets
		grid = QtGui.QGridLayout()
		grid.addWidget(self.pic_label,0,0,10,6)
		
		grid.addWidget(self.guesses_label,1,2)
		grid.addWidget(self.guess1_label,2,2)
		grid.addWidget(self.guess2_label,3,2)
		grid.addWidget(self.guess3_label,4,2)
		
		grid.addWidget(self.guess1Ans_label,2,3)
		grid.addWidget(self.guess2Ans_label,3,3)
		grid.addWidget(self.guess3Ans_label,4,3)
		
		grid.addWidget(self.guess1Is_label,2,4)
		grid.addWidget(self.guess2Is_label,3,4)
		grid.addWidget(self.guess3Is_label,4,4)
		
		grid.addWidget(self.guessbox_edit,5,3)
		grid.addWidget(self.guess_button,5,4)
		
		grid.addWidget(self.interface_label,6,2)
		
		grid.addWidget(self.picture_label,7,2)
		grid.addWidget(self.picture_combo,7,3)
		
		grid.addWidget(self.colour_label,8,2)
		grid.addWidget(self.colour_combo,8,3)
		grid.addWidget(self.change_button,8,4)
		
		grid.addWidget(self.close_button,9,2)
		grid.addWidget(self.newGame_button,9,3)
		
		self.setLayout(grid)
		
	  #code for connecting signals and slots so as to handle the events as per user
		self.connect(self.newGame_button,QtCore.SIGNAL('clicked()'), self.newGameClicked)
		self.connect(self.change_button,QtCore.SIGNAL('clicked()'), self.changeClicked)
		self.connect(self.close_button,QtCore.SIGNAL('clicked()'), self.closeClicked)
		self.connect(self.guess_button,QtCore.SIGNAL('clicked()'), self.guessClicked)
		
       #below is a method to reset the game back to original state
	def newGameClicked(self):
		self.Guesses = 0
		self.guess1Ans_label.setText('')
		self.guess2Ans_label.setText('')
		self.guess3Ans_label.setText('')
		self.guess1Is_label.setText('')
		self.guess2Is_label.setText('')
		self.guess3Is_label.setText('')
		#print(self.randomNumber)
		self.randomNumber = random.randrange(1,11)
		#enable guess button when new game is clicked
		self.guess_button.setEnabled(True)
		
	#method to allow user to guess	
	def guessClicked(self):
		self.Guesses = self.Guesses + 1
		guess = int(self.guessbox_edit.displayText())	
		if(self.Guesses==1):
			self.guess1Ans_label.setText(str(guess))
			self.guess1Is_label.setText(self.checkGuess(guess))
		elif(self.Guesses==2):
			self.guess2Ans_label.setText(str(guess))
			self.guess2Is_label.setText(self.checkGuess(guess))
		else:
			self.guess3Ans_label.setText(str(guess))
			self.guess3Is_label.setText(self.checkGuess(guess))
	#disables the guess button when all three guesses are done to prevent user from playing mor ethan 3 times
			self.guess_button.setEnabled(False)
			print("game over")
		self.guessbox_edit.setText('')
	
		
		
	#setting colours			
	def changeClicked(self):
		new_colour = self.colour_combo.currentText()
		self.setPalette(QtGui.QPalette(QtGui.QColor(new_colour)))
		new_picture = self.picture_combo.currentText()
		self.pic_label.setPixmap(QtGui.QPixmap(new_picture+".gif"))
		
	def closeClicked(self):
		self.close() #closes the game
		
#method for checking how the guessed number compare to the randomly generated number
	def checkGuess(self,n):
		if n == self.randomNumber:
			#disables the guess button when the guess is correct!
			self.guess_button.setEnabled(False)
			return "Correct!"
		elif n > self.randomNumber:
	
			return "To big"
		
		else:
			return "To small"
		


		
		
#method to ensure app run successfully
def main():
	app = QtGui.QApplication(sys.argv)
	my_widget = GuessingGame()
	my_widget.show()
	sys.exit(app.exec_())

main()
