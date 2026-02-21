'''Lecture 7'''

#this lecture is about lists. list functions like .pop, .clear, .insert etc.
#main point is that it is mutable unlike tuples.
#additionally, list comprehensions [i**2 for i in x if i%2==0] for example are also discussed.

x = [1,2,3,4,5,6]
#print([i**2 for i in x if i%2==0])

'''
Searching lists:
Elementary idea would be to iterate through the whole list to find desired element.
Though this is not the best method. Sorted lists would provide greater efficiency.

Binary Search:
1. Find middle element. return True if it is the key
2. Else, search right side if key is bigger than middle element and search left side otherwise
note this search only works on a sorted list
'''

def binary(lst, key):
	if lst == []:					#important: this is the terminator. the program returns an exception without this statement if key is not found
		return False
	middle = lst[len(lst) // 2]		#this must be after lst==[] otherwise an out of range exception is returned since len([]) = 0
	if middle == key:
		return True
	elif middle > key:
		return binary(lst[:len(lst)//2], key)
	else:
		return binary(lst[len(lst)//2 + 1:], key)

#x = [1,2,3,4,5,6,7,8,9]
#print(binary(x, 10))
#instead of order of growth of space complexity being O(n) for elementary methods, binary searches are O(log n).

'''
Sorting lists:
1. Elementary idea would be to find the smallest number and move it to the front, recursively doing this till sorted.
	- This idea is called a Selection Sort. though it is not particularly efficient, with time being O(n^2) and space being O(1)
2. Another way would be to split the sequence in half and sort individually, then combine halves and repeat sorting
	- To combine 2 sorted halves, compare the first elements of both halves, putting the larger element behind the smaller one.
	- Run a sort-of King of the Hill where the larger element stays and elements are taken from the losing half until a larger one is found.
	- When one half runs out of elements, simply chuck whatever elements are left at the end of the sequence.
	- This is known as a Merge Sort.
'''

#Selection Sort
def selection(lst):
	result = []
	while lst != []:
		smallest = lst[0]
		for i in lst:
			if i < smallest:
				smallest = i
		lst.remove(smallest)
		result.append(smallest)
		print(lst)
	return result

#print(selection([6,5,4,3,2,1]))
#very inefficient, looping through the whole list, and doing it over and over till finally it is hard sorted.

#Merge Sort
def merge_sort(lst):
	if len(lst) < 2:
		return lst		#base case
	middle = len(lst) // 2
	left = merge_sort(lst[:middle])		#
	right = merge_sort(lst[middle:])	#returns a multi-layered recursive merge_sort

	def merge(left, right):		#separate function for merging sorted lists
		result = []
		while left and right: 	# => left != [] and right != []
			if left[0] < right[0]:		#KOTH style
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		result.extend(left)	#chuck remainder inside if left OR right is empty
		result.extend(right)
		return result					#merge having multiple outputs thus returns multiple results. BUT only one ultimate end product is returned as the rest are intermediate steps

	return merge(left, right)			#since left and right have multiple recursions, this also returns multiple outputs
#merge_sort(merge_sort...(merge_sort(lst[:middle]))...) until there is 1 term in lst, then returns merge (and therefore result) to compute all the way to final sorted list

#print(merge_sort([6,9,3,7,8,4,2,1,5]))
#order of growth for time = O(n log n), for space = O(n)

#thankfully, no need to remember time/space complexity, nor any of the functions. just use list.sort()

'''
.sort(list, key, reverse=None)
- the method sorts the list IN PLACE (replaces the variable), using only < comparisons
- returns exception if comparison fails (tuple vs int, str vs int etc.)
- key: specifies a function used to extract a key from each list element. (**0.5 + 50, x[2] etc. basically maps this function over the elements before sorting them)
- reverse: by default, None. If True, reverses direction of sorting
'''

#there is another function sorted(), which similarly works for lists but does not modify in place. Meaning original list is unchanged and a variable has to be assigned to save it.


'''Tutorial 6'''
#1a, b
#index error for both cases since list is modified during iteration

#1c
def at_least_n(lst, n):
	index = 0
	while index < len(lst):		#use while loop as a terminator
		if lst[index] < n:
			lst.pop(index)
		else:
			index += 1
	return lst 

print(at_least_n([1,2,3,4,5], 3))

#1d
def copy_at_least_n(lst, n):
	sol = []
	for i in lst:
		if i >= n:
			sol.append(i)
	return sol

print(copy_at_least_n([1,2,3,4,5], 3))

#2a
def col_sum(m):
	colsums = []
	for i in range (0, len(m)):
		colsum = 0
		for lst in m:
			colsum += lst[i]
		colsums.append(colsum)
	return colsums
	#list comprehension: [sum([lst[i] for lst in m]) for i in range(0, len(m))]

m = [[ 1 , 2 , 3 ] , [4 , 5 , 6] , [7 , 8 , 9], [10,11,12]]
#print(col_sum(m))

def comp_sum(m):
	return [sum([lst[i] for lst in m]) for i in range(0, len(m))]

#print(comp_sum(m))

#2b
def row_sum(m):
	return [sum(lst) for lst in m]

print(row_sum(m))

#2c
def transpose(m):
	transposed = []
	for i in range(0, len(m[0])):
		newcol = []
		for lst in m:
			newcol.append(lst[i])
		transposed.append(newcol)
	return transposed

print(transpose(m))

#3
#just learn logic

#4
students = [
('tiffany ', 'A', 15 ) ,
('jane ', 'B', 10 ) ,
('ben ', 'C', 8 ) ,
('simon ', 'A', 21 ) ,
('eugene ', 'A', 21 ) ,
('john ', 'A', 15 ) ,
('jimmy ', 'F', 1 ) ,
('charles ', 'C', 9 ) ,
('freddy ', 'D', 4 ) ,
('dave ', 'B', 12 )]

#a (dk)
def mode_score(students):
	scores = [i[2] for i in students]	#list scores
	freq = 0
	for score in scores:
		if scores.count(score) > freq:
			freq = scores.count(score)	#get highest frequency, does not memorise any specific score
	result = []
	for score in scores:
		if scores.count(score) == freq and score not in result:
			result.append(score)	#record only scores with highest frequency
	return result

#b
def top_k(students, k):
	students.sort(key = lambda x: x[1])		#sort according to grade
	topk = students[:k]		#top k students -- without additional
	for i in students[k:]:
		if i[1] == topk[-1][1]:		#if grade of the next guy = grade of last guy in top k, add him in
			topk.append(i)
	return topk 

print(top_k(students, 7))
