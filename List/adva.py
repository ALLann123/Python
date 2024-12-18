#!/usr/bin/python3

students=[]

while True:
	name=str(input("Enter first name:"))
	if name.lower()=='stop':
		break
	students.append(name)

print()
for jina in students:
	print("Student Name>>",jina)