import re
#regular expressions (re) allow for matching of specific text patterns


#below is a sample text allowing for searching of characters

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
'''

'''Regex uses'''
#raw string - regular string prefixed with an 'r'. inteprets a string literally.

print(r'no new line -> \n')
#notice the \n does not go to the next line like it would in a normal string. \n is treated like normal characters in the string


findabc = re.compile(r'abc') 	#case-sensitive
matchabc = findabc.finditer(text_to_search)
for match in matchabc:
	print(match)
	#<re.Match object; span=(1, 4), match='abc'>. this means that, one match for 'abc' was found in text_to_search, at range(1,4) i.e the first 4 characters of the string.


#the string above contains 'Metacharacters'. They are special characters in regex that, when searched, functions differently. similar to making a raw string to print a '\n' for example, these metacharacters need to be escaped as well, via a backslash in front. note the r in front is still needed nonetheless
findperiod = re.compile(r'\.')
matchperiod = findperiod.finditer(text_to_search)
for match in matchperiod:
	print(match)