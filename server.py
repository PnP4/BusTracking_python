from nanomsg import Socket, BUS

s1 = Socket(BUS)
s1.bind('tcp://*:5551')
#a = str(raw_input())
#s1.send(a)
while True:
    l = s1.recv()
    print(l)
    s1.send(l)
s1.close()
