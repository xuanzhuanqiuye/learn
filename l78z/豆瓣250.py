import requests
from bs4 import BeautifulSoup
import pandas as pd
page_index=range(0,250,25)
def download_htmls():
    htmls=[]
    for idx in page_index:
        url=f"https://movie.douban.com/top250?start={idx}&filter="
        headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
        }
        res=requests.get(url,headers=headers)
        if res.status_code!=200:
            raise Exception("error!")
        htmls.append(res.text)
    return htmls


def parse_single_html(html):
    soup = BeautifulSoup(html, "html.parser")
    article_items = soup.find("div", class_="article").find("ol", class_="grid_view").find_all("div",class_="item")
    data = []
    for article_item in article_items:
        rank = article_item.find("div", class_="pic").find("em").text
        title = article_item.find("div", class_='hd').find("a").find("span", class_="title").text
        info = article_item.find("div", class_='bd').find("p").text.replace("\n", "").replace("&nbsp", "").replace(' ', '')
        star = article_item.find("div", class_='star').find("span", class_="rating_num").text
        comments = article_item.find("div", class_='star').find_all("span")[3].text
        data.append({
            "rank": rank,
            "title": title,
            "info": info,
            "star": star,
            "comments": comments
        })
    return data

if __name__=="__main__":
    htmls = download_htmls()
    soup = BeautifulSoup(htmls[0], "html.parser")
    all_datas = []
    for html in htmls:
        print(parse_single_html(html))
        all_datas.extend(parse_single_html(html))
    # df=pd.DataFrame(all_datas)
    # df.to_excel("doubantop.xlsx")