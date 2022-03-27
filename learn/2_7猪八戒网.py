#拿道页面源代码
#提取和解析数据
import requests
from lxml import etree

url='https://jilin.zbj.com/search/f/?kw=saas'
resp=requests.get(url)
# print(resp.text)
html=etree.HTML(resp.text)
divs=html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div")
for div in divs:
    price=div.xpath("./div/div/a[2]/div[2]/div[1]/span[1]/text()")[0].strip("¥")
    title="saas".join(div.xpath("./div/div/a[2]/div[2]/div[2]/p/text()"))
    name=div.xpath("./div/div/a[1]/div[1]/p/text()")[1].strip()
    where=div.xpath("./div/div/a[1]/div[1]/div/span/text()")[0].strip()
    print(name)