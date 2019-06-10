# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tango/PycharmProjects/Med/EntryWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
#import MainWindow
#import ShowWindow
import Mediator, Patient
import SelectList

class Ui_EntryWindow(object):
    def setupUi(self, EntryWindow):
        EntryWindow.setObjectName("EntryWindow")
        EntryWindow.resize(391, 133)

        self.centralwidget = QtWidgets.QWidget(EntryWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(160, 40, 89, 25))
        self.loadButton.setObjectName("loadButton")
        self.Opnum = QtWidgets.QLineEdit(self.centralwidget)
        self.Opnum.setGeometry(QtCore.QRect(30, 40, 113, 25))
        self.Opnum.setObjectName("Opnum")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 17))
        self.label.setObjectName("label")
        self.newButton = QtWidgets.QPushButton(self.centralwidget)
        self.newButton.setGeometry(QtCore.QRect(260, 40, 89, 25))
        self.newButton.setObjectName("newButton")
        self.error = QtWidgets.QLabel(self.centralwidget)
        self.error.setGeometry(QtCore.QRect(20, 60, 300, 70))
        self.error.setObjectName("error")
        self.error.setWordWrap(True)
        EntryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EntryWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 391, 22))
        self.menubar.setObjectName("menubar")
        EntryWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EntryWindow)
        self.statusbar.setObjectName("statusbar")
        EntryWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EntryWindow)
        QtCore.QMetaObject.connectSlotsByName(EntryWindow)
        self.newButton.clicked.connect(self.newWindow)
        self.loadButton.clicked.connect(self.showWindow)

    def retranslateUi(self, EntryWindow):
        _translate = QtCore.QCoreApplication.translate
        EntryWindow.setWindowTitle(_translate("EntryWindow", "MainWindow"))
        self.loadButton.setText(_translate("EntryWindow", "Load"))
        self.label.setText(_translate("EntryWindow", "OP Number"))
        self.newButton.setText(_translate("EntryWindow", "New"))

    def newWindow(self):
        Mediator.newWindow(self,"MainWindow",EntryWindow)
        '''self.window = QtWidgets.QMainWindow()
        self.ui = MainWindow.Ui_MainWindow()
        self.ui.setupUi(self.window)
        EntryWindow.hide()
        self.window.show()'''

    def showWindow(self):
        if self.Opnum.text()=="":
            #self.error.setText("Enter OP Number to load an existing record or Click New to add a new record")
            self.window = QtWidgets.QWidget()
            self.ui = SelectList.Ui_Form()
            self.ui.setupUi(self.window)
            EntryWindow.hide()
            self.window.show()
        else:
            op_no = self.Opnum.text()
            print(op_no)
            self.patient = Mediator.fetchrecord(op_no)
            Mediator.newWindow(self,"ShowWindow",EntryWindow,self.patient)
            '''self.window = QtWidgets.QMainWindow()
            self.ui = ShowWindow.Ui_ShowWindow()
            self.ui.setupUi(self.window,self.Opnum.text())
            EntryWindow.hide()
            self.window.show()'''


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EntryWindow = QtWidgets.QMainWindow()
    ui = Ui_EntryWindow()
    ui.setupUi(EntryWindow)
    EntryWindow.show()
    sys.exit(app.exec_())
