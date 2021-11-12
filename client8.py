import socket
import sys
import json
class Account:
    def __init__(self,name,balance,city):
        self.name = name
        self.balance = balance
        self.city = city
class Employee:
    def __init__(self, name, age,company):
        self.name = name
        self.age = age
        self.company= company
class Box:
    def __init__(self,height,width,depth):
        self.height = height
        self.width = width
        self.depth = depth

class Customer:
    def __init__(self, name, age, company):
        self.name = name
        self.age = age
        self.company = company
if __name__ == "__main__":
    acc = Account("Sandeep",50000,"Vijayawada")
    e1=Employee("Sudhakar","21","LTTS")
    bo = Box(15, 20, 5)
    c1=Customer("Harish","22","Byjus")
    jsonstr1 = json.dumps(acc.__dict__).encode('utf-8')
    jsonstr2=json.dumps(e1.__dict__).encode('utf-8')
    jsonstr3 = json.dumps(bo.__dict__).encode('utf-8')
    jsonstr4=json.dumps(c1.__dict__).encode('utf-8')
try:
    s=socket.socket()
except socket.error as err:
    print("Socket Error because of %s" % (err))
port=12345
ipaddress="127.0.0.1"
try:
    s.connect((ipaddress,port))
    s.send(jsonstr1)
    s.send(jsonstr2)
    s.send(jsonstr3)
    s.send(jsonstr4)
except socket.gaierror:
    print("There was an error resolving host")
    sys.exit()
