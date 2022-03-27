import pymysql

conn=pymysql.connect(user='root',password='root',host='127.0.0.1',port=3306,database='hrs',charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        cursor.execute("select * from tb_dept")
        # row=cursor.fetchone()
        # while row:
        #     print(row)
        #     row=cursor.fetchone()
        rows=cursor.fetchall()
        print(rows)
except pymysql.MySQLError as e:
    print(e)
finally:
    conn.close()