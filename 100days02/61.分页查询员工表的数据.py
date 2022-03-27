import pymysql

page=int(input("页码"))
size=int(input("大小"))

conn=pymysql.connect(user='root',password='root',host='127.0.0.1',port=3306,database='hrs',charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        cursor.execute("select * from tb_emp limit %s,%s",(page,size))
        rows=cursor.fetchall()
        for row in rows:
            print(row)
finally:
    conn.close()