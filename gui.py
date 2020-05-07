from tkinter import ttk
import tkinter as tk
import client
#import server
# from tkinter import scrolledtext

def button_pressed():
    print("Button")
    client.send(text.get("1.0","end"))
    text.delete("1.0","end")


def display_chat():
    var = tk.StringVar()
    var.set('aaaaaaaaaaa')






app = tk.Tk()
app.iconphoto(False, tk.PhotoImage(file="chat_icon2.png"))
app.title("Chat Room")
app.geometry("720x580")


# app.configure(background='#041c07')
frame = tk.Frame(app,bg='#041c07',bd=5)
frame.place(relx=0,rely=0,relwidth=0.98,relheight=1)

scroll = tk.Scrollbar(app)
text = tk.Text(frame,bg="#333830",font=40)
text.place(relx=0,rely=0.95,relwidth=0.9,relheight=0.5)
#scroll.pack(side=tk.RIGHT,fill=tk.Y)
scroll.place(relx=0.98,rely=0,relwidth=0.02,relheight=1)
#text.pack(side=tk.BOTTOM,fill=tk.Y)
#scroll.config(command=text.yview)
#text.config(yscrollcommand=scroll.set,background="#1a2118")

button = tk.Button(frame,relief="solid",text="Send",activebackground="#ad1717",activeforeground="#FFFFFF",bg="#89a18d",command=button_pressed )
button.place(relx=0.901,rely=0.95,relwidth=0.1,relheight=0.05)
#button.pack(side=tk.BOTTOM)
# scrolledtext.ScrolledText(app).pack()

var = tk.StringVar()
var.set("Hey!? How are you doing?")
display = tk.Message(frame,bg="#FFFFFF",textvariable=var)

display.place(relx=0.1,rely=0.075,relwidth=0.8,relheight=0.8)



app.mainloop()
