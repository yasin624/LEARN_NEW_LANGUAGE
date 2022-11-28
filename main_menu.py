from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,setings



class menu_içerik(QWidget):
    def __init__(self):
        super().__init__()
        self.etiketler()

    def etiketler(self):
        ###############################################   app main icon
        self.yazı = QLabel(self)
        self.yazı.setText("WORLD")
        self.yazı.setFont(QFont("BOLD", 20))
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


        h = QHBoxLayout()
        h.addStretch()
        h.addWidget(self.control)
        h.addStretch()
        h.addStretch()
        h.addWidget(self.git)
        h.addStretch()

        v.addLayout(h)
        v.addStretch()

        self.setLayout(v)


