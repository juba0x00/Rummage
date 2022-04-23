# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'great.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from logging import PlaceHolder
from PyQt5 import QtCore, QtGui, QtWidgets
from modules.leaksfinder import LeaksFinder 
from modules.search import Search


class Ui_MainWindow(LeaksFinder):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 10, 791, 561))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab, clicked=lambda: self.__StartSearching())
        self.pushButton.setGeometry(QtCore.QRect(330, 50, 141, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.tab, placeholderText='Search')
        self.lineEdit.setGeometry(QtCore.QRect(200, 10, 391, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(0, 140, 391, 381))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setGeometry(QtCore.QRect(390, 140, 391, 381))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_3.setGeometry(QtCore.QRect(0, 140, 391, 381))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_4.setGeometry(QtCore.QRect(390, 140, 391, 381))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2, placeholderText='Email')
        self.lineEdit_2.setGeometry(QtCore.QRect(0, 30, 281, 34))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2, placeholderText='Phone Number')
        self.lineEdit_3.setGeometry(QtCore.QRect(0, 90, 281, 34))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2, placeholderText='User name')
        self.lineEdit_4.setGeometry(QtCore.QRect(482, 90, 301, 34))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2, placeholderText='Visa Card (First 5 Numbers-Last 5)')
        self.lineEdit_5.setGeometry(QtCore.QRect(482, 30, 301, 34))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 60, 131, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rummage"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Single Search"))
        self.pushButton_2.setText(_translate("MainWindow", "Search"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Full Search"))

    
    
    def __StartSearching(self):
        Finder = Search()
        Finder.StartSearch(self.lineEdit.text())
        res = LeaksFinder.GetResult()
        status = LeaksFinder.GetStatus()
        print('working')
        print(status)
        print(res)


        self.textBrowser.setText(self.GetStatus)
        self.textBrowser_2.setText(self.GetResult)
        

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
