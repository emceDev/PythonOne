from tkinter import *
from loggeddb import *



def logged_in(name, password):
    
    print("in logged" + name + password)
    w = Tk()
    w.geometry("525x525")
    
    label1=Label(w, text=name, background="blue")
    label1.grid(sticky=E)

    receiver_label = Label(w, text="Type receiver name below")
    receiver_label.grid()
    receiver_entry = Entry(w)
    receiver_entry.grid()

    message_label = Label(w, text="Type message below")
    message_label.grid()
    message_e = Entry(w)
    message_e.grid()

   


    def route_message():
        message = message_e.get()
        receiver = receiver_entry.get()
        send_message(name, receiver, message)

    send_button = Button(w, text="SEND", command = route_message)
    send_button.grid()

    
    # show_message(name, password,w)
    mainloop()

# logged_in("Mateusz","123")