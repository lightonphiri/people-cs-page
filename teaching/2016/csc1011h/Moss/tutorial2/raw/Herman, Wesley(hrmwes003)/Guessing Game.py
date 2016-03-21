# A guessing game GUI
# Wesley Herman
# HRMWES003

import sys
import random
import subprocess
from PyQt4 import QtGui, QtCore

class GuessingGame(QtGui.QWidget):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(275, 125, 300, 300)
        self.setWindowTitle("Guessing Game")

# default background colour
        self.setPalette(QtGui.QPalette(QtGui.QColor("red")))
        self.setAutoFillBackground(True)
# answer
        self.answer = random.randint(0, 10)
# counter        
        self.counter = 0

# heading 1        
        guesses_label = QtGui.QLabel("Guesses:")
        guesses_label.setFont(QtGui.QFont("Arial",24))

# guess labels  
        guess_1_label = QtGui.QLabel("Guess 1:             ")
        guess_2_label = QtGui.QLabel("Guess 2:             ")
        guess_3_label = QtGui.QLabel("Guess 3:             ")

# display guesses and feedback       
        self.show_guess_1 = QtGui.QLabel()
        self.show_guess_2 = QtGui.QLabel()
        self.show_guess_3 = QtGui.QLabel()
        self.reply_1 = QtGui.QLabel()
        self.reply_2 = QtGui.QLabel()
        self.reply_3 = QtGui.QLabel()

# enter and pass user input        
        self.guess_edit = QtGui.QLineEdit()
        self.guess = QtGui.QPushButton("Guess")

# heading 2       
        interface_label = QtGui.QLabel("Interface:")
        interface_label.setFont(QtGui.QFont("Arial",24))
    
# picture and colour combo boxes, close, change and new game buttons
        picture_label = QtGui.QLabel("Picture:")
        self.picture_combo = QtGui.QComboBox()
        self.picture_combo.addItem("mickey")
        self.picture_combo.addItem("pluto")
        colour_label = QtGui.QLabel("Colour:")
        self.colour_combo = QtGui.QComboBox()
        self.colour_combo.addItem("red")
        self.colour_combo.addItem("blue")
        self.colour_combo.addItem("green")
        self.colour_combo.addItem("yellow")
        self.change = QtGui.QPushButton("Change")
        self.clos = QtGui.QPushButton("Close")
        self.newgame = QtGui.QPushButton("New Game")

# default picture        
        y = self.picture_combo.currentText()
        x = y + ".gif"
        
        self.pixmap = QtGui.QPixmap(x)
        self.pic_label = QtGui.QLabel()
        self.pic_label.setPixmap(self.pixmap)        
        
# grid 1
        grid1 = QtGui.QGridLayout()
        grid1.addWidget(guess_1_label, 0, 0)
        grid1.addWidget(self.show_guess_1, 0, 1)
        grid1.addWidget(self.reply_1, 0, 2)
        grid1.addWidget(guess_2_label, 1, 0)
        grid1.addWidget(self.show_guess_2, 1, 1)
        grid1.addWidget(self.reply_2, 1, 2)
        grid1.addWidget(guess_3_label, 2, 0)
        grid1.addWidget(self.show_guess_3, 2, 1)
        grid1.addWidget(self.reply_3, 2, 2)
        grid1.addWidget(self.guess_edit, 3, 1)
        grid1.addWidget(self.guess, 3, 2)
        
        grid_widget1 = QtGui.QWidget()
        grid_widget1.setLayout(grid1)
       
# grid 2 
        grid2 = QtGui.QGridLayout()
        grid2.addWidget(picture_label, 0, 0)
        grid2.addWidget(self.picture_combo, 1, 1)
        grid2.addWidget(colour_label, 2, 0)
        grid2.addWidget(self.colour_combo, 2, 1)
        grid2.addWidget(self.change, 2, 2)
        grid2.addWidget(self.clos, 3, 0)
        grid2.addWidget(self.newgame, 3, 1)
        
        grid_widget2 = QtGui.QWidget()
        grid_widget2.setLayout(grid2)
        
# vbox with grids and headings
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(guesses_label)
        vbox.addWidget(grid_widget1)
        vbox.addWidget(interface_label)
        vbox.addWidget(grid_widget2)
        vbox_widget = QtGui.QWidget()
        vbox_widget.setLayout(vbox)
        
# hbox with picture and vbox
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.pic_label)
        hbox.addWidget(vbox_widget)
        self.setLayout(hbox)
        
# connected buttons
        self.newgame.clicked.connect(self.restartGame)
        self.connect(self.guess, QtCore.SIGNAL("clicked()"), self.guessButtonClicked)
        self.connect(self.clos, QtCore.SIGNAL("clicked()"), self.closeButtonClicked)
        self.connect(self.change, QtCore.SIGNAL("clicked()"), self.changeButtonClicked)
        
    def guessButtonClicked(self):
 
        if self.counter==0:
            g1 = self.guess_edit.displayText()
            self.show_guess_1.setText(g1)
            if int(g1)==self.answer:
                fb = "Correct!"
                self.counter+=1
                self.reply_1.setText(fb)
            elif int(g1)<self.answer:
                fb = "Too small"
                self.counter+=1
                self.reply_1.setText(fb)
            elif int(g1)>self.answer:
                fb = "Too big"
                self.counter+=1
                self.reply_1.setText(fb)
        elif self.counter==1:
            g2 = self.guess_edit.displayText()
            self.show_guess_2.setText(g2)
            if int(g2)==self.answer:
                fb2 = "Correct!"
                self.counter+=1
                self.reply_2.setText(fb2)
            elif int(g2)<self.answer:
                fb2 = "Too small"
                self.counter+=1
                self.reply_2.setText(fb2)
            elif int(g2)>self.answer:
                fb2 = "Too big"
                self.counter+=1            
                self.reply_2.setText(fb2)
        elif self.counter==2:
            g3 = self.guess_edit.displayText()
            self.show_guess_3.setText(g3)
            if int(g3)==self.answer:
                fb3 = "Correct!"
                self.counter+=1
                self.reply_3.setText(fb3)
            elif int(g3)<self.answer:
                fb3 = "Too small"
                self.counter+=1
                self.reply_3.setText(fb3)
            elif int(g3)>self.answer:
                fb3 = "Too big"
                self.counter+=1            
                self.reply_3.setText(fb3)        

       
    def restartGame(self):
        self.close()
        subprocess.call("Guessing Game.py", shell=True)    
        
    def closeButtonClicked(self):
        self.close()
        
    def changeButtonClicked(self):
        colour_text = self.colour_combo.currentText()
        self.setPalette(QtGui.QPalette(QtGui.QColor(colour_text)))
        self.setAutoFillBackground(True)
        
        y = self.picture_combo.currentText()
        x = y + ".gif"
        self.pixmap = QtGui.QPixmap(x)
        self.pic_label.setPixmap(self.pixmap)
        self.pic_label.show()
        
        
    
def main():
    app = QtGui.QApplication(sys.argv)
    guessing_game = GuessingGame()
    guessing_game.show()
    sys.exit(app.exec_())
    
main()