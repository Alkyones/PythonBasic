
#!/usr/bin/env python3
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import tkinter

HOST = input('Enter Host: ') # Enter host of the server without inverted commas 
PORT = 9900
BUFSIZ = 1024
INFO = (HOST, PORT)

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(INFO)

def receive():
    while True:
        try:
            msg = client_socket.recv(BUFSIZ).decode("utf8")
            msg_list.insert(tkinter.END, msg)
        except OSError:  
            break


def send(event=None):  # event is passed by binders.
    msg = my_msg.get()
    my_msg.set("")  # Clears input field.
    client_socket.send(bytes(msg, "utf8"))
    if msg == "{quit}":
        client_socket.close()
        top.quit()


def on_closing(event=None):
    my_msg.set("{quit}")
    send()

top = tkinter.Tk()
top.title("ChatPY")
top.configure(bg="lightgrey")
top.geometry('700x700')

messages_frame = tkinter.Frame(top)

my_msg = tkinter.StringVar()  # For the messages to be sent.
my_msg.set("")

scrollbar = tkinter.Scrollbar(messages_frame) 
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
messages_frame.pack()

msg_list = tkinter.Listbox(messages_frame, height=40, width=90, yscrollcommand=scrollbar.set)
scrollbar.config(command=msg_list.yview)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()

entry_field = tkinter.Entry(top,width=93, textvariable=my_msg)

entry_field.bind("<Return>", send)

entry_field.pack()

send_button = tkinter.Button(top, text="Send", command=send)
send_button.config(height=15, width=15)
send_button.pack()



top.protocol("WM_DELETE_WINDOW", on_closing)

receive_thread = Thread(target=receive)
receive_thread.start()

tkinter.mainloop() 