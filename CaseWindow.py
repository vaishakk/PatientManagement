# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tango/PycharmProjects/Med/casewindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Mediator

class Ui_CaseWindow(object):
    def setupUi(self, CaseWindow,op_no,date=""):
        CaseWindow.setObjectName("CaseWindow")
        CaseWindow.resize(640, 480)
        self.mainwindow = CaseWindow
        self.centralwidget = QtWidgets.QWidget(CaseWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 60, 101, 17))
        self.label.setObjectName("label")
        self.ac = QtWidgets.QComboBox(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(140, 60, 86, 25))
        self.ac.setObjectName("ac")
        self.ac.addItem("")
        self.ac.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 60, 91, 17))
        self.label_2.setObjectName("label_2")
        self.drincharge = QtWidgets.QLineEdit(self.centralwidget)
        self.drincharge.setGeometry(QtCore.QRect(350, 60, 113, 25))
        self.drincharge.setObjectName("drincharge")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 151, 17))
        self.label_3.setObjectName("label_3")
        self.provdiag = QtWidgets.QTextEdit(self.centralwidget)
        self.provdiag.setGeometry(QtCore.QRect(180, 130, 401, 71))
        self.provdiag.setObjectName("provdiag")
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(540, 400, 89, 25))
        self.nextButton.setObjectName("nextButton")
        self.prevButton = QtWidgets.QPushButton(self.centralwidget)
        self.prevButton.setGeometry(QtCore.QRect(10, 400, 89, 25))
        self.prevButton.setObjectName("prevButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 101, 17))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(140, 220, 441, 161))
        self.textEdit.setObjectName("textEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 20, 31, 17))
        self.label_5.setObjectName("label_5")
        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(70, 20, 110, 26))
        self.date.setCalendarPopup(True)
        self.date.setObjectName("date")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(430, 20, 51, 17))
        self.label_6.setObjectName("label_6")
        self.op_no = QtWidgets.QLineEdit(self.centralwidget)
        self.op_no.setGeometry(QtCore.QRect(490, 20, 113, 25))
        self.op_no.setReadOnly(True)
        self.op_no.setObjectName("op_no")
        self.op_no.setText(op_no)
        self.histButton = QtWidgets.QPushButton(self.centralwidget)
        self.histButton.setGeometry(QtCore.QRect(490, 60, 89, 25))
        self.histButton.setObjectName("histButton")
        CaseWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CaseWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        CaseWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CaseWindow)
        self.statusbar.setObjectName("statusbar")
        CaseWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CaseWindow)
        QtCore.QMetaObject.connectSlotsByName(CaseWindow)

        self.nextButton.clicked.connect(self.nextWindow)
        self.prevButton.clicked.connect(self.prevWindow)
        if date != "":
            self.date.setReadOnly(True)
            self.date.setDate(QtCore.QDate.fromString(date,"dd/MM/yy"))
    def retranslateUi(self, CaseWindow):
        _translate = QtCore.QCoreApplication.translate
        CaseWindow.setWindowTitle(_translate("CaseWindow", "Case Summary"))
        self.label.setText(_translate("CaseWindow", "Acute/Chronic"))
        self.ac.setItemText(0, _translate("CaseWindow", "Acute"))
        self.ac.setItemText(1, _translate("CaseWindow", "Chronic"))
        self.label_2.setText(_translate("CaseWindow", "Dr. In-Charge"))
        self.label_3.setText(_translate("CaseWindow", "Provisional diagnosis"))
        self.nextButton.setText(_translate("CaseWindow", "Next"))
        self.prevButton.setText(_translate("CaseWindow", "Previous"))
        self.label_4.setText(_translate("CaseWindow", "Case Summary"))
        self.label_5.setText(_translate("CaseWindow", "Date"))
        self.label_6.setText(_translate("CaseWindow", "Op No."))
        self.histButton.setText(_translate("CaseWindow", "History"))

    def nextWindow(self):
        Mediator.newWindow(self,"FollowupWindow",self.mainwindow,args=[self.op_no.text(),self.date.text()])
    def prevWindow(self):
        Mediator.newWindow(self,"ShowWindow",self.mainwindow,args=[self.op_no.text()])



'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CaseWindow = QtWidgets.QMainWindow()
    ui = Ui_CaseWindow()
    ui.setupUi(CaseWindow)
    CaseWindow.show()
    sys.exit(app.exec_())'''
