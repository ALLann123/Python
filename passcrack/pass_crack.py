import hashlib

def crack_MD5_Hash(hash_to_crack, salt, dictionary_file):
    # Open the dictionary file containing potential passwords
    file = open(dictionary_file, "r")
    
    # Iterate through each password in the dictionary file
    for password in file:
        # Combine the salt with the password (removing newline characters) and encode it to UTF-8
        salted_password = (salt + password.strip("\n")).encode('UTF-8')
        
        # Compute the MD5 hash of the salted password
        hashed_password = hashlib.md5(salted_password).hexdigest()
        
        # Compare the computed hash with the target hash
        if hashed_password == hash_to_crack:
            # If they match, return the cracked password
            return password
    
    # If no match is found, return None
    return None

# Example usage
hash_to_crack = 'c94201dbba5cb49dc3a6876a04f15f75'  # The MD5 hash to crack
salt = 'd6a6bc0db10694a2d90e3a69648f3a03'           # The salt used in the hashing process
dict = "top10000.txt"  # Path to the dictionary file

# Call the function to crack the hash
password = crack_MD5_Hash(hash_to_crack, salt, dict)

# Print the result
if password:
    print(f"Password found: {password}")
else:
    print("Password not found in the dictionary.")
