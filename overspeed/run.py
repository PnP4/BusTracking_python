import json
import __init__


while True:
    try:
        while True:
            data = json.loads(__init__.socket.recv())
            if (data["To"] == 3):
                tosend = __init__.alert(data)
                __init__.socket.send(json.dumps(tosend))
                print json.dumps(tosend)

    except Exception, e:
        print e