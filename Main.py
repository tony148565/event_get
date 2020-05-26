import os
import __init__
import accupass
import datetime
import time
import SQL_connect


while 1:
    timenow = datetime.datetime.now()
    date = " "
    date = date + str(timenow.year) + "/" + str(timenow.month) + "/" + str(timenow.day)
    print(date)
    __init__.taichanggov(date)
    accupass.accupassget()
    print("zzzzzzzzzz")
    time.sleep(3)