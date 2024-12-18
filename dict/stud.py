#!/usr/bin/python3

students=[]

while True:
	name=str(input("Enter Name(or type stop to finish):")).strip()
	if name.lower()=='stop':
		print("[+]Closing Up!!")
		break
	course=str(input("Enter Course Studied:")).strip()
	age=int(input("AGE:"))
	print()
	print("[+]ENTER NEW ENTRY")

	student={'name':name, 'course':course, 'age':age}

	students.append(student)

print()
print("[+]List of Students")

for stud in students:
	print("Name:", stud['name'])
	print("Course:", stud['course'])
	print("AGE", stud['age'])
	print()
