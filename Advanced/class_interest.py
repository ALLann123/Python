#!/usr/bin/python3

class Simple_Interest:
	def __init__(self):
		self.principal = int(input("Enter The Principal:"))
		self.rate = (int(input("Enter the Rate:")))/100
		self.time = int(input("Enter Time:"))

	def calculate(self):
		self.si = self.principal * self.rate * self.time
		return self.si 

	def display(self):
		print("The Simple Interest> ", self.si)

prod1 = Simple_Interest()
prod1.calculate()
prod1.display()
