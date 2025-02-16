#!/usr/bin/python3

#the function converts base 10 to base 2
def DecimalToBinary(num):
	if num >= 1:
		DecimalToBinary(num // 2)
		print(num % 2, end = '')

def binaryToDecimal(binary):
	decimal, i = 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	print(decimal)
gameover=True
print("*******Number Convertions********")
print()

def binToHexa(n):
    bnum = int(n)
    temp = 0
    mul = 1  # Multiplier for powers of 2
    count = 1  # Counter to track groups of 4 bits
    hexaDeciNum = ['0'] * 100  # Array to store hexadecimal digits
    i = 0  # Counter for hexadecimal number array

    while bnum != 0:
        rem = bnum % 10  # Extract last digit
        temp = temp + (rem * mul)  # Convert binary group to decimal

        # If a group of 4 bits is completed
        if count % 4 == 0:
            # Convert decimal to hex
            if temp < 10:
                hexaDeciNum[i] = chr(temp + 48)  # ASCII for numbers
            else:
                hexaDeciNum[i] = chr(temp + 55)  # ASCII for A-F
            mul = 1
            temp = 0
            count = 1
            i += 1  # Move to the next hex digit
        else:
            mul *= 2  # Multiply by 2 for binary weight
            count += 1
        bnum = int(bnum / 10)  # Remove last digit

    # If the last group of bits is incomplete
    if count != 1:
        hexaDeciNum[i] = chr(temp + 48)
    
    # Adjust index if the last group was completed
    if count == 1:
        i -= 1

    # Construct hexadecimal output
    hex_value = ""
    while i >= 0:
        hex_value += hexaDeciNum[i]
        i -= 1

    # Print final hexadecimal value
    print("\nHexadecimal equivalent of {}: {}".format(n, hex_value))


while gameover:
	print()
	print("1.Convert from Decimal To Binary")
	print("2.Convert from Binary To Decimal")
	print("3.Convert Binary to Hexadecimal")
	print()
	print("99. Exit")

	choice=input("Choose>> ")

	if choice == "1":
		number=int(input("Enter Number(base 10):"))
		DecimalToBinary(number)
	elif choice == "2":
		number=int(input("Enter binary(base 2):"))
		binaryToDecimal(number)
	elif choice == "3":
		binary_number = input("Enter a binary number(base 2): ")
		binToHexa(binary_number)
	elif choice == "99":
		print("Bye")
		gameover=False
	else:
		print("Invalid Choice")


