import re
import requests
import csv

f=open("data.csv",mode="w",encoding="UTF-8")
csvwriter=csv.writer(f)

for num in range(0,300,25):
    url=f"https://movie.douban.com/top250?start={num}&filter="
    header={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
    }
    resp=requests.get(url,headers=header)
    content=resp.text
    obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                   r'<div class="bd">.*?<br>(?P<year>.*?)&nbsp.*?'
                   r'<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?'
                   r'<span>(?P<more>.*?)人评价</span>',re.S)
    it=obj.finditer(content)
    for i in it:
        # print(i.group("name"))
        # print(i.group("year").strip())
        # print(i.group("score"))
        # print(i.group("more"))
        dic=i.groupdict()
        dic['year']=dic['year'].strip()
        csvwriter.writerow(dic.values())
f.close()
resp.close()
print("over")