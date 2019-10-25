import psycopg2

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

def add(u_name):
       connection
       cursor = connection.cursor()
       postgreSQL_insert_Query = f"INSERT INTO users(name) VALUES ('{u_name}') "
       cursor.execute(postgreSQL_insert_Query)
       connection.commit()
       print(u_name)
       print("Uploaded")

def send_message(r_name,msg):
       connection
       cursor = connection.cursor()
       postgreSQL_insert_Query = f"UPDATE users SET message = '{msg}' WHERE name = '{r_name}'"
       cursor.execute(postgreSQL_insert_Query)
       print("Sent to:" + r_name)
       connection.commit()
       
