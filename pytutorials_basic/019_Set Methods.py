#set is like a list, but removes all duplicate values. it has some unique methods as well.
#sets also do better on performance (especially when iterating through them)

set1 = set([1,2,3,4,5])
#equivalent to {1,2,3,4,5}


'''Duplicates'''
#given x = {1,2,3,4} and y = {1,2,3,4,1,2,3}, x and y will be sets with the same values, as sets innately remove duplicate values


'''Basic Methods'''
#.add() - adds the value to the set (only one)
#.update() - pass in a list as an argument, this adds all values in the list to the set. takes multiple arguments for more lists to add
#.remove() - removes value.
#.discard() - removes value, but does not return an error even if the value does not exist


'''Unique Methods'''
set_1 = {1, 2, 3}
set_2 = {2, 3, 4}
set_3 = {3, 4, 5}

#set_a.intersection(set_b) - returns common values
#set_a.intersection(set_b, set_c) - returns common values between all sets listed
print(set_1.intersection(set_2, set_3))

#set_a.difference(set_b) - returns values in set_a ONLY that are not in set_b. takes multiple arguments and same logic applies
print(set_1.difference(set_2))

#set_a.symmetric_difference(set_b) - returns all values in BOTH set_a and set_b that are not their common values