#!/usr/bin/python3

class employe:
	def __init__(self):
		self.name = str(input("ENTER NAME: "))
		self.ID = str(input("ENTER ID: "))
		self.salary = int(input("ENTER SALARY: "))

	def displayEmployee(self):
		print("Name> ", self.name)
		print("Employee ID> ", self.ID)
		print("Salary> ", self.salary)
