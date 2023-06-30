import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings
import parameters as prt






class menu_içerik(QWidget):
    def __init__(self,word_src=prt._main_word_list):
        super().__init__()

        self.word_list=self.word_list_upload(word_src)
        self.now_word=0
        self.word_revers=True
        self.show_word=True
        self.etiketler()

    def word_list_upload(self,src=prt._main_word_list):
        with open(src,"r",encoding="utf-8")as file:
            words=file.read().split("\n")
        return words[:-1]

    def etiketler(self):

        ###############################################   word
        self.yazı = QLabel(self)
        self.yazı.setFont(QFont("BOLD", 18))
        word=self.word_list[self.now_word].split("(")[1].replace(")","").split(":")[0]
        self.yazı.setText(word)
        ###############################################   this is meaning of word
        self.value = QLabel(self)
        self.value.setText("")
        self.value.setFont(QFont("BOLD", 18))
        ###############################################   enter  the word
        self.url = QTextEdit(self)
        self.url.setFont(QFont("Ariel", 12))
        self.url.setStyleSheet(f'background: {prt._texteditcolor};')
        ###############################################   the button is  for next word
        self.git = QPushButton(self)
        self.git.setText("Show")
        self.git.setFont(QFont("Ariel", 10))
        self.git.setStyleSheet(f'background: {prt._buttoncolor};')
        ###############################################  the button is  for before word
        self.before = QPushButton(self)
        self.before.setText("Before")
        self.before.setFont(QFont("Ariel", 10))
        self.before.setStyleSheet(f'background: {prt._buttoncolor};')
        ###############################################  the button is  for before word
        self.reverse = QPushButton(self)
        self.reverse.setText("reverse")
        self.reverse.setFont(QFont("Ariel", 10))
        self.reverse.setStyleSheet(f'background: {prt._buttoncolor};')

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





        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.before)
        h.addStretch()
        h.addWidget(self.reverse)
        h.addStretch()
        h.addWidget(self.git)
        h.addStretch()


        v.addLayout(h)
        v.addStretch()

        self.git.clicked.connect(self.after_word)
        self.before.clicked.connect(self.before_word)
        self.reverse.clicked.connect(self.tr_en_reverse)

        self.setLayout(v)
    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.git.click()
    def tr_en_reverse(self):
        self.word_revers=not self.word_revers
        self.after_word("print")
    def after_word(self,mode=None):
        if mode=="print":
            word=self.word_list[self.now_word].split("(")[1].replace(")","").split(":")[0 if self.word_revers else 1]
            word=word.split(" ")
            if len(word)>4:
                haft=int(len(word)/1.5)
                part1=" ".join(word[:haft])
                part2=" ".join(word[haft:])
                text="<br>".join([part1,part2])
            else:
                text=" ".join(word)
            self.yazı.setText(text)

        elif self.show_word:
            self.control_world(self.word_list[self.now_word],self.url.toPlainText())
            self.git.setText("After")
            self.show_word=False

        else:
            self.git.setText("Show")
            try:
                self.now_word+=1
            except:
                self.now_word=0
            word=self.word_list[self.now_word].split("(")[1].replace(")","").split(":")[0 if self.word_revers else 1]
            word=word.split(" ")
            if len(word)>4:
                haft=int(len(word)/1.5)
                part1=" ".join(word[:haft])
                part2=" ".join(word[haft:])
                text="<br>".join([part1,part2])
            else:
                text=" ".join(word)
            self.yazı.setText(text)
            self.clean_main()
    def before_word(self):

        if self.show_word:
            word=self.word_list[self.now_word] #.split(":")[1]

            self.control_world(word,self.url.toPlainText())


            self.show_word=False
        else:
            try:

                self.now_word-=1
            except:
                self.now_word=0
            word=self.word_list[self.now_word].split("(")[1].replace(")","").split(":")[0 if self.word_revers else 1]
            word=word.split(" ")
            if len(word)>4:
                haft=int(len(word)/1.5)
                part1=" ".join(word[:haft])
                part2=" ".join(word[haft:])
                text="<br>".join([part1,part2])
            else:
                text=" ".join(word)

            self.yazı.setText(text)
            self.clean_main()




    def clean_main(self):
        self.url.clear()
        self.value.clear()
        self.show_word=True

    def control_world(self,word,entered_word):
        word=word.split("(")[1].replace(")","").split(":")[1 if self.word_revers else 0].split(" ")
        entered_word=entered_word.split(" ")
        write_word=[]
        next=0
        for i in word:
            if i=="":
                next-=1
                pass
            else:
                try:
                    if i.lower()==entered_word[next].lower():
                        write_word.append(f"<span style='color:{prt._knowword};'>{i}</span> ")

                    elif entered_word[next].lower() in word and entered_word!="":
                        write_word.append(f"<span style='color:blue;'>{i}</span> ")
                    else:
                        write_word.append(f"<span style='color:{prt._normalwod};'>{i}</span> ")
                except:
                    write_word.append(f"<span style='color:{prt._normalwod};'>{i}</span> ")
            next+=1

        if len(write_word)>4:
            haft=int(len(write_word)/1.5)
            part1=" ".join(write_word[:haft])
            part2=" ".join(write_word[haft:])
            text="<br>".join([part1,part2])
        else:
            text=" ".join(write_word)
        self.value.setText(text)
