# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 08:43:45 2023

@author: Navi
"""

import mysql.connector
import os

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '')

mycursor = mydb.cursor()

mycursor.execute("USE school_students")
                # DELETE TABLE students")
  
sql = "CREATE TABLE company_employees(Name VARCHAR(20), ID INT)"

mycursor.execute(sql)

sql = "INSERT INTO company_employees (name, id) VALUES (%s, %s)"
val = ("John", "21")
mycursor.execute(sql, val)

mydb.commit()

# mydb.rollback()

print(mycursor.rowcount)

mycursor.execute("SELECT * FROM company_employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

sql = "INSERT INTO company_employees (name, id) VALUES (%s, %s)"
val = ("Mary", "22")
mycursor.execute(sql, val)

print(mycursor.rowcount)

mycursor.execute("SELECT * FROM company_employees")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


