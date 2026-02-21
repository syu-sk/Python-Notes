#creating a class in a class, i.e a 'subclass'
#keeps functionality in the parent class while being able to overwrite/add more functionality to the daughter class

'''Inheritance'''
def example1():

	class Bank_Account:
		interest_rate = 1.02

		def __init__(self, name, balance, age):
			self.name = name
			self.balance = balance
			self.age = age 

		def interest(self):
			self.balance = int(self.balance * self.interest_rate)

	class Premium(Bank_Account):
		#Premium is another class, but by passing Bank_Account as an argument, the new class has 'inherited' it, i.e it has become its parent class

		interest_rate = 1.06
		#overwrites class variable interest_rate for 'Premium' instances

		def __init__(self, name, balance, age, tier):
			super().__init__(name, balance, age)
			self.tier = tier
			#super() retrieves the parent class method without needing to manually define the arguments
	
	pbacc1 = Premium('Joe', 50000, 30, 1)
	#a subclass inherits all methods, class variables from its parent class. here, __init__ from class Bank_Account is inherited, so variable pbacc1 can still be made an instance.
	#help(Premium) for more info
	pbacc1.interest()
	print(pbacc1.balance)
	#returns balance using interest rate value of the subclass. note the interest() method has to be using self.interest_rate, where self will be the Premium class, which uses its correlating i/r value

#example1()


'''Tests'''
#1. isinstance(instance, class). returns a boolean on whether that instance is an instance of the referenced class
#2. issubclass(class1, class2). returns a boolean on whether class1 is a subclass of class2