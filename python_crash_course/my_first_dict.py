#!/usr/bin/python3

print("         AllSafe Cybersecurity Firm EMP       ")

user_db={"allan":"analyst", "bonny":"pentester", "moses":"SOC", "ann":"social-engineer"}

user_name=input("Enter name to ID Job title: ")

if user_name in user_db:
    #access the value using the key
    role=user_db[user_name]
    print("Job Title: ", role)
else:
    print("No Employee with that name")