#assumption data recived as bunch of set which collected in maximum waiting time.
#if max wait time=1min data colleted for 1min and send to the system

import json
from math import radians, cos, sin, asin, sqrt
import requests


#data=json.loads('{"time": 125885555, "id": 1001, "regno": "300-2050", "movedata": [{"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}]}')



def haversine(lon1, lat1, lon2, lat2):
    # haversine formula
    dlon = radians(radians(lon2) - radians(lon1))
    dlat = radians(radians(lat2) - radians(lat1))
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371*1000 #get as meters
    return c * r

def sendalert(data):
    url = "http://localhost:5006"
    firstcoor=data["movedata"][0]
    lastcoor=data["movedata"][len(data["movedata"])-1]
    distance= haversine(firstcoor["lon"],firstcoor["lat"],lastcoor["lon"],lastcoor["lat"])

    if(distance<5):
        alert={}
        alert["id"] = data["id"]
        alert["movedata"] = data["movedata"][0]
        alert["regno"] = data["regno"]
        alert["alerttype"] = "Over waiting"
        alert["alertmsg"] = "Wait for long time"
        alert["time"] = data["time"]
        print json.dumps(alert)
        #requests.post(url, json=alert)