import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings






class menu_içerik(QWidget):
    def __init__(self):
        super().__init__()

        self.translate_type="TR"
        self.word_list=self.word_list_upload()
        self.etiketler()

    def word_list_upload(self,src="word_library.dbs"):
        with open(src,"r",encoding="utf-8")as file:
            words=file.read().split("\n")
        return words[:-1]

    def etiketler(self):
        ###############################################   meaning of word
        self.meaning = QTextEdit(self)
        self.meaning.setFont(QFont("Ariel", 10))
        self.meaning.setStyleSheet('background: white;')
        self.meaning.setFocusPolicy(Qt.NoFocus)

        ###############################################   this is meaning of word
        self.value = QLabel(self)
        self.value.setText("")
        self.value.setFont(QFont("BOLD", 20))
        self.value.setFocusPolicy(Qt.NoFocus)
        ###############################################   enter  the word
        self.url = QLineEdit(self)
        self.url.setFont(QFont("Ariel", 12))
        self.url.setStyleSheet('background: white;')
        ###############################################   the button is  for next word
        self.git = QPushButton(self)
        self.git.setText("Translate")
        self.git.setFont(QFont("Ariel", 10))

        ###############################################  the button is  for before word
        self.before = QPushButton(self)
        self.before.setText("TR->EN")
        self.before.setFont(QFont("Ariel", 10))

        ###############################################   arrangement

        v = QVBoxLayout()
        l=QHBoxLayout()
        l.addStretch()
        l.addWidget(QLabel("<h1><i> LEARNİNG NEW LANGUAGE </i></h1>"))
        l.addStretch()
        v.addLayout(l)
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




        h = QVBoxLayout()
        h.addWidget(self.before)
        h.addStretch()
        h.addWidget(self.git)

        ort = QHBoxLayout()
        ort.addStretch()
        ort.addLayout(h)
        ort.addStretch()


        v.addLayout(ort)
        v.addStretch()

        self.git.clicked.connect(self.after_word)
        self.before.clicked.connect(self.change)
        self.setLayout(v)

    def after_word(self):
        print(" burdaaaa")
        self.control_world(self.word_list,self.url.text())


    def change(self):
        if self.before.text()=="TR->EN":
            self.before.setText("EN->TR")
            self.translate_type="EN"
        else:
            self.translate_type="TR"
            self.before.setText("TR->EN")

    def control_world(self,words,entered_word):
        print(words)
        for word in words:
            print("word : ",word)
            text=word.split("(")[1].replace(")","")
            print("text :" ,text)
            word=word.split("(")[0].split(":")[1].replace(" ","")




            self.value.setText(word)
            self.meaning.setText(" "+text.split(":")[0]+"\n\n"+text.split(":")[1])



            break

        if word.lower()==entered_word.lower():
            self.value.setStyleSheet('color: green;')
        else:
            self.value.setStyleSheet('color: black;')