#Crawls a page and get their word count

import requests
from bs4 import BeautifulSoup
import operator

#create a list of every single word on the page
def start(url):
	word_list = [ ]
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code)
	for post_text in soup.findAll('a', {'class': 'index_singleListingTitles'}):
		content = post_text.string
		words = content.lower().split()
		for each_word in words:
			word_list.append(each_word)
	#Clean up our list of words 
	clean_up_list(word_list)

def clean_up_list(word_list):
	clean_word_list = [ ]
	for word in word_list:
		#for each word, replace these symbols by empty char
		symbols = "~!@#$%^&*()_+<>?,./\"\'[]"
		for i in range(0, len(symbols)):
			word = word.replace(symbols[i], "")
		#after cleaning, only add word if its lengh is more than 0 char
		if len(word) > 0:
			clean_word_list.append(word)
	create_dictionary(clean_word_list)

def create_dictionary(clean_word_list):
	word_count = { }
	for word in clean_word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1

	#sorted each value, sort by value,
	for key, value in sorted(word_count.items(), key * operator.itemgetter(1)):
		print key, value

start('http://www.mywebsite.com')
