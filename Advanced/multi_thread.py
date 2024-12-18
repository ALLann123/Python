#!/usr/bin/python3

import threading
from time import sleep

#print(threading.active_count()) #used to print the number of threads inthe program

def eat_breakfast():
	sleep(2)
	print("Eating breakfast")

def drink_coffee():
	sleep(5)
	print("Drinking coffee")

def study():
	sleep(3)
	print("Studing")

#now lets create threads for this tasks
x = threading.Thread(target = eat_breakfast, args = ())
x.start()

y = threading.Thread(target = drink_coffee, args = ())
y.start()

z = threading.Thread(target = study, args= ())
z.start()

x.join()
y.join()
z.join()
#eat_breakfast()
#drink_coffee()
#study()
print(threading.active_count())
print(threading.enumerate())
#print(time.perf_counter())

