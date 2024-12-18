#!/usr/bin/python3
import threading
import time

done = Falses

def worker():
	counter = 0
	while True:
		time.sleep(1)
		print(counter)
		counter+=1

x = threading.Thread(target=worker, daemon = True, args=())
x.start()
y = threading.Thread(target=worker, daemon = False, args=())
#y.start()

input(print("press enter to quit"))
done = True
