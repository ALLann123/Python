#!/usr/bin/python3
import threading
import time

class myThread(threading.Thread):
	def __init__(self, threadID, name, counter):
		threading.Thread.__init__(self)
		self.threadId = threadID
		self.name = name
		self.counter = counter

	def run(self):
		print("starting>", self.name)
		threadLock.acquire()
		print_time(self.name, self.counter, 0)
		threadLock.release()

def print_time(threadName, delay, counter):
	while counter < 5:
		time.sleep(delay)
		print(threadName, time.ctime(time.time()))
		counter+=1

threadLock = threading.Lock()
threads = []                  #creating a list

#create new threads

thread1 = myThread(1, "Thread-1", 2)
thread2 = myThread(2, "Thread-2", 3)

#start new threads
thread1.start()
thread2.start()

# add the threads to a list

threads.append(thread1)
threads.append(thread2)

#wait for all threads to finish and join back to main
for i in threads:
	i.join()

print("Exiting Main[+]")
