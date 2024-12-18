#!/usr/bin/python3
#while True:    #infinity loop
try:              #the code we want to handle the exception
	a = int(input("Enter first number> "))
	b = int(input("Enter Second number> "))
	c = a/b
	print("Answer", c)
except ZeroDivisionError:          #the code that handles the exception encountered to get meaningful message
	print("[+]Division by zero not permited!!")
	print(ZeroDivisionError)

