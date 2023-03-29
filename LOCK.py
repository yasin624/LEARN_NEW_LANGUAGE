import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings






class menu_içerik(QWidget):
    def __init__(self):
        super().__init__()

        #########################################  main setting
        self.setWindowTitle("LOCK LEARNİNG ")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setStyleSheet("background-color:#516BEB;")
        self.setMaximumSize(500,200)
        self.setMinimumSize(500,200)

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
        self.meaning.setStyleSheet('background: white;')
        self.meaning.setFocusPolicy(Qt.NoFocus)
        self.meaning.setMaximumSize(190,100)
        self.meaning.setMaximumSize(190,100)

        ###############################################   this is meaning of word
        self.value = QLabel(self)
        self.value.setText("")
        self.value.setFont(QFont("BOLD", 20))
        self.value.setFocusPolicy(Qt.NoFocus)
        ###############################################   enter  the word
        self.url = QLineEdit(self)
        self.url.setFont(QFont("Ariel", 12))
        self.url.setStyleSheet('background: white;')
        self.url.setMaximumSize(300,30)
        self.url.setMaximumSize(300,30)
        ###############################################   the button is  for next word
        self.git = QPushButton(self)
        self.git.setText("After")
        self.git.setFont(QFont("Ariel", 10))

        ###############################################  the button is  for before word
        self.before = QPushButton(self)
        self.before.setText("I don't")
        self.before.setFont(QFont("Ariel", 10))

        ###############################################   arrangement
        self.clean_main()

        v = QVBoxLayout()

        k=QHBoxLayout()
        k.addStretch()
        k.addWidget(self.yazı)
        k.addStretch()
        k.addStretch()
        k.addStretch()
        k.addWidget(self.before)
        v.addLayout(k)

        label=QHBoxLayout()
        label.addWidget(self.url)
        label.addStretch()
        label.addWidget(self.value)
        label.addStretch()
        label.addStretch()
        label.addStretch()
        v.addLayout(label)
        v.addStretch()

        value=QHBoxLayout()
        value.addStretch()
        value.addStretch()

        v.addLayout(value)
        v.addStretch()

        meaning=QHBoxLayout()
        meaning.addWidget(self.meaning)
        meaning.addStretch()
        meaning.addStretch()
        meaning.addWidget(self.git)

        v.addLayout(meaning)
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
            self.value.setStyleSheet('color: green;')
        else:
            self.value.setStyleSheet('color: black;')

app=QApplication(sys.argv)
lock=menu_içerik()
lock.show()
sys.exit(app.exec_())