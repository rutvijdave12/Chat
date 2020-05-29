import socket
import threading




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
DISCONNECT_MESSAGE = "DISCONNECTED!"
msgs_list = ['aa']

# def msgs(msg):
#     msgs_list.append(msg)
#     #print(msgs_list)
#     return msgs_list
    

def init():
    global server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

def handle_client(conn,addr):
    print(f'[NEW CONNECTION] {addr} connected.')

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            msgs_list.append(f"[{addr}] {msg}")
            print(msgs_list)
            print((addr, msg))
            conn.send("Message recieved".encode(FORMAT))
            conn.send('-'.join(msgs_list).encode(FORMAT))
            if msg == DISCONNECT_MESSAGE:
                conn.close()
                break
            


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting...")
init()
start()
