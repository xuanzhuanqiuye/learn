import smtplib
from email.mime.text import MIMEText
from email.header import Header
#准备邮件
msg=MIMEText('python本地邮件测试','plain','utf8')
msg['from']=Header('root','utf8')
msg['to']=Header('yu','utf8')
msg['subject']=Header('py test','utf8')
#发送邮件
smtp=smtplib.SMTP('127.0.0.1')
sender='root'
receivers=['yu','root']
smtp.sendmail(sender,receivers,msg.as_bytes())