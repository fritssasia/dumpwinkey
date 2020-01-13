# Import module 
import os, sys
from colorama import Fore, Back, Style

# Color (using colorama module)
RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE

# Check root access
def check_access():
    if not os.geteuid()==0:
        sys.exit(RED+"WARNING!!!\nThis tool requires root access!"+YELLOW+"\nTry : sudo python dumpwinkey.py")
    else:
        header()
        choice()

# Header
def header():
    os.system('clear')
    print "    " + YELLOW + "===================================="
    print "    " + BLUE + "[+] ""       "+ BLUE + "DUMPWINKEY""           " + BLUE +" [+]"
    print "    " + BLUE +   "[+]  "+ GREEN + "Created by : Frits Sasia" + BLUE +"    [+]"
    print "    " + BLUE +   "[+] "+ GREEN + "Facebook : Rivas Frits Sasia" + BLUE +" [+]"
    print "    " + YELLOW + "===================================="

# Just Option
def choice():
    pil = raw_input("Continue to this tool? [y/n] : ")
    if pil == "y":
        app()
    else:
        os.system('exit')

# The process of finding a windows product key
def app():
    COA = '/sys/firmware/acpi/tables/MSDM' # COA (Certificate of Authenticity)
    file = os.path.isfile(COA)
    if file == True:
        print GREEN+"\nMSDM file found! :)\nTry to find the windows product key"
        os.system('sudo cat /sys/firmware/acpi/tables/MSDM | tail -c 32 | xargs -0 echo "Windows product key :">winkey.txt')
        print GREEN+"Windows product key has been saved, please check the file winkey.txt"
    else:
        print RED+"\nCannot found MSDM file :( FAILED!"

check_access()
