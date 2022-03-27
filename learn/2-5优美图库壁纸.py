import time

import requests
from bs4 import BeautifulSoup
url="https://www.umei.cc/bizhitupian/fengjingbizhi/"
resp=requests.get(url)
resp.encoding='utf-8'
# print(resp.text)

main_page=BeautifulSoup(resp.text,"html.parser")
alist=main_page.find("div",class_="TypeList").find_all("a")
# print(alist)
for a in alist:
    href='https://www.umei.cc'+a.get("href")
    child_resp=requests.get(href)
    child_resp.encoding='utf-8'
    child_text=child_resp.text
    child_page=BeautifulSoup(child_text,"html.parser")
    div=child_page.find("div",class_="ImageBody")
    img=div.find("img")
    src=img.get("src")
    img_resp=requests.get(src)
    img_name=src.split("/")[-1]
    with open("img/"+img_name,mode="wb") as f:
        f.write(img_resp.content)
    time.sleep(1)
    print("over "+img_name)
print("all over")