import time
import datetime
from datetime import date
from datetime import timedelta
from datetime import datetime

numb = str(input("Number of alarms"))

datetimes = []

i = 0
while i < numb:
    
    Date = str(input("Date"))
    Time = str(input("Time"))

    if Date == "today":
        Date = str(date.today())

    elif Date == "tomorrow":
        yesterday = date.today()
        Date = yesterday + timedelta(days=1)
        Date = str(Date)

    datetime_string = Date + ' ' + Time
    datetime_obj = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
    datetimes.append(datetime_obj)
    
    i = i + 1

while True:
    current_time = datetime.now()
    u = 0
    while u < len(datetimes):
        if current_time > datetimes(u):
            print("alarm")
            datetimes.remove(datetimes(u))
            break
        else:
            u = u + 1
    time.sleep(0.1)