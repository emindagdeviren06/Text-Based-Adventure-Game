import pyfiglet 
from colorama import Fore, Style


ascii_art = pyfiglet.figlet_format("Bad Ending", font="gothic", width=50)

secret_ending = (Fore.MAGENTA + ascii_art + Style.RESET_ALL)
