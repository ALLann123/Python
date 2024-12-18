#!/usr/bin/python3

class Employee:
	empCount = 0

	def __init__(self, name, salary):
		self.name = name
		self.salary = salary
		Employee.empCount+=1

	def displayCount(self):
		print(Employee.empCount)

	def displayEmployee(self):
		print("Name: ", self.name, "salary: ", self.salary)

emp1 = Employee(name = str(input("Enter name> ")), salary = int(input("Enter salary> ")))
emp2 = Employee(name = str(input("Enter name> ")), salary = int(input("Enter salary> ")))
emp1.displayEmployee()
emp2.displayEmployee()
print("The Count> ", Employee.empCount)


