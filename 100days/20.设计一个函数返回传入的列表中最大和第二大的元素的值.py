
def returnMax(listnum):
    listsort=sorted(listnum,reverse=True)
    return listsort[0],listsort[1]

if __name__ == '__main__':
    list1=[2,4,6,22,46,1,62,9,6,3,91,24,8]
    x,y=returnMax(list1)
    print(x,y)