import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
web=Chrome()
web.get('https://kyfw.12306.cn/otn/resources/login.html')
time.sleep(2)
web.find_element(By.XPATH,'//*[@id="J-userName"]').send_keys('wangpinyu1228')
web.find_element(By.XPATH,'//*[@id="J-password"]').send_keys('w4604654')
web.find_element(By.XPATH,'//*[@id="J-login"]').click()