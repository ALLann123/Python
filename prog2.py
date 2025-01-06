# Program to decode XOR-obfuscated values

# Define the XOR-obfuscated sequence
getting_boring = [
    70, 111, 82, 69, 97, 67, 72, 45, 111, 66, 106, 69, 67, 116, 123, 32, 91,
    99, 72, 65, 82, 93, 40, 36, 95, 32, 45, 66, 120, 111, 82, 32, 34, 48, 120,
    50, 67, 34, 32, 41, 32, 125, 32, 41  # Example sequence extracted from the PowerShell script
]

# Perform XOR decoding with 0x2C and convert to characters
decoded_getting_boring = ''.join([chr(x ^ 0x2C) for x in getting_boring])

# Print the result
print("Decoded 'getting_boring':", decoded_getting_boring)
