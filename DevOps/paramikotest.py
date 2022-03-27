import getpass
import os.path
import sys
import threading
# 多线程
import paramiko


def rcmd(host, username, password, port=22, cmds=None):
    # 创建ssh实例，用于远程执行命令
    ssh = paramiko.SSHClient()
    # 自动接收服务器发来的密钥
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, username=username, password=password)
    # 输入，输出，错误
    stdin, stdout, stderr = ssh.exec_command(cmds)
    out = stdout.read().decode()
    err = stderr.read().decode()
    if out:
        print('[%s] \033[32;1mOUT\033[0m:\n%s' % (host, out))
    if err:
        print('[%s] \033[31;1mERROR\033[0m:\n%s' % (host, err))
    ssh.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipfile commands' % sys.argv[0])
        exit(1)
    if not os.path.exists(sys.argv[1]):
        print('No such file', sys.argv[1])
        exit(2)
    ipfile = sys.argv[1]
    password = getpass.getpass()
    cmds = sys.argv[2]
    with open(ipfile) as f:
        for line in f:
            ip = line.strip()
            print(ip)
            t = threading.Thread(target=rcmd, args=(ip, 'yu', password, 22, cmds))
            t.start()
