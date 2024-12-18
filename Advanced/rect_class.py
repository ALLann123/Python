#!/usr/bin/python3

class Rectangle:

	def __init__(self, length, width):
		self.length = length     #int(input("Enter the length: "))
		self.width = width      #int(input("Enter the width: "))

	def area(self):
		self.area = self.width * self.length
		return self.area

	def perimeter(self):
		self.perimeter = (self.length + self.width) * 2
		return self.perimeter

	def display(self):
		print("The area is> ", self.area)
		print("The perimeter is> ", self.perimeter)

rect1 = Rectangle(length = int(input("Enter the length: ")), width = int(input("Enter the width: ")))
rect1.area()
rect1.perimeter()
rect1.display()
