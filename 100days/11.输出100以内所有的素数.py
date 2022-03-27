import math

list1=[]
for i in range(2,101):
    isprime = True
    for j in range(2,math.ceil(i/2)+1):
        if i%j ==0:
            isprime=False
            break
    if isprime:
        list1.append(i)
print(list1)
