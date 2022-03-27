
import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QAction
from PyQt5.QtWidgets import qApp
from PyQt5.QtGui import QIcon

class Ex(QMainWindow):

    def __init__(self):
        super(Ex, self).__init__()
        self.initUI()

    def initUI(self):
        exitAct = QAction(QIcon("exit.png"),'&Exit',self)
        print(exitAct)
        exitAct.setShortcut("ctrl+q")
        exitAct.setStatusTip('tuichu应用')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,399,200)
        self.setWindowTitle('决赛你电脑的')
        self.show()

app = QApplication(sys.argv)
demo1 = Ex()
sys.exit(app.exec_())

