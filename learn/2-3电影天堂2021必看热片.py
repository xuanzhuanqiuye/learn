import requests
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
child_list=[]
url="https://www.dytt89.com/"
resp=requests.get(url,verify=False) #verify=False 去掉安全验证
resp.encoding="gb2312"
obj1=re.compile(r'2021必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
result1=obj1.finditer(resp.text)
for it1 in result1:
    str=it1.group("ul")
    obj2=re.compile(r"<a href='(?P<href>.*?)' title",re.S)
    result2=obj2.finditer(str)
    for it2 in result2:
        childhref=url+it2.group("href")
        child_list.append(childhref)

for href in child_list:
    resp1=requests.get(href,verify=False)
    resp1.encoding="gb2312"
    obj3=re.compile(r'<div class="title_all"><h1>(?P<name>.*?)</h1></div>.*?'
                    r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<href>.*?)">',re.S)
    result3=obj3.finditer(resp1.text)
    for it3 in result3:
        print(it3.group("name"))
        print(it3.group("href"))
resp.close()
resp1.close()