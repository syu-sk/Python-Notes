#methods - functions associated with a class

'''Creating a Class'''
#class - a blueprint for creating instances. then methods can be passed through it
#instance - contains data that is unique to each instance. a class creates unique instances so to speak
#object - all things in python. functions, classes, instances, strings etc are all objects. essentially defined as 'anything' in Python

def example1():
	class Student:
		#similarly, use pass for empty class
		pass

	stu_1 = Student()
	stu_2 = Student()

	stu_1.first = 'john'
	stu_1.last = 'lee'
	stu_1.age = 16

	stu_2.first = 'jane'
	stu_2.last = 'tan'
	stu_2.age = 17

	print(stu_1.first)
	#stuff like 'jane' or 16 are attributes of instances, which can be printed out. though, it is pretty pointless to enter these attributes manually
#example1()


'''using __init__ & creating methods'''
def example2(): 	#a function

	class Student(): 		#a class

		def __init__(self, first, last, age): 	
		#a method, in this case a dunder method. refer to 05_Special Methods
			#init for initialise. 'self' is the instance itself, and can be anything but it is the convention

			self.first = first 	#an attribute (of class 'Student')
			self.last = last
			self.age = age
			#define attributes, which are specified in the __init__ method

		def fullname(self): 	#a method, i.e function of a class
			return f'{self.first} {self.last}'
			#this is a method, i.e a defined function within a class. note that the instance argument i.e 'self' has to be passed.

	stu_1 = Student('john', 'lee', 16) 		#an instance
	stu_2 = Student('jane', 'tan', 17) 		#an instance
	#stu_1/stu_2 is the instance, i.e 'self'. here instances are being defined

	print(stu_1.fullname())
	#method is passed in the form of .method(), which then runs whatever is in the method. note that () has to be present

	print(Student.fullname(stu_1))
	#does the same thing as above. since the method is passed through a class instead of an instance, the instance will then need to be passed as the argument
#example2()