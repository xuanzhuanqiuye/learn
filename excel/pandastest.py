import pandas as pd

df=pd.read_excel('./data/test.xls','内网数据')
df1=pd.read_excel('./data/learn.xls','模板')
df.sort_values(by=['银行设备编号'],inplace=True)
df2=pd.concat([df1['设备编号'], df.iloc[0:,0]],axis=1)
print(df2)

