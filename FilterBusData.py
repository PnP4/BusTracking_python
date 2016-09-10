import json

data=json.loads('{"id":1001,"regno":"300-2050","datamov":[{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
                '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
                '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589}],"time":125885555,"nooftickets":150,"fuel":15000}')

def getspeeddata(data):
    id=data["id"]
    regno = data["regno"]
    movementdata = data["datamov"]
    speeds=[]
    for i in movementdata:
        speeds.append(i["speed"])
    time = data["time"]
    extracteddata={"id":id,"regno":regno,"speed":speeds,"time":time}
    return json.dumps(extracteddata)

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
    return json.dumps(extracteddata)

print getspeeddata(data)
print getlocationdata(data)
