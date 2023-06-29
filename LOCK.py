import numpy as np
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys






class menu_içerik(QMainWindow):
    def __init__(self,sleep,main_menu):
        super().__init__()

        #########################################  main setting
        self.start_parametrs(sleep)

        self.word_list=self.word_list_upload()
        self.now_word=0
        self.main_menu=main_menu
        self.show_word=True
        self.Qmenu_bar()
        self.etiketler()
    def show_mainmanu(self):
        self.main_menu.show()
        self.timer.stop()
        self.close()

    def Qmenu_bar(self):
        self.menubar=self.menuBar()
        # İlk QMenu örneği
        file_menu = self.menubar.addMenu('File')  # 'File' adında bir QMenu oluştur

        new_action = QAction('MainMenu', self)  # QAction oluştur
        file_menu.addAction(new_action)  # QAction'ı QMenu'ya ekle
        new_action.triggered.connect(self.show_mainmanu)
        self.setMenuBar(self.menubar)
    def start_parametrs(self,sleep):
        self.setWindowTitle("LOCK LEARNİNG ")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setStyleSheet("background-color:#516BEB;")
        self.setMaximumSize(500,200)
        self.setMinimumSize(500,200)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setGeometry(1420,0,500,200)
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint |  Qt.WindowStaysOnTopHint)
        self.close_button(False)
        self.wrong=0
        self.objects=[]
        self.focus_obje=0
        self.timer = QTimer(self)
        self.setSleep=1000*sleep
    def window_show(self):
        self.close_button(False)
        self.wrong=0
        self.timer.stop()
        self.show()

    def closeEvent(self, event):
        event.ignore() # pencereyi kapatma
        if event.type() == QEvent.Close:
            self.hide() # pencereyi gizle
             # bir zamanlayıcı oluştur

            self.timer.timeout.connect(self.window_show) # zamanlayıcı bittiğinde pencereyi göster
            self.timer.start(self.setSleep) # zamanlayıcıyı 120000 milisaniye (2 dakika) olarak başlat

    def word_list_upload(self,src="word_library.dbs"):
        with open(src,"r",encoding="utf-8")as file:
            words=file.read().split("\n")
        return words[:-1]

    def Layout_1(self,word):
        ###############################################   word
        self.yazı = QLabel(self)
        self.yazı.setText(word.split(":")[0])
        self.yazı.setFont(QFont("BOLD", 15))
        ###############################################   meaning of word
        self.meaning = QTextEdit(self)
        self.meaning.setText(word.split("(")[1])
        self.meaning.setFont(QFont("Ariel", 10))
        self.meaning.setStyleSheet('background: white;')
        self.meaning.setFocusPolicy(Qt.NoFocus)
        self.meaning.setMaximumSize(190,80)
        self.meaning.setMinimumSize(190,80)
        ###############################################   enter  the word
        self.url = QLineEdit(self)
        self.url.setFont(QFont("Ariel", 12))
        self.url.setStyleSheet('background: white;')
        self.url.setMaximumSize(190,30)
        self.objects.append(self.url)

        H = QVBoxLayout()
        H.addWidget(self.yazı)
        H.addWidget(self.url)
        H.addWidget(self.meaning)

        #setContentsMargins(left: int, top: int, right: int, bottom: int):
        H.setContentsMargins(0,0,0,50)
        H.setAlignment(Qt.AlignVCenter)
        return H

    def Layout_2(self):
        ###############################################   this is meaning of word
        self.value = QLabel(self)
        self.value.setText("")
        self.value.setFont(QFont("BOLD", 20))
        self.value.setFocusPolicy(Qt.NoFocus)

        H = QVBoxLayout()

        H.addWidget(self.value)

        H.setContentsMargins(0,0,0,50)
        H.setAlignment(Qt.AlignVCenter)
        return H
    def Layout_3(self):
        ###############################################   the button is  for next word
        self.git = QPushButton(self)
        self.git.setText("Show")
        self.git.setFont(QFont("Ariel", 10))
        self.objects.append(self.git)
        ###############################################   the button is  for next word


        ###############################################  the button is  for before word
        self.before = QPushButton(self)
        self.before.setText("I don't")

        self.before.setFont(QFont("Ariel", 10))


        H = QVBoxLayout()

        H.addWidget(self.before)
        H.addStretch(100)

        H.addWidget(self.git)
        H.setContentsMargins(0,0,0,5)
        H.setAlignment(Qt.AlignVCenter)
        return H

    def etiketler(self):

        word=self.word_list[self.now_word]

        Layout_1=self.Layout_1(word)
        Layout_2=self.Layout_2()
        Layout_3=self.Layout_3()



        ###############################################   arrangement
        self.objects.append(self.before)

        self.objects[self.focus_obje].setFocus()  # Düğmeye odaklan
        self.clean_main()

        v = QHBoxLayout()


        v.addLayout(Layout_1)
        v.addStretch(4)
        v.addLayout(Layout_2)
        v.addStretch(4)
        v.addLayout(Layout_3)
        v.addStretch(1)


        widget=QWidget()
        widget.setLayout(v)


        self.git.clicked.connect(self.after_word)
        self.before.clicked.connect(self.before_word)
        self.setCentralWidget(widget)


    def after_word(self):
        if self.show_word:
            word=self.word_list[self.now_word] #.split(":")[1]
            self.control_world(word,self.url.text())
            self.show_word=False

            self.git.setText("After")
        else:
            self.git.setText("Show")
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
            word=self.word_list[self.now_word]
            self.control_world(word,self.url.text())
            self.show_word=False
            self.git.setText("After")




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
            self.close_button(True)

        else:
            self.value.setStyleSheet('color: black;')
            if self.wrong==5:
                self.wrong=0
                self.close_button(True)
            else:
                self.wrong+=1
    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.git.click()
        elif event.key() ==9999999999999999 :
            print("burada tab ")
            if self.focus_obje==len(self.objects)+1:
                self.focus_obje=0
                self.objects[self.focus_obje].setFocus()

            else:
                self.objects[self.focus_obje].setFocus()
            self.focus_obje+=1
        else:
            pass
    def close_button(self,evet):

        if evet:
            self.setWindowFlag (Qt.WindowCloseButtonHint, True)
            self.show()
        else:
            self.setWindowFlag (Qt.WindowCloseButtonHint, False)


if "__main__"==__name__:
    app=QApplication(sys.argv)
    lock=menu_içerik(21)
    lock.show()
    app.exec_()
    #sys.exit(app.exec_())
