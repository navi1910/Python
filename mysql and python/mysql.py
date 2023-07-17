# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 10:32:02 2023

@author: Navi
"""

import mysql.connector
import os

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password = os.environ.get('my_password')
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

