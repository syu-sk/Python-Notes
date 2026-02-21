'''Lecture 6'''

'''
Creating Compound Data:
Compound data is a more complex form of data that involves second and higher orders of primitive data.
They require:
1. Constructors -- functions like make_fraction() which involves more than one argument, and returns a *computer-readable* data form whereby operations can act on it
2. Selector (or Accessor) -- functions that access a component of the compound data. (such as denominator() etc.)
3. Predicates -- functions that ask questions / provide a state of a data. (such as is_improper() etc.)
4. Printers -- functions that display compound data in human-readable form.

Question 4 of Tutorial 4 is a basic example of constructing compound data of several orders.
'''

#1
def make_fraction(a, b):
	return (a, b)			#advise tuple for data not meant to be modified

#2
def numerator(f):
	return f[0]
def denominator(f):
	return f[1]

#3
def is_improper(f):
	return numerator(f) > denominator(f)	#boolean

#4
def fraction(f):
	return f'{numerator(f)} / {denominator(f)}'

'''
Things to note:
- ALL compound data functions are to work with the principal compound data form that they are made for
- It is common to make the mistake of using the original arguments of the constructor in making other functions. Selectors should be used instead (data abstraction)
'''

myfrac = make_fraction(5, 3) 	#this assigns myfrac to this constructor
#print(numerator(myfrac), denominator(myfrac))
#print(is_improper(myfrac))
#print(fraction(myfrac))

'''
Sequences:
'Handle the first element, then iterate/recurse down the rest'

Pretty similar to regular recursive solutions, except sequences are in context of tuples.
Note .append for tuples is +
'''

def exp_seq(seq, factor):
	if seq == ():		#important: this is the terminator, similar to if n == 0 for prior recursive questions.
		return ()
	else:
		return (seq[0] ** factor, ) + (exp_seq(seq[1:], factor))	#remember , for len(tuple) = 1

#iterative version
def iexp_seq(seq, factor):
	result = ()
	for i in seq:
		result += (i ** factor, )
	return result

#Mapping is an advanced version of a sequence function in which a FUNCTION is applied on each term in the sequence
#there is already a map() function, but create one organically for knowledge purposes.

def rmap(seq, f):
	if seq == ():
		return ()
	else:
		return (f(seq[0]), ) + (rmap(seq[1:], f))

#print(rmap((1,2,3,4), lambda x: x**x))
#it can be seen that this function is a more general function (i.e higher order) than the two exp_seq functions above

#iterative version
def imap(seq, f):
	result = ()
	for i in seq:
		result += (f(i), )
	return result

'''
Trees:
Shortly defined as sequences of other sequences. (i.e a tuple that can contain other tuples)
'''

def count_leaves(tree):
	if tree == ():
		return 0
	elif type(tree) != tuple:
		return 1
	else:
		return count_leaves(tree[0]) + count_leaves(tree[1:])

#print(count_leaves(((1,2,3), 5, 6, (1, 2), 4, 3, 2, (1,))))
#this recursion is slightly different in the sense that it 'branches out' as opposed to normally isolating one case and separately solving the rest.

#as imagined, mapping trees is more easily done with recursion as opposed to iteration.
#an iterative solution would require checking if a value was nested, and nested how many times. a recursive solution is more elegant and easier to write.
#same concept as counting -- except instead of counting leaves, we are doing something to the leaves when we walk through it
def treemap(f, tree):
	if tree == ():
		return ()
	elif type(tree) != tuple:
		return f(tree)
	else:
		return (treemap(f, tree[0]),) + (treemap(f, tree[1:]))

#print(treemap(((1,2,(3, 4)), 5, 6, (1, 2), 4, 3, 2, (1,)), lambda x: x*2))


'''Computation'''
#suppose we want to create a function that sums the squares of odd numbers in a tree.
#this can be done by slightly altering the treemap() function
def sumoddsq(tree, f):
	if tree == ():
		return 0
	elif type(tree) != tuple:
		if tree % 2 != 0:
			return f(tree)
		else:
			return 0
	else:
		return sumoddsq(tree[0], f) + sumoddsq(tree[1:], f)
#print(sumoddsq((1,2,3,4), lambda x: x**2))

'''
however, this involves editing the original function treemap. 
A better way to do this would be to use a higher order, more general function similar to how fold is to summation.

Advantages:
1. Modularity - Each component is independent of others, and may be reused for different purposes
2. Clarity - Separates data from processes, no numbers hard coded
3. Flexibility - Due to modularity, new components can be easily implemented and work well with prior functions

Generally, there are 4 steps:
1. Enumerate -- means flattening out tuples into single layer non-nested sequences.
2. Filter -- obtaining relevant data, in this case the odd numbers
3. Map -- apply function, in this case square
4. Accumulate -- 'summation'
'''

#step 1 -- shares similarities with count_leaves, except leaves are now shifted to a tuple.
def enum(tree):
	if tree == ():
		return ()	#since this is added to a tuple at the end
	elif type(tree) != tuple:
		return (tree,)		#add single tuple term, only nesting upon final layer (no multilayer nesting)
	else:
		return enum(tree[0]) + (enum(tree[1:]))		#making the term here a tuple will result in nesting since it is enclosed everytime it is not a leaf
#print(enum(((1,2,(3, 4)), 5, 6, (1, 2), 4, 3, 2, (1,))))

#step 2 -- tuple terms kept selectively
def filt(condition, seq):
	if seq == ():
		return ()
	elif condition(seq[0]): 	#condition is a function
		return (seq[0],) + filt(condition, seq[1:])
	else:
		return filt(condition, seq[1:])	#if not fulfill condition, skip straight to next term
#or alternatively, return (i for i in x if condition(i))
#print(filt(lambda x: x%2 != 0, (1,2,3,4,5,6)))

#step 3 -- return binary operation on the filtered sequence
def accumulate(op, base, seq):
	for i in seq:
		base = op(base, i)
	return base
print(accumulate(lambda x, y: x*y, 1, (1,2,3,4)))
#iterative version. recursive version is largely similar to fold, as well as the functions above.

#all in all,
def sum_odd_squares(tree):
	return 
		accumulate(lambda x, y: x + y, 0, 	#accumulate: add
			treemap((lambda x: x**2			#map: square
				filt(lambda x: x%2 != 0, 	#filter: odd
					enum(tree)))))
#wowza so long
print(sum_odd_squares(((1,2,(3, 4)), 5, 6, (1, 2), 4, 3, 2, (1,))))