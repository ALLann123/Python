#!/usr/bin/python3

def change_me(mylist):
	print("List Before Change:", mylist)
	#mylist[2]=35
	mylist=[20,30,34,56]
	print("List After Update:",mylist)
	return
mylist=[1,2,3,4,5]
#mylist=[10,20,30,40,50]
change_me(mylist)
print("List Outside function:", mylist)
