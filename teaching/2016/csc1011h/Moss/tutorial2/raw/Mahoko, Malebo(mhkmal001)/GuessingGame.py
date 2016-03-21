# malebo mahoko
# 03 March 2016
# a guessing game 

"""importing modules to be used"""
import random
import sys
from PyQt4 import QtGui, QtCore

class GuessingGame(QtGui.QWidget):                  # class GuessingGame inherits from QtGui.QWidget
    def __init__(self,parent = None):
        """ Main Window """
        QtGui.QWidget.__init__(self,parent)
        self.setGeometry(250,250,500,300)
        self.setWindowTitle("Guessing Game")
     
        """ creat and display heading guesses(in bold) on the window"""
        self.guess = QtGui.QLabel("Guesses:",self)        
        self.guess.setFont(QtGui.QFont('Times',20,10))       
        self.guess.move(215,40) 
        
        """ creat and place number of guesses on the window"""
        self.guess1 = QtGui.QLabel("Guess 1:",self)
        self.guess1.move(215,80)
        self.guess2 = QtGui.QLabel("Guess 2:",self)
        self.guess2.move(215,100)
        self.guess3 = QtGui.QLabel("Guess 3:",self)
        self.guess3.move(215,120)        
        
        """ creating empty labels where the interaction between the user and game will take place (top right coner)"""
        self.emptyLabel1 = QtGui.QLabel('',self)            
        self.emptyLabel1.setGeometry(310,80,20,15)
        self.emptyLabel2 = QtGui.QLabel('',self)             
        self.emptyLabel2.setGeometry(310,100,20,15)        
        self.emptyLabel3 = QtGui.QLabel('',self)           
        self.emptyLabel3.setGeometry(310,120,20,15)        
        self.emptyLabel4 = QtGui.QLabel('',self)             
        self.emptyLabel4.setGeometry(390,80,70,15)        
        self.emptyLabel5 = QtGui.QLabel('',self)             
        self.emptyLabel5.setGeometry(390,100,70,15)    
        self.emptyLabel6 = QtGui.QLabel('',self)             
        self.emptyLabel6.setGeometry(390,120,70,15)        
        
        """ the heading interface"""
        self.interface = QtGui.QLabel("Interface:",self)
        self.interface.move(215,170) 
        self.interface.setFont(QtGui.QFont('Times',20,10))
        
        self.picture = QtGui.QLabel('Picture:',self)                # creating and setting the label picture
        self.picture.move(215,210)
        
        self.picture_choice_combo = QtGui.QComboBox(self)            # constructing a combox called picture_choice_combo
        self.picture_choice_combo.addItem("mickey") 	             # add pluto to picture_picture_combo combobox
        self.picture_choice_combo.addItem("pluto")                  # add pluto to picture_choice_combo combobox   
        self.picture_choice_combo.setGeometry(310,210,75,22)         # setting geometry of picture_choice_combo_box
        
        self.colour = QtGui.QLabel("Colour:",self)              # creating and setting the label colour
        self.colour.move(215,240)
        
        """ creating and setting combobox for colour and adding items(colours) to it""" 
        self.colour_change_combo = QtGui.QComboBox(self)             
        self.colour_change_combo.addItem("red") 	          
        self.colour_change_combo.addItem("blue")
        self.colour_change_combo.addItem("yellow")
        self.colour_change_combo.addItem("orange")
        self.colour_change_combo.addItem("pink")
        self.colour_change_combo.addItem("brown")
        self.colour_change_combo.setGeometry(310,235,75,22)
        
        """ creating,setting and connecting the change button to slot changeClicked """
        self.change_button = QtGui.QPushButton("Change",self)
        self.change_button.move(390,235)  
        self.change_button.clicked.connect(self.changeClicked)

        """ creating,setting and connecting the close button to slot closeGame """
        self.close_button = QtGui.QPushButton("Close",self)
        self.close_button.move(215,265)
        self.connect(self.close_button,QtCore.SIGNAL('clicked()'), self.closeGame)
        
        """ creating,setting and connecting the new game to slot newClicked """
        self.new_game_button = QtGui.QPushButton("New Game",self)
        self.new_game_button.move(310,265)
        self.new_game_button.clicked.connect(self.newClicked)
        
        self.edit = QtGui.QLineEdit(self)             # creating the edit line
        self.edit.setGeometry(310,142,75,22)          # setting the edit line
        
        """ creating,setting and connecting the guess_button to slot guessClicked"""
        self.guess_button = QtGui.QPushButton("Guess",self)
        self.guess_button.move(390,142) 
        self.guess_button.clicked.connect(self.guessClicked)   
        
        self.setPalette(QtGui.QPalette(QtGui.QColor("Red")))     # setting the default colour of the window to red
        
        """ setting the default piture to mickey"""
        self.mickey_label = QtGui.QLabel(self) 
        self.mickey = QtGui.QPixmap("mickey.gif")
        self.mickey_label.move(10,20)
        self.mickey_label.setPixmap(self.mickey)   
        
        self.Random = random.randint(1,10)                       # a variable containing a random number 
        
        self.counter = 1                                         # a count variable to keep on check that user only guesses three times
        
    """ slot newClicked"""
    def newClicked(self):
        self.Random = random.randint(1,10)                  # for each and everytime the new button is clicked a new random value is generated and stored
        self.counter = 1
        
        """ clearing all teh previous guesses"""
        self.emptyLabel1.clear()
        self.emptyLabel2.clear()
        self.emptyLabel3.clear()
        self.emptyLabel4.clear()
        self.emptyLabel5.clear()
        self.emptyLabel6.clear() 
        
    """ slot changeClicked"""
    def changeClicked(self):
        self.text_colour = self.colour_change_combo.currentText()               # getting the current text in the colour combobox
        self.setPalette(QtGui.QPalette(QtGui.QColor(self.text_colour)))         # setting the bacground colour to be the current colour text in combobox
        
        self.text_picture = self.picture_choice_combo.currentText()
        
        """ updating the picture if pluto is on the picture combobox"""
        if self.text_picture == "pluto":
            self.pluto = QtGui.QPixmap("pluto.gif")
            self.mickey_label.move(10,35)
            self.mickey_label.setPixmap(self.pluto) 
            self.mickey_label.show()
            
        else:
            """ updating teh picture if mickey is on the picture combobox"""
            self.mickey = QtGui.QPixmap("mickey.gif") 
            self.mickey_label.move(10,20)
            self.mickey_label.setPixmap(self.mickey)   
            self.mickey_label.show()
                
            
    def guessClicked(self):
        
        if self.counter == 1:                                       # for first guess
            """ getting the input value and pringting it on the window(top right coner) """
            self.text_guess = self.edit.displayText()
            self.emptyLabel1.setText(self.text_guess)
            self.emptyLabel1.show()  
            
            if int(self.text_guess) == self.Random:                 # comparing the guessed value with the random number and printing results
                self.answer = "Correct!"
                self.emptyLabel4.setText(self.answer)
                self.edit.clear()
                self.emptyLabel4.show()
                
            elif int(self.text_guess) > self.Random:                # comparing the guessed value with the random number and printing results
                self.answer = "Too big"
                self.emptyLabel4.setText(self.answer)
                self.edit.clear()
                self.emptyLabel4.show() 
            elif int(self.text_guess) < self.Random:                # comparing the guessed value with the random number and printing results
                self.answer = "Too small"
                self.emptyLabel4.setText(self.answer)
                self.edit.clear()
                self.emptyLabel4.show()    
            self.counter += 1
            
            
        #""" second attempt on guessing the correct number"""
        elif self.counter == 2:
            self.text_guess = self.edit.displayText()
            self.emptyLabel2.setText(self.text_guess)
            self.edit.clear()
            self.emptyLabel2.show()   
            
            if int(self.text_guess) == self.Random:                     # comparing the guessed value with the random number and printing  results
                self.answer = "Correct!"
                self.emptyLabel5.setText(self.answer)
                self.edit.clear()
                self.emptyLabel5.show() 
                
            elif int(self.text_guess) > self.Random:                    # comparing the guessed value with the random number and printing results
                self.answer = "Too big"
                self.emptyLabel5.setText(self.answer)
                self.edit.clear()
                self.emptyLabel5.show() 
            elif int(self.text_guess) < self.Random:                    # comparing the guessed value with the random number and printing results
                self.answer = "Too small"
                self.emptyLabel5.setText(self.answer)
                self.edit.clear()
                self.emptyLabel5.show()    
            self.counter += 1  
            
        #"""third attempt on guessing the value"""
        elif self.counter == 3:
            self.text_guess = self.edit.displayText()
            self.emptyLabel3.setText(self.text_guess)
            self.emptyLabel3.show()   
            
            if int(self.text_guess) == self.Random:                         # comparing the guessed value with the random number and printing results
                self.answer = "Correct!"
                self.emptyLabel6.setText(self.answer)
                self.edit.clear()
                self.emptyLabel6.show()
        
            elif int(self.text_guess) > self.Random:                         # comparing the guessed value with the random number and printing results
                self.answer = "Too big"
                self.emptyLabel6.setText(self.answer)
                self.edit.clear()
                self.emptyLabel6.show() 
            elif int(self.text_guess) < self.Random:                         # comparing the guessed value with the random number and printing results
                self.answer = "Too small"
                self.emptyLabel6.setText(self.answer)
                self.edit.clear()                                            # clearing th edit box
                self.emptyLabel6.show()    
            self.counter += 1                  
   
    def closeGame(self):                                    # slot closeGame
        self.close()                                        # colse the window
         
""" main for running the window"""         
def main():
    app = QtGui.QApplication(sys.argv)
    game = GuessingGame()
    game.show()
    sys.exit(app.exec_())
main()