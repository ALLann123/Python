#!/usr/bin/python3

def rectangle(length, width):
	area = length * width
	perimeter = length + length + width + width
	print("The Area> ", area)
	print()
	print("The Perimeter> ", perimeter)
	return

#now call the function
rectangle( length = int(input("Enter the length: ")), width = int(input("Enter the Width: ")))


