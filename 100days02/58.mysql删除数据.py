import pymysql

no=int(input("请输入你要删除的部门编号："))


conn=pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='hrs', charset='utf8mb4')

try:
    with conn.cursor() as cursor:
        affected_rows=cursor.execute('delete from tb_dept where dno=%s;',(no,))
        if affected_rows == 1:
            print('success del')
    conn.commit()
except pymysql.MySQLError as e:
    conn.rollback()
    print("rollback")
finally:
    conn.close()

