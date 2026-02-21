from bs4 import BeautifulSoup
import requests


'''Parsing from a test website'''

source = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops').text
#without .text only returns the response code. the html form is required to be passed into bs

soup = BeautifulSoup(source, 'lxml')
#always remember this code - it passes it into BeautifulSoup, giving it the whole lot of functionality. just use lxml as parser
#<head> normally contains metadata/other stuff that do not actually appear on the website
#<body> contains most of the useful information

laptops = soup.find('div', class_='col-lg-9').div
laptop = laptops.find_all('div', class_='caption')

print('Web Scraper Laptops:\n')

for i in laptop:
	laptop_description = i.find('p', class_='description card-text').text
	
	# laptop_name = (laptop_description.split(',')[0])
	# monitor = (laptop_description.split(',')[1])
	# processor = (laptop_description.split(',')[2])
	# ram = (laptop_description.split(',')[3])
	# ssd_space = (laptop_description.split(',')[4])
	# operating_sys = (laptop_description.split(',')[5])
	#due to non-uniformity in description formatting, parsing at this specific level is difficult

	print(f'{laptop_description} \n')

