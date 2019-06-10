import sqlite3
connection = sqlite3.connect("DB.db")
cmd = """CREATE TABLE Patient(OP_Number VARCHAR(10) PRIMARY KEY,name VARCHAR(30),Weight CHAR(3),Height CHAR(4),pulse CHAR(2), bp CHAR(7), occupation VARCHAR(15),phone_number CHAR(10),sex CHAR(1),age CHAR(3),place VARCHAR(20),hospital VARCHAR(20))"""
cursor = connection.cursor()
cursor.execute(cmd)
connection.commit()
connection.close()
connection = sqlite3.connect("DB.db")
cmd = """CREATE TABLE CaseRecord(Case_Number VARCHAR(10) PRIMARY KEY, OP_Number VARCHAR(10) ,date CHAR(8),Subjective_Symptoms VARCHAR(300),Objective_Findings VARCHAR(300),Appetite VARCHAR(20), Thirst VARCHAR(20),Sleep VARCHAR(20),Bowels VARCHAR(20),Urine VARCHAR(20),Sweat VARCHAR(20),Lab_Investigation VARCHAR(300), PAM VARCHAR(300),Events VARCHAR(300),Totality VARCHAR(300),Rubrics VARCHAR(300),Comments VARCHAR(300),Rx VARCHAR(200))"""
cursor = connection.cursor()
cursor.execute(cmd)
connection.commit()
connection.close()