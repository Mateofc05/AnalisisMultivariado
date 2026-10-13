import random
import numpy

# Creates a random individual using the binary representation.
# Each bit tells in which subset the number goes (0 = first subset, 1 = second subset).
def createIndividual(nbBits):
  return numpy.random.randint(2, size = nbBits)

# Implements the one point crossover on individuals using the binary representation.
def combine(parentA, parentB, cRate):
  if (random.random() <= cRate):
    cPoint = numpy.random.randint(1, len(parentA))
    offspringA = numpy.append(parentA[0:cPoint], parentB[cPoint:])
    offspringB = numpy.append(parentB[0:cPoint], parentA[cPoint:])
  else:
    offspringA = numpy.copy(parentA)
    offspringB = numpy.copy(parentB)
  return offspringA, offspringB

# Implements the flip mutation on individuals using the binary representation.
def mutate(individual, mRate):
  for i in range(len(individual)):
    if (random.random() <= mRate):
      if (individual[i] == 0):
        individual[i] = 1
      else:
        individual[i] = 0
  return individual

# Splits the numbers into two subsets according to the bits of the individual.
def split(numbers, individual):
  subsetA = []
  subsetB = []
  for i in range(len(individual)):
    if (individual[i] == 0):
      subsetA.append(numbers[i])
    else:
      subsetB.append(numbers[i])
  return subsetA, subsetB

# Fitness function for the balanced partition problem.
# It returns the absolute difference between the sums of the two subsets (lower is better).
def evaluate(individual, numbers):
  subsetA, subsetB = split(numbers, individual)
  return abs(sum(subsetA) - sum(subsetB))

# Implements the tournament selection (the individual with the smallest difference wins).
def select(population, evaluation, tournamentSize):
  winner = numpy.random.randint(0, len(population))
  for i in range(tournamentSize - 1):
    rival = numpy.random.randint(0, len(population))
    if (evaluation[rival] < evaluation[winner]):
      winner = rival
  return population[winner]

# Implements a genetic algorithm for solving the balanced partition problem.
def geneticAlgorithm(numbers, populationSize, cRate, mRate, generations):
  n = len(numbers)
  # Creates the initial population (it also evaluates it)
  population = [None] * populationSize
  evaluation = [None] * populationSize
  for i in range(populationSize):
    individual = createIndividual(n)
    population[i] = individual
    evaluation[i] = evaluate(individual, numbers)
  # Keeps a record of the best individual found so far
  index = 0
  for i in range(1, populationSize):
    if (evaluation[i] < evaluation[index]):
      index = i
  bestIndividual = numpy.copy(population[index])
  bestEvaluation = evaluation[index]
  # Runs the evolutionary process
  for i in range(generations):
    k = 0
    newPopulation = [None] * populationSize
    for j in range(populationSize // 2):
      parentA = select(population, evaluation, 3)
      parentB = select(population, evaluation, 3)
      newPopulation[k], newPopulation[k + 1] = combine(parentA, parentB, cRate)
      k = k + 2
    population = newPopulation
    for j in range(populationSize):
      population[j] = mutate(population[j], mRate)
      evaluation[j] = evaluate(population[j], numbers)
      # Keeps a record of the best individual found so far
      if (evaluation[j] < bestEvaluation):
        bestEvaluation = evaluation[j]
        bestIndividual = numpy.copy(population[j])
  # Builds the two subsets of the best solution found
  subsetA, subsetB = split(numbers, bestIndividual)
  return subsetA, subsetB, bestEvaluation

# Example from the activity
numbers = [1, 7, 4, 11]
subsetA, subsetB, difference = geneticAlgorithm(numbers, 20, 0.9, 0.1, 50)
print("Numbers:", numbers)
print("Subset 1:", subsetA)
print("Subset 2:", subsetB)
print("Difference:", difference)
print()

# A bigger example
numbers = [15, 3, 42, 8, 27, 19, 6, 33, 11, 24, 5, 38, 17, 2, 29]
subsetA, subsetB, difference = geneticAlgorithm(numbers, 50, 0.9, 0.05, 200)
print("Numbers:", numbers)
print("Subset 1:", subsetA)
print("Subset 2:", subsetB)
print("Difference:", difference)
