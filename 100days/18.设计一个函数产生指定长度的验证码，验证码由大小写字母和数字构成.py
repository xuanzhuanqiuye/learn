
import random

def getCode(length=4):
    listcode=list(range(0,10))
    listcode.extend([chr(i) for i in range(97,123)])
    codereturn=[]
    for i in range(0,length):
        code=random.choice(listcode)
        codereturn.append(str(code))
    return codereturn

if __name__ == '__main__':
    num=int(input("请输入你需要几位的验证码："))
    print("你的验证码为：",''.join(getCode(num)))