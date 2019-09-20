import os, sys

class dcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'

if not os.geteuid()==0:
    sys.exit(dcolors.BOLD+"Only root can run this script!"+dcolors.FAIL)

check_COA = os.system('ls /sys/firmware/acpi/tables/MSDM')
os.system('clear')

if check_COA == False:
    print dcolors.OKGREEN+"Windows key found!"
else:
    print dcolors.BOLD+"Cannot found windows key!"+dcolors.FAIL

winkey = os.system('sudo cat /sys/firmware/acpi/tables/MSDM | tail -c 32 | xargs -0 echo "Windows product key :">winkey.txt')

file_winkey = open("winkey.txt", "r")
files = file_winkey.read()

print files
file_winkey.close()

print dcolors.BOLD+"Windows product key has been saved!"+dcolors.OKGREEN
