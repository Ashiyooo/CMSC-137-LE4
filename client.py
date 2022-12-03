import socket       #for setting up client
import time         #for pausing

#Set up client
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#get information to connect with the server
server_host = input('Enter server\'s IP address:')
name = input('Enter Client\'s name: ')
ADDR = (server_host, PORT)
soc.connect(ADDR)

#Get Server name
soc.send(name.encode())
s_name = soc.recv(MSG_LENGTH).decode()


while True:
    pass
