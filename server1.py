import socket

FORMAT = 'utf-8'
server1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server address(host,port number)

server1.bind((socket.gethostname(),10001))

server1.listen(1)

print("waiting for connection")
while True:
    clientcon, adr = server1.accept()
    print("Received connection",adr)
    #data = clientcon.recv(1024).decode(FORMAT)
    data = clientcon.recv(1024)
    if data == b'squit':
        print("server closed")
        clientcon.close()
        server1.close()
    else:
        print("Received :", data)
        clientcon.sendall(data)
        clientcon.close()






