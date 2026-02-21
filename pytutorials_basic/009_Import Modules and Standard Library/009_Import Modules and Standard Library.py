import module_support as ms 		#'as' is used to shorten file name, for easy application
#imports the file 'module support' i.e its code and its functions now apply here
#only works directly if it is in the same directory

fruits = ['apple', 'orange', 'banana', 'grape']

print (ms.calc_mod(50,60))
print (ms.index_mod(fruits, 'grape'))
#the functions calc_mod and index_mod are present within the imported file
#as seen, ms is used rather than module_support which is longer to type

#alternatively, one may import selected functions from the module
from module_support import calc_mod as calc, index_mod as ind 	#similarly, 'as' can be used
#print (calc(20,30))
#print (ind(fruits,'apple'))

import sys
print (sys.path)
#If module does not reside in the same directory as the main code, import will not work as python will not
#be able to find it. This can be solved via appending the system path. (it is a list)

#The standard library is a provided set of modules in Python that are highly efficient with high 
#functionality. Some examples are random, math etc. Highly recommended to use
#Link: https://docs.python.org/3/library/index.html