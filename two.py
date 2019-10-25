from tkinter import *
from dbcommands import *

root = Tk()
root.title("okno funkcyjne")
root.geometry("500x500")


l1 = Label(root, text="Wyszukaj usera O imieniu")
l1.pack()

i1 = Entry(root, width=100)
i1.pack()

def search():
    u_name = i1.get()
    select(u_name)
    print(u_name)

przycisk = Button(root,text="Wykonaj",command=search)
przycisk.pack()



l2 = Label(root, text="Dodaj usera o imieniu")
l2.pack()

i2 = Entry(root, width=100)
i2.pack()

def addu():
    u_name = i2.get()
    add(u_name)

przycisk = Button(root,text="Wykonaj",command=addu)
przycisk.pack()



l3 = Label(root, text="Napisz wiadomość do usera")
l3.pack()

i3 = Entry(root, width=20)
i3.pack()

i4 = Entry(root, width=78)
i4.pack()

def send():
    r_name = i3.get()
    msg = i4.get()
    send_message(r_name,msg)
    
przycisk = Button(root,text="Wykonaj",command=send)
przycisk.pack()


mainloop()