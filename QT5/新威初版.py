# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QColor
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QHeaderView, QTableWidgetItem


def query(customerName,area,matterCode,matterDes):
    data=[]
    conn = sqlite3.connect('./sqlite3/data.db')
    cursor = conn.cursor()
    cursor = cursor.execute(f"SELECT *  from info where customerName like'%{customerName}%' and area like '%{area}%' and mattercode like '%{matterCode}%' and matterDes like '%{matterDes}%'")
    for row in cursor:
        data.append(row)
    return data


class Ui_Form(object):
    def setupUi(self, Form, 供应商代码=None):
        Form.setObjectName("Form")
        Form.resize(1024, 768)

        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 30, 867, 273))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMaximumSize(QtCore.QSize(400, 300))
        font = QtGui.QFont()
        font.setFamily("幼圆")
        font.setPointSize(28)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label0 = QtWidgets.QLabel(self.widget)
        self.label0.setObjectName("label0")
        self.horizontalLayout.addWidget(self.label0)
        self.lineEdit0 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit0.setObjectName("lineEdit0")
        self.horizontalLayout.addWidget(self.lineEdit0)
        self.label1 = QtWidgets.QLabel(self.widget)
        self.label1.setObjectName("label13")
        self.horizontalLayout.addWidget(self.label1)
        self.lineEdit1 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit1.setObjectName("lineEdit1")
        self.horizontalLayout.addWidget(self.lineEdit1)
        self.label2 = QtWidgets.QLabel(self.widget)
        self.label2.setObjectName("label2")
        self.horizontalLayout.addWidget(self.label2)
        self.lineEdit2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit2.setObjectName("lineEdit2")
        self.horizontalLayout.addWidget(self.lineEdit2)
        self.label3 = QtWidgets.QLabel(self.widget)
        self.label3.setObjectName("label3")
        self.horizontalLayout.addWidget(self.label3)
        self.lineEdit3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit3.setObjectName("lineEdit3")
        self.horizontalLayout.addWidget(self.lineEdit3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton.clicked.connect(self.buttonClicked)

        # self.verticalLayout = QtWidgets.QVBoxLayout()
        # self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(1000)
        # 列宽自动分配
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置可以手动调整列宽
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
        #设置某一列完整显示，其他自动分配，及其影响性能
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # # self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        # # self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        # # self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeToContents)
        # # self.tableWidget.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeToContents)
        # # self.tableWidget.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeToContents)
        # # self.tableWidget.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeToContents)
        # # self.tableWidget.horizontalHeader().setSectionResizeMode(7, QHeaderView.ResizeToContents)
        #手动分配列宽
        # self.tableWidget.setColumnWidth(0, 40)
        # self.tableWidget.setColumnWidth(1, 200)
        # self.tableWidget.setColumnWidth(2, 200)
        # self.tableWidget.setColumnWidth(3, 40)
        # self.tableWidget.setColumnWidth(4, 200)
        # self.tableWidget.setColumnWidth(5, 200)
        # self.tableWidget.setColumnWidth(6, 40)
        # self.tableWidget.setColumnWidth(7, 200)
        # self.tableWidget.setColumnWidth(8, 200)
        # self.tableWidget.setColumnWidth(9, 200)

        self.tableWidget.setHorizontalHeaderLabels(['id','过账日期','客户/供应商代码','客户/供应商名称','省级','地市','物料编号','物料/服务描述','数量','销售员姓名'])
        # 添加表头样式
        self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{background-color:rgb(155, 194, 230);font:11pt '宋体';color: black;};")
        # 垂直表格头是否隐藏
        self.tableWidget.verticalHeader().setVisible(True)

        # self.verticalLayout.addWidget(self.tableWidget)
        self.retranslateUi(Form)

        gridLayout_2 = QGridLayout()
        gridLayout_2.setSpacing(10)
        gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        # gridLayout_2.addLayout(self.verticalLayout, 2, 0, 1, 1)
        gridLayout_2.addWidget(self.tableWidget)
        Form.setLayout(gridLayout_2)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "数据查询"))
        self.label.setText(_translate("Form", "新威数据查询"))
        self.label0.setText(_translate("Form", "按客户名称"))
        self.label1.setText(_translate("Form", "按地区"))
        self.label2.setText(_translate("Form", "按型号"))
        self.label3.setText(_translate("Form", "按描述"))
        self.pushButton.setText(_translate("Form", "查询数据"))

    def buttonClicked(self):
        self.tableWidget.clear()
        customerName=self.lineEdit0.text()
        area = self.lineEdit1.text()
        matterCode = self.lineEdit2.text()
        matterDes = self.lineEdit3.text()
        data=query(customerName,area,matterCode,matterDes)
        row=len(data)
        col=len(data[0])
        for i in range(row):
            for j in range(col):
                temp=str(data[i][j])
                dat=QTableWidgetItem(temp)
                self.tableWidget.setItem(i,j,dat)
                # 每隔一行变换一行的颜色
                # if i%2==0:
                #     self.tableWidget.item(i,j).setBackground(QBrush(QColor(155, 180, 200)))

app = QApplication([])
window = QWidget()
ui=Ui_Form()
ui.setupUi(window)
window.show()
app.exec_()