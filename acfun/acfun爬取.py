import json
import time
from concurrent.futures import ThreadPoolExecutor
from pprint import pprint

import requests
import re
def download(ac):
    url=f'https://www.acfun.cn/v/{ac}'
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    }
    resp=requests.get(url,headers=headers)
    #获取标题
    title=re.findall('<title >(.*?)</title>',resp.text)[0].split('-')[0]
    #获取m3u8文件url
    html_data=re.findall('window.pageInfo = window.videoInfo =(.*?);',resp.text)[0]
    json_data=json.loads(html_data)
    m3u8_url=json.loads(json_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
    #对m3u8发送请求
    m3u8_data=requests.get(m3u8_url,headers=headers).text
    host_url='https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/'
    m3u8_data=re.sub('#EXT.*','',m3u8_data).split()
    for link in m3u8_data:
        ts_url=host_url+link
        ts_name=link.split('.')[1]
        ts_content=requests.get(ts_url,headers=headers).content
        with open(f'./data/{title}.mp4','ab') as f:
            f.write(ts_content)
        print("下载：",ac,ts_name)
    print("下载完成:",ac)

def getUrl():
    # url='https://www.acfun.cn/search'
    # url='https://www.acfun.cn/v/list218/index.htm'
    url='https://www.acfun.cn/search?type=video&keyword=%E5%A5%B3%E4%BC%98'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "referer":"https://www.acfun.cn/v/list218 /index.htm?sortField=rankScore&duration=all&date=default&page=1"
    }
    res=requests.get(url,headers=headers)
    data=res.text
    aclist=re.findall("ac[0-9]{8}",data)
    ac=list(set(aclist))
    return ac

if __name__ == '__main__':
    aclist=getUrl()
    print(aclist)
    with ThreadPoolExecutor(max_workers=16) as pool:
        for ac in aclist:
            pool.submit(download,ac)