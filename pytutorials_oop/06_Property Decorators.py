'''Decorators'''
def decorator():

	class Bank_Account:

		def __init__(self, name, balance, age):
			self.name = name
			self.balance = balance
			self.age = age 

		interest_rate = 1.02

		def interest(self):
			self.balance = int(self.interest_rate * self.balance)

		@property
		def interest_return(self):
			return int((self.interest_rate - 1.00) * self.balance)
			#originally, to return the value above, print(bacc1.interest_return()) would have to be passed. but giving the property decorator has made the value retrievable like an attribute)

	bacc1 = Bank_Account('tim', 10000, 20)
	print(bacc1.interest_return)
	#the decorator simply changes a method into an attribute. though do note that this new attribute actually has to return something
#decorator()


'''Setters'''
def setter():

	class Name:

		def __init__(self, first, last):
			self.first = first
			self.last = last

		@property
		def fullname(self):
			return f'{self.first} {self.last}'

		@fullname.setter 	#note this @ is required
		#what you want to redefine, followed by .setter
		def fullname(self, name):
			#name value takes in the input value. i.e 'Max Lee'
			first, last = name.split(' ')
			self.first = first
			self.last = last
			#setters intepret a string and edit the instance, while the method inteprets an instance an returns another output


	name1 = Name('Jane', 'Tan')
	name1.fullname = 'Max Lee'
	#note redefining the fullname here without a setter returns an error whereby attributes cannot be edited. thus a setter is needed
	print(name1.fullname)
#setter()


'''Deleters'''
def deleter():

	class Name:

		def __init__(self, first, last):
			self.first = first
			self.last = last

		@property
		def fullname(self):
			return f'{self.first} {self.last}'

		@fullname.deleter 	#note this @ is required
		#what you want to delete, followed by .deleter
		def fullname(self):
			self.first = None
			self.last = None
			print('name deleted')

	name1 = Name('Jane', 'Tan')
	print(name1.fullname)
	del name1.fullname
	print(name1.last)
#deleter()