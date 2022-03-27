import requests
url="https://movie.douban.com/j/chart/top_list"
param={
    "type":"24",
    "interval_id":"100:90",
    "action":"",
    "start":0,
    "limit":20,
}
header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}
resp=requests.get(url=url,params=param,headers=header)
print(resp.json())
