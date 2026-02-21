import requests
import pandas

def reqtext():
	r_text = requests.get('https://www.python.org/')
	#requests.get() to retrieve information from a website

	print(r_text.text)
	#.text prints out website in unicode form. dir(r) for more info
#reqtext()

def reqimage():
	r_image = requests.get('https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png')

	#print(r_image.content)
	#.content prints out image in bytes. this data is unusable on its own, requiring a byte reader

	with open('pylogo.png', 'wb') as pycopy:
		pycopy.write(r_image.content)

	print(r_image.ok)
	#True if .get() works as intended
#reqimage()


#httpbin.org - site made by request library guy to test code pertaining to the request module

def httpbin():
	payload = {'page': 2, 'count': 25}
	#a payload is a data package that is sent between a client and server in a web API
	r = requests.get('https://httpbin.org/get', params = payload)
	#pass arguments into params. check 'args' and 'url'

	print(r.url)	
	#url i.e link

	print(r.text)	
	#website details in text form

	print(r.json())	
	#website details compiled as a python dictionary. naturally, its keys may be retrieved 

#httpbin()

