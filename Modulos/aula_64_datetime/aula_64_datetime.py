from datetime import datetime, timedelta


data = datetime(2019,4,20,10,53,20)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print(data.strftime('%H %M %S'))
data2 = datetime.strptime('20/04/2019','%d/%m/%Y')
print(data2.timestamp())
print(datetime.fromtimestamp(1555729200.0))


data3 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
data3 = data3 + timedelta(days=5,seconds=2*60*60)
print(data3)

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:24:00', '%d/%m/%Y %H:%M:%S')
dif = d2-d1
print(dif)
print(dif.days)
print(dif.seconds)
print(dif.total_seconds())
print(d1.time())
print(d2<d1)