# *
# **
# ***
# ****
# *****
#     *
#    **
#   ***
#  ****
# *****
#     *
#    ***
#   *****
#  *******
# *********

def printStar1(m):
    for i in range(1,m+1):
        print("*"*i)

def printStar2(m):
    for i in range(1,m+1):
        print((m-i)*' '+i*'*')

def printStar3(m):
    for i in range(1, m + 1):
        print((m-i)*' '+(2*i-1)*"*")



if __name__ == '__main__':
    printStar1(5)
    printStar2(5)
    printStar3(5)