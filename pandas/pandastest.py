import pandas as pd

df=pd.read_excel("./ex4/test.xls")

df1=df.apply(lambda x:(x['库存数量']-1),axis=1)
print(df1)

