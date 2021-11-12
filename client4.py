import os
import socket

client4Sock = socket.socket()
host = socket.gethostname()
port = 12345

client4Sock.connect((host, port))
client4Sock.send(b"Hello server!")

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = client4Sock.recv(1024)
        print('data= %s' %(data))
        if not data:
            break

        f.write(data)
f.close()
print('Successfully get the file')
client4Sock.close()
print('connection closed')