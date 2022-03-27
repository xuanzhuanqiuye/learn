
num=int(input("请输入一个两位以上的正整数："))
reserve=0
num1=num
if num<10:
    print("输入的有误")
    num = int(input("请输入一个两位以上的正整数："))
    num1=num
while num >0:
    reserve=reserve*10+num%10
    num=num//10
if reserve==num1:
    print("echo",reserve,num1)
else:
    print("not echo")

