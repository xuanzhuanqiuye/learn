# 此接口支持发送验证码短信、订单通知短信；
# 调试期间，请使用测试专用短信模板：您的验证码是：1234。请不要把验证码泄露给其他人；
# 请求参数中的account和password分别为 APIID、APIKEY，请在本页面上方处获取。

# !/usr/local/bin/python
# -*- coding:utf-8 -*-
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 查看用户名 登录用户中心->验证码通知短信>产品总览->API接口信息->APIID
account = "用户名"
# 查看密码 登录用户中心->验证码通知短信>产品总览->API接口信息->APIKEY
password = "密码"


def send_sms(text, mobile):
    params = urllib.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = urllib.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "138xxxxxxxx"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))