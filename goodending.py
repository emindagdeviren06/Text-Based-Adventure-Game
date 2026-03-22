import pyfiglet 
from colorama import Fore, Style


ascii_art = pyfiglet.figlet_format("Good Ending", font="gothic", width=50)
good_ending_text = (Fore.GREEN + ascii_art + Style.RESET_ALL)