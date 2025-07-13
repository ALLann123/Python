#!/usr/bin/python3
import base64
from time import sleep

#title of application
print("************************"*5)
print("                                             View Secret      ")
print("************************"*5)

#function decrypts our flag if username is correct
def decrypt(secret):
    decoded_text=base64.b64decode(secret.encode()).decode()
    return decoded_text

#function checks the username before decrypting the flag in plain text
def check_username(username):
    secret="b3RuQ1RGe3B5dGgwbl9pc18zYXN5fQ0K"

    if username=="root":
        sleep(3)
        print("[-]Ooops I fell asleep...")

        print("[+]Correct Username Opening Flag.... ")
        result=decrypt(secret)
        return result

    else: 
        return "❌ Nope! Try again."
    
user_input=input("Enter Username to View Secret: ").split()

flag=check_username(user_input)

print("\n",flag)

