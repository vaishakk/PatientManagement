from pony.orm import *
db = Database("sqlite", "PR_DB.sqlite", create_db=True)
class Patient(db.Entity):
    name = Required(str)
    op_no = PrimaryKey(str)
    case_record = Set('CaseRecord')
    weight = Optional(str)
    height = Optional(str)
    pulse = Optional(str)
    occu = Optional(str)
    bp = Optional(str)
    ph_no = Optional(str)
    sex = Optional(str)
    age = Optional(str)
    place = Optional(str)
    hos = Optional(str)

    def print(self):
        print("Name: "+self.name)
        print("OP No.: "+self.op_no)
        print("Weight: " + self.weight)
        print("Height: " + self.height)
        print("Pulse Count: " + self.pulse)
        print("BP: " + self.bp)
        print("Occupation: " + self.occu)
        print("Phone Number: " + self.ph_no)
        print("Sex: " + self.sex)
        print("Age: " + self.age)
        print("Place: " + self.place)
        print("Hospital: " + self.hos)

class CaseRecord(db.Entity):
    #case_no = Required(str)
    patient = Required(Patient)
    date = Required(str)
    acu_chr = Optional(str)
    dr = Optional(str)
    prov_diag = Optional(str)
    summary = Optional(str)
    subjective = Optional(str)
    objective = Optional(str)
    appetite = Optional(str)
    thirst = Optional(str)
    sleep = Optional(str)
    bowels = Optional(str)
    urine = Optional(str)
    sweat = Optional(str)
    lab = Optional(str)
    phy_men = Optional(str)
    events = Optional(str)
    totality = Optional(str)
    rubrics = Optional(str)
    comments = Optional(str)
    rx = Optional(str)

    def printRecord(self):
        print('Name: '+self.patient.name)
        print('Op No.: '+self.patient.op_no)
        print('Date: '+self.date)

db.generate_mapping(create_tables=True)

@db_session
def createPatientRecord(name,
                        op_no,
                        weight = '',
                        height = '',
                        pulse = '',
                        occu = '',
                        bp = '',
                        ph_no = '',
                        sex = '',
                        age = '',
                        place = '',
                        hos = ''):
    p1 = Patient(name=name,op_no=op_no,weight = weight,height = height,pulse = pulse,occu = occu,bp = bp,ph_no = ph_no,
                 sex = sex,age = age,place = place,hos = hos)
@db_session
def addCase(op_no,
            date,
            acu_chr = '',
            dr = '',
            prov_diag = '',
            summary = '',
            subjective = '',
            objective = '',
            appetite = '',
            thirst = '',
            sleep = '',
            bowels = '',
            urine = '',
            sweat = '',
            lab = '',
            phy_men = '',
            events = '',
            totality = '',
            rubrics = '',
            comments = '',
            rx = ''):
    patient = select(p for p in Patient if p.op_no == op_no)[:][0]
    c1 = CaseRecord(patient=patient,date=date,acu_chr=acu_chr,dr=dr,prov_diag=prov_diag,summary=summary,
                    subjective=subjective,objective=objective,appetite=appetite,thirst=thirst,sleep=sleep,bowels=bowels,
                    urine=urine,sweat=sweat,lab=lab,phy_men=phy_men,events=events,totality=totality,rubrics=rubrics,
                    comments=comments,rx=rx)

@db_session
def fetchCaseRecords(op_no):
    cases = select(c for c in CaseRecord if c.patient.op_no == op_no)[:]
    return cases

def test():
    with db_session:
        cases = fetchCaseRecords('100')
        for case in cases:
            case.printRecord()

test()