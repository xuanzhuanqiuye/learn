import asyncio
import selectors
import time
from datetime import datetime
from lxml import html
import aiofiles
import aiohttp
import requests

url = "https://pic.netbian.com"


def getUrls():
    src_dic = {}
    for index in range(11, 20):
        meinv_url = url + f'/shoujibizhi/index_{index}.html'
        res = requests.get(meinv_url)
        if res.status_code == 200:
            res.encoding = 'gbk'
            # print(res.text)
            html1 = html.etree.HTML(res.text)
            allContent = html1.xpath('/html/body/div[2]/div/div[3]/ul/li/a/@href')
            for a in allContent:
                meinvurl = url + a
                res1 = requests.get(meinvurl)
                if res1.status_code == 200:
                    res1.encoding = 'gbk'
                    html2 = html.etree.HTML(res1.text)
                    title = html2.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@title")[0]
                    src = html2.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@src")[0]
                    src_dic[title] = url + src
    return src_dic


async def aiodownload(title, furl):
    async with aiohttp.ClientSession() as session:
        async with session.get(furl) as res:
            async with aiofiles.open(f"./download2/{title}.jpg", 'wb') as f:
                content = await res.content.read()
                await f.write(content)


async def main():
    tasks = []
    for furl, title in getUrls().items():
        tasks.append(aiodownload(furl, title))
    await asyncio.wait(tasks)


if __name__ == "__main__":
    print("start...")
    t1 = time.time()
    print(len(getUrls()))
    t2 = time.time()
    print('花费时间', (datetime.fromtimestamp(t2) - datetime.fromtimestamp(t1)).seconds)
    # asyncio.run(main())
    selector = selectors.SelectSelector()  # New line
    loop = asyncio.SelectorEventLoop(selector)  # New line
    try:
        loop.run_until_complete(main())  # 完成事件循环，直到最后一个任务结束
    finally:
        loop.close()  # 结束事件循环.
    t3 = time.time()
    print('花费时间', (datetime.fromtimestamp(t3) - datetime.fromtimestamp(t2)).seconds)
    print("all over")
