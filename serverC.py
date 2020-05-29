import socket
import threading


class Server:
    HEADER = 64
    PORT = 5555
    SERVER ='192.168.1.103'
    ADDR = (SERVER,PORT)
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "DISCONNECT!"
    clients = set()

    

    def __init__(self):
        self.server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server.bind(Server.ADDR)

    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {Server.SERVER}...")
        while True:
            #The server will wait overhere until a connection is established
            conn,addr = self.server.accept()
            Server.clients.add(conn)
            print(Server.clients)
            #A thread is created
            thread = threading.Thread(target=self.handle_client, args=(conn,addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

    def handle_client(self,conn,addr):
        print(f'[NEW CONNECTION] {addr} connected.')
        connected =True
        while connected:
            msg_length = conn.recv(Server.HEADER).decode(Server.FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(Server.FORMAT)
                # msgs_list.append(f"[{self.addr}] {msg}")
                # print(msgs_list)
                print((addr, msg))
                # conn.send("Message recieved".encode(Server.FORMAT))
                self.broadcast(msg,conn)
                # conn.send('-'.join(msgs_list).encode(FORMAT))
                if msg == Server.DISCONNECT_MESSAGE:
                    conn.close()
                    break
    
    def broadcast(self,msg,conn):
        temp = Server.clients.copy()
        temp.remove(conn)
        print(temp)
        for client in temp:
            client.sendall(msg.encode(Server.FORMAT))



s = Server()
s.start()

