

def getFormat(path):
    liststr=path.split('.')
    formatstr=liststr[1]
    return formatstr

if __name__ == '__main__':
    path='/opt/exe/readme.txt'
    print(getFormat(path))