from datetime import datetime

#get nth letter of a string, 0 based
#output: L
print "HELLO"[3]

#return length of a string
parrot = "Norwegian Blue"
print len(parrot)

#Lower & upper case
print "HELLO".lower()
print "hello".upper()

#String conversion
pi = 3.14
print str(pi)

#check for alpha
#output: true
print "FEFRE".isalpha()

#floor division, remove the last digit from number
print 1234 // 10

#string concatination
print "spam" + " and " + "eggs"

#print with c like variable replacement
string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." %(string_1, string_2)

#Simple IO
name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")
print "Ah, so your name is %s, your quest is %s, and your favorite color is %s." %(name, quest, color)

now = datetime.now()
print now
print now.year
print now.month
print now.day


