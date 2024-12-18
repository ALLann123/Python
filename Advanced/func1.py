#!/usr/bin/python3

def printme(name, age, skill):
	print()
	print("STUDENT DETAILS")
	print("Name> ", name)
	print("Age> ", age)
	print("Speciality> ", skill)
	return

while True:
	printme(name = str(input("Enter your Name: ")), age = int(input("Enter your age: ")), skill = str(input("Enter your Speciality: ")))

	print("Bye!")

