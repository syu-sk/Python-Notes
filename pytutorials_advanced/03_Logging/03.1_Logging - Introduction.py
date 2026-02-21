import logging

'''Logging Levels'''
#1: Debug - Detailed information, useful when diagnosing problems
#2: Info - Confirmation that the code works
#3: Warning - Indication of a non-threatening issue, or a problem in the near future (low disk space etc.) note the code still works as expected
#4: Error - Indication of a problem, rendering parts of the software dysfunctional
#5: Critical - Serious problem, rendering the ENTIRE CODE unable to run.

#Default for logging captures everything warning level and above
#https://docs.python.org/3/library/logging.html --> logging documentation

#Normally, logging is done through a created file. this is done by passing a filename argument
logging.basicConfig(filename='test.log', level = logging.DEBUG, format = '%(asctime)s:%(levelname)s:%(message)s')
#By running this method, the root logger has been configured, and any subsequent logging.basicConfig code will not run

def addfunction(x, y):
	return x + y

def func_1():
	print('func_1 run successfully')

a = addfunction(2, 3)
logging.debug(f'result: {a}')
#note this continues to add onto the log file, refrain from running excessively. log method has to be the same one in the basicconfig, i.e 'debug'