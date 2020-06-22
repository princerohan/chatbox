import socket
import sys
import datetime

s = socket.socket()
now = datetime.datetime.now()
host = input(str("Please enter the hostname of the server : "))
port = 8080
s.connect((host,port))
nm=input("Enter your name:- ")
print(" Connected to chat server as ",nm)
nam = s.recv(1024)
nam = nam.decode()
while 1:
            incoming_message = s.recv(1024)
            incoming_message = incoming_message.decode()
            print(nam, " : ", incoming_message)
            print('                   ',now.strftime("%H:%M:%S"))
            print("")
            message = input(str(">> "))
            message = message.encode()
            s.send(message)
            print('                   ',now.strftime("%H:%M:%S"))
            print("")
