import json
import csv
import  requests
from concurrent.futures import ThreadPoolExecutor

url="http://www.xinfadi.com.cn//getPriceData.html"
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95"
    }
a=[]
filednames=["id","prodName","prodCatid","prodCat","prodPcatid","prodPcat","lowPrice","highPrice","avgPrice","place","specInfo","unitInfo","pubDate","status","userIdCreate","userIdModified","userCreate","userModified","gmtCreate","gmtModified"]
f=open("caijia.csv",mode="w",encoding="utf-8")
csvwriter=csv.writer(f)
csvwriter.writerow(filednames)
def down_one_page(i):
    data = {
        "limit": "20",
        "current": i,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": ""
    }
    resp=requests.post(url,data=data,headers=headers)
    content=resp.json()
    list1=content["list"]
    for row in list1:
        csvwriter.writerow(list(row.values()))

if __name__ =="__main__":
    with ThreadPoolExecutor(50) as t:
        for i in range(1,21):
            t.submit(down_one_page,i)
            print(i,"下载完毕")
    print("all over")