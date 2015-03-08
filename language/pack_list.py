#name things easier, make sure length match
date, item, price = ['March 20 2015', 'Piggybank', '9.32']
print (item)	#Piggybank

def drop_first_last(grades):
	# look at the list passed in, store first value of list in first,
	# last value in grades, and the values in middle in middle
	first, *middle, last = grades
	avg = sum (middle) / len (middle)
	print (avg)

drop_first_last([65, 76, 98, 54, 21])
