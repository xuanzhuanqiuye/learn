import time
import asyncio

async def func():
    print("哈哈哈哈")
    # time.sleep(3)#当程序出现了同步操作的时候，异步就中断了
    await asyncio.sleep(3)
    print("你是大聪明")
async def func1():
    print("哈哈哈哈1111")
    # time.sleep(1)#
    await asyncio.sleep(1)
    print("你是大聪明1111")
async def func2():
    print("哈哈哈哈2222")
    # time.sleep(2)
    await asyncio.sleep(2)
    print("你是大聪明2222")
async def func3():
    print("哈哈哈哈3333")
    # time.sleep(3)
    await asyncio.sleep(3)
    print("你是大聪明3333")
async def func4():
    print("大傻子")
    # time.sleep(1)
    await asyncio.sleep(1)
    print("大傻子哈哈哈")
async def main():
    # #第一中写法
    # f1=func1() #一般 await挂起操作放在协程对象前面
    # await f1
    #第二种写法(推荐)
    tasks=[asyncio.create_task(func()),asyncio.create_task(func1()),asyncio.create_task(func2()),asyncio.create_task(func3()),asyncio.create_task(func4())]#3.8之后推荐写法
    # tasks = [func1(),func2(),func3(),func4()]#3.8之前的写法
    await asyncio.wait(tasks)
if __name__ =="__main__":
    # g=func()#此时的函数是异步协程函数，此时函数执行得到的是一个协程对象
    # f1=func1()
    # f2=func2()
    # f3=func3()
    # f4=func4()
    # tasks=[g,f1,f2,f3,f4]
    # t1 = time.time()
    # asyncio.run(asyncio.wait(tasks))#协程程序运行需要asyncio模块的支持,多任务一起跑固定写法
    # t2 = time.time()
    # print(t2-t1)#执行只花了3秒多一点，比同步操作快了将近6秒（顺序执行）
    t1 = time.time()
    asyncio.run(main())
    t2 = time.time()
    print(t2 - t1)
