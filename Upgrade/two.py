from tkinter import *
from functions import *
    
root = Tk() 
root.geometry("500x500")

def r_register_menu():
    show("register")


def r_log_menu():
    show("login")

b1_command = r_log_menu
b2_command = r_register_menu


menu = Menu(root)
menu.add_command(label="login", command=b1_command)
menu.add_command(label="register", command=b2_command)
root.config(menu=menu)
mainloop() 