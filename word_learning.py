from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,main_menu,setings,random,add_word,sentence,translate



class setup(QMainWindow):
    def __init__(self):
        super().__init__()
        ##########################################################  table
        self.WORD = add_word.ADD_WORLD()
        self.WORD.__init__()
        self.main_m = main_menu.menu_içerik()
        self.main_m.__init__()
        self.sentence = sentence.menu_içerik()
        self.sentence.__init__()
        self.translate = translate.menu_içerik()
        self.translate.__init__()
        self.yol_k = setings.yol()
        ######################################################  setup settings
        self.setWindowTitle("WORD LEARNİNG ")
        self.setWindowIcon(QIcon("logo.ico"))
        self.setStyleSheet("background-color:#516BEB;")
        self.setMaximumSize(600,900)
        self.setMinimumSize(500,700)

        ######################################################## they parameters
        self.içerik()

    def içerik(self):
        #######################################################  text menu
        """
        menu=self.menuBar()
        self.dosya=menu.addMenu("file")
        self.konum=QAction("save")
        self.dosya.addAction(self.konum)"""

        ######################################################  table menu
        self.tablo=QTabWidget()
        self.tablo.tablo1=QWidget()
        self.tablo.tablo2=QWidget()
        self.tablo.tablo3=QWidget()
        self.tablo.tablo4=QWidget()
        self.tablo.tablo5=QWidget()

        self.tablo.addTab(self.tablo.tablo1,"WORD_L ")
        self.tablo.addTab(self.tablo.tablo2, "SENTENCE_L")
        self.tablo.addTab(self.tablo.tablo3, "TRANSLATE")
        self.tablo.addTab(self.tablo.tablo4, "ADD WORD")
        self.tablo.addTab(self.tablo.tablo5, "SETİNG")

        self.tablo.setStyleSheet("background-color:#516BEB;")
        #####################################################  satatus bar (info the bar)
        self.status=QStatusBar()
        self.setStatusBar(self.status)
        self.status.showMessage("Tüm hakları saklıdır © 2020 | yalcınyazılımcılık")



        ###################################################   full the tables
        self.tab1()
        self.tab2()
        self.tab3()
        self.tab4()
        self.tab5()
        self.setCentralWidget(self.tablo)
        ################################################################### file download location
        #self.dosya.triggered.connect(self.konum_belirle)


    def tab1(self):
        ############################################################### main_menu fulling
        v = QVBoxLayout()
        v.addWidget(self.main_m)
        self.tablo.tablo1.setLayout(v)
    def tab2(self):
        v = QVBoxLayout()
        v.addWidget(self.sentence)
        self.tablo.tablo2.setLayout(v)
    def tab3(self):
        v = QVBoxLayout()
        v.addWidget(self.translate)
        self.tablo.tablo3.setLayout(v)

    def tab4(self):
        v = QVBoxLayout()
        v.addWidget(self.WORD)
        self.tablo.tablo4.setLayout(v)
    def tab5(self):
        ############################################################### the settings fulling
        v = QVBoxLayout()
        v.addWidget(self.yol_k)
        v.addStretch()
        self.tablo.tablo5.setLayout(v)


    def konum_belirle(self,dene):
        # cur_index = self.tabWidget.currentIndex() tablo indexleri
        if dene.text()=="Dowland Local":
            self.tablo.setCurrentIndex(2)
        elif dene.text() == "Dowland files":
            self.tablo.setCurrentIndex(1)


app=QApplication(sys.argv)
dowland=setup()
dowland.show()
sys.exit(app.exec_())
