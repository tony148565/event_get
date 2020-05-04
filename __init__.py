import requests
import json
from  bs4 import BeautifulSoup
import re
taichang_city="https://www.taichung.gov.tw/"
url="https://www.taichung.gov.tw/8868/8872/12026?currentDate=2020/5/04%20%E4%B8%8A%E5%8D%88%2012:00:00&topcats=&topcat="
d = {'key1': 'value1', 'key2': 'value2'}
headers = {'referer': 'www.taichung.gov.tw', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#payload = {'__RequestVerificationToken':'0Z8IG9S7KOrZpJAcodDUfx5ipRJsxbfWNRQmH8tcNo9yi0ahMrKIifQIw-NZf3SFV5a3csKg4dQEtCVleP97t0hfK7rc3PJijUCa6BdZA081','currentDate':'2020/4/14 上午 12:00:00'}
r = requests.post(url, data=json.dumps(d), headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
section = soup.find('section', {'class': 'list event'})
events = section.find_all_next('tr')
#database need count number
for event in events:
    i = 1
    tds = event.find_all('td')
    #print(tds)
    for td in tds:
        if i == 5:
            #print(td.a.string)
            #print(td.a.get('href'))
            ur = taichang_city + td.a.get('href')
            #print(ur)
            p = requests.post(ur, data=json.dumps(d), headers=headers)
            post = BeautifulSoup(p.text, 'html.parser')
            post_section = post.find('section', {'class': 'meta'})
            events_details = post_section.find_all_next('tr')
            k = 1
            for events_detail in events_details:
                sch = events_detail.find('th')
                detail = events_detail.find('td')
                sss = str(sch.string)
                ddd = str(detail.string)
                #print(type(ddd))
                #print(type(sss))
                sss = re.sub(r"\s+", "", sss)
                ddd = re.sub(r"^\s+", "", ddd)
                #print(sss)
                #print(detail.string)
                if sss == "活動名稱":
                    print("Activity name: ")
                    print(ddd)
                elif sss == "主辦單位":
                    print("address: ")
                    print(ddd)
                elif sss == "行政區":
                    print("district: ")
                    print(ddd)
                elif sss == "活動起日":
                    print("start Date: ")
                    print(ddd)
                elif sss == "活動迄日":
                    print("end Date: ")
                    print(ddd)
                elif sss == "*市政分類":
                    print("activityType: ")
                    print(ddd)
                    #k = 1
                #k = k + 1
            i = 1
        i = i+1
    print('-----------------------------------')

