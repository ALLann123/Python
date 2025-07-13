#!/usr/bin/python3

#empty list
targets=[]

#add five targets to our list
for i in range(5):
    target_ip=input("Enter IP>> ")
    targets.append(target_ip)

print()

#display our targets
for target in targets:
    print(target)

