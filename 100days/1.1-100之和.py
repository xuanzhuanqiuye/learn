
def sum(m,n):
    sum=0
    if m<n:
        for i in range(m,n+1):
            sum+=i
    else:
        print("请输入正确的数值,第一个数需要小于第二个数")
        return
    return  sum

if __name__ == '__main__':
    a=int(input("请输入一个正整数:"))
    b=int(input("请输入另一个正整数:"))
    print("这两个数之间的和为：",sum(a,b))