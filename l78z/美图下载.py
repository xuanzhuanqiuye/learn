import requests
from lxml import etree
url="https://pic.netbian.com"
for index in range(1,100):
    meinv_url=url+f'/4kmeinv/index_{index}.html'
    res=requests.get(meinv_url)
    res.encoding='gbk'
    # print(res.text)
    html=etree.HTML(res.text)
    all=html.xpath('/html/body/div[2]/div/div[3]/ul/li/a/@href')
    src_dic={}
    for a in all:
        meinvurl=url+a
        res1=requests.get(meinvurl)
        res1.encoding='gbk'
        html1=etree.HTML(res1.text)
        title=html1.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@title")[0]
        src=html1.xpath("/html/body/div[2]/div[1]/div[2]/div[1]/div[2]/a/img/@src")[0]
        src_dic[title]=url+src

    for title,src in src_dic.items():
        # print(title,src)
        res=requests.get(src).content
        with open(f'./download/{title}.jpg',"wb") as f:
            f.write(res)
    print(f"第{index}页完成")
print('over')