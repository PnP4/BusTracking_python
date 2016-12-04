import json
from nanomsg import Socket, BUS

socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')

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