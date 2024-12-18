#!/usr/bin/python3

def calc_area(base, height):
	area=0.5*base*height
	print("[+]The Area is>>", area)
	return

def calc_perimeter(base, height, hyp):
	perimeter=base+height+hyp
	print("[+]The perimeter is>>", perimeter)
	return
	
print("WELCOME")
print("Enter The Triangle Measurements")
base=int(input("Enter the Base:"))
height=int(input("Enter the height:"))
hyp=int(input("Enter Hypotenus:"))
print()

calc_area(base, height)
calc_perimeter(base, height, hyp)
print()
print("[-]Good Bye!!")