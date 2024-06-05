## create a ASCII logo art for welcoming the user 
import colorama
from colorama import Fore, Style, Back
import pyfiglet

def print_logo():
    colorama.init()
    logo = pyfiglet.figlet_format('Password Manager')
    print(Fore.LIGHTCYAN_EX + logo + Style.RESET_ALL)
    
print_logo()