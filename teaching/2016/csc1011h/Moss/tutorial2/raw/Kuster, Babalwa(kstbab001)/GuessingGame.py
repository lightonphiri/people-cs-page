import sys
from PyQt4 import QtGui,QtCore

import math
import random

class GuessingGame(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setGeometry(250, 250, 200, 150)    
        self.setWindowTitle('Guessing Game')
        
        
        #Labels
        label = QtGui.QLabel('Guesses:',self)
        label1 = QtGui.QLabel('Guesses 1:',self)
        label2 = QtGui.QLabel('Guesses 2:',self)
        label3 = QtGui.QLabel('Guesses 3:',self)
        lable4 = QtGui.QLabel('Picture:',self)
        lable5 = QtGui.QLabel('Colour:',self)
        interF = QtGui.QLabel('Interface:',self)
        answer1=QtGui.QLabel('',self)
        answer2=QtGui.QLabel('',self)
        answer3=QtGui.QLabel('',self)
        empty_str1=QtGui.QLabel('',self)
        empty_str2=QtGui.QLabel('',self)
        empty_str3=QtGui.QLabel('',self)
        
        #Labels layout
        label.setFont(QtGui.QFont('Times',18))
        interF.setFont(QtGui.QFont('Times',18))
        edit = QtGui.QLineEdit(self)	             
        
                
        
        #button
        self.guess=QtGui.QPushButton('Guess')
        self.close=QtGui.QPushButton('Cancel')
        self.new_game=QtGui.QPushButton('New Game')
        self.change=QtGui.QPushButton('Change')
        
        #combo
        self.combo_col=QtGui.QComboBox()
        self.combo_pic=QtGui.QComboBox()
        self.combo_col.addItem('red')
        self.combo_col.addItem('blue')
        self.combo_pic.addItem('pluto')
        self.combo_pic.addItem('mickey')
        
        #get stuff
        #self.text_col=combo_col.currentText()
        #self.text_pic=combo_pic.currentText()
        text_edit=edit.displayText()
        
        self.pic=QtGui.QPixmap('mickey.gif')
        self.pic_label=QtGui.QLabel()
        self.pic_label.setPixmap(self.pic)
        #random
        rand_num=random.randint(1,10)
        list_text=[]
                
        #grid layout
        grid=QtGui.QGridLayout()
        grid.addWidget(self.pic_label,0,0,8,1)
        grid.addWidget(label,0,2)
        grid.addWidget(label1,1,2)
        grid.addWidget(label2,2,2)
        grid.addWidget(label3,3,2)
        grid.addWidget(edit,4,3)
        grid.addWidget(self.guess,4,4)
        grid.addWidget(interF,5,2)
        grid.addWidget(lable4,6,2)
        grid.addWidget(self.combo_pic,6,3)
        grid.addWidget(lable5,7,2)
        grid.addWidget(self.combo_col,7,3)
        grid.addWidget(self.change,7,4)
        grid.addWidget(self.close,8,2)
        grid.addWidget(self.new_game,8,3)
        grid.addWidget(answer1,1,3)
        grid.addWidget(answer2,2,3)
        grid.addWidget(answer3,3,3)
        grid.addWidget(empty_str1,1,4)
        grid.addWidget(empty_str2,2,4)
        grid.addWidget(empty_str3,3,4)
        self.setLayout(grid)
        self.connect(self.guess,QtCore.SIGNAL('clicked()'), self.buttonGuess)
        self.connect(self.close,QtCore.SIGNAL('clicked()'), self.buttonClosed)
        #self.connect(self.new_game,QtCore.SIGNAL('clicked()'), self.buttonClicked)
        #self.connect(self.change,QtCore.SIGNAL('clicked()'), self.buttonClicked)
        #background
        #self.setPalette(QtGui.QPalette(QtGui.QColor(self.text_col)))
        self.change.clicked.connect(self.buttonChange)
        
    def buttonClosed(self):
        sys.exit()
        
    def buttonChange(self):
        self.text_col=self.combo_col.currentText()
        self.text_pic=self.combo_pic.currentText()        
        if self.text_pic=="mickey"and self.text_col=='red':
            self.pic=QtGui.QPixmap(self.text_pic+'.gif')
            self.pic_label.setPixmap(self.pic)
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            
        elif self.text_pic=='pluto' and self.text_col=='red':
            self.pic=QtGui.QPixmap(self.text_pic+'.gif')
            self.pic_label.setPixmap(self.pic)
            self.setPalette(QtGui.QPalette(QtGui.QColor('red')))
            
        elif self.text_pic=='pluto' and self.text_col=='blue':
            pic=QtGui.QPixmap(self.text_pic+'.gif')
            self.pic_label.setPixmap(self.pic)
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            
        elif self.text_col=='blue' and self.text_pic=="mickey":
            self.setPalette(QtGui.QPalette(QtGui.QColor('blue')))
            self.pic=QtGui.QPixmap(self.text_pic+'.gif')
            self.pic_label.setPixmap(self.pic)
    def buttonGuess(self):
        self.rand_num=random.randint(1,10)
        self.text_edit=self.edit.displayText()
        self.list_text=[] 
        self.list_text.append(self.text_edit)
        if int(self.list_text[0])==self.rand_num:
            self.answer1.setText(str(self.list_text[0]))
            self.empty_str1.setText('Correct')
        elif int(self.list_text[0])>self.rand_num:
            self.answer1.setText(str(self.list_text[0]))
            self.empty_str1.setText('To big')           
        elif int(self.list_text[0])<self.rand_num:
            self.answer1.setText(str(self.list_text[0]))
            self.empty_str1.setText('To small')     
            
def main():
    app = QtGui.QApplication(sys.argv)
    game=GuessingGame()
    game.show()
    sys.exit(app.exec_())
    
main()
    