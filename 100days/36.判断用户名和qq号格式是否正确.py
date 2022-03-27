"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re

def main():
    username=input("请输入用户名：")
    flag1=re.match(r'^[A-Z][a-zA-Z0-9_]{5,19}',username)
    if not flag1:
        print("请输入正确的用户名")
    else:
        print("输入正确")
    qq = input("请输入你的qq：")
    flag2=re.match(r'^[1-9][0-9]{4,11}',qq)
    if not flag2:
        print("请输入正确的qq")
    else:
        print("输入正确")

if __name__ == '__main__':
    main()