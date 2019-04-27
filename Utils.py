import random
class Utils:
	def __init__(self):
		self.COLOR_LEN=3
		self.MAX_WORLD_VALUE = 254
		self.MIN_WORLD_VALUE = 0
		self.FIT_CHROMO_COUNT = 3

	def getUnsignedInt(b):
		return 0;

	def getSignedInt(b):
		return -1

	@staticmethod
	def getrandInt(self,min,max):
		rand=Random()
		randomNum=random.random(min,max)
		return randomNum

	@staticmethod
	def getMinDx(self,allGenes,solution):
		genes=allGenes
		minDX=abs(solution-genes[0])
		chosen=0
		for i in range(len(genes)):
			if abs(solution-genes[i])<minDX:
				minDX=abs(solution-genes[i])
				chosen=i
		for i in range(len(genes)):
			if chosen==i:
				genes[i]=(solution-genes[i])
			else:
				genes[i]=-1000
		return genes

	@staticmethod
	def getFileExtension(file):
		name=file.name
		return 	substring.substringByChar(name, startChar=".")
	
