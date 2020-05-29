import socket


class Client:
    HEADER = 64
    PORT = 5555
    FORMAT = 'utf-8'
    DISCONNECT_MESSAGE = "DISCONNECT!"
    SERVER = "192.168.1.103"

    ADDR = (SERVER,PORT)

    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.client.connect(Client.ADDR)

    def send_msg(self,msg):
        message = msg.encode(Client.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(Client.FORMAT)
        send_length += b' '*(Client.HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)
        print(self.client.recv(2048).decode(Client.FORMAT))
    
    def close_connection(self):
        self.client.close()


c = Client()
while True:
    msg = input()
    c.send_msg(msg)
    if msg == Client.DISCONNECT_MESSAGE:
        c.close_connection()
        break
        
