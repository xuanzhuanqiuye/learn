import asyncio
#多任务异步协程在爬虫里面应用的模板

async  def download(url):
    print("准备开始下载")
    await  asyncio.sleep(2)#网络请求
    print("下载完成")
async def main()
    urls=[
        "https://www.baidu.com",
        "https://www.bilibili.com",
        "http://www.wangyi.com"
    ]
    tasks=[]
    for url in urls:
        d=asyncio.create_task(dowmload(url))
        tasks.append(d)

if __name__ =="__main__":
    asyncio.run(main())