import sys
from PyQt4 import QtGui, QtCore
from random import *

class GuessingGame(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250,250,500,250)
        self.setWindowTitle('Guessing Game')
        self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
        self.setAutoFillBackground(True)        
        
        self.mickey=QtGui.QPixmap('mickey.gif')
        self.mickey_label=QtGui.QLabel()
        self.mickey_label.setPixmap(self.mickey)
        
        self.pluto=QtGui.QPixmap('pluto.gif')
        self.pluto_label=QtGui.QLabel()
        self.pluto_label.setPixmap(self.pluto)
        
        guesses_label=QtGui.QLabel('Guesses:')
        guesses_label.setFont(QtGui.QFont('Arial',16,3))
        
        self.guess_1=QtGui.QLabel('Guess 1:')
        self.guess_2=QtGui.QLabel('Guess 2:')
        self.guess_3=QtGui.QLabel('Guess 3:')
        #self.numbers=QtGui.QLabel(GuessNumber())
        #answer
        
        self.guess_edit=QtGui.QLineEdit()
        self.guess_input=self.guess_edit.displayText()
        
        self.guess=QtGui.QPushButton('Guess')
        
        interface_label=QtGui.QLabel('Interface:')
        interface_label.setFont(QtGui.QFont('Arial',16,3))
        picture_label=QtGui.QLabel('Picture:')
        picture_label.setFont(QtGui.QFont('Arial',9,1))        
        colour_label=QtGui.QLabel('Colour:')
        colour_label.setFont(QtGui.QFont('Arial',9,1))        
                
        self.combo_chars=QtGui.QComboBox()
        self.combo_chars.addItem('mickey')
        self.combo_chars.addItem('pluto')
        #self.combo_chars_text=self.combo_chars.currentText()
        
        self.combo_colours=QtGui.QComboBox()
        self.combo_colours.addItem('red')
        self.combo_colours.addItem('blue')
        self.combo_colours.addItem('yellow')
        self.combo_colours.addItem('green')
        self.combo_colours.addItem('brown')        
        self.combo_colours_text=self.combo_colours.currentText()
        
        self.change=QtGui.QPushButton('Change')
        
        self.new_game=QtGui.QPushButton('New Game')
        self.close_button=QtGui.QPushButton('Close')
        self.close_button.setMaximumSize(100,50)
        
        grid=QtGui.QGridLayout()
        grid.addWidget(guesses_label,0,0)
        grid.addWidget(self.guess_1,1,0)
        #grid.addWidget(int(self.guess_input),1,1)
        #grid.addWidget(answer,1,2)
        grid.addWidget(self.guess_2,2,0)
        #grid.addWidget(self.numbers[1],2,1)
        #grid.addWidget(,2,2)
        grid.addWidget(self.guess_3,3,0)
        #grid.addWidget(self.numbers[2],3,1)
        #grid.addWidget(,3,2)        
        grid.addWidget(self.guess_edit,4,1)
        grid.addWidget(self.guess,4,2)
        grid.addWidget(interface_label,5,0)
        grid.addWidget(picture_label,6,0)
        grid.addWidget(self.combo_chars,6,1)
        grid.addWidget(colour_label,7,0)
        grid.addWidget(self.combo_colours,7,1)
        grid.addWidget(self.change,7,2)
        grid.addWidget(self.close_button,8,0)
        grid.addWidget(self.new_game,8,1)
        grid_widget=QtGui.QWidget()
        grid_widget.setLayout(grid)
        
        self.hbox=QtGui.QHBoxLayout()
        self.hbox.addWidget(self.mickey_label)
        self.hbox.addStretch(3)
        self.hbox.addWidget(grid_widget)
        hbox_widget=QtGui.QWidget()
        self.setLayout(self.hbox)       
        
        self.close_button.clicked.connect(self.closeClicked)
        self.guess.clicked.connect(self.guessClicked)
        self.change.clicked.connect(self.changeClicked)
        '''
        self.connect(self.,QtCore.SIGNAL('clicked()'),self.buttonClicked)'''
        
    def guessClicked(self):
        print(self.guess_input)
        '''
        tries=0
        numbers
        guess_num=random.randint(1,10)
        
        if tries<3:
            num=self.guess_input
            
            if guess_num==num:
                response='Correct!'
                print(response)
            
            elif num>guess_num: 
                response='Too high.'
                print(response)
            
            else: 
                response='Too low.'
                print(response)
            tries+=1
        '''
        
    def closeClicked(self): self.close()
        
    #def new_gameClicked(self):
        #self.GuessNumber()
        
    def changeClicked(self):
        char=self.combo_chars.currentText()
        colour=self.combo_colours.currentText()
        if char=='mickey':
            self.mickey=QtGui.QPixmap("mickey.gif")
            self.mickey_label.setPixmap(self.mickey)
            self.mickey_label.show()
            if colour=='red':
                self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            elif colour=='blue':
                self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            elif colour=='yellow':
                self.setPalette(QtGui.QPalette(QtGui.QColor('yellow')))
            elif colour=='green':
                self.setPalette(QtGui.QPalette(QtGui.QColor('green')))
            elif colour=='brown':
                self.setPalette(QtGui.QPalette(QtGui.QColor('brown')))            
            self.setAutoFillBackground(True)
        
        else:
            self.pluto=QtGui.QPixmap("pluto.gif")
            self.mickey_label.setPixmap(self.pluto)
            if colour=='red':
                self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            elif colour=='blue':
                self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            elif colour=='yellow':
                self.setPalette(QtGui.QPalette(QtGui.QColor('yellow')))
            elif colour=='green':
                self.setPalette(QtGui.QPalette(QtGui.QColor('green')))
            elif colour=='brown':
                self.setPalette(QtGui.QPalette(QtGui.QColor('brown')))            
            self.setAutoFillBackground(True)            
            
def main():
    app=QtGui.QApplication(sys.argv)
    guessing_game=GuessingGame()
    guessing_game.show()
    sys.exit(app.exec_())
    
main()