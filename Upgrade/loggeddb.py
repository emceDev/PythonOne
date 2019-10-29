import psycopg2
from tkinter import *
connection = psycopg2.connect(user = "postgres",
                                  password = "zaq",
                                  host = "127.0.0.1",
                                  port = "59488",
                                  database = "First")
def show_message(name, password, w):
       connection
       cursor = connection.cursor()
       postgreSQL_select_Query = f"select msg from users WHERE name = '{name}' and password = '{password}'"
       cursor.execute(postgreSQL_select_Query)
       message = cursor.fetchall()
       print(message)
           #w bazie ma byc tablica 
           #kazdy wiersz tablicy do tej samej kolumny

def send_message(name, receiver, message):

    connection
    cursor = connection.cursor()
    postgreSQL_insert_Query = f"UPDATE users SET message = '{message}' WHERE name = '{receiver}'"
    cursor.execute(postgreSQL_insert_Query)
    print("Sent to:" + receiver)
    connection.commit()
    
    print("nadawca "+ name)
    print("receiver "+ receiver)
    print("message "+ message)