#!/usr/bin/env python
"""Simple server that listens on port 6000 and after password check multiplies recieved integers by two """
from gevent.server import StreamServer

password = "12345"

# this handler will be run for each incoming connection in a dedicated greenlet
def echo(socket, address):
    print ('Client connected, waiting for password from %s:%s' % address)
    # using a makefile because we want to use readline()
    fileobj = socket.makefile()
    line = fileobj.readline()
    if not line:
        return 
    if line.strip() != password:
        fileobj.write("WRONG\n")
        fileobj.flush()
        return
    fileobj.write("OK\n")
    fileobj.flush()
    c = 0
    while True:
        line = fileobj.readline()
        if not line:
            print ("client disconnected")
            break
        c += 1
        number = int(line)
        result = number * 2
        fileobj.write(str(result) + "\n")
        fileobj.flush()

if __name__ == '__main__':
    # to make the server use SSL, pass certfile and keyfile arguments to the constructor
    server = StreamServer(('0.0.0.0', 6000), echo)
    # to start the server asynchronously, use its start() method;
    # we use blocking serve_forever() here because we have no other jobs
    print ('Starting server on port 6000')
    server.serve_forever()
