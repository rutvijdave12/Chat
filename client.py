import socket
from tkinter import ttk
import tkinter as tk

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
SERVER = "192.168.1.103"


ADDR = (SERVER,PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

chat = ''
z = 10
def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    chat = client.recv(2048).decode(FORMAT)
    chat = chat.split('-')
    print(chat)
    d = tk.Message(frame,text=chat[-1])
    d.pack(side=tk.LEFT)
    # if msg == DISCONNECT_MESSAGE:
    #     client.close()


def quit_pressed():
    send('DISCONNECTED!')
    client.close()
    app.quit()


# def display():
#     # print(M.retrieve())
#     msg_list = msgs
#     d = tk.Message(frame,text=msg_list[-1])
#     d.place(x=0,y=texty)
#     texty += 20


def button_pressed():
    print("Button")
    prompt = text.get("1.0","end")
    send(prompt)
    text.delete("1.0","end")


app = tk.Tk()
app.iconphoto(False, tk.PhotoImage(file="chat_icon2.png"))
app.title("Chat Room")
app.geometry("720x580")



# app.configure(background='#041c07')
frame = tk.Frame(app,bg='#041c07',bd=5)
frame.place(relx=0,rely=0,relwidth=0.98,relheight=1)

scroll = tk.Scrollbar(app,bg="#333830",activebackground="#000000",highlightbackground="#000000")
text = tk.Text(frame,bg="#333830",font=40,borderwidth=0,highlightthickness = 0)
text.place(relx=0,rely=0.91,relwidth=0.94,relheight=0.08)
#scroll.pack(side=tk.RIGHT,fill=tk.Y)
scroll.place(relx=0.98,rely=0,relwidth=0.02,relheight=1)
#text.pack(side=tk.BOTTOM,fill=tk.Y)
#scroll.config(command=text.yview)
#text.config(yscrollcommand=scroll.set,background="#1a2118")

send_button = tk.PhotoImage(file="send_48.png")
#send_img = tk.Label(image=send_button,borderwidth=0)
#send_img.pack()

quit_button = tk.PhotoImage(file="quit.png")
#quit_img = tk.Label(image=quit_button,borderwidth=0)
# quit_img.pack(pady=20)


button = tk.Button(frame,relief="solid",image=send_button,activebackground="#041c07",highlightthickness = 0,command=button_pressed,borderwidth = 0,bg='#041c07')
#button.pack(pady=20)
button.place(relx=0.931,rely=0.85,relheight=0.2,relwidth=0.08)
z = 10
#button.pack(side=tk.BOTTOM)
# scrolledtext.ScrolledText(app).pack()

# var = tk.StringVar()
# var.set("Hey!? How are you doing?")
# display = tk.Message(frame,bg="#FFFFFF",textvariable=var)
# display.place()

# thread = threading.Thread(target=display)
# thread.start()

quit_btn = tk.Button(frame,image=quit_button,activebackground="#041c07",highlightthickness = 0,command=quit_pressed,borderwidth = 0,bg='#041c07')
quit_btn.place(relx=0.931,rely=0,relwidth=0.08)





app.mainloop()



