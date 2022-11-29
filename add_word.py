from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings



class ADD_WORLD(QWidget):
    def __init__(self):
        super().__init__()
        self.etiketler()

    def etiketler(self):
        ###############################################   app main icon
        self.new = QLabel(self)
        self.new.setText("New word ")
        self.new.setFont(QFont("BOLD", 12))

        self.new_v = QLineEdit(self)
        self.new_v.setFont(QFont("Ariel", 12))
        ###############################################   files the url
        self.meaning = QLabel(self)
        self.meaning.setText("Meaning")
        self.meaning.setFont(QFont("BOLD", 12))

        self.meaning_v = QLineEdit(self)
        self.meaning_v.setFont(QFont("Ariel", 12))
        ###############################################   the button dowloand files
        self.save = QPushButton(self)
        self.save.setText("SAVE")
        self.save.setFont(QFont("Ariel", 10))

        ###############################################  the button for world control

        self.DEL = QPushButton(self)
        self.DEL.setText("DEL")
        self.DEL.setFont(QFont("Ariel", 10))

        ###############################################   arrangement
        v = QVBoxLayout()
        l=QHBoxLayout()
        l.addStretch()
        l.addWidget(QLabel("<h1><i> NEW WORD ADD </i></h1>"))
        l.addStretch()
        v.addLayout(l)
        v.addStretch()

        word=QHBoxLayout()
        word.addStretch()
        word.addWidget(self.new)
        word.addStretch()
        word.addWidget(self.new_v)
        word.addStretch()
        v.addLayout(word)
        v.addStretch()

        value=QHBoxLayout()
        value.addStretch()
        value.addWidget(self.meaning)
        value.addStretch()
        value.addWidget(self.meaning_v)
        value.addStretch()
        v.addLayout(value)
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

        self.setLayout(v)

    def word_save(self):
        word=self.new_v.text()+":"+self.meaning_v.text()+"\n"

        print(word)
        self.new_v.clear()
        self.meaning_v.clear()

        with open("word_library.dbs","a+") as file:


            file.write(word.upper())





