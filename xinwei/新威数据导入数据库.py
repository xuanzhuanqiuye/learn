import pandas as pd
import pymysql
df=pd.read_excel('./data/xinwei.xlsx')
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='xinwei', charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        for index,row in df.iterrows():
            affected_rows=cursor.execute('insert into info values(%s, %s, %s,%s, %s, %s,%s, %s, %s,%s);',\
                                         (int((row[0])),str(row[1]).split()[0],str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6]),str(row[7]),int(row[8]),str(row[9])))
            if affected_rows==1:
                print("数据添加成功")
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()