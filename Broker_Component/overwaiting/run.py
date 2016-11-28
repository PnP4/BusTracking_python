#assumption data recived as bunch of set which collected in maximum waiting time.
#if max wait time=1min data colleted for 1min and send to the system
import json
import pika
import __init__


#data=json.loads('{"time": 125885555, "id": 1001, "regno": "300-2050", "movedata": [{"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}, {"lat": 83.045, "lon": 79.589}]}')

while True:
    try:
        while True:
            __init__.channel.basic_consume(__init__.callback,
                                  queue='overwaiting',
                                  no_ack=True)
            __init__.channel.start_consuming()

    except Exception, e:
        print e
