

from multiprocessing import Process

# def func():
#     for i in range(10000):
#         print("子进程：",i)
#
# if __name__ == "__main__":
#     p=Process(target=func)
#     p.start()
#     for i in range(10000):
#         print("主进程：",i)
class myProcess(Process):
    def run(self):
        for i in range(10000):
            print("子进程", i)


if __name__ =="__main__":
    p=myProcess()
    p.start()
    for i in range(10000):
        print("子进程", i)