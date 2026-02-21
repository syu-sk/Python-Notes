'''Lecture 9'''
import math
#Multiple representations
#This can be exemplified using complex numbers, with standard and polar form

#standard - a + bi
def make_from_real_imag(x, y):
	return (x, y)
def real_part(z):
	return z[0]
def imag_part(z):
	return z[1]

def magnitude(z):
	return math.hypot(imag_part(z), real_part(z))
def angle(z):
	return math.atan(imag_part(z) / real_part(z))
def add_complex(z1, z2):
	return make_from_real_imag(real_part(z1) + real_part(z2),imag_part(z1) + imag_part(z2))

#polar - r(cos(a) + i sin(a))
def make_from_mag_ang(r, a) :
	return (r, a)
def real_part(z):
	return magnitude(z) * math.cos(angle(z))
def imag_part(z):
	return magnitude(z) * math.sin(angle(z))

def magnitude(z):
	return z[0]
def angle(z):
	return z[1]

#observe above. clearly the functions are different, but they both output the same code.

'''
Multiple Representations:
1. Different representations can have slightly different accuracies.
2. Same code can be reused even though representation is different. (Data abstraction)

Issues:
1. As seen with above, both constructors use tuples, which means a polar function can be used on a standard object, even though the function would not work properly. Representations have to be matched to operations.
2. Name conflicts. Same name, function override.

Solutions:
1. Tagged data.
Each representation to be given a tag to explicitly indicate representation type. This can be done through a function
'''

def make_tag(tag, contents):
	return (tag, contents)		#additional tag object to differentiate between representations

def type_tag(datum):
	if type(datum) == tuple and len(datum) == 2:
		return datum[0]
	else:
		raise Exception('Bad tagged datum -- type_tag: ' + str(datum)) #raise error if tag is not on the intended object

def contents(datum):
	if type(datum) == tuple and len(datum) == 2:
		return datum[1]
	else:
		raise Exception('Bad tagged datum -- contents: ' + str(datum))

#attach tag. the functions will have the same name so adopt another naming convention
def make_from_real_imag_standard(x, y):
	return attach_tag('standard', (x, y))
def make_from_real_imag_polar(x, y):
	return attach_tag('polar', (math.hypot(x, y), math.atan(y/x)))

#check for tag (predicates)
def is_rectangular(z):
	return type_tag(z) == 'rectangular'
def is_polar(z):
	return type_tag(z) == 'polar'

#attaching the tag to constructors does not solve the problem itself, functions still have to be matched.

'''
coder may decide to implement an alternate naming scheme for all functions (magnitude_rectangular, angle_polar).

However, there may be changes to code in the future.
- One representation is removed.
- New representation is added, which co-exists with current representations. Maybe a new exponential representation is created, which once again creates the problem of matching representations to operations.
- New function is created by coder for only one representation.

Managing complexity:
- To solve the problem above, generic operators can be used.
- Done by creating another layer of abstraction. This can be created by anyone.
- For example, a new function can be created that works for BOTH rectangular and polar representations. This is a generic operator.
'''

def real_part(z):
	if is_rectangular(z):
		return real_part_rectangular(contents(z))	#real_part_rectangular is hidden from user, they only know to use real_part (more convenient)
	elif is_polar(z):
		return real_part_polar(contents(z))
	else:
		raise Exception('Unknown type -- real_part' + z)
#an operation that differs based on type_tag.
#user no longer has to manually match reps to ops. the function even catches errors.
#in fact, selectors(real_part, imag_part etc.) are meant to be as generic as possible as they are most primarily used in operations, which are directly used by the user.

#as for constructors, use the most convenient one. eg. rectangular when real-imag is available, else polar. How to implement this?

'''
Strategy 1: Dispatching on type.
Involves providing generic operators based on checking datatype, then calling the appropriate function.
Generic operators work on polymorphic data (data which take on multiple forms)
1. Call generic operator on data
2. Based on datatype, generic operator executes a function. Note data going down will be stripped of tag
3. Returned data going up will be tagged

Advantages:
1. Removes the need to manually search for the appropriate function - just use operator for all data tags
2. If a representation is removed, a portion of the code becomes useless, though the generic operator itself will still work

Disadvantages:
1. The generic operator will need to be instructed which operation to use for ALL representations
2. Adding a new representation will require modifications to all generic operators
3. Still does not resolve name conflict

Strategy 2: Data-directed programming
Similarly uses a generic operator. However rather than being hard coded on which function to use, it instead does a lookup on a table, and then decides on what to do.
This addresses the problem of naming conflicts(each table entry can have different id) and allows easy extensions(just add an entry)

A readable table will look something like:

          Polar     Rectangular
real_part real_part real_part
imag_part imag_part imag_part
magnitude magnitude magnitude
angle     angle     angle

The generic operator decides which operation to use based on the datatype and the desired output.

Table fundamentals:
2 basic functions - put and get
put(<op>, <type>, <item>) -> enters <item> into table, indexed by <op> and <type>
get(<op>, <type>) -> looks up <op> and <type> in the table, returning the corresponding <item> entered.

There will be no name conflicts since all function names are local to the installer.
The installer is a function which contains all functions for that representation, as well as all the put operations to enter the functions into the table.
That said tags are still used to distinguish between types.
'''

