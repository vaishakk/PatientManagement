import sqlite3
class CaseRecord:
    def createRecord(self,case_no,op_no,date,acu_chr,dr,prov_diag,summary,subjective="",objective="",appetite="",thirst="",
                     sleep="",bowels="",urine="",sweat="",lab="",phy_men="",events="",totality="",rubrics="",comments="",rx=""):
        self.case_no = case_no
        self.op_no = op_no
        self.date = date
        self.acu_chr = acu_chr
        self.dr = dr
        self.prov_diag = prov_diag
        self.summary = summary
        self.subjective = subjective
        self.objective = objective
        self.appetite = appetite
        self.thirst = thirst
        self.sleep = sleep
        self.bowels = bowels
        self.urine = urine
        self.sweat = sweat
        self.lab = lab
        self.phy_men = phy_men
        self.events = events
        self.totality = totality
        self.rubrics = rubrics
        self.comments = comments
        self.rx = rx

    def saverecord(self):
        connection = sqlite3.connect("DB.db")
        cursor = connection.cursor()
        data = (self.case_no,self.op_no,self.date,self.acu_chr,self.dr,self.prov_diag,self.summary,self.subjective,
                self.objective,self.appetite,self.thirst,self.sleep,self.bowels,self.urine,self.sweat,self.lab,
                self.phy_men,self.events,self.totality,self.rubrics,self.comments,self.rx)
        cmd = """INSERT INTO CaseRecord (Case_Number, OP_Number ,date, Subjective_Symptoms, Objective_Findings, Appetite, Thirst, Sleep, Bowels, Urine, Sweat, Lab_Investigation, PAM, Events, Totality, Rubrics, Comments, Rx)
              VALUES ("{case_no}","{opno}","{date}","{sub}","{obj}","{app}","{th}","{sl}","{bo}","{ur}","{swt}","{lab}","{pam}","{events}","{tot}","{rub}","{comm}","{rx}")"""

        cursor.execute(cmd.format(case_no=data[0],opno=data[1],date=data[2],sub=data[3],obj=data[4],app=data[5],
                                  th=data[6],sl=data[7],bo=data[8],ur=data[9],swt=data[10],lab=data[11],pam=data[12],
                                  events=data[13],tot=data[14],rub=data[15],comm=data[16],rx=data[17]))
        connection.commit()
        connection.close()

    def printall(self):
        connection = sqlite3.connect("DB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CaseRecord")
        result = cursor.fetchall()
        for p in result:
            print(p)

    def getNewRecordNumber(self):
        connection = sqlite3.connect("DB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT Case_Number FROM CaseRecord")
        result = cursor.fetchall()
        return len(result)+1


    def fetchrecord(self,op_no):
        connection = sqlite3.connect("DB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM CaseRecord WHERE OP_Number = {val}".format(val = op_no))
        result = cursor.fetchall()
        return result