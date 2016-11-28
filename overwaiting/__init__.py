import json
from math import radians, cos, sin, asin, sqrt
import pika
import json


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='overwaiting')
channel.queue_declare(queue='map')

def haversine(lon1, lat1, lon2, lat2):

    # haversine formula
    dlon = radians(radians(lon2) - radians(lon1))
    dlat = radians(radians(lat2) - radians(lat1))
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371*1000 #get as meters
    return c * r


def callback(ch, method, properties, body):
    print "sdsdfsds"
    data = json.loads(body)
    firstcoor=data["overwaiting"]["movedata"][0]
    lastcoor=data["overwaiting"]["movedata"][len(data["overwaiting"]["movedata"])-1]
    distance= haversine(firstcoor["lon"],firstcoor["lat"],lastcoor["lon"],lastcoor["lat"])
    print "sdsdfsds"

    if(distance<5):
        alert={}
        alert["id"] = data["overwaiting"]["id"]
        alert["movedata"] = data["overwaiting"]["movedata"][0]
        alert["regno"] = data["overwaiting"]["regno"]
        alert["alerttype"] = "Over waiting"
        alert["alertmsg"] = "Wait for long time"
        alert["time"] = data["overwaiting"]["time"]
        print "sdsdfsds"

        data["overwaiting"] = alert
        print "sdsdfsds"
        print "sdsdfsds"
        print json.dumps(data)
        channel.basic_publish(exchange='',
                              routing_key='map',
                              body=json.dumps(data))