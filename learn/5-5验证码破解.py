#1.图像识别
#2.选择互联网上成熟的验证码破解工具
import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

web=Chrome()
web.get("http://www.chaojiying.com/user/login/")
img=web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
ying=Chaojiying_Client('wangpinyu1228','w4604654','926864')
dic=ying.PostPic(img,1902)
code=dic['pic_str']

web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('wangpinyu1228')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('w4604654')
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(code)
time.sleep(5)
web.find_element(By.XPATH,'/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()