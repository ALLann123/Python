#!/usr/bin/python3
search=str(input("Enter student first name:")).lower()
names=['allan', 'eliot', 'alvin', 'mark']

for name in names:
	if name==search:
		print("Name Found>>", name)
		break
else:
	print("[-]Name not Found")
	print("AVAILABLE NAMES INCLUDE:")
	for name in names:
		print("Name:",name)

print()
print("Bye!!")