#!/usr/bin/python3

import time
import threading

def print_time(threadName, delay):
	count = 0
	while count < 5:
		time.sleep(delay)                   #calling out the sleep function from the time module
		count+=1
		print(threadName, time.ctime(time.time()))      #calling another fucntion from the time module for getting system clock

#lets create new threads now
try:
	y = threading.Thread(target = print_time, args = ("Thread1:", 2))
	y.start()
	x = threading.Thread(target = print_time, args = ("Thread2:", 3))
	x.start()
except Exception as a:
	print("[+]Error encountered> ", a)

while 1:
	pass

