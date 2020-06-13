import req_get
import String_process
import SQL_connext

def info(url, types):
    #url = "https://amyslschool.kktix.cc/events/ad9224fc-copy-3"
    page = req_get.get_sel_html(url)
    #print(page)
    content = page.find('div', {'class': 'content container'})
    title = content.find('div', {'class': 'header'})  # name
    name = title.find('h1')
    #  print(name.string)
    info = content.find('div', {'class': 'event-info'})  # time address
    #print(info)
    infos = info.find('span', {'class': 'info-desc'})
    time_list = []
    r = 0
    time = infos.find_all('span', {'class': 'timezoneSuffix'})
        # time_list = []
        # r = 0
    for t in time:
        time_list.append(t.string)
        #print(t.string)
        # r = r+1
    #print(time_list)
    re = String_process.kktix_date(time_list)
    #  print(re)
    pic = content.find('div', {'class': 'og-banner'})  # picture
    picture = pic.img.get('src')
    #  print(picture)
    ticket = content.find('div', {'class': 'tickets'})  # booking
    bookingurl = ticket.a.get('href')
    booking = ticket.find('div', {'class': 'table-wrapper'})
    period = booking.find('td', {'class': 'period'})
    #print(period)
    bookingtimes = period.find_all('span', {'class': 'timezoneSuffix'})
    bookingtime_list = []
        # r = 0
    for t in bookingtimes:
        bookingtime_list.append(t.string)
        #print(t.string)
        # r = r+1
    #  print(bookingtime_list)
    booking_re = String_process.kktix_booking_date(bookingtime_list)
    #print(booknng_re)
    prices = booking.find('td', {'class': 'price'})
    price = prices.find('span', {'class': 'price'})
    # print(price)
    #print(price.string)
    if price.string == "免費":
        price = 0
    else:
        extra = prices.find('span', {'class': 'currency-value'})
        price = extra.string
        #  print(price)
    #  print(price)
    #  print(bookingurl)
    locate = content.find('div', {'class': 'location clearfix'})  # locate
    addr = locate.find('div', {'class': 'address'})
    addr = addr.string
    addr = addr.replace(' ', '')
    addr = addr.replace('\n', '')
    #  print(addr)
    address = String_process.address_where(addr)
    #  print(address)

    #print(locate)
    location = locate.find('div', {'class': 'map-wrapper'})
    #print(location)
    locat = location.find('div', {'class': 'map-wrapper'})
    #print(locat)
    lat = locat.get('data-lat')  # north
    lng = locat.get('data-lng')  # east
    address['northLatitude'] = lat
    address['eastLongitude'] = lng
    data = {'activityID': 0,
            'name': name.string,
            'activityType': types,
            'activityPicture': picture,
            'activityURL': url,
            'openTime': re.get('openTime'),
            'closeTime': re.get('closeTime'),
            'startDate': re.get('startDate'),
            'endDate': re.get('endDate'),
            'bookingID': 0,
            'addressID': 0}
    booking_data = {'bookingID': 0,
                    'bookingURL': bookingurl,
                    'bookingStartDate': booking_re[0],
                    'bookingEndDate': booking_re[1],
                    'price': int(price)}
    #  print(lat, lng)
    SQL_connext.insertdata(data, address, booking_data)
    #print(address)
    #print(data)
    #print(booking_data)
