'''Tutorial 10'''

#1a
def collatz_distance(n):
	steps = 0
	while n != 1:
		if n % 2 == 0:
			n = n / 2
			steps += 1
		else:
			n = 3 * n + 1
			steps += 1
	return steps

#print(collatz_distance(1))
#print(collatz_distance(27))

#1b
def max_collatz_distance(n):
	return max([collatz_distance(i) for i in range(1, n+1)])

#print(max_collatz_distance(100))
#scaling the operation would increase the processing time linearly, hence the need for memoisation to save outputs.

#1c
memory = {}
def memoize(f):
	def inner(n):
		if n not in memory:
			memory[n] = f(n) 	#manually calculate for saving
			print(f'function result of input: {n} saved')
		else:
			print(f'retrieving result for input: {n}') 		#if already saved, simply retrieve. saves alot of time
		return memory[n]
	return inner

				#essentially: max_collatz_distance = memoize(max_collatz_distance)
@memoize		#convenient means of attaching a decorator to a function without reassigning it to a variable
def max_collatz_distance(n):
	return max([collatz_distance(i) for i in range(1, n+1)])
#memoizing collatz_distance instead would save the individual results for each number, rather than the result for the range of numbers.

print(max_collatz_distance(100))
print(max_collatz_distance(100))

#2a
#url does not exist, no internet connection etc.
#2b
#returning an exception terminates the whole code, so that future outputs will not be inappropriately modified, and the issue is located easier.
#2c
#use try:, then except blocks for exception criterias. Note to check for HTTPError before URLError, check more specific errors before broader errors.
#2d
def download_URLs(URL_filenames):
	for i in URL_filenames:
		contents = httpget(i[0])
		with open(i[1], 'wb') as f:
			f.write(contents)
	return 'done'
#httpget() function in tutorial itself. this code will not work without it.