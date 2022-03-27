#登录——》得到cookie
#带着cookie 去请求到书架url——》书架上的内容
#必须得把上面两个操作联系起来
#我们可以使用session进行请求——》session你可以认为是一连串得请求，在这个过程中cookie不会丢失
import requests
#session 会话
session=requests.session()

data={
    "loginName":"18028706448",
    "password":"W4604654"
}
url="https://passport.17k.com/ck/user/login"
session.post(url,data=data)

# print(resp.cookies)
resp=session.get("https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919")
print(resp.json())