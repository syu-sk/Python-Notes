'''Lecture 10'''
#dailou OOP...

#Contents: Object-Oriented Programming, Inheritance, Polymorphism

#Variables in global/local scope
x = 5
def foo():
	global x	#global needs to be called, otherwise a global variable x cannot be updated within a function foo. 
	x += 1		#for variables in an enclosing function as opposed to global, nonlocal is used in place of global
	print(x)
#foo()


#a list, on the other hand, can be updated from within a function.
y = [10]		#list
def foo2():
	y[0] += 1 	#does not reassign y. rather, it rebinds the first element of y.
	print(y)
#foo2()

'''
OOP:
Combines two powerful computational ideas:

1. Recall message passing
- Uses an inner function act as an extension 
- This allows the object to accept arguments which are handled by the inner function.
- These arguments are the operations

2. Recall data abstraction
- Involves constructors, accessors, predicates, printers etc. as learnt in previous lectures
- Involves many separate functions.

Concepts:
- Classes and instances
- Methods and message passing
- Inheritance
- Polymorphism
'''

'''Classes'''
#Defining an object itself. Analogous to a blueprint that defines properties and behavior of an object
#An 'Instance' of a class is a particular object made from the class. If a class is a blueprint of a car, an instance is one car.
#In fact, classes are already inherent in Python. They also have methods such as .pop etc.

class BankAccount:

	def __init__(self, initial_bal):		#constructor. self is a conventional keyword, a reference to the entire instance.
		self.balance = initial_bal			#attribute -- like getbal(acc1)

	def withdraw(self, amount):				#operator. a function within a class (i.e a method) allows it to be operated on its instance.
		if self.balance >= amount:
			self.balance -= amount
			return self.balance
		else:
			return 'Not Enough Money'

	def deposit(self, amount):
		self.balance += amount
		return self.balance
	#any attributes can be updated from within a method, and is automatically saved into the instance.

'''Inheritance'''
#A class 'inherits' from a superclass. A superclass is an even more general form of the class, for example how apples and oranges are both a fruit.
#Exploit common traits to create a standard structure / behaviour for multiple classes.
#A subclass is an extension of the function / behaviour of a superclass i.e a 'specialisation'
#When executing a method, if a function is not defined locally, Python will move up the class hierarchy to find that function. In this aspect, classes are similar to functions.

#Root class: All user defined classes should inherit from either root-object classes or from another superclass.
#An example of a root class below. A super general form of any object, whose function can be extended easily into subclasses.
class NamedObject(object):
	def __init__(self, name):
		self.name = name 

#Let's modify BankAccount() slightly.
class BankAccount(NamedObject):			#Parentheses after class definition are used for inheritance.
										#In this case, indicates that NamedObject is BankAccount's superclass
	def __init__(self, name, initial_bal):	
		self.balance = initial_bal		
		super().__init__(name)			#super() calls the superclass i.e NamedObject, thereby initialising this superclass as well when creating an instance of BankAccount

	def withdraw(self, amount):				
		if self.balance >= amount:
			self.balance -= amount
			return self.balance
		else:
			return 'Not Enough Money'

	def deposit(self, amount):
		self.balance += amount
		return self.balance

'''Polymorphism'''
#English terms - Many forms
#OOP provides a means for handling polymorphic functions i.e functions that take different types of arguments. (Overloading)
#Same message can be sent to different object types, which are handled by different methods based on the object class. (Overriding)
#This is useful as the programmer does not have to worry about the object type, as long as they have implemented how the class reacts to a message.

'''
Multiple Inheritance:
When a subclass inherits from multiple superclasses, i.e parentheses after class definition has more than one superclass.
If two superclasses have the same method, priority is with the first superclass.

'Diamond Inheritance':
If a subclass inherits from two superclasses, both of which are subclasses of a root class.

		Class A
	 /	         \
	/             \
Class B          Class C             'Diamond'
      |        /
        Class D

Think of it procedurically -- 
The path followed by the method will be the prioritised superclass, if it has a method of the same name.
If that method does again inherit from its superclass (as with this case), it follows, all the way to the root class.

Example:
Object D (A Class D instance) calls a method 'quack'. The method 'quack' is inherited from a super class.
1. If Class B and Class C both have the method 'quack', then the referenced superclass is the first one in the parentheses by Class D.
2. If Class B ONLY has the method 'quack', then Class D inherits from Class B. 
3. If Class C ONLY has the method 'quack', then Class D inherits from Class C. 
4. If neither Class B nor Class C has the method 'quack', but Class A has the method 'quack', then Class D inherits from Class A.

Once inherited into either Class B or C, if a superclass is referenced yet again (into Class A), then Class B/C inherits from Class A.
Hence Object D will return an output with inheritance from its whole tree, depending on superclass references and scope rules.

note similarity to decorators with functions? though using OOP is more convenient as it simplifies this hierarchical structure.
'''


'''
Summary:

1. Classes: Capture common behaviour. Superclasses have even more general behaviour but are less extended.
2. Instances: Unique identity with its own local modifyable state.
3. Hierarchy: Inheritance of state and behaviour from superclasses.
4. Multiple Inheritance: Particular rules for finding methods
5. Polymorphism: Override methods with new functionality. Different objects handled differently by the same method.
'''