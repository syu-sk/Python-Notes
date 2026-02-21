import time
import concurrent.futures
#basically a better threading module
#however do note that threading is only useful when doing simple, non-computational heavy tasks, like downloading images etc. anything cpu-bound like resizing/editing images which require lots of computation would slow down threading instead

def func_1(i):
		time.sleep(i)
		return f'func_1: {i}'


'''ThreadPoolExecutor context manager & .submit'''
def example1():

	with concurrent.futures.ThreadPoolExecutor() as executor:

		'''One function'''
		f1 = executor.submit(func_1, 1)
		#.submit(function, argument)
		#schedules a function to be executed and returns a future object. a future object encapsulates the execution of the function, allowing the user to check the progress of the function (done executing, still executing etc...) or retrieve its return value
		print(f1.result())
		#waits for the function to complete and returns its return value.

		'''Looping through submit function'''
		results = [executor.submit(func_1, x) for x in range(4)]
		for f in concurrent.futures.as_completed(results):
			print(f.result())
		#.as_completed accepts any number of futures, waits for them to complete and yields the finished future immediately. it does so until all futures are done

#example1()


'''concurrent.futures map method'''
def example2():
	with concurrent.futures.ThreadPoolExecutor() as executor:
		secs = [5,4,3,2,1]
		results = executor.map(func_1, secs)
		#similar to the python built-in version, this method applies the values in list 'secs' on func_1

		for i in results:
			print(i)
		#starts running threads concurrently, but returns the results in the order that they are started, even if they end at different times. since the first future waits 5 seconds, it waits for this future to complete, and returns it at which point the others have long been completed, thus returning all instantaneously
		#any exceptions obtained are only raised when results are retrieved -- using .map itself will not raise any.

#example2()