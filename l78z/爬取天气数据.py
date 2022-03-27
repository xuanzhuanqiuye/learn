import requests
from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import Workbook
urls=[f"https://tianqi.2345.com/Pc/GetHistory?areaInfo[areaId]=54161&areaInfo[areaType]=2&date[year]=2021&date[month]={str(x+1)} " for x in range(12)]
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
col = ["日期", "最高温", "最低温", "天气", "风力风向", "空气质量指数"]
df = pd.DataFrame(columns=col, index=None)
for url in urls:
    index=df.shape[0]
    print(index)
    res=requests.get(url,headers=headers)
    data=res.json()["data"]
    bs=BeautifulSoup(data,"html.parser")
    table=bs.find('table',class_="history-table")
    trs=table.find_all("tr")[1:]
    for k, tr in enumerate(trs):
        tds=tr.find_all('td')
        list = []
        for td in tds:
            list.append(td.text)
        df.loc[k+index+1]=list
df.reset_index()
df.to_excel('tianqi.xlsx')


