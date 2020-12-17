import os
import optparse
import subprocess
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="interface to change its mac address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new mac address")
    options, arguments = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] please specify an new mac, use --help for more info")
    return options


def change_mac(interface, new_mac):
    print(f"Changing MAC address for {interface} to {new_mac}")
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo ifconfig {interface} hw ether {new_mac}")
    os.system(f"sudo ifconfig {interface} up")


def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result[0]
    else:
        print("[-] Could not get mac address")


options = get_arguments()
current_mac = get_current_mac(options.interface)
print(f"current mac = {str(current_mac)}")
change_mac(options.interface, options.new_mac)
current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac:
    print(f"Mac address successfully change to {str(current_mac)}")
else:
    print("[-] Mac address not changed..")
