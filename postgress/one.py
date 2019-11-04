from tkinter import *
from functions import *

def sample_label_text_change():
    sample_label_text.set("sample label text changed!")

w = Tk()
w.geometry("600x500")
w.title("Window title")

#tworzenie menu
menu = Menu(w)
menu.add_cascade(label="login")
menu.add_command(label="register")
w.config(menu=menu)

sample_label_text = StringVar()
sample_label = Label(w, textvariable = sample_label_text)
sample_label_text.set("text przykładowego labela")
sample_label.pack()

sample_button = Button(w, text="sample OK", command = sample_label_text_change)
sample_button.pack()



mainloop()