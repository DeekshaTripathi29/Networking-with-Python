import socket


client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server address(host,port number)

client1.connect((socket.gethostname(),10001))

print("connection established")


message = input()
print("Sending message to server ")

if message == 'cquit':
    msg = 'squit'
    client1.sendall(msg.encode())
    print("Original :", message)
    client1.close()
    print("client closed")
    #data = client1.recv(1024).decode()
    #print("Echo:", data)
else:
    client1.sendall(message.encode())
    print("Original :", message)
    data = client1.recv(1024).decode()
    print("Echo:", data)


'''
while True:
    print("Please enter a message you want to pass to the server")
    message = input()
    print("Sending message to server ", message)

    if message == 'cquit':
        msg = 'squit'
        client1.sendall(msg.encode())
        print("Original :", message)
        client1.close()
    else:
        client1.sendall(message.encode())
        print("Original :", message)
        data = client1.recv(1024).decode()
        print("Echo:", data)

'''

