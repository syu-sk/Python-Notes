#Web Scraping - retrieving useful information from websites in the form of code-readable files (csv etc.)

from bs4 import BeautifulSoup 	#BeautifulSoup is a function, not module


'''Parsing html file'''
def example1():

	with open('samplehtml.html') as htmlf:
		soup = BeautifulSoup(htmlf, 'lxml')
		#passes the html file into BeautifulSoup, using lxml as its parser. soup is an object that contains the entire html code.

	#print(soup.prettify())
	#.prettify() is a convenient method that automatically creates indents for nested tags

	divs = soup.div
	print(divs)
	#.() returns the first occurrence of the tag (and its child tags) in the parentheses. 

	titles = soup.title.text
	print(titles)
	#.text returns in text-readable, without html elements

	print(soup.div.h2.a.text)
	#it is possile to chain together these methods to access more deeply nested tags

#example1()


'''.find(), .findall()'''
def example2():

	with open('samplehtml.html') as htmlf:
		soup = BeautifulSoup(htmlf, 'lxml')

	footerdiv = soup.find('div', class_='footer')
	secondheadline = soup.find('a', href = "article_2.html")
	print(footerdiv.text)
	print(secondheadline.text)
	#similarly, find also returns the first occurrence, but allows for additional details to narrow down the specific occurrence
	#underscore after 'class' since it is a Python keyword

	allarticles = soup.find_all('div', class_='article')
	#similar to .find, returns a list of all occurrences instead
	for i in allarticles:
		print(f'{i}\n')

#example2()