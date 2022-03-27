
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
import  time
web=Chrome()
web.get("http://lagou.com")
#找到某个元素，点击他
el=web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')
#点击按钮
el.click()
#让浏览器反应一会，碰到ajax的网站特别需要注意
time.sleep(1)
#找到输入框，输入python，输入回车
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)
#查找存放数据的位置，进行数据提取
#找到页面中存放数据的所有的div
li_list=web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
for li in li_list:
   name=li.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
   print(name)


