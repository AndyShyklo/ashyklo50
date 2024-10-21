'''
  Ankita Saha, Andy Shyklo, Abidur Rahman
  Python Pigs
  SoftDev
  K19 - Working with SQL and CSV files
  2024-10-20
  time spent: 1 hour
'''

#a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")

db.commit() #save changes
db.close()
