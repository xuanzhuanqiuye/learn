import hashlib
import os
import tarfile

import requests
import wget


def has_new_ver(ver_fname, ver_url):
    # 如果服务器上有新版本返回True，否则返回False
    # 如果本地没有版本文件，则远端有新版本
    if not os.path.exists(ver_fname):
        return True
    # 如果本地版本文件和服务器版本文件不一致
    with open(ver_fname) as f:
        local_ver = f.read()
    r = requests.get(ver_url)
    if local_ver != r.text:
        return True
    return False


def file_ok(fname, md5url):
    # 如果文件未损坏，返回True，否则返回False
    m = hashlib.md5()
    with open(fname, 'rb') as f:
        while True:
            data = f.read(4096)
            if not data:
                break
            m.update(data)
    r = requests.get(md5url)
    if m.hexdigest() == r.text.strip():
        return True
    return False


def deploy(app_fname, deploy_dir, dest):
    # 部署软件
    # 解压
    tar = tarfile.open(app_fname)
    tar.extractall(path=deploy_dir)
    tar.close()

    # 拼接出解压后的绝对路径
    app_dir = os.path.basename(app_fname)
    app_dir = app_dir.replace('.tar.gz', '')
    app_dir = os.path.join(deploy_dir, app_dir)

    # 创建软链接
    if os.path.exists(dest):
        os.remove(dest)
    os.symlink(app_dir, dest)


if __name__ == '__main__':
    # 判断服务器上是否有新版本
    ver_url = 'http://192.168.0.188/deploy/live_ver'
    ver_fname = '/var/www/deploy/live_ver'
    if not has_new_ver(ver_fname, ver_url):
        print("未发现新版本")
        exit(1)
    # 下载新版本
    resp = requests.get(ver_url)
    app_url = 'http://192.168.0.188/deploy/packages/mysite-%s.tar.gz' % resp.text.strip()
    app_fname = '/var/www/download/mysite-%s.tar.gz' % resp.text.strip()
    wget.download(app_url, app_fname)

    # 校验下载的软件包是否损坏
    md5url = app_url + '.md5'
    if not file_ok(app_fname, md5url):
        print("文件已损坏")
        os.remove(app_fname)
        exit(2)

    # 部署软件
    deploy_dir = '/var/www/deploy'
    dest = '/var/www/html/current'
    deploy(app_fname, deploy_dir, dest)

    # 更新本地版本文件
    if os.path.exists(ver_fname):
        os.remove(ver_fname)
    wget.download(ver_url, ver_fname)
