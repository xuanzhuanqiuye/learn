

def main():
    with open("./data/test.jpg",'rb') as f:
        content=f.read()
        with open("./data/testbak.jpg",'wb') as f1:
            f1.write(content)
    f1.close()
    f.close()

if __name__ == '__main__':
    main()