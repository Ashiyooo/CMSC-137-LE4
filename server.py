import socket       #use to setup server
import threading    #use to handle multiple clients
import time         #use to let variables update before moving to the next instruction

#Setup Socket
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(socket.gethostname())
PORT = 1234
ADDR = (ip, PORT)
soc.bind(ADDR)

#function to handle each thread/client
def handle_client(conn, client_name, addr):
    pass

    #close the connection
    #conn.close()

#function to start the game
def start():
    #wait for any client to connect
    soc.listen()

    #a client connected
    while True:
        pass

print(f"[STARTING] Server is starting...\nIP Address:{ip}")
start()