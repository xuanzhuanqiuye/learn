import datetime
def unix_to_date(unix):
    result_date=datetime.datetime.fromtimestamp(unix)
    result=result_date.strftime("%Y-%m-%d %H:%M:%S")
    return result

unix=1620747647
print(unix_to_date(unix))