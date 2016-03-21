# NDLOVU MXOLELENI
# NDLMXO003

"""importing required modules"""
import sys
from PyQt4 import QtGui, QtCore
import random

class Guessing_Game(QtGui.QWidget):         # creating guessing Game class
    def __init__(self, parent=None):            # parent defines parent widget
        QtGui.QWidget.__init__(self, parent)            # super class constructor
        self.setGeometry(550, 300, 480, 260)            # x,y,width,height based on screen

        grid = QtGui.QGridLayout()          # create grid layout
        
        self.g = random.randint(1,10)           # assigning a random number btween 1 and 10
        
        self.setWindowTitle('Guessing Game')            # create Label, self object is parent
        self.guesses = QtGui.QLabel("Guesses:")	            # create Label, self object is parent
        self.guesses.setFont(QtGui.QFont('Ariel',15,2))         # create Label, self object is parent with font
        self.interface = QtGui.QLabel("Interface:")	         # create Label, self object is parent
        self.interface.setFont(QtGui.QFont('Ariel',15,2))           # create Label, self object is parent with font
        
        self.combo_1 = QtGui.QComboBox()         # constructor
        self.combo_1.addItem('mickey') 	        # adds item to combobox
        self.combo_1.addItem('pluto')           # adds item to combobox
        self.combo_2 = QtGui.QComboBox()         # constructor
        self.combo_2.addItem('red')          # adds item to combobox
        self.combo_2.addItem('blue')    
        
        """# create Labels, self object is parent"""
        self.guess_1 = QtGui.QLabel("Guess 1:")
        self.guess_2 = QtGui.QLabel("Guess 2:")
        self.guess_3 = QtGui.QLabel("Guess 3:")        
        self.edit = QtGui.QLineEdit()
        self.label_1 = QtGui.QLabel("")
        self.label_2 = QtGui.QLabel("")
        self.label_3 = QtGui.QLabel("")
        self.label_4 = QtGui.QLabel("")
        self.label_5 = QtGui.QLabel("")
        self.label_6 = QtGui.QLabel("")
        
        self.guess = QtGui.QPushButton("Guess")
        self.guess.clicked.connect(self.guess_fun)
        
        self.picture = QtGui.QLabel("Picture:")
        
        self.colour = QtGui.QLabel("Colour:")
        
        self.change = QtGui.QPushButton("Change")
        self.change.clicked.connect(self.change_pic)
        self.change.clicked.connect(self.change_col)
        
        self.close = QtGui.QPushButton("Close")
        self.close.clicked.connect(self.ButtonClicked)

        self.new_game = QtGui.QPushButton("New Game")
        self.new_game.clicked.connect(self.new_gam)
        
        """# add labels in their position"""
        grid.addWidget(self.guesses,0,1)
        grid.addWidget(self.guess_1,1,1)
        grid.addWidget(self.guess_2,2,1)
        grid.addWidget(self.guess_3,3,1)
        grid.addWidget(self.edit,4,2)
        grid.addWidget(self.label_1,1,2)
        grid.addWidget(self.label_2,2,2)
        grid.addWidget(self.label_3,3,2)
        grid.addWidget(self.label_4,1,3)
        grid.addWidget(self.label_5,2,3)
        grid.addWidget(self.label_6,3,3)
        grid.addWidget(self.guess,4,3)
        grid.addWidget(self.interface,5,1)
        grid.addWidget(self.picture,6,1)
        grid.addWidget(self.colour,7,1)
        grid.addWidget(self.change,8,3)
        grid.addWidget(self.close,9,1)
        grid.addWidget(self.new_game,9,2)
        grid.addWidget(self.combo_1,6,2)
        grid.addWidget(self.combo_2,7,2)       
        
        self.setLayout(grid)            # set grid layout as widget�s layout
        
        self.pixmap = QtGui.QPixmap('mickey.gif') # constructor
        self.pic_label = QtGui.QLabel(self) # QLabel to hold pixmap
        self.pic_label.setPixmap(self.pixmap)   # add pixmap to label
        grid.addWidget(self.pic_label,0,0,8,1)          # adding picture
        
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))            # setting the colour to red
        
        self.counter = 3          # initialising counter to 3 
        
    def change_pic(self):           # defining change picture function
        self.pic = self.combo_1.currentText()
        if self.pic == "mickey":
            self.pixmap = QtGui.QPixmap('mickey.gif')
            self.pic_label.setPixmap(self.pixmap)
        else:
            self.pixmap = QtGui.QPixmap('pluto.gif')
            self.pic_label.setPixmap(self.pixmap)            
            
    def change_col(self):           # defining change colour function
        self.col = self.combo_2.currentText()
        if self.col == "red":
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        else:
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
    
    def ButtonClicked(self):            # defining a close function called ButtonClicked
        sys.exit()
    
    """function to check whether the number guessed is correct,big or small"""   
    def guess_fun(self):            # defining guess fuction
        user_num = self.edit.displayText()
        if int(user_num) == self.g:
            if self.counter == 3:
                self.label_1.setText(user_num)
                self.label_4.setText("Correct!")
                self.edit.clear()
                self.counter -= 3
            elif self.counter == 2:
                self.label_2.setText(user_num)
                self.label_5.setText("Correct!")
                self.edit.clear()
                self.counter -= 2
                
            elif self.counter == 1:
                self.label_3.setText(user_num)
                self.label_6.setText("Correct!")
                self.edit.clear()
                self.counter -= 1                # decreasing counter by 1
         
            """checking if the number is guessed is less than the correct one"""
        elif int(user_num) < self.g:
            if self.counter == 3:
                self.label_1.setText(user_num)
                self.label_4.setText("Too small")
                self.edit.clear()
                self.counter -= 1           # decreasing counter by 1
                
            elif self.counter == 2:
                self.label_2.setText(user_num)
                self.label_5.setText("Too small")
                self.edit.clear()
                self.counter -= 1           # decreasing counter by 1
            elif self.counter == 1:
                self.label_3.setText(user_num)
                self.label_6.setText("Too small")
                self.edit.clear()
                self.counter -= 1            # decreasing counter by 1
                
            """checking if the number is guessed is greater than the correct one"""
        elif int(user_num) > self.g:
            if self.counter == 3:
                self.label_1.setText(user_num)
                self.label_4.setText("Too big")
                self.edit.clear()
                self.counter -= 1           # decreasing counter by 1
        
            elif self.counter == 2:
                self.label_2.setText(user_num)
                self.label_5.setText("Too big")
                self.edit.clear()
                self.counter -= 1           # decreasing counter by 1
                
            elif self.counter == 1:
                self.label_3.setText(user_num)
                self.label_6.setText("Too big")
                self.edit.clear()
                self.counter -= 1           # decreasing counter by 1
            
    def new_gam(self):          # defining new game fuction
        self.edit.clear()
        self.label_1.clear()
        self.label_2.clear()
        self.label_3.clear()
        self.label_4.clear()
        self.label_5.clear()
        self.label_6.clear()
        self.counter = 3
        self.g = random.randint(1,10)           # assigning a random number btween 1 and 10
        
def main():         # defining main()
    app = QtGui.QApplication(sys.argv)
    abs_widget = Guessing_Game()            # create MyWidget object
    abs_widget.show()
    sys.exit(app.exec_())
main()          # calling the main function