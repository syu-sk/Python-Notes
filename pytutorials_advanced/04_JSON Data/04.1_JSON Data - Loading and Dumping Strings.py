'''json - JavaScript Object Notation'''
#Used alot when retrieving data from online APIs etc. Data in a code-readable format

'''
Conversions:

Json - Python
object - dict
array - list
string - str
number(int) - int
number(real) - float
true - True
false - False
null - None
'''

import json

sample_json = '''
	{
	  "name": "John",
	  "age": 30,
	  "married": true,
	  "divorced": false,
	  "children": ["Ann","Billy"],
	  "pets": null,
	  "cars": [
	    {"model": "BMW 230", "mpg": 27.5},
	    {"model": "Ford Edge", "mpg": 24.1}
	  ]
	}
	'''

'''loading a json string into Python dictionary'''
def example1():
	
	sample_data = json.loads(sample_json)
	#.loads is a method to load json data into a Python object. load(s), s for string

	print(f'Decoded json: {sample_data}\n')
	#comes in the form of a dictionary, so the sample_json is a json object

	print(f'Some keys:\n{sample_data['name']}\n{sample_data['children']}\n{sample_data['cars']}')
	#specific information can be retrieved from the json data directly, since sample_data as decoded is now a Python dictionary

#example1()


'''dumping Python objects into json data'''
def example2():
	sample_data = json.loads(sample_json)
	del sample_data['cars']

	new_string = json.dumps(sample_data, indent=2)
	#.dumps converts a Python string into json object format
	#indent defines how many characters each level is indented. makes data more readable
	#additional argument sort_key = True can be used, to sort keys in alphabetical order
	print(new_string)
	#this new string, if loaded, will give the same Python dictionary as the original sample_data (with the deleted 'cars' key)

example2()


