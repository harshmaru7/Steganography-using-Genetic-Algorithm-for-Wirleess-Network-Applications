from PIL import Image
from numpy import array
from cryptography.fernet import Fernet
import random
from Chromosome import Chromosome
from Population import Population
from Fitness import Fitness
from Utils import Utils
class GA:
	def __init__(self,arr_solution,populationSize):
		self.crossoverRate=0.5
		self.mutationRate=0.05
		self.uniformRate=0.5
		self.elitism = True
		self.MAX_GENERATIONS = 3
		self.m_fitness = Fitness(arr_solution)
		self.m_population = Population(populationSize)
		self.Solution_Index = 0

	def initializePopulation(self, population):
		fitPopulation = self.m_fitness.calculateFitness(population)
		self.m_population.initializePopulation(fitPopulation)
	def evolvePopulation(self):
		
		child = None
		for i in range(self.MAX_GENERATIONS):
			
			parent1 = self.rankSelection(self.m_population)
			parent2 = self.rankSelection(self.m_population)
			child = self.crossover(parent1, parent2)
			self.m_population.updateChromosome(child)
			if(child.getSolutionId() == -1 and i==(self.MAX_GENERATIONS -1 )):
				child.setSolutionId(self.Solution_Index)
				self.m_population.updateChromosome(child)
				break
			elif child.getSolutionId() != -1 :
				break
			fittestChromosomes =  self.m_population.getFittestChromoCount()
			for j in range(len(fittestChromosomes)): #Check
				self.m_population.updateChromosome(self.mutate(fittestChromosomes[j]))
		
		self.m_fitness.incrementSolutionIndex();
		self.Solution_Index+=1
		
		return self.m_population

	
	def crossover(self,parent1,parent2):
		child = Chromosome();
		if (parent1.getFitness()<parent2.getFitness()):
			child = parent1
		else:
			child = parent2

		solution = self.m_fitness.getSolution()
		r = child.getGene(0)
		g = child.getGene(1)
		b = child.getGene(2)
		dr = abs(solution - r)
		dg = abs(solution - g)
		db = abs(solution - b)
		
		minz = dr
		chosen = 1
		if ( dg < minz	):
			minz = dg
			chosen = 2
		if (db < minz):
			minz = db
			chosen = 3
		if chosen == 1:
			if r > solution :
				r = r - int(dr*self.crossoverRate)
			elif r < solution :
				r = r + int(dr*self.crossoverRate)
			else :
				child.setSolutionId(self.Solution_Index)
			child.setGene(0,r)
			

		elif chosen == 2:
			if 	g > solution:
				g = g - int(dg*self.crossoverRate)

			elif g < solution:
				g = g + int(dg*self.crossoverRate)
			else:
				child.setSolutionId(self.Solution_Index)
			child.setGene(1,g)
			
		elif chosen == 3:
			if b > solution:
				b = b - int(db*self.crossoverRate)
			elif b < solution:
				b = b + int(db*self.crossoverRate)
			else:
				child.setSolutionId(self.Solution_Index)
			child.setGene(2,b)
			
		return child

	
	def mutate(self,c):
		gene_count=3
		SUBRACT=1
		ADD=2
		operation=random.randint(1,2)

		for index in range(gene_count):
			value=c.getGene(index)
			if(operation==SUBRACT):
				value-=int(value*self.mutationRate)
				if(value<0):
					value+=int(value*self.mutationRate)

			elif (operation==ADD):
				value+=int(value*self.mutationRate)
				if(value>254):
					value-=int(value*self.mutationRate)

			c.setGene(index,value)
		return c

	def rankSelection(self, pop):

		randomFromRank=random.randint(0, 2)
		fittestChromosomes=pop.getFittestChromoCount()
		abc=fittestChromosomes[0]

		return fittestChromosomes[randomFromRank]