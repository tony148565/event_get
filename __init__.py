import re
import req_get

taichang_city = "https://www.taichung.gov.tw/"
url = "https://www.taichung.gov.tw/8868/8872/12026?currentDate=2020/5/04%20%E4%B8%8A%E5%8D%88%2012:00:00&topcats=&topcat="
soup = req_get.get_html(url, taichang_city)
section = soup.find('section', {'class': 'list event'})
events = section.find_all_next('tr')
#database need count number
for event in events:
    i = 1
    tds = event.find_all('td')
    #print(tds)
    for td in tds:
        if i == 5:
            ur = taichang_city + td.a.get('href')
            post = req_get.get_html(ur, taichang_city)
            post_section = post.find('section', {'class': 'meta'})
            events_details = post_section.find_all_next('tr')
            k = 1
            for events_detail in events_details:
                sch = events_detail.find('th')
                detail = events_detail.find('td')
                sss = str(sch.string)
                ddd = str(detail.string)
                sss = re.sub(r"\s+", "", sss)
                ddd = re.sub(r"^\s+", "", ddd)
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
            i = 1
        i = i+1
    print('-----------------------------------')

