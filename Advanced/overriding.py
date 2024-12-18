#!/usr/bin/python3

class Parent:   #the base class
	def my_method(self):      #create a method inthe base class
		print("calling Parent method")

class Child(Parent):         #the derived class inheriting from the base class
	def my_method(self):     #create a method with the same name as the base class inorder to override it
		print("calling Child method")

allan = Child()        #create an instance of the Child class
allan.my_method()