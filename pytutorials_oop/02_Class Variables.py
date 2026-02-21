#instance variables (name, age etc) are unique for each instance, but class variables should be the same for each instance


'''Class Variables'''

def example1():

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

	bacc1 = Bank_Account('tim', 10000, 20)
	bacc2 = Bank_Account('sam', 15000, 19)

	print(bacc1.balance)
	bacc1.interest()
	print(bacc1.balance)
#example1()

def example2():

	class testclass:
		class_var = 2

	testinstance = testclass()
	testinstance.class_var = 3

	print (testclass.class_var)
	print (testinstance.class_var)

	#this example uses a test class with a class variable defined as integer 2. then a test instance of this class is made, where the class_var method is passed through it, newly defined as integer 3. printing out the class variable retrieved from the test class will still be 2, though retrieving the class variable from the test instance will return 3.
#example2()


'''Case where self is not used'''
def example3():
	class Bank_Account:

		num_of_accs = 0
		interest_rate = 1.02 	
		#Class variable

		def __init__(self, name, balance, age):
			self.name = name
			self.balance = balance
			self.age = age 

			Bank_Account.num_of_accs += 1
			#use class instead of self since this variable is universal rather than defined for each instance

		def interest(self):
			self.balance = int(Bank_Account.interest_rate * self.balance)
			#the class variable is an attribute. thus to retrieve the value, the class/instance i.e self has to be put before it.
			#the instance retrieves the attribute value from the class

	bacc1 = Bank_Account('tim', 10000, 20)
	bacc2 = Bank_Account('sam', 15000, 19)
	print(Bank_Account.num_of_accs)
#example3()