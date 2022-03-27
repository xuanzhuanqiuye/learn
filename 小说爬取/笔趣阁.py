import requests
from lxml import etree
import re


def download(url):
    res = requests.get(url)
    num = re.findall('<dd><a href =(.*?)>.*</a></dd>[\s]*</dl>', res.text)[0].split('/')[-1].split('.')[0]
    name = re.findall('<span class="title">(.*?)</span>', res.text)[0]
    print(f'本书一共{num}章')
    count = int(num)
    pageContent = []
    for page in range(1, count + 1):
        downloadurl = url + str(page) + '.html'
        res1 = requests.get(downloadurl)
        if res1.status_code == 200:
            tree = etree.HTML(res1.text)
            title = tree.xpath('//h1[@class="wap_none"]/text()')
            content = tree.xpath('//*[@id="chaptercontent"]/text()')
            content.insert(0, (title[0] + '\n'))
            txt = '\n'.join(content)
            pageContent.append(txt)

            print(f"下载完成第{page}章:{title[0]}")
        else:
            print(f'第{page}章无法下载')
            print(f'开始重试：')
            for i in range(3):
                res2 = requests.get(downloadurl)
                print(f'开始重试：第{i + 1}次')
                if res2.status_code == 200:
                    tree = etree.HTML(res2.text)
                    title = tree.xpath('//h1[@class="wap_none"]/text()')
                    content = tree.xpath('//*[@id="chaptercontent"]/text()')
                    content.insert(0, (title[0] + '\n'))
                    txt = ''.join(content)
                    pageContent.append(txt)
                    print(f"下载完成第{page}章:{title[0]}")
                else:
                    print(f'第{page}章无法下载')
                    continue
    for page in pageContent:
        with open(f'./book/{name}.txt', 'a', encoding='utf-8') as f:
            f.write(page)
    print("下载完成")


if __name__ == '__main__':
    url = 'https://www.bige3.com/book/57025/'
    download(url)
