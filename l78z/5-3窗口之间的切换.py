from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
web=Chrome()
web.get("http://lagou.com")
web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a').click()
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
#在selenium眼中，焦点仍在旧窗口，不在新窗口。需要切换窗口
web.switch_to.window(web.window_handles[-1])
#在新窗口中提取内容
content=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div/p').text
web.close()
print(content)
web.switch_to.window(web.window_handles[0])
name=web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').text
print(name)
web.close()
# 处理视频网站iframe的话，必须先拿到iframe ，然后切换视角到iframe，再然后才可以拿到数据