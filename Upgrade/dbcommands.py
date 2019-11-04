import psycopg2
from logged import *

connection = psycopg2.connect(user = "postgres",
                                   password = "zaq",
                                   host = "127.0.0.1",
                                   port = "5432",
                                   database = "First")
def select(u_name):
    connection
    cursor = connection.cursor()
    postgreSQL_select_Query = f"select * from users WHERE name = '{u_name}' "

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from users")
    user_data = cursor.fetchall() 
   
    print("Print each row and it's columns values")
    for row in user_data:
       print("Id = ", row[1], )
       print("name = ", row[0])
    connection.commit()

# def send_message(r_name,msg):
#        connection
#        cursor = connection.cursor()
#        postgreSQL_insert_Query = f"UPDATE users SET message = '{msg}' WHERE name = '{r_name}'"
#        cursor.execute(postgreSQL_insert_Query)
#        print("Sent to:" + r_name)
#        connection.commit()
       

def data(name, password, email="FALSE"):
       if email !="FALSE":
              register(name, email, password)
       else:
              login(name, password)

def login(name, password):
       connection
       cursor = connection.cursor()
       postgreSQL_select_Query = f"select * from users WHERE name = '{name}' and password = '{password}'"
       cursor.execute(postgreSQL_select_Query)
       user_data = cursor.fetchall()
       if user_data != []:
              logged_in(name, password)
       else:
              print("wrong credentials")
       connection.commit()
def register(name, email, password):
       print(name)
       print(password)
       print(email)
       print("checking values")
       
       connection
       cursor = connection.cursor()
       postgreSQL_select_Query = f"select * from users WHERE email = '{email}' "
       cursor.execute(postgreSQL_select_Query)
       user_data = cursor.fetchall()
       if user_data != []:
              print("user already exists")
       else:
              print("Add user")
              postgreSQL_insert_Query = f"INSERT INTO users (name, email, password) VALUES ('{name}','{email}', '{password}')"
              cursor.execute(postgreSQL_insert_Query)
              print("registration succesfull")
       connection.commit()
       