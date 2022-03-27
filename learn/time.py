import pandas

df=pandas.DataFrame({'id':[1,2,3],'name':['lily','bill','cell']})
df.set_index('id')
df.to_excel("D:/PycharmProjects/pythonProject/learn/1.xlsx")
