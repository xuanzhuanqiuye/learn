import os
import selectors
import time
from datetime import datetime

import requests
import aiofiles
import aiohttp
import asyncio


def getUrls():
    urls = []
    if not os.path.exists('images/images/beauty3'):
        os.makedirs('images/images/beauty3')
    start = time.time()
    for page in range(10, 12):
        resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={page * 30}')
        if resp.status_code == 200:
            pic_dict_list = resp.json()['list']
            for pic in pic_dict_list:
                urls.append(pic['qhimg_url'])
    return urls
async def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                async with aiofiles.open(f'images/beauty3/{filename}', 'wb') as file:
                    content = await resp.content.read()
                    await file.write(content)
            else:
                print('error:',resp.status_code)

async def main():
    tasks = []
    for url in getUrls():
        tasks.append(download_picture(url))
    await asyncio.wait(tasks)

if __name__ == '__main__':
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
