#dunder - terminology for double underscore. __main__, __init__ are considered dunder methods
#learn how such methods work. makes understanding Python itself much easier


'''__repr__ and __str__'''

def example1():

	class Bank_Account:

		def __init__(self, name, balance, age):
			self.name = name
			self.balance = balance
			self.age = age 

		def __repr__(self):
			return f'''Employee {self.name}.\nBalance: {self.balance}\nAge: {self.age}'''
			#provides unambiguous representation of instance. without __repr__, print(bacc1) returns an output that is not comprehensible easily. somewhat defining how an instance is represented

		def __str__(self):
			return f'{self.name},{self.balance},{self.age}'
			#similarly allows one to define how the instance appears in a string form. if __str__ undefined, __repr__ is returned

	bacc1 = Bank_Account('tim', 10000, 20)
	print(repr(bacc1))  	#== print(bacc1.__repr__())
	print(str(bacc1))  		#== print(bacc1.__str__())
	print(bacc1.__dict__) 	#good method to know
#example1()


'''Working with other Dunder Methods'''

def example2():

	class Bank_Account:

		def __init__(self, name, balance, age):
			self.name = name
			self.balance = balance
			self.age = age 

		def __add__(self, other):
			return self.balance + other.balance
			#__add__ is a dunder method, represented by '+'. allows the defining of addition between these two classes which otherwise would not be possible as they are not integers

	bacc1 = Bank_Account('tim', 10000, 20)
	bacc2 = Bank_Account('sam', 15000, 19)
	print(bacc1 + bacc2)

	#https://www.geeksforgeeks.org/dunder-magic-methods-python/
	#^site for a list of dunders. allows one to create/overwrite certain functions and operators provided by python. for example, one can completely redefine the len() function on an instance, or customise how len is operated on that instance
#example2()


'''NotImplemented'''
#return NotImplemented is used to postpone the raising of an error in the case where another dunder method down the code has the capability to process given data. only when all subsequent methods are unable to process it will the error be raised.