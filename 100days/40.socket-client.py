# from socket import socket
#
#
# def main():
#     # 1.创建套接字对象默认使用IPv4和TCP协议
#     client = socket()
#     # 2.连接到服务器(需要指定IP地址和端口)
#     client.connect(('192.168.1.2', 6789))
#     # 3.从服务器接收数据
#     print(client.recv(1024).decode('utf-8'))
#     client.close()
#
#
# if __name__ == '__main__':
#     main()
import random
from datetime import datetime
from socket import socket

def main():
    client=socket()
    client.connect(('192.168.0.108',6000))
    print("connecting..")
    client.send(str(random.randint(1,10)).encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
    client.close()

if __name__ == '__main__':
    main()