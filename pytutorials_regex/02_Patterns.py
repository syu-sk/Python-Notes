import re

#finding matches also works for files, under read mode.

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

shaunyusk@gmail.com
shaunyusk-alt@gmail.com
181799J@student.hci.edu.sg
maxtan_lim@hotmail.net
'''

def example1():
	#using metacharacters.
	#re.compile accepts a positional argument defined to be the 'search'. finditer then compiles all of these searches into a single iterable containing each match. 
	pattern1 = re.compile(r'\d')
	matches1 = pattern1.finditer(text_to_search)
	for match in matches1:
		print(match)

	pattern2 = re.compile(r'\s')
	matches2 = pattern2.finditer(text_to_search)
	for match in matches2:
		print(match)

	pattern3 = re.compile(r'$')
	matches3 = pattern3.finditer(text_to_search)
	for match in matches3:
		print(match)

#example1()


'''Finding phone numbers'''
def example2():

	pattern = re.compile(r'\d\d\d\W555\W\d\d\d\d')
	match = pattern.finditer(text_to_search)
	for match in match:
		print(match)
		#retrieves all phone numbers

	pattern2 = re.compile(r'[89]00.555.\d\d\d\d')
	match2 = pattern.finditer(text_to_search)
	for match in match2:
		print(match)
		#retrieves phone numbers starting with '800' or '900'

#example2()


'''Finding names'''
def example3():

	#r'M[rs]s?[.\s]?\s[A-Z]*\w*' works - but its ugly
	pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]*\w*')
	#syntax using the parentheses is known as a group, which is used in conjunction with | to accept any specified patterns 
	match = pattern.finditer(text_to_search)
	for match in match:
		print(match)

#example3()


'''Finding emails'''
def example4():
	emailpattern = re.compile(r'[\w-]+@[a-z]+..*')
	match = emailpattern.finditer(text_to_search)
	for match in match:
		print(match)
example4()


'''Metacharacter uses'''

# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)

# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String

# []      - Matches Characters in brackets**
# [^ ]    - Matches Characters NOT in brackets**, even new line
# |       - Either Or
# ( )     - Group

# Quantifiers (number of characters):
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One (at the end of a group) OR Non-greedy matching (at the end of a quantifier)
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)