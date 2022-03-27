import requests
url="http://api.tianapi.com/dialogue/index"
params={
    'key':"8254d5444e19770d60b9b77d570cc96b"
}
def main():

    with open("./data/电影.txt",'w') as f:
        for i in range(0,100):
            res = requests.post(url, params=params)
            res.encoding = 'utf-8'
            print(res.json())
            str1=res.json()['newslist'][0]['source']+"\n"+res.json()['newslist'][0]['dialogue']+"\n"
            f.write(str1)
    f.close()

if __name__ == '__main__':
    main()