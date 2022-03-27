import pyautogui
import time
#屏幕大小
size=pyautogui.size()
print(size)
#鼠标位置
mouse_pos=pyautogui.position()
print(mouse_pos)
#判断点是否在屏幕内
print(pyautogui.onScreen(100,100))

#把鼠标移动到10，10，周期1秒
pyautogui.moveTo(10,10,duration=1)
#把鼠标移动到画面中央，周期0.5s
pyautogui.moveTo(size.width/2,size.height/2,duration=0.5)
#鼠标相对移动，周期1s
pyautogui.moveRel(100,None,duration=1)

###实时获取鼠标位置
last_pos=pyautogui.position()
try:
    while True:
        new_pos=pyautogui.position()
        if last_pos !=new_pos:
            print(new_pos)
            last_pos=new_pos
except KeyboardInterrupt:
    print('\nExit')

###鼠标的移动加点击
# 系统准备时间
time.sleep(2)
#取得帮助菜单的位置
help_pos=pyautogui.locateOnScreen('./icon/btn_help.png')
goto_pos=pyautogui.center(help_pos)
#移动鼠标
pyautogui.moveTo(goto_pos,duration=1)
#点击
pyautogui.click()
#再移动鼠标
pyautogui.moveRel(None,650,duration=1)
#双击
pyautogui.doubleClick()

###键盘输入
time.sleep(2)
#点击一次编辑器
pyautogui.click(button='left')
# 输入i like python
pyautogui.typewrite('i like python')
#输入回车，然后继续输入内容
pyautogui.typewrite('\ni like python too',0.1)
#输入good ，然后将头文字改为大写G，最后再行尾写个句号
pyautogui.typewrite(['enter','g','o','o','d','left','left','left','backspace','G','end','.'],0.1)

###组合键的使用
time.sleep(3)
#每个操作间隔0.5s
pyautogui.PAUSE=0.5
# pyautogui.FAILSAFE=True
#记事本打出时间
pyautogui.press('f5')
#打入三行内容
pyautogui.typewrite('\ni like python')
pyautogui.typewrite('\ni like python')
pyautogui.typewrite('\ni like python')
# 按下ctrl
pyautogui.keyDown('ctrl')
pyautogui.press('a')
pyautogui.press('c')
pyautogui.keyUp('ctrl')
#鼠标点击记事本下方
pos=pyautogui.moveRel(100,0,duration=0.2)
pyautogui.click()
pyautogui.typewrite('\n\n')
pyautogui.hotkey('ctrl','v')

