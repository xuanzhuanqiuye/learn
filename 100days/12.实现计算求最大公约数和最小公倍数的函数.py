
def getBig(m,n):
    (m,n)=(n,m) if m>n else(m,n)
    for i in range(m,0,-1):
        if m%i==0 and n%i==0:
            return  i
64

def getSmall(m,n):
    return m*n//getBig(m,n)

if __name__ == '__main__':
    m=int(input("请输入一个整数："))
    n=int(input("请输入一个整数："))
    print(getBig(m,n))
    print(getSmall(m,n))