import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#easier way of using sql commands
def lazySQL(inputCommand):
	command = inputCommand
	c.execute(command)
	
#create tables	
lazySQL("CREATE TABLE courses (code TEXT, id INTEGER, mark INTEGER)")
lazySQL("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")

#populate tables
with open("courses.csv","rb") as csvfile:
	dictReader = csv.DictReader(csvfile)
	for row in dictReader:
		#print row
		sqlString = "INSERT INTO courses VALUES("
		sqlString += "'" + row["code"] + "'" + ","
		sqlString += "'" + row["mark"] + "'" + ","
		sqlString += "'" + row["id"] + "'" + ")"
		lazySQL(sqlString)

#testing different way to write sql command
with open("peeps.csv", "rb") as csvfile:
    dictReader = csv.DictReader(csvfile)
    for row in dictReader:
		#print row
        lazySQL("INSERT INTO peeps VALUES ('" + row["name"] + "', '" + row["age"] + "', '" + row["id"] + "')")

#==========================================================
db.commit() #save changes
db.close()  #close database


