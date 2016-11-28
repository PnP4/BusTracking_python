import json
import requests

def getspeeddata(data):
    id=data["id"]
    regno = data["regno"]
    movementdata = data["datamov"]
    speeds=[]
    for i in movementdata:
        speeds.append(i["speed"])
    time = data["time"]
    extracteddata={"id":id,"regno":regno,"speed":speeds,"time":time}
    return extracteddata

def getlocationdata(data):
    id=data["id"]
    regno = data["regno"]
    movementdata = data["datamov"]
    locations = []
    for i in movementdata:
        temp={}
        temp["lat"]=i["lat"]
        temp["lon"] = i["lon"]
        locations.append(temp)
    time = data["time"]
    extracteddata={"id":id,"regno":regno,"movedata":locations,"time":time}
    return extracteddata

def senddata():
    data = json.loads(
        '{"id":1001,"regno":"300-2050","datamov":[{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
        '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
        '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589}],"time":125885555,"nooftickets":150,"fuel":15000}')

    urlspeed = "http://localhost:5004"
    urlwait = "http://localhost:5005"
    speed = getspeeddata(data)
    print json.dumps(speed)
    requests.post(urlspeed, json=speed)
    wait = getlocationdata(data)
    print json.dumps(wait)
    requests.post(urlwait, json=wait)
