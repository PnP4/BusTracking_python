import json
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='overwaiting')
channel.queue_declare(queue='overspeed')

def getspeeddata(data):
    speed = data["overspeed"]["speed"]
    print "dsfsdf"
    maxspeed = max(speed)
    return maxspeed

def callback(ch, method, properties, body):
    data = json.loads(body)
    speedval = getspeeddata(data)

    alert = {}
    if speedval > 100:
        alert["id"] = data["overspeed"]["id"]
        alert["maxspeed"] = speedval
        alert["alerttype"] = "Overspeed"
        alert["alertmsg"] = "Too Speed"
        alert["time"] = data["overspeed"]["time"]
    elif speedval > 80:
        alert["id"] = data["id"]
        alert["maxspeed"] = speedval
        alert["alerttype"] = "Overspeed"
        alert["alertmsg"] = "Warning speed"
        alert["time"] = data["overspeed"]["time"]
    data["overspeed"] = alert
    print(json.dumps(data))

    channel.basic_publish(exchange='',
                          routing_key='overwaiting',
                          body=json.dumps(data))