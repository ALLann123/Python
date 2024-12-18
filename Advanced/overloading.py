#!/usr/bin/python3

class Vector:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __str__(self):
		return 'Vector (%d %d)' %(self.a, self.b)

	def __add__(self, other):
		return Vector(self.a + other.b, self.b + other.b)

v1 = Vector(2, 3)
v2 = Vector(1, 7)
print(v1, v2)

