from psycopg2 import *

try:
    connection = psycopg2.connect(user = "postgres",
                                    password = "zaq",
                                    host = "127.0.0.1",
                                    port = "59488",
                                    database = "First")
except:
    print("connection fucked up")

def login(name,password):
       try:
              connection
       except:
              print("login")
       cursor = connection.cursor()
       postgreSQL_select_Query = f"select * from users WHERE name = '{name}' and password = '{password}'"
       cursor.execute(postgreSQL_select_Query)
       user_data = cursor.fetchall()
       if user_data != []:
              print(name, password)
       else:
              print("wrong credentials")
def register(name,password,email):
    try:
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
    except:
        print("registration fucked up!s")