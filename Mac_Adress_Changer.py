#!/usr/bin/env python3
#This script is for changing the mac address of an interface
import subprocess
import optparse
import re

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Please enter the interface you want to change the Mac address for")
    parser.add_option("-m", "--mac", dest="new_mac", help="Please enter the new mac address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("Please specify an interface. Use --help for more information")
    elif not options.new_mac:
        parser.error("Please specify an new_mac . Use --help for more information")
    return options
def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])   
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_add_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode())
    if mac_add_result:
        return mac_add_result.group(0)
    else:
        print("Cloud not find Mac Address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("the current Mac : ", str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("The Mac Address was changer successfuly change to :", current_mac)
else:
    print("The Mac Address did not change.")
