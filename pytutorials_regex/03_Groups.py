import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''


'''Calling groups'''
def example1():
	pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
	matches = pattern.finditer(urls)

	for match in matches:
		print(match.group(2))
	#.group(0) - entire match
	#.group(1) - first group in the match, subsequent numbers(2,3...) correlate to subsequent groups
#example1()


'''.sub'''
def example2():
	subbed_urls = pattern.sub(r'\2\3', urls)
	print(subbed_urls)
	#regex allows for calling of groups
	#above, a pattern has been formed via the .compile method. this pattern has multiple groups, which is used to form a reduced form of the pattern via the .sub method, assigned to another variable. the backslash \ is used to call each group.
#example2()


'''Flags'''
def example3():
	sentence = 'Start a sentence and then bring it to an end'
	pattern = re.compile(r'start', re.IGNORECASE) 
	#re.IGNORECASE is a flag for taking lower and uppercase characters
	matches = pattern.search(sentence)
	print(matches)
#example3()



#notice .finditer is the only method used throughout the tutorial. it is the most commonly used one

'''
Other Methods from regex:
.findall - only returns first group. if no group, returns entire string(s) in an iterable. no group calling functionality
.match - only matches at the START of the string. otherwise returns none (quite useless). not an iterable
.search - matches anywhere in the string, but only returns the first match. not an iterable
'''


'''Automate the boring stuff w Python Exercise'''

#20.
tosearch20 = '1,234,567'

numberRE = re.compile(r'^\d{1,3}(,\d{3})*$')
mo20 = numberRE.search(tosearch20)
print(mo20.group())


#21.
tosearch21 = '''
Alice Watanabe Haruto Watanabe hehe haha
'''

nameRE = re.compile(r'\s[A-Z][a-z]*\sWatanabe\s')
mo21 = nameRE.finditer(tosearch21)
for match in mo21:
	print(match)