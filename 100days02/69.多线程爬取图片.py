import os
import time
from threading import Thread
import requests


def download_picture(url):
    filename = url[url.rfind('/') + 1:]
    resp = requests.get(url)
    if resp.status_code == 200:
        with open(f'images/beauty1/{filename}', 'wb') as file:
            file.write(resp.content)
    else:
        print('error:',resp.status_code)

if __name__ == '__main__':
    urls=[]
    if not os.path.exists('images/beauty1'):
        os.makedirs('images/beauty1')
    start = time.time()
    for page in range(8,10):
        resp = requests.get(f'https://image.so.com/zjl?ch=beauty&sn={page * 30}')
        if resp.status_code == 200:
            pic_dict_list = resp.json()['list']
            for pic in pic_dict_list:
                urls.append(pic['qhimg_url'])
    for url in urls:
        t=Thread(target=download_picture,args=(url,))
        t.start()
        print('over')
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')