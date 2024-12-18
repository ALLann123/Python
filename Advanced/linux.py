#!/usr/bin/python3
import subprocess
import optparse

def get_input():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="Enter interface to change")
	parser.add_option("-m", "--mac", dest="new_mac", help="Enter the new MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface:
		parser.error("[-] Please specify an Interface or use --help for help")
	if not options.new_mac:
		parser.error("[-]Please write a valid new MAC address to change or use --help for help")
	return options 

def change_mac(interface, new_mac):
	print("[+]Changing the new MAC address of", interface, "to", new_mac)
	subprocess.call(["ifconfig", interface, "down"])
	subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
	subprocess.call(["ifconfig", interface, "up"])

#now lets call the functions above
options = get_input()
change_mac(options.interface, options.new_mac)
