#!/usr/bin/python3

file_open=input("Enter File name>> ")

with open(file_open, "r") as f:
	for read_line in f:
		print(read_line)
		

print("[+]Good Bye")
