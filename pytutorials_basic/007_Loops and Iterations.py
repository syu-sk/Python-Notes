#1. For loops
	#for x in list. The 'x' can be anything, it is simply a variable that may be changed

#example_1 [break]
list = [1, 2, 3, 4, 5]
for num in list:
	if num == 2:
		print ('2 is in the list')
		break		#"break" function stops the loop there, and no further operations in the loop is done
	print (num)
#the code goes line by line, meaning the location at which the break is placed matters

#example_2 [continue]
nums = [1, 2, 3, 4, 5]
for num in nums:
	if num == 2:
		print ('2 is in the list')
		continue
	print (num)
#"continue" function skips to the next iteration; no further operations in that same loop
#likewise, location matters, by this logic putting continue at the end of a loop has no significance

#example_3 [loop in a loop]
levels = [1, 2, 3]
classes = ['A', 'B', 'C']
for level in levels:
	for _class in classes:
		print (level,_class)
#it is possible to make a loop within a loop

#example_4 [range()]
for item in range(1,3):
	print (item)
#"range()" function returns a list of integers from the lower bound, up to but not including upper bound

#2. While loops
	#keeps looping until its condition is no longer true

#example_5 [while]
x = 0
while x < 5:
	print (x)
	x += 1
#while loop continues operating until condition of x < 5 is no longer true
#while loops can continue INDEFINITELY -- Ctrl + C to stop the loop