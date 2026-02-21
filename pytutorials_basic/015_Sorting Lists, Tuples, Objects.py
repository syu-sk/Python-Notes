#Basic sorting can be done via sorted()
#works on lists, tuples, dictionaries

li = [-4, -2, 1, 3]
s_li = sorted(li, key=abs)
	#'key' argument sorts based on absolute value
print(s_li)

#.sort() can also be used - this changes the original obj
#can accept argument 'reverse=True', works only on lists


'''sorting complex variables'''
dict1 = {'name': 'John', 'age': 18, 'index': 1}
dict2 = {'name': 'Jane', 'age': 20, 'index': 2}
dict3 = {'name': 'Jake', 'age': 14, 'index': 3}
dicts = [dict1, dict2, dict3]

def dict_sort(dic):
	return dic['age']
s_dict = sorted(dicts, key=dict_sort)
print(s_dict)

#in the case of a dictionary where a certain key needs to be
#sorted, a custom function has to be made to specify value
#to be sorted. this is then passed through as an argument
#in the sorted() function


from operator import attrgetter
#attrgetter allows attrgetter to be passed into the 'key'
#argument in sorted() to automatically retrieve the attribute from the tuple