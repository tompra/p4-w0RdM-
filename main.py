## create a ASCII logo art for welcoming the user 
import colorama
from colorama import Fore, Style, Back
import pyfiglet

def print_logo():
    colorama.init()
    logo = pyfiglet.figlet_format('Password Manager', font='larry3d')
    print(Fore.LIGHTCYAN_EX + logo + Style.RESET_ALL)
    
print_logo()

def welcome_text():
    print('Protect yourself with secure passwords, passkeys and sensitive information.\n')

welcome_text()

def menu():
    print('1. Register')
    print('2. Login')
    print('3. Exit')
    return input('Enter your choice: ')

menu()
