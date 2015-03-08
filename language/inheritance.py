#Class Inheritance

class Parent():

	def print_last_name(self):
		print ('Barker')

#Inherit from Parent class
class Child(Parent):

	def print_first_name(self):
		print ('Daniel')

	#override parent function
	def print_last_name(self):
		print('My Own last name from Child')

newKid = Child()
newKid.print_last_name()

#multiple Inheritance
class BigPerson(Parent, Child):
	pass

big_guy = BigPerson()
big_guy.print_last_name()
