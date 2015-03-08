#merging list tuples with zip

first = ['ben', 'daniel', 'bob']
last = ['hanks', 'swift', 'pitt']

names = zip(first, last)
#will look something like
#[('ben', 'hanks'), ('daniel', 'swift'), ('bob', 'pitt')]

for a, b in names:
	print (a, b)

