#1. Conditionals
	#executed via if else statements
	#all conditionals have the same indentation

#example_1 [if]
colour = 'blue'
if colour == 'blue':
	print('colour is blue') 
	#Note that since the variable colour is the string 'blue', the conditional is true 
	#'colour is blue' is hence returned

#example_2 [else]
num = 4
if num < 3:
	print ('number is smaller than 3')
	#note comparisons are always used for if statements; refer to topic 2
else: print ('number is not smaller than 3')
#else acts as a separate pathway for when if statement is not true
#in this case, the integer num is not smaller than 3, thus the else pathway is taken

#example_3 [elif]
fruit = 'apple'
if fruit == 'orange':
	print ('fruit is orange')
elif fruit == 'apple':
	print ('fruit is apple')
else: print ('nil')
#if more than one if statement is needed, elif is used to consider for the following conditionals
#the variable fruit is not 'orange', so the elif statement is considered next

#example_4 [and]
num = 2
if num % 2 == 0 and num < 3:
	print ('num is 2')
else: print ('num is not 2')
#"and" operator may be used if there are 2 requirements for the conditional to be met
#in this case, number needs to be less than 3 and be even

#example_5 [or]
num_list = [2, 27, 1]
for num in num_list:					#testing the 3 integers in the conditional
	if num % 2 == 0 or num > 3:
		print ('even and >3')
	else: print ('not even and >3')
#"or" operator used if there are multiple requirements for a conditional, but only one has to be fulfilled
# 2 fulfills first requirement, 27 fulfills the second, but 1 does not fulfill any, returning 'no'

#2. Booleans

#example_6 [not]
sold = False
if not sold:
	print ('not sold')
else: print ('sold')
#"not" operator inverts a Boolean. Booleans are 'True' and 'False' values

#example_7 [is]
a = [1, 2, 3]
b = [1, 2, 3]
print (id(a))			# id of a is not the same as id of b, so False is returned
print (id(b))
print (a is b)
#"is" operator checks if the id is equal, unlike == comparison which checks only for content
#a and b are considered to have different ids; if b = a was instead used, then a is b would return True


#Python has particular criterion in evaluating whether a value is 'False'
	# a. Returns 'False' i.e if condition is not met
	# b. None
	# c. Zero of any numeric type
	# d. Any empty sequence ('', (), [] etc.)
	# e. Any empty mapping ({} etc.)

#example_8 [False Values]
false_list = [False, None, 0, '', {}]
for item in false_list:
	if item:
		print ('evaluated true')
	else: print ('evaluated false')
#any of the conditions above (a to e) if met will return a False value
#note that if item: basically means if item == True: