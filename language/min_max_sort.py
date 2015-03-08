#min, max, sorting dictionaries

#we cant sort dictionaries by default
stocks = {
	'GOOG' : 520.54,
	'FB': 76.45,
	'YHOO': 39.28,
	'AMZN' : 306.21,
	'AAPL' : 99.76
}

#we CAN sort tuples

#(39.28, 'YHOO')
print (min(zip(stocks.values(), stocks.keys())))

#Max
print (max(zip(stocks.values(), stocks.keys())))

#Sory by value
print (sorted(zip(stocks.values(), stocks.keys())))

#Sort by keys
print (sorted(zip(stocks.keys(), stocks.values())))
