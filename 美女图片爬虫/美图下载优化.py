from concurrent.futures import ThreadPoolExecutor
import requests
from lxml import etree

def getpic():
    url = "https://pic.netbian.com"
    for index in range(10, 50):
        meinv_url = url + f'/4kmeinv/index_{index}.html'
        res = requests.get(meinv_url)
        res.encoding = 'gbk'
        # print(res.text)
        html = etree.HTML(res.text)
        all = html.xpath('/html/body/div[2]/div/div[3]/ul/li/a/@href')
        src_dic = {}
        for a in all:
            meinvurl = url + a
            res1 = requests.get(meinvurl)
            res1.encoding = 'gbk'
            html1 = etree.HTML(res1.text)
            title = html1.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@title")[0]
            src = html1.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@src")[0]
            src_dic[title] = url + src

        for title, src in src_dic.items():
            # print(title,src)
            res = requests.get(src)
            if res.status_code !=200:
                continue
            with open(f'./download1/{title}.jpg', "wb") as f:
                f.write(res.content)
        print('下载完毕一页')
if __name__ =='__main__':
    with ThreadPoolExecutor(50) as t:
        t.submit(getpic)
    print('over')