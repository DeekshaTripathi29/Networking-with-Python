import socket

client7Sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ServerAddress = input("hostname:port\n").split(":")

ServerAddress[1] = int(ServerAddress[1])
ipAddress = socket.gethostbyname(ServerAddress[0])
port = ServerAddress[1]
print(ipAddress)
print(port)
msg = "Hello server"
client7Sock.connect((ipAddress,port))
print("connection established")
client7Sock.send(msg.encode())
print(client7Sock.recv(1024))

client7Sock.close()