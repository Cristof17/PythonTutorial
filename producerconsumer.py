#!/usr/bin/python

from threading import Thread , Semaphore, Lock , current_thread
from random import randint
from time import sleep

buff = []
sleepTime = 6
maxSize = 5
	
threadSize = 2


def produ(semaphore):
	while(1):
		global buff
		while not len(buff) == maxSize:
			value = randint(0,10)
			semaphore.acquire()
			print "%s are lock-ul si produce %d " % (current_thread().name , value)
			buff.append(value)
			semaphore.release()
			sleep(sleepTime)
		
def consu(semaphore):
	valueRead = 0
	while(1):
		while not len(buff) == 0:
			semaphore.acquire()
			value = buff[-1]
			print "%s are lock-ul si consuma %d " % (current_thread().name, value)
			buff.remove(buff[-1])
			semaphore.release()
			sleep(sleepTime)	

	

if __name__ == "__main__":
	
	semaphore = Semaphore(value = 2)
	produ = [Thread(target = produ, args = (semaphore,)) for i in range(threadSize)]
	consu = [Thread(target = consu, args = (semaphore,)) for i in range(threadSize)]

	for i in range(threadSize):
		produ[i].start()
		consu[i].start()

	for i in range(threadSize):
		produ[i].join()
		consu[i].join()	
	
