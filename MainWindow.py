# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tango/PycharmProjects/Med/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Mediator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.mainwindow = MainWindow
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 67, 17))
        self.label.setObjectName("label")
        self.op_no = QtWidgets.QLineEdit(self.centralwidget)
        self.op_no.setGeometry(QtCore.QRect(80, 20, 113, 25))
        self.op_no.setObjectName("op_no")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(80, 60, 113, 25))
        self.name.setText("")
        self.name.setObjectName("name")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 41, 17))
        self.label_2.setObjectName("label_2")
        self.age = QtWidgets.QLineEdit(self.centralwidget)
        self.age.setGeometry(QtCore.QRect(250, 60, 41, 25))
        self.age.setText("")
        self.age.setObjectName("age")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 60, 31, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 60, 31, 17))
        self.label_4.setObjectName("label_4")
        self.sex = QtWidgets.QLineEdit(self.centralwidget)
        self.sex.setGeometry(QtCore.QRect(340, 60, 41, 25))
        self.sex.setText("")
        self.sex.setObjectName("sex")
        self.place = QtWidgets.QLineEdit(self.centralwidget)
        self.place.setGeometry(QtCore.QRect(450, 60, 113, 25))
        self.place.setText("")
        self.place.setObjectName("place")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 60, 41, 17))
        self.label_5.setObjectName("label_5")
        self.ph_no = QtWidgets.QLineEdit(self.centralwidget)
        self.ph_no.setGeometry(QtCore.QRect(100, 100, 211, 25))
        self.ph_no.setText("")
        self.ph_no.setObjectName("ph_no")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 81, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(150, 140, 51, 17))
        self.label_7.setObjectName("label_7")
        self.weight = QtWidgets.QLineEdit(self.centralwidget)
        self.weight.setGeometry(QtCore.QRect(210, 140, 41, 25))
        self.weight.setText("")
        self.weight.setObjectName("weight")
        self.pulse = QtWidgets.QLineEdit(self.centralwidget)
        self.pulse.setGeometry(QtCore.QRect(310, 140, 41, 25))
        self.pulse.setText("")
        self.pulse.setObjectName("pulse")
        self.bp = QtWidgets.QLineEdit(self.centralwidget)
        self.bp.setGeometry(QtCore.QRect(400, 140, 51, 25))
        self.bp.setText("")
        self.bp.setObjectName("bp")
        self.height = QtWidgets.QLineEdit(self.centralwidget)
        self.height.setGeometry(QtCore.QRect(80, 140, 51, 25))
        self.height.setText("")
        self.height.setObjectName("height")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 140, 51, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(260, 140, 41, 17))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(370, 140, 41, 17))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(10, 180, 81, 20))
        self.label_11.setObjectName("label_11")
        self.occu = QtWidgets.QLineEdit(self.centralwidget)
        self.occu.setGeometry(QtCore.QRect(100, 180, 211, 25))
        self.occu.setText("")
        self.occu.setObjectName("occu")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(10, 220, 61, 20))
        self.label_12.setObjectName("label_12")
        self.hos = QtWidgets.QLineEdit(self.centralwidget)
        self.hos.setGeometry(QtCore.QRect(80, 220, 211, 25))
        self.hos.setText("")
        self.hos.setObjectName("hos")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(520, 390, 89, 25))
        self.nextButton.setObjectName("nextButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.nextButton.clicked.connect(self.nextWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Op Num"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Age"))
        self.label_4.setText(_translate("MainWindow", "Sex"))
        self.label_5.setText(_translate("MainWindow", "Place"))
        self.label_6.setText(_translate("MainWindow", "Phone No."))
        self.label_7.setText(_translate("MainWindow", "Weight"))
        self.label_8.setText(_translate("MainWindow", "Height"))
        self.label_9.setText(_translate("MainWindow", "Pulse"))
        self.label_10.setText(_translate("MainWindow", "BP"))
        self.label_11.setText(_translate("MainWindow", "Occupation"))
        self.label_12.setText(_translate("MainWindow", "Hospital"))
        self.nextButton.setText(_translate("MainWindow", "Next"))


    def nextWindow(self):
        Mediator.readinputs(self)
        Mediator.newWindow(self,"CaseWindow",self.mainwindow,self.op_no.text())

'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''