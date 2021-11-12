import socket
s=socket.socket()
print("Socket Created .....")
port=12345
ipaddress='127.0.0.1'
s.bind((ipaddress,port))
s.listen(5)
print("Socket is Listening")
while True:
    c, addr=s.accept()
    print("Got Connection From" , addr)
    jsonReceived=c.recv(1024)
    print("Json Received ------>", jsonReceived)
    c.close()