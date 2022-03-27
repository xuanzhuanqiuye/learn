import pymysql

no=int(input("请输入部门号："))
name=input("部门名称：")
addr=input("部门地址：")

conn=pymysql.connect(user='root',password='root',host='127.0.0.1',port=3306,database='hrs',charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        affected_rows=cursor.execute("update tb_dept set dname=%s, dloc=%s where dno= %s",(name,addr,no))
        if affected_rows==1:
            print("更新成功")
    conn.commit()
except pymysql.MySQLError as e:
    print('rollback',e)
    conn.rollback()
finally:
    conn.close()