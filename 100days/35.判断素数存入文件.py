# 要将文本信息写入文件文件也非常简单，在使用`open`函数时指定好文件名并将文件模式设置为`'w'`即可。注意如果需要对文件内容进行追加式写入，应
# 该将模式设置为`'a'`。如果要写入的文件不存在会自动创建文件而不是引发异常。下面的例子演示了如何将1-9999之间的素数分别写入三个文件中
# （1-99之间的素数保存在a.txt中，100-999之间的素数保存在b.txt中，1000-9999之间的素数保存在c.txt中）。
import os
def isPrime(m):
    # isprime=1
    for i in range(2,m):
        if m%i==0:
            return False

    return True

def main():
    list1=range(1,9999)
    if not os.path.isdir('data'):
        os.mkdir('data')
    with open('./data/a.txt', 'w') as f1:
        with open('./data/b.txt', 'w') as f2:
            with open('./data/c.txt', 'w') as f3:
                for i in list1:
                    if isPrime(i):
                        if i<99:
                                f1.write(str(i)+' ')
                        elif i<999:
                                f2.write(str(i)+' ')
                        else:
                                f3.write(str(i)+' ')
    f1.close()
    f2.close()
    f3.close()
if __name__ == '__main__':
    main()