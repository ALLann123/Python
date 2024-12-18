#!/usr/bin/python3
amount=int(input("ENTER AMOUNT PAID:"))
if amount<1000:
	discount=amount*0.05
	print("[+]Discount is>>", discount)
elif amount<5000:
	discount=amount*0.10
	print("[+]Discount is >>", discount)
else:
	discount=amount*0.15
	print("[+]Discount is>>",discount)

print("[+]NetPay is>>", amount-discount)
print()
print("Goodbye!!")