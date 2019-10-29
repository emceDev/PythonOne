from tkinter import *
from dbcommands import *

def show(option):
    root = Tk()
    root.geometry("250x250")

    r_frame = Frame(root)
    r_frame.grid(sticky=E)
    r_name_label = Label(r_frame, text="Type your name here")
    r_name_label.grid(row=1)
    r_name_e = Entry(r_frame)
    r_name_e.grid(row=2)
    r_email_label = Label(r_frame, text="Type ur email here")
    r_email_label.grid(row=3)
    r_email_e = Entry(r_frame)
    r_email_e.grid(row=4)
    r_pass_label = Label(r_frame, text="Type your pass here")
    r_pass_label.grid(row=5)
    r_pass_e = Entry(r_frame, show='*')
    r_pass_e.grid(row=6)

    def pass_register_data():
        name=r_name_e.get()
        password=r_pass_e.get()
        email = r_email_e.get()

        if '@' not in email or len(name)<2 or len(password)<6:
            print("Give the correct credentials")
        else:
            data(name, password, email)

    def pass_logging_data():
        name=r_name_e.get()
        password=r_pass_e.get()
        data(name, password)
    if option=="register":
        print(option)
        root.title("Register")
        r_button = Button(r_frame, text="register", command=pass_register_data)
        r_button.grid(row=7)

    if option=="login":
        print(option)
        root.title("Log In")
        r_email_e.destroy()
        r_email_label.destroy()
        r_button = Button(r_frame, text="Login", command=pass_logging_data)
        r_button.grid(row=7)


