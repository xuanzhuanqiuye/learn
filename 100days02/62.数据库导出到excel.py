import pymysql
import  openpyxl

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='hrs', charset='utf8mb4')

wb=openpyxl.Workbook()
sheet=wb.active
sheet .append(['工号', '姓名', '职位', '月薪', '补贴', '部门'])
try:
    with conn.cursor() as cursor:
        cursor.execute('select `eno`, `ename`, `job`, `sal`, ifnull(`comm`, 0) as comm1, `dname`  from tb_emp natural join \
        tb_dept')
        row=cursor.fetchone()
        while row:
            sheet.append(row)
            row=cursor.fetchone()
    wb.save('./员工基本信息.xlsx')
except pymysql.MySQLError as e:
    print(e)
finally:
    conn.close()