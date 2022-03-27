from math import sqrt

class Point():
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def moveTo(self,x,y):
        self.x=x
        self.y=y
    def moveBy(self,dx,dy):
        self.x += dx
        self.y += dy
    def farFrom(self,other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.moveBy(-1, 2)
    print(p2)
    print(p1.farFrom(p2))

if __name__ == '__main__':
    main()