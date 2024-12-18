#!/usr/bin/python3
while True:
	numbers=[10, 34, 25, 674, 234, 34, 53, 23, 20, 30, 56, 13, 39]

	no=int(input("SEARCH NUMBER:"))

	for num in numbers:
		if num==no:
			print("[+]Number is in the List")
			print()
			break
	else:
		print("[-]Number is not in the List")
		print()

print()