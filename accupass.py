import requests
import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import req_get
from selenium.webdriver.chrome.options import Options

#driver_path = r"C:\Chrome_driver\chromedriver.exe"
#driver = webdriver.Chrome(driver_path)
url = "https://www.accupass.com/?area=center"
#driver.get(url)

cc = req_get.get_sel_html(url)
#print(cc)
#driver.close()
soup = BeautifulSoup(cc, "html.parser")
#print(soup)
time.sleep(2)
contain = soup.find('div', {'id': 'content'})
#print(contain)
events = contain.find_all('div', {'class': 'style-6d9f2c7b-mobile-theme-container'})

#print(events)
for event in events:
    #print(event, '\n')
    details = event.find_all('div', {'class': 'style-5735f327-card'})
    #print(detail, '\ninto\n')
    for detail in details:
        #print(detail, '\n')
        d = detail.find('div')
        di = d.find('div')
        main_url = "https://www.accupass.com"
        page_url = main_url + di.a.get('href')
        #print(page_url)
        #driver.get(page_url)
        dcc = req_get.get_sel_html(page_url)


#d = {'area': 'center'}
#headers = {'referer': 'www.accupass.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#r = requests.post(url, data=json.dumps(d), headers=headers)

