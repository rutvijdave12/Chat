from tkinter import ttk
import tkinter as tk
#import client
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

scroll = tk.Scrollbar(app,bg="#333830",activebackground="#000000",highlightbackground="#000000")
text = tk.Text(frame,bg="#333830",font=40,borderwidth=0,highlightthickness = 0)
text.place(relx=0,rely=0.91,relwidth=0.94,relheight=0.08)
#scroll.pack(side=tk.RIGHT,fill=tk.Y)
scroll.place(relx=0.98,rely=0,relwidth=0.02,relheight=1)
#text.pack(side=tk.BOTTOM,fill=tk.Y)
#scroll.config(command=text.yview)
#text.config(yscrollcommand=scroll.set,background="#1a2118")

send_button = tk.PhotoImage(file="send_48.png")
send_img = tk.Label(image=send_button,borderwidth=0)
#send_img.pack()


button = tk.Button(frame,relief="solid",image=send_button,activebackground="#041c07",highlightthickness = 0,command=button_pressed,borderwidth = 0,bg='#041c07')
#button.pack(pady=20)
button.place(relx=0.931,rely=0.85,relheight=0.2,relwidth=0.08)
#button.pack(side=tk.BOTTOM)
# scrolledtext.ScrolledText(app).pack()

# var = tk.StringVar()
# var.set("Hey!? How are you doing?")
# display = tk.Message(frame,bg="#FFFFFF",textvariable=var)
# display.place()




app.mainloop()
