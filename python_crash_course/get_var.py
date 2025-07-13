#!/usr/bin/python3

#and example
print("SSH LOGIN")

user_name=input("\nEnter Username: ")

if user_name == "root":
    while True:
        password=input("\nEnter password: ")

        if password == "kali":
            print("LogIn successfull")
            print("Welcome", user_name)
            break
        
        else:
            print("\nWrong password")

else:
    print("username not found!!!")