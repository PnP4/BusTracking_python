import json

data=json.loads('{"speed": [50, 50, 50, 90, 50, 50, 50, 50], "id": 1001, "regno": "300-2050", "time": 125885555}')
alert={}
def getspeeddata():
    speed = data["speed"]
    maxspeed=max(speed)
    return maxspeed

speedval=getspeeddata()


if speedval>100:
    alert["id"]=data["id"]
    alert["maxspeed"] = speedval
    alert["alerttype"] = "Overspeed"
    alert["alertmsg"] = "Too Speed"
    alert["time"] = data["time"]
elif speedval>80:
    alert["id"] = data["id"]
    alert["maxspeed"] = speedval
    alert["alerttype"] = "Overspeed"
    alert["alertmsg"] = "Warning speed"
    alert["time"] = data["time"]

print alert


print json.dumps(alert)