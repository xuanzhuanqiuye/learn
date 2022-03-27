
def echoNumber(m):
    reserve = 0
    num1 = m
    if m < 10:
        print("输入的有误")
        num = int(input("请输入一个两位以上的正整数："))
        num1 = num
    while m > 0:
        reserve = reserve * 10 + m % 10
        m = m // 10
    if reserve == num1:
       return True
    else:
        return False

def isPrime(m):
    # isprime=1
    for i in range(2,m):
        if m%i==0:
            return False

    return True

if __name__ == '__main__':
    num = int(input("请输入一个数："))
    if echoNumber(num) and isPrime(num):
        print("是回文素数")
    else:
        print("啥也不是")
    list1=[11,101,131,151,181,191,313,353,373,383,727,757,787,797,919,929]
    for i in list1:
        if echoNumber(i) and isPrime(i):
            print(f"{i}是回文素数")
        else:
            print(f"{i}啥也不是")