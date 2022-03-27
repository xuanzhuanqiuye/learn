import time
import requests
import execjs

node = execjs.get()
ctx = node.compile(open('./test.js',encoding='utf-8').read())
pwdtemp1 = ctx.eval("hex_md5('w4604654')")
pwdtemp2 = str(pwdtemp1)+str(200)
func='hex_md5("{0}")'.format(pwdtemp2)
pwd=ctx.eval(func)

urlLogin="https://iboss.yihuacomputer.com/api/login/loginLocal"
#https://iboss.yihuacomputer.com/api/login/loginLocal?username=600823&password=7eb9f048e690e70eba5147cee8aacab3&timestamp=179&dataSource=1
# &validation=4219&Sun Jan 16 2022 09:37:23 GMT+0800 (中国标准时间)
loginTime=time.strftime('%b %d %Y %H:%M:%S',time.localtime())
data={
    'username':'600823',
    'password':pwd,
    'timestamp':"200",
    'dataSource':1,
    'validation':"4219&Sun "+loginTime+"GMT+0800 (中国标准时间)"

}
headers={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

}
resp=requests.post(urlLogin,data=data,headers=headers)
print(resp.json())
cook=resp.cookies
cookies = requests.utils.dict_from_cookiejar(cook)
headers1={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
    "Referer": "https://iboss.yihuacomputer.com/index.jsp",
    "Cookie": cookies['JSESSIONID']
}
#https://iboss.yihuacomputer.com/api/serviceReportCspa?_dc=1642324043311&serviceDeptName=吉林长春九台办事处&serviceDeptId=85834&isAll=1&bankSiteName=中国建设银行
# &bankSite=76751&beginDate=2022-01-01&endDate=2022-01-16&caseSource=S-0&planType=0&start=0&limit=25
dc=str(int(round(time.time()*1000)))
print(dc)
params={
    "_dc": dc,
    "serviceDeptName": "吉林长春九台办事处",
    "serviceDeptId": "85834",
    "isAll": 1,
    "bankSiteName": "中国建设银行",
    "bankSite": "76751",
    "beginDate": "2022-01-01",
    "endDate": "2022-01-16",
    "caseSource": "S-0",
    "planType": 0,
    "start": 0,
    "limit": 25,
}
urlData="https://iboss.yihuacomputer.com/api/serviceReportCspa"
resp1=requests.get(urlData,params=params,headers=headers1)
resp1.encoding='utf-8'
print(resp1.status_code)
