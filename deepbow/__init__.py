import requests
import json
from  bs4 import BeautifulSoup
url="https://www.taichung.gov.tw/8868/8872/12026?currentDate=2020/4/17%20%E4%B8%8A%E5%8D%88%2012:00:00&topcats=&topcat="
d = {'key1': 'value1', 'key2': 'value2'}
headers = {'referer': 'www.taichung.gov.tw', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
#payload = {'__RequestVerificationToken':'0Z8IG9S7KOrZpJAcodDUfx5ipRJsxbfWNRQmH8tcNo9yi0ahMrKIifQIw-NZf3SFV5a3csKg4dQEtCVleP97t0hfK7rc3PJijUCa6BdZA081','currentDate':'2020/4/14 上午 12:00:00'}
r = requests.post(url, data=json.dumps(d), headers=headers)
soup = BeautifulSoup(r.text, 'html.parser')
section = soup.find('section', {'class': 'list event'})
events = section.find_all_next('tr')

for event in events:
    i = 1
    tds = event.find_all('td')
    #print(tds)
    for td in tds:
        if i ==1:
            print(td.span.string)
        elif i == 5:
            print(td.a.string)
            i = 1
        else:
            print(td.string)
        i = i+1
    print('-----------------------------------')

