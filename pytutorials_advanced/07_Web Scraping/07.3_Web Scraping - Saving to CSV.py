from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://crawler-test.com/').text
soup = BeautifulSoup(source, 'lxml')

panelheads = soup.find_all('div', class_='panel-header')
panels = soup.find('div', class_='panel').find_all('a')

with open('crawlertest.csv', 'w') as csv_file:
	csv_writer = csv.writer(csv_file)
	csv_writer.writerow(['header', 'panel'])

	for header in panelheads:
		for panel in panels:
			csv_writer.writerow([header.h3.text, panel.text])
			
