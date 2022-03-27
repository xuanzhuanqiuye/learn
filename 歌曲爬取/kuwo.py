import json
import re

import requests
from lxml import etree

url='http://www.kuwo.cn/playlist_detail/3313318491'
headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}
resp=requests.get(url,headers=headers)
tree=etree.HTML(resp.text)
namelist=tree.xpath('//ul/li/div[2]/a/text()') 
urllist=tree.xpath('//ul/li/div[2]/a/@href')
ids=[]
songurl='http://www.kuwo.cn/api/v1/www/music/playUrl'
for url in urllist:
    id=url.split('/')[-1]
    ids.append(id)
print("解析歌曲id完毕")
print(ids)
params={
    'mid':' 202954717',
    'type':' music',
    'httpsStatus':' 1',
    'reqId':' 92a3ea91-9fac-11ec-81f3-29ebfb62e44f',
}
durls=[]
for id  in ids:
    params = {
        'mid': id,
        'type': ' music',
        'httpsStatus': ' 1',
        'reqId': ' 92a3ea91-9fac-11ec-81f3-29ebfb62e44f',
    }
    res=requests.get(songurl,headers=headers,params=params)
    durl=res.json()['data']['url']
    durls.append(durl)

for k,url in enumerate(durls):
    res=requests.get(url,headers=headers)
    with open(f'./kuwo/{namelist[k]}.mp3',"wb") as f:
        f.write(res.content)
        print(f'{namelist[k]}.mp3下载完毕')
print('下载完成')