import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings






class menu_içerik(QWidget):
    def __init__(self):
        super().__init__()

        self.word_list=self.word_list_upload()
        self.now_word=0
        self.show_word=True
        self.etiketler()

    def word_list_upload(self,src="word_library.dbs"):
        with open(src,"r")as file:
            words=file.read().split("\n")

        return words[:-1]

    def etiketler(self):

        word=self.word_list[self.now_word]
        ###############################################   app main icon
        self.yazı = QLabel(self)
        self.yazı.setText(word.split(":")[0])
        self.yazı.setFont(QFont("BOLD", 20))
        ###############################################   app main icon
        self.value = QLabel(self)
        self.value.setText("")
        self.value.setFont(QFont("BOLD", 20))
        ###############################################   files the url
        self.url = QLineEdit(self)
        self.url.setFont(QFont("Ariel", 12))
        ###############################################   the button dowloand files
        self.git = QPushButton(self)
        self.git.setText("NEXT")
        self.git.setFont(QFont("Ariel", 10))

        ###############################################  the button for world control
        self.control = QPushButton(self)
        self.control.setText("MEMORİZED")
        self.control.setFont(QFont("Ariel", 10))

        ###############################################   arrangement
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




        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.control)
        h.addStretch()
        h.addStretch()
        h.addWidget(self.git)
        h.addStretch()


        v.addLayout(h)
        v.addStretch()

        self.git.clicked.connect(self.next_word)

        self.setLayout(v)

    def next_word(self):
        if self.show_word:
            self.value.setText(self.word_list[self.now_word].split(":")[1])
            self.show_word=False
        else:
            try:
                self.now_word+=1
                self.yazı.setText(self.word_list[self.now_word].split(":")[0])
            except:
                self.now_word=0
                self.word_list=self.word_list_upload()
                self.yazı.setText(self.word_list[self.now_word].split(":")[0])

            self.value.clear()
            self.show_word=True





