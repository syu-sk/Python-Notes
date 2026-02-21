import json

'''Loading/Dumping json data from a file'''
def example1():

	with open('states_data.json') as f:
		data = json.load(f)
		#.load, similar to .loads, loads a file instead of a string into a Python object.

	for state in data['states']:
		del(state['abbreviation'])
		#note the del function modifies data itself

	with open('new_state_data.json', 'w') as f:
		#note write mode to edit the file
		json.dump(data, f, indent=2)
		#.dump([data to encode], [file to dump to])

example1()