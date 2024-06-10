## create a ASCII logo art for welcoming the user 
import colorama
from colorama import Fore, Style, Back
import pyfiglet
from db import create_table
from user import User

def print_logo():
    colorama.init()
    logo = pyfiglet.figlet_format('Password Manager', font='larry3d')
    print(Fore.LIGHTCYAN_EX + logo + Style.RESET_ALL)
    

def welcome_text():
    print(f'{Fore.LIGHTRED_EX}Protect yourself with secure passwords, passkeys and sensitive information.\n')

def menu():
    print(f'{Fore.LIGHTYELLOW_EX}1. Register')
    print(f'{Fore.LIGHTYELLOW_EX}2. Login')
    print(f'{Fore.LIGHTYELLOW_EX}3. Exit')
    user_choice = input(f'{Fore.LIGHTGREEN_EX}Enter your choice: ')
    return int(user_choice)

def logged_user_menu():
    print("1. Add Password")
    print("2. Update Password")
    print("3. Delete Password")
    print("4. Show Password")
    print("5. Logout")
    choice = input("Enter your choice: ")
    return choice


def main():
    print_logo()
    welcome_text()
    create_table()
    
    while True:
        user_choice = menu()
        print(f'{Fore.LIGHTMAGENTA_EX} Choice from user: {user_choice}')
        
        ## create a new user name with the password of minimum of 10 characters
        if user_choice == 1:
            username_register = input('Enter username: ')
            password_register = input('Enter password: ')
            user = User(username_register, password_register)
            user.register_user()
            print('User registered successfully!')

        ## user login check username and password are valid
        elif user_choice == 2:
            username_login = input('Enter your username: ')
            password_login = input('Enter your password: ')
        
            ## If username and password valid. Greeting message with username
            if User.authenticate_user(username_login, password_login):
                print(f"Welcome, {username}!")
                current_user = User(username_login, password_login)                
            ## User can choose through 5 possibilities
                while True:
                    user_choice = logged_user_menu()
                    if user_choice == '1':
                        current_user.add_password()
                    elif user_choice == '2':
                        current_user.update_password()
                    elif user_choice == '3':
                        current_user.delete_password()
                    elif user_choice == '4':
                        current_user.show_passwords()
                    elif user_choice == '5':
                        print(f'Bye, {username_login}!')
                        return
                    else: 
                        print('Invalid choice. Please try again!')
            else: 
                print('Invalid username or password. Please try again!')
         
        ## user choose to exit
        elif user_choice == 3:
            break
        
        else:
            print('Invalid choice. Please try again!')
        
if __name__ == "__main__":
    main()