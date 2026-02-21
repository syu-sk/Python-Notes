'''1010s midterms 2021/2022'''

#Question 1

#A
#Output: 7 + (6 + (-5 + (-4 + (3 + (-2 + (0)))))) = 5

#B
'''
Output: 
'zyxa'
'zyb'
'zb'
False
'''

#C
#4
#9

#D
#13

#Question 2

#A
#Time - O(n^2) due to while loop
#Space - O(1) 

#B
def binary_to_denary(s):
	power = len(s) - 1
	if not s:
		return 0
	else:
		return int(s[0]) * 2**power + binary_to_denary(s[1:])

#print(binary_to_denary('11010011'))

#C
#O(n), O(n) for recursive

#D
def binary_to_denary(s):
	result = 0
	reverse = s[::-1]
	print(reverse)
	for i in range(0, len(s)):
		result += int(reverse[i]) * 2**i
		print(result)
	return result
#print(binary_to_denary('11010011'))

#E
#O(n), O(1). Goes through the string at one fell swoop

#F
def denary_to_binary(s):
	result = ''
	binary = 0
	power = 0
	if s == 0:
		return 0
	while binary <= s:
		power += 1
		binary = binary ** power
	if binary > s:
		binary /= 2				#find largest binary, if s > 0
	result += '1'
	




def add_binary()
