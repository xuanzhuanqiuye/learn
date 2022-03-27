import smtplib
from email.mime.text import MIMEText
from email.header import Header

def inet_mail(host,sender,passwd,receivers,body,subject):
    # 准备邮件
    msg=MIMEText(body,'plain','utf8')
    msg['from']=Header(sender,'utf8')
    msg['to']=Header(receivers[0],'utf8')
    msg['subject']=Header(subject,'utf8')
    #发送邮件
    smtp=smtplib.SMTP()
    smtp.connect(host)
    #smtp.starttls() #如果服务器要求安全连接，则打开此注释
    smtp.login(sender,passwd)
    smtp.sendmail(sender,receivers,msg.as_bytes())


if __name__ == '__main__':
    server='smtp.163.com'
    sender='love458538235178@163.com'
    receivers=['love458538235178@163.com','316959120@qq.com']
    passwd='VGRWVTTHOPEJVHXM'
    body='我的网络邮件测试，从163发往qq'
    subject='python发送邮件测试'
    inet_mail(server,sender,passwd,receivers,body,subject)