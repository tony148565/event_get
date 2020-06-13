

def date_and_time(dateandtime):  # for accupass
    time = dateandtime.rpartition('T')
    #print(time)
    re = {'date': time[0], 'time': time[2]}
    #print(re)
    return re


def kktix_date(time_list):  # ex: 2000/01/01 --> 2000-01-01
    afrp = []  # after replace
    for i in time_list:
        rpart = i.rpartition('(')
        tt = rpart[0]
        rpart2 = tt.rpartition('(')
        tt2 = rpart2[0]
        tt3 = rpart2[2]
        rpart3 = tt3.rpartition(' ')
        tt4 = rpart3[2]
        tt5 = tt4 + ":00"
        afrp.append(tt2.replace('/', '-'))
        afrp.append(tt5)
    if len(afrp) == 2:
        afrp.append(afrp[0])
        afrp.append(afrp[1])
    re = {'startDate': afrp[0], 'openTime': afrp[1], 'endDate': afrp[2], 'closeTime': afrp[3]}
    return re


def kktix_booking_date(time_list):
    afrp = []
    for i in time_list:
        rpart = i.rpartition('(')
        tt = rpart[0]
        tt2 = tt.replace('/', '-')
        tt3 = tt2 + ':00'
        afrp.append(tt3)
    if len(afrp) == 1:
        afrp.append(afrp[0])
    #  print(afrp)
    return afrp


def kktix_react(strr):
    #  print(strr)
    strr = strr.rpartition('<!--')
    #  print(strr)
    st = strr[0].rpartition('-->')
    #  print(st[2])
    re = st[2]
    return re


def address_where(address):
    addre = ""
    if address[0:2:1] == "台灣":
        addre = address[2::1]
    else:
        addre = address
    list = addre.rpartition('市')
    city = list[0]
    city2 = city[0:2:1]
    dis = list[2]
    district = dis.rpartition('區')
    district2 = district[0]
    for i in range(10):  # 去郵遞區號
        district2 = district2.replace(str(i), '')
    full_address = address.rpartition('區')
    full = full_address[0]
    for i in range(10):  # 去郵遞區號
        full = full.replace(str(i), '')
    final_address = full + full_address[1] + full_address[2]
    #print(final_address)
    addresss = {'addressID': 0,
                'eastLongitude': 0,
                'northLatitude': 0,
                'city': city2,
                'district': district2,
                'fullAddress': final_address}
    return addresss


