#!/usr/bin/python3

class Employee:    # class name
	empCount = 0    # class variable

	def __init__(self, name, salary):     #constructor- executed when a new object is created
		self.name = name
		self.salary = salary
		Employee.empCount+=1

	def displayCount(self):                     #class method
		print("The total:", Employee.empCount)

	def displayEmployee(self):               #class method
		print("Name>", self.name)
		print("salary>", self.salary)

emp1 = Employee("Allan", 20000)                 #creating an instance of the class(object)
emp2 = Employee("Tracy", 29300)

emp1.displayEmployee()                          #the object using the class method for displaying
emp2.displayEmployee()

print("Total Employee's>", Employee.empCount)

