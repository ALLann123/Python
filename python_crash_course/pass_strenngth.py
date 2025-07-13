#!/usr/bin/python3

#get the password
user_pass=input("Enter Password: ").strip()

if len(user_pass) >=8:
    print("Strong Password")

else:
    print("Weak Password")