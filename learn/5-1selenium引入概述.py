#把解压缩的浏览器驱动chromedriver 放在python解释器所在的文件夹,selenium可以启动浏览器，让浏览器帮你完成各种复杂的操作

from selenium.webdriver import  Chrome
# 创建个浏览器对象
web=Chrome()
# 打开一个网址
web.get("http://www.baidu.com")
print(web.title)