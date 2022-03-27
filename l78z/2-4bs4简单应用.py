import requests
from bs4 import BeautifulSoup
url="https://www.lvguo.net/baojia/蔬菜/9501/"
resp=requests.get(url)
page=BeautifulSoup(resp.text,"html.parser")
# table=page.find_all("table",class_="bjtbl")
table=page.find("table",attrs={"class":"bjtbl"})
trs=table.find_all("tr")[2:]
for tr in trs:
    tds=tr.find_all("td")
    time=tds[0].text
    where = tds[1].text
    what= tds[3].text
    print(time,where,what)