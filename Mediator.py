from PyQt5 import QtCore, QtGui, QtWidgets
import Patient
import MainWindow
import ShowWindow
import CaseWindow
import FollowupWindow
import CaseRecord

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
    patient = Patient.Patient()
    patient.addrecord(name, op_no, weight, height, pulse, occu, bp, ph_no, sex, age, place, hos)
    patient.print()
    patient.saverecord()
    patient.printall()

def showRecord(op_no):
    patient = Patient.Patient()
    #patient.printall()
    return patient.fetchrecord(op_no)

def loadpatientlist():
    patient = Patient.Patient()
    return patient.loadlist()

def newWindow(obj,windowname,curr_window,args=[]):
    obj.window = QtWidgets.QMainWindow()
    if windowname == 'MainWindow':
        obj.ui = MainWindow.Ui_MainWindow()
        obj.ui.setupUi(obj.window)
    if windowname == 'ShowWindow':
        obj.ui = ShowWindow.Ui_ShowWindow()
        obj.ui.setupUi(obj.window, args[0])
    if windowname == "CaseWindow":
        obj.ui = CaseWindow.Ui_CaseWindow()
        if len(args) == 1:
            args.append("")
        obj.ui.setupUi(obj.window,args[0],args[1])
    if windowname == "FollowupWindow":
        obj.ui = FollowupWindow.Ui_HistoryWindow()
        obj.ui.setupUi(obj.window, args[0],args[1])
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
    acu_chr = obj.acu_chr
    dr = obj.dr

    record.createRecord(self, case_no, op_no, date, acu_chr, dr, prov_diag, summary, subjective, objective, appetite, thirst,
                 sleep,
                 bowels, urine, sweat, lab, phy_men, events, totality, rubrics, comments, rx)
