
import socket
import sys
import datetime

## end of imports ###


s = socket.socket()
now = datetime.datetime.now()
host = socket.gethostname()
print(" server will start on host : ", host)
port = 8080
s.bind((host,port))
print("")
print("Server is waiting for incoming connections")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, " Has connected to the server and is now online ...")
print("")
n=input("Enter your name:- ")
n=n.encode()
conn.send(n)
while 1:
            message = input(str(">> "))
            message = message.encode()
            conn.send(message)
            print('                   ',now.strftime("%H:%M:%S"))
            print("")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print( "Clint : ", incoming_message)
            print('                   ',now.strftime("%H:%M:%S"))
            print("")
