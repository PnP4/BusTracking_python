import json
import time
from nanomsg import Socket, BUS

data=json.loads('{"alertmsg": "Warning speed", "alerttype": "Overspeed", "maxspeed": 90, "id": 1001, "time": 125885555}')
data2=json.loads('{"alerttype": "Over waiting", "movedata": {"lat": 83.045, "lon": 79.589}, "alertmsg": "Wait for long time", "regno": "300-2050", "time": 125885555, "id": 1001}')

isdatasend=True
isdata2send=True

time.sleep(0.5)

mainalert={}
mainalert["alert"]=[]

if(isdatasend):
    mainalert["alert"].append(data)
if (isdata2send):
    mainalert["alert"].append(data2)

if(isdatasend & isdata2send):
    print json.dumps(mainalert)