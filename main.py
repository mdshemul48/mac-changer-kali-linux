import os
import optparse


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
    print("Done")


options = get_arguments()
change_mac(options.interface, options.new_mac)