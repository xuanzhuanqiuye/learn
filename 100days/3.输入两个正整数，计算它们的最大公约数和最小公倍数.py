#两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。


def getGongyue(m,n):
    if m<=n:
        for i in range(m,0,-1):
            if m%i ==0 and n%i ==0:
                return i
    else:
        for i in range(n,0,-1):
            if m%i ==0 and n%i ==0:
                return i
def getGongbei(m,n):
    if m<=n:
        for i in range(n,m*n+1):
            if i%m==0 and i%n==0:
                return i
    else:
        for i in range(m,n*m+1):
            if i % m == 0 and i % n == 0:
                return i

if __name__ == '__main__':
    a=int(input("请输入一个正整数："))
    b=int(input("请输入另一个正整数："))
    print("这两个数的最大公约数是：",getGongyue(a,b))
    print("这两个数的最小公倍数是：", getGongbei(a,b))