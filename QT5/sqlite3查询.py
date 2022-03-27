import sqlite3
conn = sqlite3.connect('./sqlite3/xinwei.db')
cursor=conn.cursor()
cursor = cursor.execute("SELECT *  from info where city='长春'")
for row in cursor:
   print("ID = ", row[0])
   print("NAME = ", row[3])
   print("PROVINCE = ", row[4])
   print("CITY = ", row[5], "\n")
