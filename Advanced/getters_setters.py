#!/usr/bin/python3

class MyClass:
	def setAge(self, num):
		self.age = num

	def getAge(self):
		return self.age

allan = MyClass()
allan.setAge(23)
print(allan.getAge())

karis = MyClass()
karis.setAge("twenty-three")
print(karis.getAge())
