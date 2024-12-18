#!/usr/bin/python3

def printinfo(arg1, *vartuple):
	print("Output is:")
	print(arg1)
	for var in vartuple:
		print(var)
	return

printinfo(10)
printinfo(1,2,3,4,5,6,67,76,54)