import os, sys
from colorama import Fore, Back, Style

RED = Fore.RED
YELLOW = Fore.YELLOW
GREEN = Fore.GREEN
BLUE = Fore.BLUE

def check_access():
    if not os.geteuid()==0:
        sys.exit(RED+"WARNING!!!\nThis tool requires root access!"+YELLOW+"\nTry : sudo dumpwinkey.py")
    else:
        header()
        choice()
        app()

def header():
    print "    " + YELLOW + "===================================="
    print "    " + BLUE + "[+] ""       "+ BLUE + "DUMPWINKEY""           " + BLUE +" [+]"
    print "    " + BLUE +   "[+]  "+ GREEN + "Created by : Frits Sasia" + BLUE +"    [+]"
    print "    " + BLUE +   "[+] "+ GREEN + "Facebook : Rivas Frits Sasia" + BLUE +" [+]"
    print "    " + YELLOW + "===================================="

def choice():
    pil = raw_input("Continue to this tool? [y/n] : ")
    if pil == "y":
        app()
    else:
        sys.exit


def app():
    check_COA = os.system('ls /sys/firmware/acpi/tables/MSDM')
    os.system('clear')

    if check_COA == False:
        print YELLOW+"Windows key found!"
        os.system('sudo cat /sys/firmware/acpi/tables/MSDM | tail -c 32 | xargs -0 echo "Windows product key :">winkey.txt')
        print GREEN+"Windows product key has been saved!"
    else:
        print RED+"Cannot found windows key!"
        os.system('sudo cat /sys/firmware/acpi/tables/MSDM | tail -c 32 | xargs -0 echo "Windows product key :">winkey.txt')
        print "Sorry we could not find your windows key! :("

check_access()
