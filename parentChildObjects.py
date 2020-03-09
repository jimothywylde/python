class person:
	def __init__(self, fname, lname):
		self.fname = "fname"
		self.lname = "lname"
	def printname():
		print(self.fname)
		print(self.lname)

class student(person):
	self.studentID = "000000"
	def printstudentID():
		print(self.studentID)

x = student("John", "Doe")

x.printname()
x.printstudentID()
