import datetime
def date():
    now=datetime.datetime.now()
    print(now.strftime("%d/%m/%Y"))
   # print(datetime.datetime.now())
    print(datetime.date.today()) 
    x=datetime.datetime(2024, 6, 20, hour=10, minute=30, second=0)
    y=datetime.datetime(2026, 5, 20, hour=15, minute=45, second=30)
    diff=y-x
    print(diff)
    end=datetime.datetime.now()
    difference=end-now
    print(difference)
date()