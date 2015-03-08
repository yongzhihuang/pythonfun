import requests
from bs4 import BeautifulSoup

def digg_crawler():
	url = 'http://digg.com/'
	source_code = requests.get(url)
	plain_text = source_code.text 

	#creates a 'view-source' of the site source code 
	soup = BeautifulSoup(plain_text)

	#Go through each link of the page and print out title and url
	for link in soup.findAll('a', {'class': 'story-title-link'}):
		href = link.get('href')
		title = link.string
		print title + ' / ' + href

digg_crawler()

