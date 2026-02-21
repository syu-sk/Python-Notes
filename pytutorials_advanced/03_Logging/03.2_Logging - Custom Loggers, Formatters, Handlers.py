import logging

#it is not recommended to use a root logger for your code. when importing code from other files, the root loggers from both files will conflict, resulting in certain code potentially not being logged


'''Creating separate loggers for different code'''

#Settings for logger
'''
1. getLogger - set name
2. setLevel - set level
3. FileHandler
	- file in which logs are passed into (.addHandler)
	- format in which logs are passed in (setFormatter). this must be set before handler is added to the logger
	- set level (if needed, let say only errors need to be logged)

in the event the settings are not configured, the custom logger will inherit settings from the root logger (.basicConfig) if applicable.
'''

#Step 1:
logger1 = logging.getLogger(__name__)
#__name__ is the convention for naming loggers - directly retrieves name from the module, or __main__ if in the file itself

#Step 2:
logger1.setLevel(logging.INFO)
#setting logging level for the custom logger

#Step 3:
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger1.addHandler(file_handler)
#for every custom logger, a file handler is needed (for logs to be passed into). the format is passed into the file_handler

#it is also possible to create multiple handlers using a custom logger. for example, an error handler which catches logs ERROR or higher
error_handler = logging.FileHandler('errors.log')
error_handler.setLevel(logging.ERROR)
#level can be configured in a handler as well
error_handler.setFormatter(formatter)
logger1.addHandler(error_handler)

#another type of handler is the stream handler, which logs just like a file handler, but on console instead.
stream_handler = logging.StreamHandler() 
#no arguments, straight to console
logger1.addHandler(stream_handler)
#a logger can take multiple handlers


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger1.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        #note replace 'logging' with custom logger variable. logging uses the basicConfig i.e root logger

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')


def divfunc(x,y):
	try:
		result = x / y
	except ZeroDivisionError:
		logger1.error('Cannot divide by 0')
		#when divide by zero, the logger creates a log of this action
	else:
		return result

divfunc(5, 0)