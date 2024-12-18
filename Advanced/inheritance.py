#!/usr/bin/python3

class Parent:       #base/parent class
	attribute = 100   #class variable
	def __init__(self):     #constructor
		print("Parent Constructor")

	def parent_method(self):       
		print("calling parent method")

	def set_attribute(self, attr):
		Parent.attribute = attr

	def get_attribute(self):
		print("Parent Attribut> ", Parent.attribute)

class Child(Parent):           #the derived class(inheriting class)
	def __init__(self):
		print("Child Constructor")

	def child_method(self):
		print("Calling child method")

allan = Child()    #an object created from the child class which inherits all atributes of the parent class
allan.parent_method()
allan.child_method()
allan.set_attribute(288)
allan.get_attribute()