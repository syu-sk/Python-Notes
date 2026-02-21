'''Decorators accepting arguments'''

def prefix_decorator(prefix):
	#extra nest needed to customise each 'decoration'
	def decorator_f(original_f):

		def wrapper_f():
			print(f'{prefix}: {original_f.__name__} executed by wrapper function')
			return original_f()

		return wrapper_f

	return decorator_f


@prefix_decorator('func_1') 	#note new @, prefix will also have to be passed. recall @ encloses the below function in it
def func_1():
	print('func_1 run successfully')

func_1()
#this aint something thats normally used though, like 'adding' onto an addition