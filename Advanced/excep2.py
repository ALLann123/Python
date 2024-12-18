#!/usr/bin/python3

try:
	a = int(input("Enter first number> "))
	b = int(input("Enter the Second number> "))
	c = a/b
	print("ANSWER> ", c)

except ZeroDivisionError as a:
	print("Division by zero not allowed!!")

except ValueError: 
	print("ENTER A NUMBER!!")

except KeyboardInterrupt:
	print()
	print("[+]Exiting")

except Exception:
	print("something went wrong")

else:
	print("Try Only executed")

finally:
	print()
	print("GOOD BYE!")



