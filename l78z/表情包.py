import requests
from bs4 import BeautifulSoup
import re

headers={
        "user-agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 96.0.4664.110Safari / 537.36"
    }
def download_htmls():
    htmls=[]
    for idx in range(20):
        url=f"https://fabiaoqing.com/biaoqing/lists/page/{idx+1}.html"
        print("craw html:",url)
        r=requests.get(url,headers=headers)
        if r.status_code!=200:
            continue
            # raise Exception("error!")
        htmls.append(r.text)
    print("success")
    return htmls

def parse_single_html(html):
    soup=BeautifulSoup(html,"html.parser")
    img_divs=soup.find_all("div",class_="tagbqppdiv")
    datas=[]
    for div in img_divs:
        img_node=div.find("img")
        if not img_node:continue
        datas.append((img_node["title"],img_node["data-original"]))
    return datas


if __name__=='__main__':
    htmls=download_htmls()
    for html in htmls:
        imgs=parse_single_html(html)
        for idx,(title,img_url) in enumerate(imgs):
            reg="[^0-9A-Za-z\u4e00-\u9fa5]"
            title=re.sub(reg,"",title)
            if len(title)>10:title=title[:10]
            post_fix=img_url[-3:]
            filename=f"./download/{title}.{post_fix}"
            print(idx,filename)
            img_data=requests.get(img_url,headers=headers)
            with open(filename,"wb") as f:
                f.write((img_data.content))
    print("success")