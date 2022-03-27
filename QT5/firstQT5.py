import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
import urllib.request as request


class MyTableWidget(QTableWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(400)
        self.setColumnCount(1)
        self.setColumnWidth(0, 400)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.itemClicked.connect(self.handleItemClick)

    def handleItemClick(self, item):
        print(item.text())


class MainScene(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.grid = QGridLayout()
        self.setLayout(self.grid)
        self.novelNameEdit = QLineEdit("http://xs.dmzj.com/2012/index.shtml")
        self.searchBtn = QPushButton("Search")
        self.novelText = QLabel("Content")
        self.tableWidget = MyTableWidget()

        self.grid.addWidget(self.novelNameEdit, 0, 0, 1, 2)
        self.grid.addWidget(self.searchBtn, 0, 2, 1, 1)
        self.grid.addWidget(self.tableWidget, 1, 0, 2, 2)
        self.grid.addWidget(self.novelText, 1, 2, 1, 1)
        self.resize(1024, 600)
        self.searchBtn.clicked.connect(self.searchBtnClick)

    def searchBtnClick(self):
        self.tableWidget.clear()
        Sp = Spider.Catalogue()
        content = request.urlopen(self.novelNameEdit.text()).read()
        content = str(content, 'utf-8')
        Sp.feed(content)
        Sp.close()
        catalogueCount = len(Sp.catalogueList)
        self.tableWidget.setRowCount(catalogueCount)
        for index, item in enumerate(Sp.catalogueList):
            self.tableWidget.setItem(index, 0, QTableWidgetItem(item))


if __name__ == "__main__":
    App = QApplication(sys.argv)
    MS = MainScene()
    MS.show()
    sys.exit(App.exec_())