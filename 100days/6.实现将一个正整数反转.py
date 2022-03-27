

num=int(input("请输入一个正整数："))
reserve=0
while num >0:
    reserve=reserve*10+num%10
    num=num//10
print(reserve)