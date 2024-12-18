#!/usr/bin/python3
num=int(input("ENTER A NUMBER:"))

if num%2==0:
	if num%3==0:
		print("[+]The number is divisible by both 2 and 3")
	else:
		print("[+]The number is divisible by only 2")
else:
	if num%3==0:
		print("[+]The number is divisible by 3 only")
	else:
		print("[-]The number is not divisible by 2 or 3")

print("Bye!")