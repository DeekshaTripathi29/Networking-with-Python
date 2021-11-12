import json
import socket

sock = socket.socket()
print("Socket Created .....")

port =1500
address = "127.0.0.1"
sock.bind((address,port))
sock.listen(5)

print('Socket is listening')
while True:
    c,addr =sock.accept()
    print('got connection from ',addr)
    jsonReceived = c.recv(1024)
    list = json.loads(jsonReceived)
    print("Json converted to dictionary -->", list)

    c.close()