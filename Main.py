import os
import __init__
import accupass
import datetime
import time
import String_process
import locate
import SQL_connect


while 1:
    timenow = datetime.datetime.now()
    date = " "
    #print(timenow)
    date = date + str(timenow.year) + "/" + str(timenow.month) + "/" + str(timenow.day)
    updatedata = timenow.hour
    #print(updatedata)
    #print(date)
    if updatedata == 23:
        #__init__.taichanggov(date)
        accupass.accupassget()
        #SQL_connect.select('Address')
        #gg = locate.loc('卓越商務中心')
        #print(gg.get('latitude'))
        #print(gg.get('longitude'))
        #re = String_process.date_and_time("2020-06-13T14:00:00")
        #gg = String_process.address_where("台灣台中市台灣大道二段二號16樓之2")
        #print(gg)
        print("zzzzzzzzzz")
    else:
        print("no update")
    time.sleep(3600)
    break
