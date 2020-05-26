import requests
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import req_get
from selenium.webdriver.chrome.options import Options

#driver_path = r"C:\Chrome_driver\chromedriver.exe"
#driver = webdriver.Chrome(driver_path)


def accupassget():
    url = "https://www.accupass.com/?area=center"
    url2 = "https://api.accupass.com/v3/home/center/channel/taichung_s"
    url3 = "https://api.accupass.com/v3/events/"
#driver.get(url)

    cc = req_get.get_xhr(url, url2).json()
#print(type(cc))
#print(cc)
    aa = cc.get('channel')
#print(type(aa))
    bb = aa.get('tagEvents')
#print(type(bb))
    for k in bb:
    #print(k)
        webId = k.get('eventIdNumber')
    #webName = k.get('name')
        url4 = url3 + webId
    #print(url4)
        inWeb = req_get.get_xhr(url, url4).json()
    #print(inWeb)
        print(inWeb.get('title'))
        print(inWeb.get('address'))
        eventDate = inWeb.get('eventTimeObj')
        print(eventDate.get('startDateTime'))
        print(eventDate.get('endDateTime'))
        cate = inWeb.get('category')
        print(cate.get('name'))
        booking = inWeb.get('registerBtn')
        print(booking.get('price'))
    #print(inWeb)



#driver.close()
#soup = BeautifulSoup(cc, "html.parser")
#soup = req_get.get_sel_html(url)
#print(soup)
#time.sleep(2)
#contain = soup.find('div', {'id': 'content'})
#print(contain)
#events = contain.find_all('div', {'class': 'style-6d9f2c7b-mobile-theme-container'})

#print(events)
#for event in events:
    #print(event, '\n')
    #details = event.find_all('div', {'class': 'style-5735f327-card'})
    #print(detail, '\ninto\n')
    #for detail in details:
        #print(detail, '\n')
        #di = d.find('div')
        #main_url = "https://www.accupass.com"
        #page_url = main_url + di.a.get('href')
        #print(page_url)
        #driver.get(page_url)
        #dcc = req_get.get_sel_html(page_url)
        #dca = dcc.find('div', {'class': 'style-08a13ad7-event-detail'})
        #dcb = dca.find('section', {'class': 'style-2980af29-event-basicinfo-container'})
        #dce = dca.find('section', {'class': 'style-906f804a-event-content-container'})
        #print(dcb)


#d = {'area': 'center'}
#headers = {'referer': 'www.accupass.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#r = requests.post(url, data=json.dumps(d), headers=headers)

