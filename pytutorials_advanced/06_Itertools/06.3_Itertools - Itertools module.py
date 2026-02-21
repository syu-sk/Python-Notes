import itertools

testlist = [100, 200, 300, 400]
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 3, 4]
selectors = [True, True, False, False]

'''Basic Itertools functions'''
def itertoolfuncs():
	#1: count - returns an iterator that counts
	counter = itertools.count()
	list1 = list(zip(itertools.count(), testlist))
		#count accepts start argument, works similar to enumerate
		#count accepts step, which defines the increment for subsequent values. step can be negative and/or a float
	print(list1)

	#2: zip_longest
		#recall zip combines >1 iterables, limiting number of values to the iterable with the least values
		#zip_longest is like zip, but uses the iterable with the most number of values
	list2 = list(itertools.zip_longest(range(6), testlist))
	print(list2)

	#3: cycle - returns an iterator that cycles across a list
	cycler = itertools.cycle([1, 'second', ('3rd', 4)])
	print([next(cycler) for n in range(7)])

	#4: repeat - returns an iterator that repeats the same value
	repeater = itertools.repeat('clone', times = 3)
		#repeat accepts the times argument, defining the upper limit. going past this limit returns a StopIteration exception
	print([i for i in repeater])

	#5: starmap
		#recall map passes any iterables it receives into its assigned function (map(func, iterable)), returning an iterable with no. of values = iterable passed with lowest no. of values
		#star map takes arguments that are already paired together as tuples instead of taking arguments from the iterables themselves as in map
	squares = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])
		#through map: squares = map(pow, range(3), itertools.repeat(2))
	print(list(squares))

	#6: chain - chains together iterables (combines them into a single iterable). more efficient than regular concatenation
	combined = itertools.chain(testlist, letters, numbers)
	print(list(combined))

	#7: islice - allows for slicing on iterables
	iterslicer = itertools.islice(range(100), 0, 100, 10)
	#.islice(iterable, lower, upper, step). similar to [x:y:z]. however this removes the need to cast iterable into a list, which can be helpful if the iterable is long enough to put a strain on memory
	print(list(iterslicer))


#itertoolfuncs()


'''Permutations, Combinations and Product'''
#Combinations - No. of ways to group together, WITHOUT consideration for order
#Permutations - No. of ways to group together, WITH consideration for order
def pnc():

	print(list(itertools.combinations(numbers, 2))) 
	#order does not matter, no duplicates
	#(iterable, number of values to group together)

	print(list(itertools.combinations_with_replacement(numbers, 2))) 
	#order does not matter, duplicates accepted

	print(list(itertools.permutations(numbers, 2)))
	#order matters, no duplicates
	#(iterable, number of values to group together)

	print(list(itertools.product(numbers, repeat = 2)))
	#order matters, duplicates accepted
	#(iterable, repeat = number of values to group together)

#pnc()


'''Advanced itertools functions'''
def advancediterfunc():
	#1: compress - returns a truncated list with values whose corresponding indexes in the second list are True
	compressor = itertools.compress(letters, selectors)
	print(list(compressor))

	#2: filterfalse - similar to the built_in filter function, but inverse
	def morethan2(x):
		return True if x>2 else False
	filterfalse = itertools.filterfalse(morethan2, numbers)
	print(list(filterfalse))

	#3: dropwhile - drop values from an iterable until it finds one that returns False, after which it stops modifying the iterable
	list1 = [3,4,5,1,3,4]
	dropwhile = itertools.dropwhile(morethan2, list1)
	print(list(dropwhile))

	#4: takewhile - take values from an iterable until it finds one that returns False, after which it stops taking values
	list1 = [3,4,5,1,3,4]
	takewhile = itertools.takewhile(morethan2, list1)
	print(list(takewhile))

	#5: accumulate - returns accumulated sums for each index going through an iterable. can also accept different operators
	accumulate = itertools.accumulate(numbers)
	print(list(accumulate))

	#6: groupby - groups values together into assigned keys, represented by a function
	def get_state(x):
		return x['state']
	people = [{'name': 'John Doe','city': 'Gotham','state': 'NY'},{'name': 'Jane Doe','city': 'Kings Landing','state': 'NY'},{'name': 'Corey Schafer','city': 'Boulder','state': 'CO'},{'name': 'Al Einstein','city': 'Denver','state': 'CO'},{'name': 'John Henry','city': 'Hinton','state': 'WV'},{'name': 'Randy Moss','city': 'Rand','state': 'WV'},{'name': 'Nicole K','city': 'Asheville','state': 'NC'},{'name': 'Jim Doe','city': 'Charlotte','state': 'NC'},{'name': 'Jane Taylor','city': 'Faketown','state': 'NC'}]
	grouper = itertools.groupby(people, get_state)
	#.groupby(iterable containing dictionaries, function to set key)
	#(limitation) however, the dictionaries within the iterable have to already be sorted by key 
	for key, group in grouper:
		print(key)
		for person in group:
			print(person)
		print()

	#7: tee - copy iterable to another assigned variable. self-explanatory, but be reminded not to iterate through the original iterable, if the position of the copied iterables are intended to remain unchanged

#advancediterfunc()