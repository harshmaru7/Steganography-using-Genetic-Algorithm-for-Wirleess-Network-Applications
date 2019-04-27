from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
# This module is used to handle operations related to a single chromosome

class Chromosome:
	# Initializing the attributes of the class Chromosome.
	def __init__(self,id=-1,r=-1, g=-1, b=-1, fit=-1, xP=-1, yP=-1, sol=-1):
		self.genes = [None]*3
		self.genes[0] = r
		self.genes[1] = g
		self.genes[2] = b
		self.fitness = fit
		self.xPixel = xP
		self.yPixel = yP
		self.solution_Id = sol
		self.id = id
	# The below fuctions are some utility functions
	# This is used toget the vlaue of x
	def getX(self):
		return self.xPixel
	# This is used to get the value of y
	def getY(self):
		return self.yPixel
	# This is used to get thevalue of r or g or b pixel
	def getGene(self,index):
		return self.genes[index]
	# This is used to set the value of r or g or b pixel
	def setGene(self,index,value):
		self.genes[index] = value
	# This is used to get the valuse of all the genes
	def getAllGenes(self):
		return self.genes
	# This is used to get the size of the genes
	def size(self):
		return self.len(self)
	# This is used to get the fitness of the chromosome
	def getFitness(self):
		return self.fitness
	# This is used to set the fitness of the chromosome
	def setFitness(self,fitness):
		self.fitness = fitness
	# This is used to set the id of the chromosome
	def setId(self,id):
		self.id=id
	# This is used to set the solutionId of the chromosome
	def setSolutionId(self, solutionId):
		self.solution_Id=solutionId
	# This is used to get the solutionId of the chromosome
	def getSolutionId(self):
		return self.solution_Id
	# This is used to compare the fitness of two chromosomes
	def compareTo(self,o):
		return self.cmp(self.fitness,o.fitness)
	# Here we define the cmp function as there is now cmp in python3
	def cmp(self,a,b):
		return a-b
	# This is used to return the details of the function
	def toString(self):
		return "X :" + str(self.xPixel) + ", Y:" + str(self.yPixel) + " SolnId: " + str(self.solution_Id) +" red: "+ str(self.genes[0]) + ", green :" + str(self.genes[1]) + ", blue :"+ str(self.genes[2])
