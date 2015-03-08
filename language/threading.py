#Use threading to do concurrent things
import threading

class myMessenger(threading.Thread):
	def run(self):
		#use _ for when u dont care about the thing you're using
		#I just want to loop 10 times
		for _ in range(10):
			print (threading.currentThread().getName())


x = myMessenger(name="Send Messages")
y = myMessenger(name="Receive Messages")

#when you do .start() it looks for function call run and run it
#both of the following will run concurrently
x.start()
y.start()
