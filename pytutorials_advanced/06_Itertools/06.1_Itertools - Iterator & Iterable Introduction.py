#Iterable - an object that can be iterated over. possesses the dunder method __iter__. using this method returns an iterator.

#Iterator - an object that enables the iterating over an object that is iterable. it is aware of its position, as well as how to get to the next position, via the dunder method __next__. iterators are self-iterable. iterators cannot reverse or copy the same value, they can only go forwards


'''Iterable vs Iterators'''
def example1():

	nums = [1,2,3] 
	#iterable (list)

	iter_nums = iter(nums)
	#converts to an iterator. the for loop retrieves this automatically

	print(iter_nums)

	print(next(iter_nums))
	print(next(iter_nums))
	print(next(iter_nums))
	#an iterator possesses the dunder method __next__, calling this allows it to iterate to the next value, starting from the first one. the for loop does this automatically
	#when there are no values left, StopIteration exception is returned
	#files are iterables as well, and calling next on a file object enters its next line.

#example1()


'''Re-engineering the range function'''
def example2():

	class MyRange:

		def __init__(self, start, end):
			self.value = start
			self.end = end

		def __iter__(self):
			return self
			#a key characteristic of an iterator is that it possesses a __next__ dunder method. this method can return self, if the class possesses a dunder next method already

		def __next__(self):

			if self.value >= self.end:
				raise StopIteration
			current = self.value
			self.value += 1
			return current
			#implementing the looping in which the old value is incremented by 1 each time it is iterated, returning that value, until it has reached the last value where it raises the exception
			
	nums = MyRange(1,10)
	for num in nums:
		print (num)
	#giving the class MyRange the dunder iter and next methods allow it to iterate over itself using for loops, making it an iterable and an iterator
	#iterables have __iter__, iterators have __next__

#example2()


'''Generators as iterators (range function)'''
def example3():

	def my_range(start, end):
		current = start
		while current < end: 	#not including end
			yield current
			current += 1
	#similar concept as with classes. involves the iterator having a start point, being capable of getting itself to the next value, and terminating the iteration when it has reached the end of the iterable (which is already done using the while loop)

	nums = my_range(1,10)
	for num in nums:
		print(num)

#example3()