from concurrent.futures import ProcessPoolExecutor, as_completed
import time

def sleeping(s):
	print(f'Sleeping {s} seconds...')
	time.sleep(s)
	print(f'Done Sleeping {s} seconds!')

if __name__ == '__main__':

	with ProcessPoolExecutor() as executor:
		#using this context manager automatically joins the process, meaning that any code after this context manager runs only after everything in it has been run

		secs = [3,2,1]
		results = [executor.submit(sleeping,sec) for sec in secs]
		#similar to the thread pool executor, the .submit creates a future and monitors it, returning its output value immediately when the future has completed.

		secs = [6,5,4]
		results = executor.map(sleeping, secs)
		#returns results in order they were started..?
		#similar to the .map() from threadpoolexecutor