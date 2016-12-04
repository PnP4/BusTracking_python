import json
from math import radians, cos, sin, asin, sqrt
from nanomsg import Socket, BUS

socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')



def haversine(lon1, lat1, lon2, lat2):

    # haversine formula
    dlon = radians(radians(lon2) - radians(lon1))
    dlat = radians(radians(lat2) - radians(lat1))
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371*1000 #get as meters
    return c * r

def alert(data):
    firstcoor = data["movedata"][0]
    lastcoor = data["movedata"][len(data["movedata"]) - 1]
    distance = haversine(firstcoor["lon"], firstcoor["lat"], lastcoor["lon"], lastcoor["lat"])

    if (distance < 5):
        alert = {}
        alert["id"] = data["id"]
        alert["movedata"] = data["movedata"][0]
        alert["regno"] = data["regno"]
        alert["alerttype"] = "Over waiting"
        alert["alertmsg"] = "Wait for long time"
        alert["time"] = data["time"]
        data["To"] = 5
        data["overwaiting"] = alert

    return data
