#used to make errors more comprehensible


'''example 1 - try/except'''
def example1():
	try:
		print(apples)
	except NameError:
		print('exception found')
#'except Exception' catches ALL errors, the moment it is detected
#normally ud want specific errors
# example1()


'''example 2 - exception as...'''
def example2():
	try:
		list1 = [1,2,3]
		print(list1[4])
	except IndexError as ie:
		print(ie)
	except Exception:
		print('non indexerror')
#using 'as' on an exception returns the error statement only
#example2()


'''example 3 - else'''
def example3():
	try:
		print('apples')
	except Exception:
		pass
	else:
		print('no error!')
#else statement checks if no exceptions are detected, 
#proceeding with instructions given in the else block
#note anything under try will still run
#example3()


'''example 4 - finally'''
def example4():
	try:
		print(apples)
	except NameError as ne:
		print (ne)
	finally:
		print('continuing process')
#finally is similar to else, except it continues to run
#in spite of any exceptions detected
#example4()

#using raise (exception), the exception will occur manually