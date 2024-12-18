#!/usr/bin/python3

def print_info(arg1, *vartuple):
	print("Output is:")
	print(arg1)
	for var in vartuple:
		print(var)

print_info(10)
print_info(10,20,30,40,506,654)