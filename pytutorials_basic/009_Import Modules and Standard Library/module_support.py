#module to be imported into the main code. it serves as a function, except it is in another file altogether

print ('module successfully imported!') 		
#good to print this message so that it is known when the module is imported

def calc_mod(int1, int2):			#basically just adds two numbers together
	print (f"adding {int1} to {int2}...")
	if (int1 + int2 >= 100):
		print ('big number')
	return (int1 + int2)

def index_mod(list, target):		#finds index of a value
	for item in list:
		if item == target:
			return (list.index(target))

	return -1			#returns -1 when target does not exist within the list