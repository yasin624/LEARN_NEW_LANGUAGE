import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings
import parameters as prt






class menu_içerik(QWidget):
    def __init__(self,word_src=prt._main_word_list):
        super().__init__()

        self.translate_type="EN"

        self.word_list=self.word_list_upload(word_src)
        self.etiketler()

    def word_list_upload(self,src=prt._main_word_list):
        with open(src,"r",encoding="utf-8")as file:
            words=file.read().split("\n")
        return words[:-1]

    def etiketler(self):
        ###############################################   meaning of word
        self.meaning = QTextEdit(self)
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
        self.git.setText("Translate")
        self.git.setFont(QFont("Ariel", 10))
        self.git.setStyleSheet(f'background: {prt._buttoncolor};')
        ###############################################  the button is  for before word
        self.before = QPushButton(self)
        self.before.setText("TR->EN")
        self.before.setFont(QFont("Ariel", 10))
        self.before.setStyleSheet(f'background: {prt._buttoncolor};')
        ###############################################  fisrt start functions
        self.change()
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
    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.git.click()
    def after_word(self):
        self.control_world(self.word_list,self.url.text().replace(" ",""))


    def change(self):
        before=self.url.text()
        self.url.setText(self.value.text())
        self.value.setText(before)

        if self.before.text()=="TR->EN":
            self.before.setText("EN->TR")
            self.translate_type="EN"
            self.git.setText("TRANSLATE")
        else:
            self.translate_type="TR"
            self.before.setText("TR->EN")
            self.git.setText("ÇEVİR")

    def control_world(self,words,entered_word):

        if self.url.text()=="":
            return None

        stop=False
        for word in words:
            if self.translate_type=="EN":
                trans=word.split("(")[0].split(":")
                for i in trans[0].split(","):

                    if entered_word.lower()==i.lower():
                        text=word.split("(")[1].replace(")","")
                        self.value.setText(trans[1])
                        self.meaning.setText(" "+text.split(":")[0]+"\n\n"+text.split(":")[1])
                        stop=True
                        break
                    else:

                        self.value.setText("wrong word")

            elif self.translate_type=="TR":
                trans=word.split("(")[0].split(":")
                for i in trans[1].split(","):
                    if entered_word.lower()==i.replace(" ","").lower():
                        text=word.split("(")[1].replace(")","")
                        self.value.setText(trans[0])
                        self.meaning.setText(" "+text.split(":")[1]+"\n\n"+text.split(":")[0])
                        stop=True
                        break
                    else:
                        self.value.setText("hatalı kelime")
            else:
                print(" dil algılanmadı")

            if stop:
                break



        if word.lower()==entered_word.lower():
            self.value.setStyleSheet('color: green;')
        else:
            self.value.setStyleSheet('color: black;')