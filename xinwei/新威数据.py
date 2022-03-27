import pandas as pd
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='root', password='root',
                       database='xinwei', charset='utf8mb4')
df=pd.read_sql_query('select * from info where city = "长春";',conn)
print(df.head())