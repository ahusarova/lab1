class Student:
	def __init__(self, name, surname, fathersName, birthDate):
		self.name = name
		self.surname = surname
		self.fathersName = fathersName
		self.birthDate = birthDate
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
	def getSurname(self):
		return self.surname
	def setSurname(self, surname):
		self.surname = surname
	def getFathersName(self):
		return self.fathersName
	def setFathersName(self, fathersName):
		self.fathersName = fathersName
	def getBirthDate(self):
		return self.birthDate
	def setBirthDate(self, birthDate):
		self.birthDate = birthDate
	def getBirthDate(self):
		return self.birthDate
	def setBirthDate(self, birthDate):
		self.birthDate = birthDate
	def getAddress(self):
		return self.address
	def setAddress(self, address):
		self.address = address
	def getPhoneNumber(self):
		return self.phoneNumber
	def setPhoneNumber(self, phoneNumber):
		self.phoneNumber = phoneNumber
	def getFaculty(self):
		return self.faculty
	def setFaculty(self, faculty):
		self.faculty = faculty
	def getStudyYear(self):
		return self.studyYear
	def setStudyYear(self, studyYear):
		self.studyYear = studyYear


class MarkTable:
	def __init__(self):
		self.marks = dict()
	def addMarks(self, student, marks):
		self.marks.update({student : marks})
	def printAllMarks(self):
		print 'All students:'
		for x, y in self.marks.items():
			print( x.getName(), x.getSurname(), ":" , y)
	def printStudentsWithBadMarks(self):
		print 'Students with bad marks:'
		for x, y in self.marks.items():
			if 3 in y or 2 in y:
				print( x.getName(), x.getSurname(), ":" , y)
	def printStudentsWithMarksHigherThen(self, value):
		print 'Students with marks higher then:', value 
		for x, y in self.marks.items():
			marksSum = sum(y)
			if marksSum >= value:
				print( x.getName(), x.getSurname(), ":" , y)
	def printStudentsWithHighMarks(self, num):
		print 'Top', num , 'students'
		newList = sorted(self.marks.items(), key=lambda x: sum(x[1]), reverse=True)
		for i in range(num):
			print newList[i][0].getName(), newList[i][0].getSurname(), ":" , newList[i][1]

markTable = MarkTable()

student1 = Student('John', 'Doe', 'Ivanovich', '2018-09-09')
student2 = Student('Ivan', 'Ivanov', 'Ivanovich', '2018-10-09')
student3 = Student('Anna', 'Husarova', 'Sergeevna', '1999-02-20')
student4 = Student('Biba', 'Boba', 'Bobovich', '0000-00-00')

markTable.addMarks(student4, [2, 2, 2, 2, 2])
markTable.addMarks(student3, [5, 5, 5, 5, 5])
markTable.addMarks(student2, [5, 4, 5, 3, 5])
markTable.addMarks(student1, [2, 5, 2, 2, 5])
markTable.printAllMarks()
markTable.printStudentsWithBadMarks()
print 'Enter sum of marks min value:'
minSum = input()
markTable.printStudentsWithMarksHigherThen(minSum)
print 'How many students with high marks to show:'
numOfStudents = input()
markTable.printStudentsWithHighMarks(numOfStudents)
	
