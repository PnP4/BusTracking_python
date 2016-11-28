import json
import pika
import __init__

#data=json.loads('{"speed": [50, 50, 50, 90, 50, 50, 50, 50], "id": 1001, "regno": "300-2050", "time": 125885555}')







while True:
    try:
        while True:
            __init__.channel.basic_consume(__init__.callback,
                                  queue='overspeed',
                                  no_ack=True)
            __init__.channel.start_consuming()

    except Exception, e:
        print e
