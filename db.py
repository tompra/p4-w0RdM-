import sqlite3
from sqlite3 import Error

def create_connection():
    """ Create a database connection to database """
    try:
        connection = sqlite3.connect('data/password_data.db')
        print('Connection to SQL DB successful')
        return connection
    except Error as err:
        print(f'There is an error in the connection: {err}')
    return None

def create_table():
    connection = create_connection()
    if connection is not None:
        create_user_table = """ CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL);  """
        
        create_password_table = """ CREATE TABLE IF NOT EXISTS passwords (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL, webapp TEXT NOT NULL, username TEXT NOT NULL, password TEXT NOT NULL, FOREIGN KEY (user_id) REFERENCES users (id) );  """
        
        try: 
            c = connection.cursor()
            c.execute(create_user_table)
            print('User table created successfully')
            c.execute(create_password_table)
            print('Password table created successfully')
            connection.commit()
        except Error as err:
            print(f'The is an error in the creation_table {err}')
        finally:
            connection.close()
            print('SQL connection is closed')
    else:
        print('Error by creating database connection')            