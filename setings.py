from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os
import parameters as prt
from PyQt5.QtCore import QTime

class yol(QWidget):
    def __init__(self):
        super().__init__()
        self.fixed=8 ############################ this code sets object sitrings to justify left and this  sets lengs of setrings
        self.fixed_v=" " ######################### this code shows which type to set the length of the texts
        self.yol_g()
        ######################################################################### these are  all function of the objects like QSlider,QSpinBox
    def QObje(self,obje,min,max,step,size=(100,10),value=0,togather=None):
        # Kaydırma tuşunun hareket edeceği minimum ve maksimum değerlerini ayarlayın
        o=obje
        o.setMinimum(min)
        o.setMaximum(max)
        # Kaydırma tuşunun ne kadar adımda hareket edeceğini ayarlayın
        o.setSingleStep(step)
        o.setFixedWidth(size[0])
        o.setFixedHeight(size[1])
        o.setValue(value)
        return o

    def hard_mod(self,text):
        self.hard=QCheckBox()

        self.hard.setMinimumSize(80,50)
        self.hard.setMinimumWidth(50)
        self.hard.setStyleSheet(f"color:{prt._lineeditcolor};")



        H = QHBoxLayout()

        label=QLabel(f"<font size=4><b> {text} :</b></font>")
        label.setFont(QFont("BOLD", 10))
        H.addWidget(label)
        H.addStretch(30)
        H.addStretch(30)
        H.addWidget(self.hard)
        H.addStretch(1)
        return H
    def reverse_mod(self,text):
        self.reverse=QCheckBox()

        self.reverse.setMinimumSize(80,50)
        self.reverse.setMinimumWidth(50)
        self.reverse.setStyleSheet(f"color:{prt._lineeditcolor};")



        H = QHBoxLayout()

        label=QLabel(f"<font size=4><b> {text} :</b></font>")
        label.setFont(QFont("BOLD", 10))
        H.addWidget(label)
        H.addStretch(30)
        H.addStretch(30)
        H.addWidget(self.reverse)
        H.addStretch(1)
        return H
    def Quit(self,text):
        self.exit=QPushButton(self)
        self.exit.setStyleSheet(f'background: {prt._buttoncolor};')
        self.exit.setText("EXİT")


        label=QLabel(f"<font size=4><b> {text} :</b></font>")
        label.setFont(QFont("BOLD", 10))

        H = QHBoxLayout()
        H.addWidget(label)
        H.addStretch(80)
        H.addWidget(self.exit)
        H.addStretch(1)
        return H
    def Reset(self,text):
        self.reset=QPushButton(self)
        self.reset.setStyleSheet(f'background: {prt._buttoncolor};')
        self.reset.setText("Reset")


        label=QLabel(f"<font size=4><b> {text} :</b></font>")
        label.setFont(QFont("BOLD", 10))

        H = QHBoxLayout()
        H.addWidget(label)
        H.addStretch(80)
        H.addWidget(self.reset)
        H.addStretch(1)
        return H
    ##################################################################### these codes make QSlider and QSpinBox , And append to menu ,next return this object
    def sleep_time(self,text):
        ###############################################  # hsv hue (renk aralığı) min ##### this make the min  huve value of hsv
        # QDateTimeEdit örneğini oluşturun
        self.sleep_t = QDateTimeEdit()
        # Zaman formatını ayarlayın
        self.sleep_t.setDisplayFormat("hh:mm:ss")

        self.sleep_t.setStyleSheet(f"background-color:{prt._lineeditcolor};")
        self.sleep_t.setMinimumSize(80,30)
        self.sleep_t.setTime(QTime(prt._sleep_time[0],
                                   prt._sleep_time[1],
                                   prt._sleep_time[2]))



        label=QLabel(f"<font size=4><b> {text} :</b></font>")
        label.setFont(QFont("BOLD", 10))
        min_hue = QHBoxLayout()
        min_hue.addWidget(label)
        min_hue.addStretch(30)
        min_hue.addWidget(self.sleep_t)

        return min_hue

    def localetion(self,text):
        self.link=QLineEdit(self)
        self.link.setStyleSheet(f'background: {prt._lineeditcolor};')

        self.ac=QPushButton(self)
        self.ac.setStyleSheet(f'background: {prt._buttoncolor};')

        self.link.setText(os.getcwd())
        self.ac.setText("AÇ")

        self.ac.clicked.connect(self.konum)

        H = QHBoxLayout()
        H.addWidget(QLabel(f"<font size=4><b> {text} :</b></font>"))
        H.addWidget(self.link)
        H.addWidget(self.ac)

        return H
    def line(self):
        line = QFrame()
        line.setFrameShape(QFrame.HLine)  # Yatay çizgi
        line.setFrameShadow(QFrame.Sunken)  # Gölge efekti
        line.setStyleSheet(f"background-color: {prt._buttoncolor};")
        return line
    def yol_g(self):

        localetion=self.localetion("KONUM")
        sleep_t=self.sleep_time("Sleep_Time")

        hard=self.hard_mod("Hard_Mode")
        reverse=self.reverse_mod("Reverse take words")
        qut=self.Quit("Exit All Setup ")
        reset=self.Reset("Reset All Setup")


        v = QVBoxLayout()
        v.addStretch(2)

        v.addLayout(localetion)
        v.addStretch(2)
        v.addWidget(self.line())
        v.addStretch(5)
        v.addLayout(sleep_t)
        v.addStretch(1)
        v.addLayout(hard)
        v.addStretch(1)
        v.addLayout(reverse)
        v.addStretch(50)
        v.addLayout(reset)
        v.addStretch(1)
        v.addLayout(qut)
        self.setLayout(v)

    def konum(self):
        self.dosya_k=QFileDialog.getExistingDirectoryUrl()
        self.link.setText(self.dosya_k.url())