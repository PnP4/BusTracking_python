import json
from nanomsg import Socket, BUS

socket = Socket(BUS)
socket.connect('tcp://192.168.1.7:5551')



def getspeeddata(data):
    speed = data["overspeed"]["speed"]
    maxspeed=max(speed)
    return maxspeed

def alert(data):
    speedval = getspeeddata(data)

    alert = {}
    if speedval > 100:
        alert["id"] = data["overspeed"]["id"]
        alert["maxspeed"] = speedval
        alert["alerttype"] = "Overspeed"
        alert["alertmsg"] = "Too Speed"
        alert["time"] = data["overspeed"]["time"]
    elif speedval > 80:
        alert["id"] = data["overspeed"]["id"]
        alert["maxspeed"] = speedval
        alert["alerttype"] = "Overspeed"
        alert["alertmsg"] = "Warning speed"
        alert["time"] = data["overspeed"]["time"]

    data["To"] = 4
    data["overspeed"] = alert

    return data