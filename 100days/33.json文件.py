
import json

content={
    "name": "骆昊",
    "age": 38,
    "qq": 957658,
    "friends": ["王大锤", "白元芳"],
    "cars": [
        {"brand": "BYD", "max_speed": 180},
        {"brand": "Audi", "max_speed": 280},
        {"brand": "Benz", "max_speed": 320}
    ]
}

def main1():
    with open("./data/test.json",'w') as f:
        json.dump(content,f)
    f.close()
def main2():
    with open("./data/test.json","r") as f:
        content=json.load(f)
        print(content)
    f.close()

##json模块主要有四个比较重要的函数，分别是：

# - `dump` - 将Python对象按照JSON格式序列化到文件中
# - `dumps` - 将Python对象处理成JSON格式的字符串
# - `load` - 将文件中的JSON数据反序列化成对象
# - `loads` - 将字符串的内容反序列化成Python对象

if __name__ == '__main__':
    # main1()
    main2()