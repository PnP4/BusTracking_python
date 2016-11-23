import json
import pika

#data=json.loads('{"id":1001,"regno":"300-2050","datamov":[{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
  #              '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
   #             '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589}],"time":125885555,"nooftickets":150,"fuel":15000}')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='filterdata')
channel.queue_declare(queue='overspeed')
channel.queue_declare(queue='overwaiting')
print "hello"


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

def callback(ch, method, properties, body):
    #print getspeeddata(data)
    #print getlocationdata(data)
    data = json.loads(body)
    print data
    channel.basic_publish(exchange='',
                          routing_key='overwaiting',
                        body=json.dumps(getspeeddata(data)))

    channel.basic_publish(exchange='',
                          routing_key='overwaiting',
                          body=json.dumps(getlocationdata(data)))
    
while True:
    try:
        while True:
            print "1"
            channel.basic_consume(callback,
                                  queue='filterdata',
                                  no_ack=True)
            channel.start_consuming()

    except Exception, e:
        print e

