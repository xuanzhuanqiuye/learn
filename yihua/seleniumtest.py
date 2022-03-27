import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client

web=Chrome()
web.get("https://iboss.yihuacomputer.com/login.html")
img=web.find_element(By.XPATH,'//*[@id="randImage"]').screenshot_as_png
ying=Chaojiying_Client('wangpinyu1228','w4604654','926864')
dic=ying.PostPic(img,1902)
code=dic['pic_str']

web.find_element(By.XPATH,'//*[@id="main"]/div[2]/input[1]').send_keys('600823')
web.find_element(By.XPATH,'//*[@id="main"]/div[2]/input[2]').send_keys('w4604654')
web.find_element(By.XPATH,'//*[@id="main"]/div[2]/input[3]').send_keys(code)

web.find_element(By.XPATH,'//*[@id="loginBtn"]').click()
time.sleep(5)