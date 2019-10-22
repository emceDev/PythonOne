from tkinter import *

root = Tk()
root.title("okno funkcyjne")
root.geometry("500x500")

tekst = StringVar()
imie = Label(root, textvariable=tekst)
imie.pack()
tekst.set("Podaj swe imie")

input = Entry(root, width=100)
input.pack()


def zmiana():
    imie2 = input.get()
    tekst.set(imie2)
    tekst.set(imie2)

przycisk = Button(root,text="ok",command=zmiana)
przycisk.pack()



mainloop()