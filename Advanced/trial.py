#!/usr/bin/python3

class Rectangle:

	def __init__(self):
		self.length = int(input("Enter the Length:"))
		self.width = int(input("Enter the width:"))

	def area(self):
		self.area = self.width * self.length
		return self.area

	def perimeter(self):
		self.perimeter = (self.length + self.width) * 2
		return self.perimeter

	def display(self):
		print("The area is> ", self.area)
		print("The perimeter is> ", self.perimeter)

#rect1 = Rectangle()
#rect2 = Rectangle()
#rect1.area()
#rect1.perimeter()
#rect1.display()
