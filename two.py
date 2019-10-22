from tkinter import *

root = Tk()
root.title("okno funkcyjne")
root.geometry("500x500")


l1 = Label(root, text="Wyszukaj usera O imieniu")
l1.pack()

i1 = Entry(root, width=100)
i1.pack()

def search():
    name = i1.get()
    print(name)

przycisk = Button(root,text="Wykonaj",command=search)
przycisk.pack()



l2 = Label(root, text="Dodaj usera o imieniu")
l2.pack()

i2 = Entry(root, width=100)
i2.pack()

def add():
    name = i2.get()
    print(name)

przycisk = Button(root,text="Wykonaj",command=add)
przycisk.pack()



l3 = Label(root, text="Napisz wiadomość do usera")
l3.pack()

i3 = Entry(root, width=20)
i3.pack()

i4 = Entry(root, width=78)
i4.pack()

def send():
    name = i3.get()
    print(name)
    msg = i4.get()
    print(msg)
przycisk = Button(root,text="Wykonaj",command=send)
przycisk.pack()



mainloop()