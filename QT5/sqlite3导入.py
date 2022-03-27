import sqlite3
import pandas as pd

df = pd.read_excel('./data/xinwei.xlsx')
conn = sqlite3.connect('./sqlite3/data.db')

try:
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute(
            'insert into info values(?,?,?,?,?,?,?,?,?);', [
                int((row[0])), str(row[1]).split()[0], str(row[2]), str(row[3]), str(row[4]), str(row[5]), str(row[6]),
                int(row[7]), str(row[8])
            ])
    conn.commit()
except sqlite3.Error as err:
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()
