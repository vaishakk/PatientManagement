from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import Patient
import MainWindow
import ShowWindow
import CaseWindow
import FollowupWindow
import CaseRecord

patient = Patient.Patient()
def readinputs(obj):
    name = obj.name.text()
    op_no = obj.op_no.text()
    weight = obj.weight.text()
    height = obj.height.text()
    pulse = obj.pulse.text()
    occu = obj.occu.text()
    bp = obj.bp.text()
    ph_no = obj.ph_no.text()
    sex = obj.sex.text()
    age = obj.age.text()
    place = obj.place.text()
    hos = obj.hos.text()
    #patient = Patient.Patient()
    patient.addrecord([name, op_no, weight, height, pulse, occu, bp, ph_no, sex, age, place, hos])
    patient.print()
    patient.saverecord()
    return patient
    #patient.printall()

def showRecord(op_no):
    #patient = Patient.Patient()
    #patient.printall()
    return fetchrecord(op_no)

def fetchrecord(op_no):
    print(op_no)
    connection = sqlite3.connect("DB.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Patient WHERE OP_Number = {val}".format(val = op_no))
    result = cursor.fetchall()
    patient.addrecord(result[0])
    return patient

def loadpatientlist():
    patient = Patient.Patient()
    return patient.loadlist()

def newWindow(obj,windowname,curr_window,pat=None):
    obj.window = QtWidgets.QMainWindow()
    if windowname == 'MainWindow':
        obj.ui = MainWindow.Ui_MainWindow()
        obj.ui.setupUi(obj.window)
    if windowname == 'ShowWindow':
        obj.ui = ShowWindow.Ui_ShowWindow()
        obj.ui.setupUi(obj.window, pat)
    if windowname == "CaseWindow":
        obj.ui = CaseWindow.Ui_CaseWindow()
        #if len(args) == 1:
        #   args.append("")
        obj.ui.setupUi(obj.window,pat)
    if windowname == "FollowupWindow":
        obj.ui = FollowupWindow.Ui_HistoryWindow()
        obj.ui.setupUi(obj.window, pat)
    #print(args[0])
    #obj.ui.setupUi(obj.window,args[0])
    curr_window.hide()
    obj.window.show()

def showCaseRecord(op_no):
    record = CaseRecord.CaseRecord()
    #patient.printall()
    return record.fetchrecord(op_no)

def readCaseRecord(obj):
    record = CaseRecord.CaseRecord()
    case_no = record.getNewRecordNumber()
    op_no = obj.op_no.text()
    date = obj.date.text()
    acu_chr = obj.ac.currentText()
    dr = obj.drincharge.text()
    prov_diag = obj.provdiag.toPlainText()
    summary = obj.summary.toPlainText()
    record.createRecord(case_no, op_no, date, acu_chr, dr, prov_diag, summary)#, subjective, objective, appetite, thirst,
                 #sleep, bowels, urine, sweat, lab, phy_men, events, totality, rubrics, comments, rx)
    obj.patient.addCaseRecord(record)
