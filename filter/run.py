import __init__

#data=json.loads('{"id":1001,"regno":"300-2050","datamov":[{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
  #              '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},'
   #             '{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589},{"speed":50,"lat":83.045,"lon":79.589}],"time":125885555,"nooftickets":150,"fuel":15000}')



    
while True:
    try:
        while True:
            __init__.channel.basic_consume(__init__.callback,
                                  queue='filterdata',
                                  no_ack=True)
            __init__.channel.start_consuming()

    except Exception, e:
        print e

