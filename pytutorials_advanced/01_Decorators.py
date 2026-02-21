'''First-class function and Closures'''
#First-class functions are functions that are treated like any other variable. python functions are all first-class functions, as all things are objects
#A closure is a nested function that is capable of accessing objects in its outer scope, even after the outer function is executed, via assigning it to a variable

def example1():

	def greeting(msg):

		def inner_func():
			print(msg)

		return inner_func
		#this returned 'inner_func' is what is called a closure. it is 'waiting' to be executed with a 'frozen' version of the outer function, through the use of a variable
		#'only after executing the closure does the function really gain closure :( '

	hi_greet = greeting('hi')
	hey_greet = greeting('hey')
	#here, due to greeting() returning a function itself (note no use of parentheses after inner_func), the returned function is now assigned to the variables hi_greet and hey_greet, allowing them to accept arguments
	hi_greet()
	hey_greet()
example1()


'''Decorators'''
def example2():

	def decorator_f(original_f):

		def wrapper_f():
			print(f'{original_f.__name__} executed by wrapper function')
			return original_f()

		return wrapper_f

	@decorator_f 	#calls decorator_f. basically encloses func_1 in decorator_f and redefines func_1 as that
	def func_1():
		print('func_1 run successfully')

	func_1()

#decorator functions allows one to add functionality to an existing function *without editing the function itself*. here, decorator_f returns wrapper_f, which waits to be executed. when it is executed, it runs original_f, as well as any other 'decorations' passed under it, effectively changing functionality of original_f. a popular use of decorators is to add a log to any functions executed by it etc.
#example2() 


'''Decorated function requiring arguments'''
def example3():

	def decorator_f(original_f):

		def wrapper_f(*args, **kwargs):
			print(f'{original_f.__name__} executed by wrapper function')
			return original_f(*args, **kwargs)
			#*args and **kwargs (convention) will need to be passed as arguments to the closure function, as well as the decorated function when it is returned. essentially, they accept any number of positional/keyword arguments for original_f

		return wrapper_f

	@decorator_f
	def func_2(arg1, arg2):
		print(f'func_2 with arguments: {arg1} and {arg2}')

	func_2('x', 'y')
#example3()


'''Classes as decorators - less commonly used'''
def example4():

	class decorator_class(object):

		def __init__(self, original_f):
			self.original_f = original_f
			#assigns a selected function to an instance of the class

		def __call__(self, *args, **kwargs):
			#similar to the wrapper function (wrapper_f) above
			#__call__ allows the instance to be 'called' as a function without impacting its constructability/destructability i.e allows the instance attributes to be changed whenever
			print(f'{self.original_f.__name__} executed by call method')
			return self.original_f(*args, **kwargs)

	@decorator_class 	#calls decorator_class, redefining func_2 as an instance of that class
	def func_2(arg1, arg2):
		print(f'func_2 with arguments: {arg1} and {arg2}')

	func_2('arg1', 'arg2')
#example4()


'''Chaining decorators'''
#This means using multiple decorators on one function.
#Let's have two decorators, dog and cat. Both decorators are to be placed on function duck.
def example5():

	def dog(func):
		def wrapper_dog():
			print(f'woof! dog function used on {func.__name__} function')
			return func()
		return wrapper_dog

	def cat(func):
		def wrapper_cat():
			print(f'meow! cat function used on {func.__name__} function')
			return func()
		return wrapper_cat

	@dog
	@cat
	def duck(): 	#sets duck = dog(cat(duck)). when using @, basically wraps all functions below and @s in it, in that order.
		print('quack')

	duck() 
	#'dog function used on wrapper function' - @dog is called on cat(duck) as explained above, which returns the function wrapper_cat. 

	print(duck.__name__)
	#as explained above, duck is redefined as dog(cat(duck)), which returns the wrapper function from dog, thus its name will likewise return wrapper_dog

	#to stack decorators without having such overlapping issues, refer to videos on module functools @wraps.
#example5()