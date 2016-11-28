import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='filterdata')
channel.queue_declare(queue='overspeed')

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

def callback(ch, method, properties, body):
    data = json.loads(body)
    tosend = {}
    tosend["overspeed"] = getspeeddata(data)
    tosend["overwaiting"] = getlocationdata(data)
    print json.dumps(tosend)
    channel.basic_publish(exchange='',
                          routing_key='overspeed',
                        body=json.dumps(tosend))