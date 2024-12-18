#!/usr/bin/python3

import threading
import time

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):                  #we create a constructor and override it
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print("starting:", self.name)
		print_time(self.name, self.counter, 1)
		print("Exiting:"+ self.name)

def print_time(threadName, delay, counter):
		while counter < 5:
			time.sleep(delay)
			counter+=1
			print(threadName, time.ctime(time.time()))

#create new threads using the class above
thread1 = myThread(1, "Thread1", 2)
thread2 = myThread(2, "Thread2", 3)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Exiting Main Thread")
