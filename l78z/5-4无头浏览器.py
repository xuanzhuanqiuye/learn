#
import time

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
opt=Options()
opt.add_argument("--headless")
opt.add_argument('--disable-gpu')
web=Chrome(options=opt)
web.get("https://www.endata.com.cn/BoxOffice/BO/Year/index.html")
sel_el=web.find_element(By.XPATH,'//*[@id="OptionDate"]')
sel=Select(sel_el)
for i in range(len(sel.options)):
    sel.select_by_index(i)
    time.sleep(2)
    content=web.find_element(By.XPATH,'//*[@id="TableList"]/table').text
    print(content)
print("over")
web.close()
#web.page_source() 可以拿显示后的页面代码，是经过ajax或者js处理后的代码，不像源代码上面内容都看不到