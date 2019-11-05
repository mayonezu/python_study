from person import Person

class Student(Person):
	def __init__(self, name, age, school, grade):
		super().__init__(name, age)
		self.school = school
		self.grade = grade
	# override
	def introduce(self):
		super().introduce()
		print("I'm {0} grade at {1} school".format(self.grade, self.school))

s1 = Student("mayo", 31, "nezu", 3)
s1.introduce()
