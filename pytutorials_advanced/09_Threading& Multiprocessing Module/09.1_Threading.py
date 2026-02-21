'''
Threading: 
Runs code concurrently. Functions are run one after the other, but threading makes it such that the code does not wait for the functions to go to completion to run the next one
'''

import threading
import time

def sleeping(s):
	print(f'Sleeping {s} seconds...')
	time.sleep(s)
	print('Done Sleeping!')


'''No threading'''
def example1():

	start = time.perf_counter()
	sleeping(1)
	sleeping(1)
	sleeping(1)
	finish = time.perf_counter()

	print(f'Finished in {round(finish - start, 2)} second(s)')
	#no threading done, functions finish executing before executing the following one. program run in ~3s

#example1()


'''Threading - start & join'''
def example2():

	t1 = threading.Thread(target=sleeping, args=[1])
	t2 = threading.Thread(target=sleeping, args=[1])
	t3 = threading.Thread(target=sleeping, args=[1])
	#set the function itself as the target, arguments to the function passed as the argument 'args'

	start = time.perf_counter()

	t1.start()
	t2.start()
	t3.start()
	#.start() by itself starts the function (as indicated by target), and immediately carries on to the next function. thus the program timer above will not work as intended as the time at 'finish' is computed before the threads complete
	
	t1.join()
	t2.join()
	t3.join()
	#.join() ensures the threads finish running before moving on to the next operation. this start and join method is quite sloppy

	finish = time.perf_counter()

	print(f'Finished in {round(finish - start, 2)} second(s)')

#example2()


'''Running threads in a loop'''
def example3():

	threads = []

	start = time.perf_counter()

	for _ in range(10):
		t = threading.Thread(target=sleeping, args=[2])
		t.start()
		#.join() cannot be used here since the threads are not different threads that can be joined together, since they are in a loop
		threads.append(t)

	for thread in threads:
		thread.join()

	finish = time.perf_counter()
	print(f'Finished in {round(finish - start, 2)} second(s)')

#example3()