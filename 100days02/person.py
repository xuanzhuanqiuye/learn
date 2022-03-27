

class Person:
    def __int__(self):
        super(Person,self).__init__()
class Beauty(Person):
    def __init__(self,name):
        super(Beauty, self).__init__()
        self.name=name
    def playGame(self,gameName):
        print(self.name,"is playing",gameName)


if __name__ == '__main__':
    girl=Beauty("lily")
    girl.playGame('lol')