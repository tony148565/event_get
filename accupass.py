import requests
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import req_get
import String_process


def accupassget():
    url = "https://www.accupass.com/?area=center"
    url2 = "https://api.accupass.com/v3/home/center/channel/taichung_s"
    url3 = "https://api.accupass.com/v3/events/"
    url5 = "https://www.accupass.com/event/"
    cc = req_get.get_xhr(url, url2).json()
    aa = cc.get('channel')
    bb = aa.get('tagEvents')
    for k in bb:
        webId = k.get('eventIdNumber')
        url4 = url3 + webId
        inWeb = req_get.get_xhr(url, url4).json()
        locat = inWeb.get('location')
        photourl = url3 + k.get("photoUrl")
        eventDate = inWeb.get('eventTimeObj')
        re = String_process.date_and_time(eventDate.get('startDateTime'))
        startdate = re.get('date')
        opentime = re.get('time')
        re2 = String_process.date_and_time(eventDate.get('endDateTime'))
        enddate = re2.get('date')
        closetime = re2.get('time')
        cate = inWeb.get('category')
        url6 = url5 + webId
        booking = inWeb.get('registerBtn')
        #print(url4)
        #print(inWeb.get('title'))
        print(inWeb.get('address'))
        #print(photourl)
        #print(locat.get('latitude'))
        #print(locat.get('longitude'))
        #print(startdate)
        #print(opentime)
        #print(enddate)
        #print(closetime)
        #print(cate.get('name'))
        #print(booking.get('price'))
        data = {'activity': 0,
                'name': inWeb.get('title'),
                'activityType': cate.get('name'),
                'activityPicture': photourl,
                'activityURL': url6,
                'openTime': opentime,
                'closeTime': closetime,
                'startDate': startdate,
                'endDate': enddate,
                'bookingID': 0,
                'addressID': 0}
        add = String_process.address_where(inWeb.get('address'))
        add['northLatitude'] = locat.get('latitude')
        add['eastLongitude'] = locat.get('longitude')
        print(add)
        print(data)