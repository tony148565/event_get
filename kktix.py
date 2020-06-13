import req_get
import String_process
import kktix_info


def kktix_get():
    url = "https://kktix.com/events?utf8=%E2%9C%93&search=%E5%8F%B0%E4%B8%AD&start_at=2020%2F06%2F11"
    url2 = "https://kktix.com/events"
    url3 = "https://kktix.com"
    date = "date: Thu, 11 Jun 2020 15:36:19 GMT"
    #  cookies = "locale=zh-TW; __auc=8942ff5c1724bf3b146c138f0b9; mobileNotVerified=1; _gid=GA1.2.85944415.1591862277; uvts=2e52c95d-8129-4c16-7e63-3571d459cf68; __asc=e9ef6b94172a40658cf835d6d4b; _dc_gtm_UA-44784359-1=1; user_display_name_v2=tony890723; user_avatar_url_v2=https%3A%2F%2Fwww.gravatar.com%2Favatar%2Fed172780aa5bf6ed09b27f971a376208.png; user_path_v2=%2Fuser%2F2753627; user_time_zone_v2=Asia%2FTaipei; user_time_zone_offset_v2=28800; kktix_session_token_v2=7e994597e802d9e0c458920148840906; XSRF-TOKEN=M0R1OFFLQ6oLzpr61ZvnfyHAfC9DZR2k2nSK4USAZ8o6xpNx31DNCECdV%2BQ7%2FYlvbgsIeNKJzeciRZi9duFmAA%3D%3D; _ga_LWVPBSFGF6=GS1.1.1591889778.6.1.1591891501.46; _ga=GA1.2.673203028.1588775573"
    #  headers = {"authority":  'kktix.com', 'referer': url2, 'date': date, 'cookie': cookies, 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    flag = 0
    while 1:
        if flag == 1:
            break
        page = req_get.get_sel_html(url)
#  print(page)
        react = page.find('div', {'id': 'react-main-container'})
        nexts = page.find('div', {'class': 'pagination pull-right'})
#  print(nexts)
        lastpag = nexts.find_all('li')
        data = react.find('div')
        inne = data.find('div')
        inner = inne.find('ul', {'class': 'events clearfix'})
        events = inner.find_all('li')
        for event in events:
            try:
                url = event.a.get('href')
                types = event.find('span', {'class': 'category'})
                types = str(types)
                types = String_process.kktix_react(types)
            #  types = types.find('react')
            #print(types)
                kktix_info.info(url, types)
            # print(url)
            except AttributeError:  # check if value is null
                continue

        for page in lastpag:  # turn the next page
        #  print(page)
            nn = page.find('a').string
        #  print(nn)
            if nn == '›':
                flag = 0
                nurl = page.a.get('href')
                url = url3 + nurl
                print(url)
                break
            else:
                flag = 1
        print("flag is", flag)
