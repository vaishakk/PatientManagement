# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tango/PycharmProjects/Med/symptomswindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow,op_no):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 60, 71, 17))
        self.label_2.setObjectName("label_2")
        self.subjective = QtWidgets.QTextEdit(self.centralwidget)
        self.subjective.setGeometry(QtCore.QRect(30, 80, 581, 161))
        self.subjective.setObjectName("subjective")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 250, 131, 17))
        self.label_3.setObjectName("label_3")
        self.objective = QtWidgets.QTextEdit(self.centralwidget)
        self.objective.setGeometry(QtCore.QRect(30, 270, 581, 131))
        self.objective.setObjectName("objective")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(30, 410, 89, 25))
        self.prevButton.setObjectName("prevButton")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(520, 410, 89, 25))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Symptoms"))
        self.label_2.setText(_translate("MainWindow", "Subjective"))
        self.label_3.setText(_translate("MainWindow", "Objective Findings"))
        self.prevButton.setText(_translate("MainWindow", "Previous"))
        self.nextButton.setText(_translate("MainWindow", "Next"))




'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())'''
