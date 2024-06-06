## create a ASCII logo art for welcoming the user 
import colorama
from colorama import Fore, Style, Back
import pyfiglet
from db import create_table

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

        ## user login check username and password are valid
        elif user_choice == 2:
            username_login = input('Enter your username: ')
            password_login = input('Enter your password: ')
        
         ## If username and password valid. Greeting message with username
         ## User can choose through 5 possibilities
         
        ## user choose to exit
        elif user_choice == 3:
            break
        
        else:
            print('Invalid choice. Please try again!')
        
if __name__ == "__main__":
    main()