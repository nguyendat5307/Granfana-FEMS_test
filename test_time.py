import time
import datetime
t = time.localtime()
print(str(t.tm_year)+str(t.tm_mon))

str_dt = '2020-06-05T10:47:16+0800'
print(str(str_dt))
ts = datetime.datetime.strptime(str_dt[:19], "%Y-%m-%dT%H:%M:%S")
print(ts.year)