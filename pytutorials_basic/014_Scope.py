#LEGB: Local, Enclosing, Global, Built-in
#^sequence of priority to defining a variable

'''Local and Global'''
import pandas
x=1
def local():
	y=2
	print(y, x)
local()

#x is a global variable while y is a local variable (to its function)

def local2(): 
	#global x 	
	#global makes the x variable in this function global
	#nonlocal does something similar, but only for the enclosing function
	
	x=2
	print(x)
local2()
print(x)

#note that print x outside the function uses the global x value,
#while print x in the function uses the local value


'''Built-ins'''

import builtins
#print(dir(builtins)) 	#list of functions that come in python original installation

# def print():
# 	pass
# print()
#defining function with the same name as one that already exists will overwrite it
#following LEGB, the globally defined function print() is higher prio than the builtin function print



'''Enclosing'''
def outer():
	x = 'outer x'
	
	def inner():
		x = 'inner x'
		print(x)

	inner()
	print(x)

outer()
#print(x) in inner() observes a local x value, thus printing it out
#if x is not defined in inner(), it uses outer x as its defined value as this x encloses the inner() function
#if x is not defined in inner() AND outer(), then any global x value will be used
#finally, if x is never defined, then python finds a builtin value for x, which doesnt exist, thus returning an error

#essentially, legb means the system will slowly go outwards to to find a value for  a variable
#however it cannot retrieve a value from another function
