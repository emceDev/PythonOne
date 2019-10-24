import psycopg2

connection = psycopg2.connect(user = "postgres",
                                  password = "zaq",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "First")


def select(u_name):
    connection
    cursor = connection.cursor()
    postgreSQL_select_Query = f"select * from users WHERE name1 = '{u_name}' "

    cursor.execute(postgreSQL_select_Query)
    print("Selecting rows from users")
    user_data = cursor.fetchall() 
   
    print("Print each row and it's columns values")
    for row in user_data:
       print("Id = ", row[1], )
       print("name1 = ", row[0])


    

