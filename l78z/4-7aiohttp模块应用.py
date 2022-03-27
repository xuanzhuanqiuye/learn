#request.get()同步的代码——》异步操作aiohttp
#pip install aiohttp
import asyncio
import aiohttp
urls=[
    "http://kr.shanghai-jiuxin.com/file/mm/20211130/jgz2yvescjs.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0331/c9903405cb8979df4baec08d520b3750.jpg",
    "http://kr.shanghai-jiuxin.com/file/2021/0324/7bb59fcf7cba78291625fa9a97b834ec.jpg"
]
async def aiodownload(url):
    name=url.rsplit("/",1)[1]
    async with aiohttp.ClientSession() as session:  #<-->requests()
        async with session.get(url) as resp:
            #resp.content.read() #<-->resp.content
            with open(name,mode="wb") as f:#可以自己学习一个模块aiofiles
                f.write(await resp.content.read())


async def main():
    tasks=[]
    for url in urls:
        tasks.append(aiodownload(url))
    await asyncio.wait(tasks)


if __name__ =="__main__":
    print("start...")
    asyncio.run(main())
    print("all over")