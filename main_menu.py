import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings
import parameters as prt






class menu_içerik(QWidget):
    def __init__(self):
        super().__init__()


        self.word_list=self.word_list_upload()
        self.now_word=0
        self.show_word=True
        self.etiketler()

    def word_list_upload(self,src="word_library.dbs"):
        with open(src,"r",encoding="utf-8")as file:
            words=file.read().split("\n")
        return words[:-1]

    def etiketler(self):

        word=self.word_list[self.now_word]
        ###############################################   word
        self.yazı = QLabel(self)
        self.yazı.setText(word.split(":")[0])
        self.yazı.setFont(QFont("BOLD", 20))
        ###############################################   meaning of word
        self.meaning = QTextEdit(self)
        self.meaning.setText(word.split("(")[1])
        self.meaning.setFont(QFont("Ariel", 10))
        self.meaning.setStyleSheet(f'background: {prt._texteditcolor};')
        self.meaning.setFocusPolicy(Qt.NoFocus)

        ###############################################   this is meaning of word
        self.value = QLabel(self)
        self.value.setText("")
        self.value.setFont(QFont("BOLD", 20))
        self.value.setFocusPolicy(Qt.NoFocus)
        ###############################################   enter  the word
        self.url = QLineEdit(self)
        self.url.setFont(QFont("Ariel", 12))
        self.url.setStyleSheet(f'background: {prt._lineeditcolor};')
        ###############################################   the button is  for next word
        self.git = QPushButton(self)
        self.git.setText("After")
        self.git.setFont(QFont("Ariel", 10))
        self.git.setStyleSheet(f'background: {prt._buttoncolor};')
        ###############################################  the button is  for before word
        self.before = QPushButton(self)
        self.before.setText("Before")
        self.before.setFont(QFont("Ariel", 10))
        self.before.setStyleSheet(f'background: {prt._buttoncolor};')
        ###############################################   arrangement
        self.clean_main()

        v = QVBoxLayout()
        l=QHBoxLayout()
        l.addStretch()
        l.addWidget(QLabel("<h1><i> LEARNİNG NEW LANGUAGE </i></h1>"))
        l.addStretch()
        v.addLayout(l)
        v.addStretch()

        k=QHBoxLayout()
        k.addStretch()
        k.addWidget(self.yazı)
        k.addStretch()
        v.addLayout(k)
        v.addStretch()

        label=QHBoxLayout()
        label.addStretch()
        label.addWidget(self.url)
        label.addStretch()
        v.addLayout(label)
        v.addStretch()

        value=QHBoxLayout()
        value.addStretch()
        value.addWidget(self.value)
        value.addStretch()

        v.addLayout(value)
        v.addStretch()

        meaning=QHBoxLayout()
        meaning.addStretch()
        meaning.addWidget(self.meaning)
        meaning.addStretch()

        v.addLayout(meaning)
        v.addStretch()




        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.before)
        h.addStretch()
        h.addStretch()
        h.addWidget(self.git)
        h.addStretch()


        v.addLayout(h)
        v.addStretch()

        self.git.clicked.connect(self.after_word)
        self.before.clicked.connect(self.before_word)

        self.setLayout(v)

    def after_word(self):
        if self.show_word:
            word=self.word_list[self.now_word] #.split(":")[1]
            self.control_world(word,self.url.text())
            self.show_word=False
        else:
            try:
                self.now_word+=1
                self.yazı.setText(self.word_list[self.now_word].split(":")[0])
            except:
                self.now_word=0
                self.word_list=self.word_list_upload()
                self.yazı.setText(self.word_list[self.now_word].split(":")[0])

            self.clean_main()
    def before_word(self):
        if self.show_word:
            word=self.word_list[self.now_word] #.split(":")[1]
            self.control_world(word,self.url.text())


            self.show_word=False
        else:
            try:
                self.now_word-=1
                self.yazı.setText(self.word_list[self.now_word].split(":")[0])
            except:
                self.now_word=0
                self.word_list=self.word_list_upload()
                self.yazı.setText(self.word_list[self.now_word].split(":")[0])

            self.clean_main()




    def clean_main(self):
        self.url.clear()
        self.value.clear()
        self.meaning.clear()
        self.show_word=True

    def control_world(self,word,entered_word):
        text=word.split("(")[1].replace(")","")

        word=word.split("(")[0].split(":")[1].replace(" ","")

        self.value.setText(word)
        self.meaning.setText(" "+text.split(":")[0]+"\n\n"+text.split(":")[1])

        if word.lower()==entered_word.lower():
            self.value.setStyleSheet(f'color: {prt._knowword};')
        else:
            self.value.setStyleSheet(f'color: {prt._normalwod};')