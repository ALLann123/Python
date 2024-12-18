#!/usr/bin/python3
while True:
	amount=int(input("Enter the amount: "))
	if amount<1000:             #bolean expression if true executes this bloack of code
		discount=amount*0.05
		print("[+]Discount>>", discount)
	else:                     #bolean expression inthe if statement when zero or false this else statement executes
		discount=amount*0.01
		print("[+]Discount", discount)
	print("NetPayable>>", amount-discount)
	print("GoodBye!")
	print()