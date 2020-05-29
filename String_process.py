

def date_and_time(dateandtime):
    time = dateandtime.rpartition('T')
    #print(time)
    re = {'date': time[0], 'time': time[2]}
    #print(re)
    return re


def address_where(address):
    addre = ""
    if address[0:2:1] == "台灣":
        addre = address[2::1]
    list = addre.rpartition('市')
    city = list[0]
    city2 = city[0:2:1]
    dis = list[2]
    district = dis.rpartition('區')
    district2 = district[0]
    for i in range(10):
        district2 = district2.replace(str(i), '')
    full_address = address.rpartition('區')
    full = full_address[0]
    for i in range(10):
        full = full.replace(str(i), '')
    final_address = full + full_address[1] + full_address[2]
    addresss = {'addressID': 0,
                'eastLongitude': 0,
                'northLatitude': 0,
                'city': city2,
                'district': district2,
                'fullAddress': final_address}
    return addresss


