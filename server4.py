import os
import socket

port = 12345
server4Sock = socket.socket()
host = socket.gethostname()
server4Sock.bind((host, port))
server4Sock.listen(5)

print('Server listening....')


while True:
    conn, addr = server4Sock.accept()
    print('Got connection from', addr)
    data = conn.recv(1024)
    print('Server received', repr(data))

    filename= 'client4.py'
    f = open(filename,'rb')
    l = f.read(1024)
    while (l):
       conn.send(l)
       print('Sent ',repr(l))
       l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send(b'Thank you for connecting')
    print(os.lstat(filename))
    conn.close()