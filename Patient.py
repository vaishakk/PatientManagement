import sqlite3
class Patient:
    def addrecord(self,params):
        self.name = params[0]
        self.op_no = params[1]
        self.weight = params[2]
        self.height = params[3]
        self.pulse = params[4]
        self.occu = params[5]
        self.bp = params[6]
        self.ph_no = params[7]
        self.sex = params[8]
        self.age = params[9]
        self.place = params[10]
        self.hos = params[11]

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

    def show(self):
        return (self.op_no, self.name, self.weight, self.height, self.pulse, self.bp, self.occu, self.ph_no, self.sex, self.age, self.place, self.hos)

    def saverecord(self):
        connection = sqlite3.connect("DB.db")
        cursor = connection.cursor()
        data = (self.op_no,self.name,self.weight,self.height,self.pulse,self.bp,self.occu,self.ph_no,self.sex,self.age,self.place,self.hos)
        cmd = """INSERT INTO Patient (OP_Number,name,Weight,Height,pulse,bp,occupation,phone_number,sex,age,place,hospital)
              VALUES ("{opno}","{name}","{w}","{h}","{pul}","{bp}","{occ}","{ph}","{sex}","{age}","{pl}","{hos}")"""

        cursor.execute(cmd.format(opno=data[0],name=data[1],w=data[2],h=data[3],pul=data[4],bp=data[5],occ=data[6],ph=data[7],sex=data[8],age=data[9],pl=data[10],hos=data[11]))
        connection.commit()
        connection.close()

    def printall(self):
        connection = sqlite3.connect("DB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM Patient")
        result = cursor.fetchall()
        for p in result:
            print(p)

    def loadlist(self):
        connection = sqlite3.connect("DB.db")
        cursor = connection.cursor()
        cursor.execute("SELECT OP_Number, name FROM Patient")
        result = cursor.fetchall()
        #print(result)
        fullarray = []
        for p in result:
            array = []
            for r in p:
                array.append(r)
            fullarray.append(array)
        return (fullarray)


