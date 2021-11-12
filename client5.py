import socket
import sys
import json

dict = '{"fname" : "Name" ,"lname" : "harish","age" : 22 ,"city":"vijayawada"}'

jsonResult =json.dumps(dict).encode('utf-8')


try:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket Created")
except socket.error as err:
    print('Socket error because of %s' %(err))

port =1500
address = "127.0.0.1"
try:
    sock.connect((address,port))
    sock.send(jsonResult)
except socket.gaierror:
    print('There is an error resolving the host')


    sys.exit()
sock.close()
