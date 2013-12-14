import socket
import random, time

password = "12345"

s = socket.create_connection(('127.0.0.1', 6000))
f = s.makefile()
try:
    f.write(password + "\n")
    f.flush()
    response = f.readline()
    if response.strip() != 'OK':
        print 'Authentification failed'
        exit()
    print 'Authentificated OK'
    for i in range(0, 10):
        number = random.randint(1,100)
        print "Sending number: {}".format(number)
        f.write("{}\n".format(number))
        f.flush()
        result = f.readline()
        print "Result: {}".format(result)
        time.sleep(1)    
except socket.error:
    #Send failed
    print 'Interaction failed'
    exit()
s.close()
