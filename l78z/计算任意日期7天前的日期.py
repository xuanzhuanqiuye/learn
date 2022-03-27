import datetime
def get_diff_days(pdate,days):
    pdate=datetime.datetime.strptime(pdate,'%Y-%m-%d')
    time_gap=datetime.timedelta(days=days)
    result=pdate-time_gap
    return result.strftime('%Y-%m-%d')

print(get_diff_days("2018-4-5",3))
print(get_diff_days("2018-4-5",2))
print(get_diff_days("2018-4-5",1))
print(get_diff_days("2018-4-5",7))