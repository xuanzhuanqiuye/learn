import pymysql

no=int(input("部门编号"))
name=input('部门名称')
addr=input('部门地点')

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='hrs', charset='utf8mb4')
try:
    with conn.cursor() as cursor:
        affected_rows=cursor.execute('insert into tb_dept values(%s, %s, %s);',(no, name,addr))
        if affected_rows==1:
            print("数据添加成功")
    conn.commit()
except pymysql.MySQLError as err:
    conn.rollback()
    print(type(err), err)
finally:
    conn.close()