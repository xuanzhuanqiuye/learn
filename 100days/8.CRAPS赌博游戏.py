#CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
# 玩家第一次摇骰子如果摇出了7点或11点，玩家胜；玩家第一次如果摇出2点、3点或12点，庄家胜；其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
# 如果玩家摇出了第一次摇的点数，玩家胜；其他点数，玩家继续要骰子，直到分出胜负。
import random
from random import randint

def play():
    m=random.randint(0,6)
    n = random.randint(0,6)
    return m,n

if __name__ == '__main__':
    times=1
    first, second = play()
    win=first+second
    print(f"第{times}次，摇出{win}点")
    if times==1 and (first+second==7 or first+second==11):
        print("player win")
        times+=1
    elif times==1 and (first+second==12 or first+second==2 or first+second==3):
        print('庄家 win')
        times += 1
    else:
        print('nobody win')
        times += 1
    while times<10:
        first, second = play()
        print(f"第{times}次，摇出{win}点")
        if first+second==7:
            print('庄家 win')
            times += 1
        elif first+second==win:
            print('player win')
            times += 1
        else:
            print('nobody win,next time')
            times += 1
print('game over')