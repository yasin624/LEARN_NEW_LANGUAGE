from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os
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
    ##################################################################### these codes make QSlider and QSpinBox , And append to menu ,next return this object
    def sleep_time(self,text):
        ###############################################  # hsv hue (renk aralığı) min ##### this make the min  huve value of hsv
        self.sleep_t =   self.QObje(QSpinBox(),0,180,1,(50,20),1)

        min_hue = QHBoxLayout()
        min_hue.addWidget(QLabel(text.ljust(self.fixed,self.fixed_v)))
        min_hue.addStretch()
        min_hue.addStretch()
        min_hue.addWidget(self.sleep_t)
        min_hue.addWidget(QLabel("minute"))

        return min_hue
    def yol_g(self):
        self.link=QLineEdit(self)
        self.ac=QPushButton(self)
        self.link.setText(os.getcwd())
        self.ac.setText("AÇ")

        self.ac.clicked.connect(self.konum)

        sleep_t=self.sleep_time("sleep_time")








        v = QVBoxLayout()
        k = QHBoxLayout()
        k.addWidget(QLabel("<font size=4><b> KONUM :</b></font>"))
        k.addWidget(self.link)
        k.addWidget(self.ac)




        v.addStretch()
        v.addLayout(k)
        v.addStretch()
        v.addLayout(sleep_t)
        self.setLayout(v)

    def konum(self):
        self.dosya_k=QFileDialog.getExistingDirectoryUrl()
        self.link.setText(self.dosya_k.url())