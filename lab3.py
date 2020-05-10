class Furniture(object):
	def __init__(self, name, type, width, height, length):
		self.name = name
		self.type = type
		self.width = width
		self.height = height
		self.length = length
	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name
	def getType(self):
		return self.type
	def setType(self, type):
		self.type = type
	def getWidth(self):
		return self.width
	def setWidth(self, width):
		self.width = width
	def getHeight(self):
		return self.height
	def setHeight(self, height):
		self.height = height
	def getLength(self):
		return self.length
	def setLength(self, length):
		self.length = length
	def printInfo(self):
		print '{:10} | {:10} | {:4} | {:4} | {:4} '.format(self.name, self.type, self.width, self.height, self.length)
		
class SoftFurniture(Furniture):
	def __init__(self, name, type, width, height, length, fillerName):
		super(SoftFurniture, self).__init__(name, type, width, height, length)
		self.fillerName = fillerName
	def setFillerName(self, fillerName):
		self.fillerName = fillerName
	def getFillerName(self):
		return self.fillerName

class CorpusniFurniture(Furniture):
	def __init__(self, name, type, width, height, length, numOfElements):
		super(CorpusniFurniture, self).__init__(name, type, width, height, length)
		self.numOfElements = numOfElements
	def setNumOfElements(self, numOfElements):
		self.numOfElements = numOfElements
	def getNumOfElements(self):
		return self.numOfElements

furnitures = [];

soft1 = SoftFurniture('KAKAO', 'divan', 1,  2, 3, 'VATA')
soft2 = SoftFurniture('PCHELKA', 'krovat', 4,  5, 6, 'PUX')

corpus1 = CorpusniFurniture('NAPOLEON', 'stol', 1,  2, 3, 4)
corpus2 = CorpusniFurniture('VISHENKA', 'komod', 5,  6, 7, 8)

furnitures.append(soft1)
furnitures.append(corpus1)
furnitures.append(soft2)
furnitures.append(corpus2)

print '{:10} | {:10} | {:4} | {:4} | {:4} '.format('Name', 'Type', 'W', 'H', 'L')
for furniture in furnitures:
        furniture.printInfo()
