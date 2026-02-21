#A function is a block of code that only runs when it is called. i.e with large blocks of code, only certain
#parts of it are needed to run. Thus functions are used to define these parts.
#note that functions can also be used under other functions just like functions like len()

#example_1 [function()]
def function():
	pass				#'pass' is used to define an empty function, allowing it to not return an error when run
print (function())		#printing out the function() causes it to run. Here 'None' is returned since its empty.
								#Function without parentheses is defined as the function itself, not the code in it

#easier to clean up mistakes made. Edits can be made to the function, rather than changing it at
#all locations. This makes the code more efficient (DRY - Dont repeat yourself)

#example_2 [return]
def func_2(name, surname = ''):
	return f"{name} {surname}'s function"	 #"return" function is used as the output of the function
print (func_2('shaun', surname = 'yu'))
#from this, it is seen that a function, similar to math's f(x), is like a machine that accepts an input,
#and returns an output based on this input. Of course the input may not be used, giving the same return
#and thus making .format() obsolete. Here func_2 takes the input name, then returns a value based on
#the name that was typed in.

#example_3 [arguments]
def func_3(*args, **kwargs):		#'args' and 'kwargs' are conventionally accepted titles
	print (f'arguments: {args} \nkeyword arguments: {kwargs}')

trait = ['10kg', 'multigrain']
nature = {'colour': 'white', 'food': 'rice'}
func_3(*trait, **nature )			#remember this is the line which runs the function
#args (arguments) and kwargs (keyword arguments) are placeholders for if multiple values 
#need to be passed into a function. Arguments will create a tuple based on any strings 
#inputted, and keyword arguments create a dictionary based on any keys (and their values) inputted.

#args and kwargs can be represented by variables, * will take it as the type of input and output accordingly