
import datetime
curr_datetime=datetime.datetime.now()
print(curr_datetime,type(curr_datetime))

str_time=curr_datetime.strftime("%Y/%m/%d")
print(str_time)
print(curr_datetime.year)
print(curr_datetime.month)
print(curr_datetime.day)
print(curr_datetime.hour)
print(curr_datetime.minute)
print(curr_datetime.second)
