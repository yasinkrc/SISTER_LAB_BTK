from datetime import datetime 
# from datetime import date 
# from datetime import time 

# import datetime

from datetime import timedelta


# result =dir(datetime.datetime)
# result=dir(datetime.time)
# result=dir(datetime.date)

simdi=datetime.now()
simdi=datetime.today()
result=simdi.day
result=simdi.hour
result=simdi.year
result=simdi.month
result=simdi.minute
result=simdi.fold  #--> fold yuvarlama yapar 
result=simdi.second
result=simdi.__class__

# result=help(simdi.fold,max)

result=simdi.ctime()
result=datetime.ctime(simdi)

result=simdi.strftime("%Y")
result=simdi.strftime("%X")
result=simdi.strftime("%d")
result=simdi.strftime("%A")
result=simdi.strftime("%B")
result=simdi.strftime("%Y  %B  %A")

# result="21 Nisan 2019"

# gun , ay , yil =result.split()



t='15 April 2019 hour 10:12:30'
result=datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
result=result.year


birthday=datetime(1983,5,9 ,12,30,10)
result=datetime.timestamp(birthday) #saniye
result=datetime.fromtimestamp(result) #saniye to datetime

result=datetime.fromtimestamp(0)

result=simdi-birthday
result=result.days
# result=result.second bende bu hata veriyır 
# result=result.microseconds bende bu hata veriyır 

"""İleri bir tarihi bulmak için ise Timedelta yı import etmeniz gerekiyor """

print(simdi)
result=simdi+timedelta(days=545,minutes=1546,microseconds=215)

print(result)