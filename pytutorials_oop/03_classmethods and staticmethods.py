'''Class methods'''
def c_method():

	class Bank_Account:

		interest_rate = 1.02 	
		#Class variable

		def __init__(self, name, balance, age):
			self.name = name
			self.balance = balance
			self.age = age 

		def interest(self):
			self.balance = int(self.interest_rate * self.balance)
			#the class variable is an attribute. thus to retrieve the value, the class/instance i.e self has to be put before it.
			#the instance retrieves the attribute value from the class

		@classmethod
		#class method set. this makes it such that the method takes first arg as the class rather than the instance. useful for changing class variables etc.
		#again, cls is the conventional term
		def set_ir(cls, rate):
			cls.interest_rate = rate

		@classmethod
		#second class method
		def class_str(cls,acc_str):
			name, balance, age = acc_str.split('-')
			return cls(name, balance, age)
			#efficient way of returning an instance from a string input

	bacc1 = Bank_Account.class_str('tim-10000-20')

	print(Bank_Account.interest_rate)

	Bank_Account.set_ir(1.04)
	#note the cls positional argument is automatically taken as the class it is put under. so it is not supposed to be passed as an argument manually

	print(Bank_Account.interest_rate)
	print(bacc1.interest_rate)

#c_method()


'''Static methods'''
#methods pass instance as first arg, while class methods pass class as first arg. static methods do not pass anything by default. they are kinda like functions, though they do have some form of connection with the class
#similarly, use @staticmethod. function can be finding whether it is a working day for the bank, for example. a static method should still be in the class block