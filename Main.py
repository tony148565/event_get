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
    date = date + str(timenow.year) + "/" + str(timenow.month) + "/" + str(timenow.day)
    print(date)
    #__init__.taichanggov(date)
    accupass.accupassget()
    #SQL_connect.select('ActivityMain')
    #gg = locate.loc('卓越商務中心')
    #print(gg.get('latitude'))
    #print(gg.get('longitude'))
    #re = String_process.date_and_time("2020-06-13T14:00:00")
    #gg = String_process.address_where("台灣台中市403西區臺灣大道二段285號31樓3117教室")
    #print(gg)
    #print("zzzzzzzzzz")
    time.sleep(3)
    break
