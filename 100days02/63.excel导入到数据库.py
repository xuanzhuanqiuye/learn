import pymysql
import  openpyxl

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='hrs', charset='utf8mb4')
wb=openpyxl.open("./员工基本信息.xlsx")
sheet=wb.active
try:
    with conn.cursor() as cursor:
        for i in sheet.values:
            print(i)
            if i[0]=='工号':
                continue
            affected_row=cursor.execute('insert into tb_emp values(%s,%s,%s,%s,%s,%s,%s);',i)
            if affected_row ==1:
                print("插入成功",i)
    conn.commit()
except pymysql.MySQLError as e:
    print(e)
    conn.rollback()
finally:
    conn.close()