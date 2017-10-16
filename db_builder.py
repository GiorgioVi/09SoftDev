import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

database = sqlite3.connect("stats.db")
c = database.cursor()    #facilitate database ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

c.execute("CREATE TABLE IF NOT EXISTS students(name TEXT, age NUMERIC, if NUMERIC)")
c.execute("CREATE TABLE IF NOT EXISTS grades(class TEXT, grade NUMERIC, id NUMERIC)")

# reads peeps.csv and fills students table
with open("peeps.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO students VALUES (?, ?, ?)", [row["name"], row["age"], row["id"]])


with open("courses.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO grades VALUES (?, ?, ?)", [row["code"], row["mark"], row["id"]])
#========================================================== It been populated yurd

database.commit() #save changes
database.close()  #close database
