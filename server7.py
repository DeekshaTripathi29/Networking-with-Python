
import socket

server7Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("Socket Created .....")

address = "127.0.0.1"
port =12345

server7Sock.bind((address,port))

server7Sock.listen(5)

while True:
    c, addr = server7Sock.accept()
    print('Received Request from ',addr)
    c.send(b'Thank you for connecting')
    c.close()


