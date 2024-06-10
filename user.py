import getpass
from db import execute_query, fetch_query

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
    def register_user(self):
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        execute_query(query, (self.username, self.password))
    
    def authenticate_user(username, password):
        query = "SELECT password FROM users WHERE username = ?"
        result = fetch_query(query, (username,))
        if result and password == result[0][0]:
            return True
        return False
    
    def get_user_id(self):
        query = "SELECT id FROM users WHERE username = ?"
        result = fetch_query(query, (self.username,))
        if result:
            return result[0][0]
        return None
    
    def add_password(self):
        web_app = input('Enter web app: ')
        username = input('Enter username: ')
        password = input('Enter password: ')
        user_id = self.get_user_id()
        query = "INSERT INTO passwords (user_id, webapp, username, password) VALUES (?, ?, ?, ?)"
        execute_query(query, (user_id, web_app, username, password))
        
    def update_password(self):
        web_app = input("Enter a web app to update: ")
        username = input('Enter username to update: ')
        password = input('Enter password to update: ')
        user_id = self.get_user_id()
        query = "UPDATE passwords SET username = ?, password = ?, WHERE user_id =? AND webapp"
        execute_query(query, (username, password, user_id, web_app))
        
    def delete_password(self):
        web_app = input("Enter webapp to delete: ")
        user_id = self.get_user_id()
        query = "DELETE FROM passwords WHERE user_id = ? and webapp = ?"
        execute_query(query, (user_id, web_app))
        
    def show_passwords(self):
        user_id = self.get_user_id()
        if self.password:
            query = "SELECT username, webapp, password FROM passwords WHERE user_id = ?"
            results = fetch_query(query, (user_id,))
            for row in results:
                print(f'Webapp: {row[0]}\nUsername: {row[1]}\nPassword: {row[2]}\n{'-'*20}')
        