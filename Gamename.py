import pyfiglet
from colorama import Fore, Style


ascii_art = pyfiglet.figlet_format("Veil of Vengeance", font="gothic", width=60)
gameName = Fore.RED + ascii_art + Style.RESET_ALL
