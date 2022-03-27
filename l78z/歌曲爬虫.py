import requests
from lxml import etree
import time

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "http://music.vaiwan.com/"
}
url='http://music.vaiwan.com/music/list'
urldownload='http://music.vaiwan.com/music/save'
for i in range(1,15):
    params={
            'key': '一人一首成名曲',
            'pageNo': i,
            'pageSize': 20
    }

    res=requests.get(url,params=params)
    jsondata=res.json()['data']['list']
    for j in range(0,20):
        paramsjson = jsondata[j]
        resdownload = requests.post(urldownload, params=paramsjson)
        dic=dict(paramsjson)
        dic.pop('mvpayinfo')
        dic.pop('payInfo')
        resdownload=requests.post(urldownload,headers=headers,params=dic)
        if resdownload.status_code !=200:
            continue
        print("准备下载")
        resurl=resdownload.json()['data']
        resp=requests.get(resurl,headers=headers)
        with open(f'./data/{paramsjson["name"]}.mp3','wb') as f:
            f.write(resp.content)
            print(f'{paramsjson["name"]}:下载完成,第{(i-1)*20+j+1}首')
            time.sleep(2)
print("下载完成")


