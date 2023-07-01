from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys,os,main_menu,setings,random,add_word,sentence,translate
from LOCK import menu_içerik
import parameters as prt
import importlib
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

        self.start_parametrs()

        ######################################################## they parameters
        self.içerik()
    def start_parametrs(self):
        ######################################################  setup settings
        self.setWindowTitle("WORD LEARNİNG ")
        self.setWindowIcon(QIcon("logo.ico"))


        self.setStyleSheet(f"background-color:{prt._background};")



        self.setMaximumSize(600,900)
        self.setMinimumSize(500,700)
        self.timer = QTimer(self)

        self.lock=None
    def tablo_make(self):

        #######################################################  text menu

        self.timer.timeout.connect(self.activite) # zamanlayıcı bittiğinde pencereyi göster
        self.timer.start(1000) # zamanlayıcıyı 120000 milisaniye (2 dakika) olarak başlat

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

        # QTabBar'ı alın
        tab_bar = self.tablo.tabBar()

        # Sekmelerin düğme stilini özelleştirin
        tab_bar.setStyleSheet("""
            QTabBar::tab:selected { background-color: #8099E1; color: white; }
            QTabBar::tab:!selected { background-color: #516BEB; color: white; }
        """)

        style = QStyleFactory.create("Fusion")
        self.tablo.setStyle(style)
        # QTabWidget'ın stil sayfasını alın
        #self.tablo.setStyleSheet()


    def içerik(self):
        self.tablo_make()
        #####################################################  satatus bar (info the bar)
        self.status=QStatusBar()
        self.setStatusBar(self.status)
        self.status.addWidget(QLabel(f"     Tüm hakları saklıdır © 2020 | yalcınyazılımcılık  {' '*90}"))

        ###################################################   full the tables
        self.tab1()
        self.tab2()
        self.tab3()
        self.tab4()
        self.tab5()
        self.setCentralWidget(self.tablo)
        ################################################################### file download location
        #self.dosya.triggered.connect(self.konum_belirle)
        self.yol_k.exit.clicked.connect(self.Setup_Exit)
        self.yol_k.reset.clicked.connect(self.Setup_Reset)


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

    def activite(self):
        if self.isActiveWindow():
            if "lock" in dir(self): del self.lock
    def konum_belirle(self,dene):
        # cur_index = self.tabWidget.currentIndex() tablo indexleri
        if dene.text()=="Dowland Local":
            self.tablo.setCurrentIndex(2)
        elif dene.text() == "Dowland files":
            self.tablo.setCurrentIndex(1)

    def closeEvent(self, event):
        if event.type() == QEvent.Close:
            self.lock=menu_içerik(self,self.yol_k.sleep_t.text(),self.yol_k.hard.isChecked(),self.yol_k.reverse.isChecked())
            self.close()
            self.lock.show()

    def Setup_Exit(self):
        sys.exit(app.exec_())
    def Setup_Reset(self):
        reset_str="""_main_word_list="main_word_list.dbs"
_dont_know_word_list="dont_know_word.dbs"
_activ_word=_main_word_list



_background="#516BEB"
_texteditcolor="#8099E1"
_lineeditcolor="#8099E1"
_buttoncolor="#8099E1"



_knowword="#FFA500"
_normalwod="#000000"

_word_local=0
_sleep_time=[0,0,5]"""
        with open("parameters.py","w")as file:
            file.write(reset_str)
        with open(prt._dont_know_word_list,"w")as file:
            file.write("")
        importlib.reload(setings)

        message_box = QMessageBox()
        message_box.setText("Basarılı bir şekilde reset atıldı.")
        message_box.exec_()
app=QApplication(sys.argv)
dowland=setup()
dowland.show()
sys.exit(app.exec_())
