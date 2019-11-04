class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def introduce(self):
		print("my name is {0}. {1} years old.".format(self.name, self.age))
