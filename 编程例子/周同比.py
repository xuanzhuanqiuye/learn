import datetime
dic={}
first_line=True
with open("./周同比数据.txt",encoding="utf-8") as fin:
    for line in fin:
        if first_line:
            first_line =False
            continue
        line=line[:-1]
        date_data,sale=line.split("\t")
        dic[date_data]=float(sale)
def get_diff_days(pdate,days):
    curr_date=datetime.datetime.strptime(pdate,"%Y/%m/%d")
    timedelta=datetime.timedelta(days=-days)
    return (curr_date+timedelta).strftime("%Y/%m/%d")

for date,sale in dic.items():
    date7=get_diff_days(date,7)
    sale7=dic.get(date7,0)
    if sale7 == 0:
        print(date,sale,0)
    else:
        week_diff=(sale-sale7)/sale7
        print(date,sale,date7,sale7,week_diff)