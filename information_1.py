import builtwith
import pyfiglet
from colorama import Fore,init
init()
import os 
os.system("cls")

banner=pyfiglet.figlet_format("Sr7",font="big")
print(Fore.GREEN+banner)

Site=input("Enter Target : ")
Information=builtwith.builtwith(Site)

for Info in Information:
    print(Fore.BLUE+Info,":",Information[Info][0])