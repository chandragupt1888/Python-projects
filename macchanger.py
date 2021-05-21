#This program changes the mac address of a linux system temporarily for the purpose of penetration testing.
#This program runs with python only.
#The MAC address of the system will  be reset after reboot of the system
#Developer info : Venkatasubramanian S, Contact : chandragupta1888@gmail.com
import subprocess
import optparse
def get_arg():
    saba=optparse.OptionParser()
    saba.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    saba.add_option("-m", "--mac", dest="mac", help="New MAC to be used")
    if not options.interface:
        saba.error("{~} Please specify an interface, use --help for more info")
    elif not options.mac:
        saba.error("{~} Please specify a new mac, use --help for more info")
    return options
def change_mac(interface,mac):
    print("{~} Changing MAC address for " + interface + "to" + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])
options = get_arg()
change_mac(options.interface, options.mac)