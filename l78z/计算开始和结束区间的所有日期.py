'''
输入开始日期，
输入结束日期
返回list[]

'''
import datetime

def get_date_range(begin ,end):
    date_list=[]
    while begin<=end:
        date_list.append((begin))
        begindate=datetime.datetime.strptime(begin,"%Y-%m-%d")
        days1=datetime.timedelta(days=1)
        begin=(begindate+days1).strftime("%Y-%m-%d")
    return date_list
begin="2021-04-28"
end="2021-05-20"
datelist=get_date_range(begin,end)

print(datelist)