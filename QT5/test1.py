import sys

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow

from QT5.新威初版 import Ui_Form


class MainWindowTest(QMainWindow,Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
     app = QApplication(sys.argv)
     A1 = MainWindowTest()
     A1.show()
     sys.exit(app.exec_())