'''
Dictionaries:
Python default data structure allowing retrieval by keyword. Mostly learnt before

Main use for dictionaries here are their suitability for tables. As the put and get functions mentioned above...
'''

def put(op, type, proc):
	if op not in procs:
		procs[op] = {} #making new key for new operation
	procs[op][type] = procs

def get(op, type):
	return procs[op][type]

'''Tutorial 8'''
#1a
#a constructor object. this object itself accepts 2 arguments insert and retrieve. insert saves an object inside 1 of 2 slots into a saved list object within the function. once the first slot is saved, it moves to the second slot then back to the first slot (and overwrites it) and so on. retrieve on the other hand returns the object that was most initially saved. if argument passed is neither insert nor retrieve, exception is returned.
#1b
def make_widget():
	stuff = ["empty", "empty", 0 ]
	def oplookup ( msg, *args ):
		if msg == "insert":
			place = stuff[2]
			stuff[place] = args[0]
			stuff[2] = (place + 1) % 2
		elif msg == "retrieve":
			return stuff[stuff[2]]
		else :
			raise Exception ("widget doesn't" + msg )
	return oplookup

widget = make_widget()
widget('insert', 1)
widget('insert', 2)
widget('insert', 3)
#1c
#retrieval 3 times -- returns the same item, since stuff[2] stays at a constant number, unless the retrieval is done in between insert operations.

#2
def make_accumulator():
	current_sum = 0
	def push(x):
		nonlocal current_sum	#a function can access an encapsulating variable, but cannot update it. 
								#nonlocal allows updating (current_sum) as it confirms the version of current_sum to update
		current_sum += x
		return current_sum
	return push

acc1 = make_accumulator()
# print(acc1(10))
# print(acc1(20))

acc2 = make_accumulator()
# print(acc2(30))
# print(acc2(-10))

#3a
def make_monitored(f):
	counter = 0
	def mf(query):
		nonlocal counter
		if query == 'how-many-calls?':
			return counter
		elif query == 'reset-count':
			counter = 0
			return 'counter has been reset'
		else:
			counter += 1
			return f(query)
	return mf

def add_1(x):
	return x + 1

s = make_monitored(add_1)
# print(s(100))
# print(s(5))
# print(s('how-many-calls?'))
# print(s('reset-count'))
# print(s('how-many-calls?'))

#3b
#just add a * in front of query. accommodate for len() == 1 or >1 inputs

#4
import random
def make_monte_carlo_integral(p, x1, y1, x2, y2):
	true_counter = 0
	false_counter = 0
	trials = 0
	def command(*query):
		nonlocal true_counter
		nonlocal false_counter
		nonlocal trials
		if query[0] == 'run trials':
			trials = query[1]
			for i in range(query[1]):
				xrandom, yrandom = random.uniform(x1, x2), random.uniform(y1, y2)
				if p(xrandom, yrandom):
					true_counter += 1
				else:
					false_counter += 1
		elif query[0] == 'trials':
			return trials
		elif query[0] == 'get estimate':
			area = abs(x2 - x1) * abs(y2 - y1)
			return (true_counter / (true_counter + false_counter)) * area 
	return command
def c_predicate(x, y):
	return x**2 + y**2 < 1

circle_estimate = make_monte_carlo_integral(c_predicate, -1, -1, 1, 1)
circle_estimate('run trials', 10000)
#print(circle_estimate('trials'))
#print(circle_estimate('get estimate'))

#5a
def translate(source, destination, string):
	translator = {source[i]:destination[i] for i in range(len(source))}		#dictionary to convert characters
	result = ''
	for letter in string:
		if letter in translator:
			result += translator[letter]	#convert if in translator, else keep the letter
		else:
			result += letter
	return result

#print(translate("dikn", "lvei", "My tutor IS kind"))

#5b
def caesar_cipher(shift, string):
	small = 'abcdefghijklmnopqrstuvwxyz'
	big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	absolute_shift = shift % 26
	t_small = small[absolute_shift:] + small[:absolute_shift]		#creates shifted small letter string
	t_big = big[absolute_shift:] + small[:absolute_shift]			#creates shifted capital letter string
	return translate(small + big, t_small + t_big, string)			#merges into a single string for translate to interpret source and destination. applies that to input string

#print(caesar_cipher(29, 'aAbB'))
