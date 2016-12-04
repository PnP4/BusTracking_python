import json
import __init__
data=json.loads('{"id":1001,"regno":"300-2050","datamov":[{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
            '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
                '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589}],"time":125885555,"nooftickets":150,"fuel":15000}')


while True:
    try:
        while True:
            data = json.loads(__init__.socket.recv())
            tosend = {}
            tosend["overspeed"] = __init__.getspeeddata(data)
            tosend["overwaiting"] = __init__.getlocationdata(data)
            print data
            if (data["To"]==2):
                tosend["To"] = 3
                __init__.socket.send(json.dumps(tosend))

    except Exception, e:
        print e
