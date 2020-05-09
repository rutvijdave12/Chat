import socket
import threading
from data import Messages

#"192.168.1.103"
#120.63.15.245
#'127.0.1.1'
#0.188.97.78"

HEADER = 64
PORT = 5050
SERVER ='192.168.1.103'
#SERVER = socket.gethostbyname(socket.gethostname())
#print(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
M = Messages()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    print(connected)
    while connected:
        print(5)
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            M.record(f"[{addr}] {msg}")
            print(f"[{addr}] {msg}")
            conn.send("Message recieved".encode(FORMAT))
            
            


    conn.close()




def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}...")
    while True:
        print(1)
        conn, addr = server.accept()
        print(2)
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        print(3)
        thread.start()
        print(4)
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
start()
