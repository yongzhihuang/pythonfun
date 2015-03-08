#Error and exception handling
#using try/exception

try:
	number = int(input('what is your favorite number? \n'))
	print (20/number)
except ValueError:
	print "Make sure to enter a number"
except ZeroDivisionError:
	print "Dont pick 0, divide by 0"
except NameError:
	print "Named error"
except:
	#try not to use this because its general
	print "Invalid Input"
finally:
	#execute this always
	print "Program ended"