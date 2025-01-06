# Program to decode integer lists to characters

# Define the integer lists
another_one = [87, 91, 24, 94, 65, 89, 92, 115, 38, 88, 28, 28, 115, 105, 24, 95, 85, 115, 38, 29, 74, 115, 85, 28, 89, 115, 109, 95, 71, 115, 38, 65, 31, 115]
too_much = [20, 78, 25, 79, 26, 24, 25, 30, 78, 27, 31, 24, 20, 78, 21, 25, 79, 73, 72, 73, 25, 28, 24, 77, 74, 74, 24, 20, 28, 29, 74, 21, 81]

# Decode the integers to characters
decoded_another_one = ''.join([chr(x) for x in another_one])
decoded_too_much = ''.join([chr(x) for x in too_much])

# Print the results
print("Decoded 'another_one':", decoded_another_one)
print("Decoded 'too_much':", decoded_too_much)
