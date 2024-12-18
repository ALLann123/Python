#!/usr/bin/python3
from time import sleep
from threading import *
class Hello(Thread):
	def run(self):
		for i in range(5):
			print("Hello!")
			sleep(1)

class Hi(Thread):
	def run(self):
		for i in range(5):
			print("Hi!")
			sleep(1)

g1 = Hello()
g2 = Hi()

g1.start()
sleep(0.2)
g2.start()

g1.join()
g2.join()

print("BYE!")