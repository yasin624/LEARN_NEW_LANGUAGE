from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings
import parameters as prt



class ADD_WORLD(QWidget):
    def __init__(self):
        super().__init__()
        self.etiketler()

    def duzen(self,obje,between=[1,3,1],*kwargs):

        for i in range(len(between)):
            for l in range(between[i]):
                obje.addStretch()
            try:
                obje.addWidget(kwargs[i])
            except:
                pass
        return obje

    def etiketler(self):
        ###############################################   saves new word
        self.new = QLabel(self)
        self.new.setText("New word ")
        self.new.setFont(QFont("BOLD", 12))
        self.new.setAlignment(Qt.AlignLeft)

        self.new_v = QLineEdit(self)
        self.new_v.setFont(QFont("Ariel", 12))
        self.new_v.setStyleSheet(f'background: {prt._lineeditcolor};')
        ###############################################   saves meaning of new word
        self.meaning = QLabel(self)
        self.meaning.setText("Meaning")
        self.meaning.setFont(QFont("BOLD", 12))
        self.meaning.setAlignment(Qt.AlignLeft)

        self.meaning_v = QLineEdit(self)
        self.meaning_v.setFont(QFont("Ariel", 12))
        self.meaning_v.setStyleSheet(f'background: {prt._lineeditcolor};')
        ###############################################   saves example of new word
        self.example = QLabel(self)
        self.example.setText("example  ")
        self.example.setFont(QFont("BOLD", 12))
        self.example.setWordWrap(True)

        self.example_v = QTextEdit (self)
        self.example_v.setFont(QFont("Ariel", 12))
        self.example_v.setStyleSheet(f'background: {prt._texteditcolor};')
        ###############################################   saves meaning of example of new word
        self.example_M = QLabel(self)
        self.example_M.setText("example-M")
        self.example_M.setFont(QFont("BOLD", 12))
        self.example_M.setWordWrap(True)

        self.example_M_v = QTextEdit (self)
        self.example_M_v.setFont(QFont("Ariel", 12))
        self.example_M_v.setStyleSheet(f'background: {prt._texteditcolor};')
        ###############################################   the button dowloand files
        self.save = QPushButton(self)
        self.save.setText("SAVE")
        self.save.setFont(QFont("Ariel", 10))
        self.save.setStyleSheet(f'background: {prt._buttoncolor};')

        ###############################################  the button for world control

        self.DEL = QPushButton(self)
        self.DEL.setText("DEL")
        self.DEL.setFont(QFont("Ariel", 10))
        self.DEL.setStyleSheet(f'background: {prt._buttoncolor};')

        ###############################################   arrangement
        v = QVBoxLayout()
        l=QHBoxLayout()
        l.addStretch()
        l.addWidget(QLabel("<h1><i> NEW WORD ADD </i></h1>"))
        l.addStretch()
        v.addLayout(l)
        v.addStretch()

        word=QHBoxLayout()
        self.duzen(word,[1,3,1],self.new,self.new_v)
        v.addLayout(word)
        v.addStretch()

        value=QHBoxLayout()
        self.duzen(value,[1,3,1],self.meaning,self.meaning_v)
        v.addLayout(value)
        v.addStretch()

        example=QHBoxLayout()
        self.duzen(example,[1,1,1],self.example,self.example_v)
        v.addLayout(example)
        v.addStretch()

        example_M=QHBoxLayout()
        self.duzen(example_M,[1,1,1],self.example_M,self.example_M_v)
        v.addLayout(example_M)
        v.addStretch()


        v.addStretch()


        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.DEL)
        h.addStretch()
        h.addStretch()
        h.addWidget(self.save)
        h.addStretch()

        v.addLayout(h)
        v.addStretch()




        self.save.clicked.connect(self.word_save)
        self.DEL.clicked.connect(self.delete)

        self.setLayout(v)
    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.save.click()
    def delete(self):
        self.new_v.clear()
        self.meaning_v.clear()
        self.example_v.clear()
        self.example_M_v.clear()
    def word_save(self):
        word=self.new_v.text()+":"+self.meaning_v.text()+"("+\
             self.example_v.toPlainText()+":"+self.example_M_v.toPlainText()+")"+"\n"
        self.delete()
        with open(prt._dont_know_word_list,"a+",encoding="utf-8") as file:
            file.write(word.lower())





