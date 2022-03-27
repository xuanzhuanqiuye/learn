"""
example05.py - 多线程版本爬虫
"""
import os
import time
from concurrent.futures import ThreadPoolExecutor

import requests

def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'images/beauty2/{filename}', 'wb') as file:
            file.write(resp.content)
    else:
        print('error:',resp.status_code)
if __name__ == '__main__':
    if not os.path.exists('images/beauty2'):
        os.makedirs('images/beauty2')
    start = time.time()
    with ThreadPoolExecutor(max_workers=16) as pool:
        for page in range(6, 8):
            resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={page * 30}')
            if resp.status_code == 200:
                pic_dict_list = resp.json()['list']
                for pic_dict in pic_dict_list:
                    pool.submit(download_picture,pic_dict['qhimg_url'])
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')