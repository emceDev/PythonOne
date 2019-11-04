from dbcommands import *

def ui_login():
    print("Please insert your name below,")
    name = input()
    print("Please insert your password below,")
    password = input()
    login(name,password)

def ui_register():
    print("Please insert your name below,")
    name = input()
    print("Please insert your password below,")
    password = input()
    print("email")
    email = input()
    if '@' not in email or len(name)<2 or len(password)<3:
        print("Give the correct credentials")
        ui_register()
    else:
        register(name,password,email)




print("Welcome to my app")
print("Do u have an account? Y/N")
has_account = input()

if(has_account=="yes" or has_account=="y"):
    ui_login()

elif(has_account=="no"or has_account=="n"):
    ui_register()

else:
    print("incorrect input")
