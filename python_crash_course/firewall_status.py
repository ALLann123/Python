#!/usr/bin/python3

#get the firewall status
firewall_status=input("Is the firewall on or off: ").strip()

if not firewall_status == "on":
    print("Warning, You are not Safe!!!")
else:
    print("Firewall is Up. Network protected")