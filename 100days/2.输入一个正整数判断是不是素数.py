#提示：素数指的是只能被1和自身整除的大于1的整数
from math import sqrt

num=int(input("请输入一个正整数："))
flag=1
for i in range(2,num):
    if num%i==0:
        print("这不是个素数")
        flag=0
        break
if flag:
    print("这是个素数")
