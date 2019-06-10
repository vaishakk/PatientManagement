# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/tango/PycharmProjects/Med/selectlist.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Mediator

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(304, 240)
        self.patientList = QtWidgets.QTableView(Form)
        self.patientList.setGeometry(QtCore.QRect(20, 10, 256, 192))
        self.patientList.setObjectName("patientList")
        patientlist = Mediator.loadpatientlist()
        tablemodel = TableModel(patientlist)
        self.patientList.setModel(tablemodel)

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 210, 89, 25))
        self.pushButton.setObjectName("cancelButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Cancel"))

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, datain, parent=None, *args):
        QtCore.QAbstractTableModel.__init__(self, parent, *args)
        self.arraydata = datain
        self.headerdata = ['Op No.','Patient Name']

    def rowCount(self, parent):
        return len(self.arraydata)

    def columnCount(self, parent):
        return len(self.arraydata[0])

    def data(self, index, role):
        if not index.isValid():
            return QtCore.QVariant()
        elif role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        return QtCore.QVariant(self.arraydata[index.row()][index.column()])

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant(self.headerdata[col])
        return QtCore.QVariant()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
