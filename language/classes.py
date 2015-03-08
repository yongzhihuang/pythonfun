#Simple Enemy classes

class Enemy:

	#init get called automatically
	def __init__(self, life):
		self.life = life
		print "An enemy has been created with " + str(self.life) + " lives"

	def attack(self):
		print "ouch"
		self.life -= 1	#access class private variable

	def checkLife(self):
		if self.life <= 0:
			print "I am dead"
		else:
			print "I am alive and I have " + str(self.life) + " life"

enemy1 = Enemy(3)

enemy1.attack()
enemy1.attack()
enemy1.attack()
enemy1.checkLife()

enemy2 = Enemy(30)
