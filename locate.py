import requests
import json


def loc(add):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyBBco6LiNuyOYcih93P9Khj4VO2lhT5Fzc&address=' + add
    r = requests.get(url)
    j = json.loads(r.text)
    #print(r.text)
    #print(j["results"][0]["geometry"]["location"]["lat"])
    #print(j["results"][0]["geometry"]["location"]["lng"])
    loca = {'latitude': j["results"][0]["geometry"]["location"]["lat"],
            'longitude': j["results"][0]["geometry"]["location"]["lng"]}
    return(loca)
