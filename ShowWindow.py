# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tango/PycharmProjects/Med/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Mediator
from MainWindow import Ui_MainWindow

class Ui_ShowWindow(Ui_MainWindow):
    def setupUi(self, MainWindow,op_no):
        Ui_MainWindow.setupUi(self,MainWindow)
        #print(Mediator.showRecord(op_no))
        self.mainwindow = MainWindow
        (op_no,name,weight,height,pulse,bp,occu,ph_no,sex,age,place,hos) = Mediator.showRecord(op_no)[0]
        self.op_no.setReadOnly(True)
        self.op_no.setText(op_no)

        self.name.setReadOnly(True)
        self.name.setText(name)

        self.age.setReadOnly(True)
        self.age.setText(age)
        self.sex.setReadOnly(True)
        self.sex.setText(sex)
        self.place.setReadOnly(True)
        self.place.setText(place)
        self.ph_no.setReadOnly(True)
        self.ph_no.setText(ph_no)

        self.weight.setReadOnly(True)
        self.weight.setText(weight)
        self.pulse.setReadOnly(True)
        self.pulse.setText(pulse)
        self.bp.setReadOnly(True)
        self.bp.setText(bp)
        self.height.setReadOnly(True)
        self.height.setText(height)
        self.occu.setReadOnly(True)
        self.occu.setText(occu)
        self.hos.setReadOnly(True)
        self.hos.setText(hos)
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
        Mediator.newWindow(self, "CaseWindow", self.mainwindow,[self.op_no.text()])

'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
'''