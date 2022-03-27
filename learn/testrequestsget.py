import requests
query=input("请输入你要查找的内容：")
url=f"https://www.sogou.com/web?query={query}"
dic={
    "User-Agent":"zilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}
#useragent表示是用什么设备访问网站，headers里面不加这段，就会被认为是机器爬虫；
res=requests.get(url,headers=dic)
print(res)
print(res.text)
res.close()
