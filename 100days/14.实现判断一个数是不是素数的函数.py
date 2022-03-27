

def isPrime(m):
    # isprime=1
    for i in range(2,m):
        if m%i==0:
            return 'no'

    return 'yes'

if __name__ == '__main__':
    # num=int(input("请输入一个数："))
    list1=[2, 4,3,12,18, 5, 7, 11, 13, 17, 19,28, 23, 29, 31, 37,99, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    for i in list1:
        print(f"{i}是素数吗？{isPrime(i)}")