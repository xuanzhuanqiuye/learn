import datetime

birthday="1997-12-20"
birthday_date=datetime.datetime.strptime(birthday,"%Y-%m-%d")
print(birthday_date,type(birthday_date))
now=datetime.datetime.now()
print(now)
minus=now-birthday_date
print(minus.days)