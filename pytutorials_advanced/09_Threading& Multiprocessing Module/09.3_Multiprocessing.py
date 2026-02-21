import time
from multiprocessing import Process, freeze_support, set_start_method
#multiprocessing involves spreading processes out across multiple processors, running the process at the same time (in parallel), making it effective for CPU bound tasks (data-intensive)
#the processes are actually running at the same time, not just putting one process on hold then calling the other like in threading
#number of processes run at the same time = number of cores on the pc. for more processes to run, the pc will assign a process to a core when it is done operating its process

def sleeping(s):
	print(f'Sleeping {s} seconds...')
	time.sleep(s)
	print('Done Sleeping!')

'''Multiprocessing - start & join'''
def example1():
	
	#in multiprocessing, .start() has to be 'guarded' with if __name__ == '__main__'. something to do with ensuring the spawned Python interpreter creates the child process without starting a whole other process.
	#when subprocess(child process) is created, it imports this whole module, which means it runs this whole code again in the subprocess. anything under name == main will not run in this imported module, and hence is 'guarded'

	
	if __name__ == '__main__':

		start = time.perf_counter()

		p1 = Process(target=sleeping, args=[1])
		p2 = Process(target=sleeping, args=[1])
		#similar to threading.Thread

		p1.start()
		p2.start()
		p1.join()
		p2.join()
		#.join() ensures the processes indicates in the join method finish running before moving on to the next operation. this start and join method is quite sloppy

		finish = time.perf_counter()

		print(f'Finished in {round(finish - start, 2)} second(s)')

#example1()


'''Creating processes through loops'''
def example2():

	if __name__ == '__main__':

		processes = []

		for _ in range(10):
			p = Process(target=sleeping, args=[2])
			p.start()
			processes.append(p)

		for i in processes:
			i.join()

#example2()



