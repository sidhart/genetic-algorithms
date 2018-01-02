# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 16:18:12 2017

@author: siddartha kandikonda
genetic algorithm to maximise the sum of five numbers
numbers can range between 1 and 5 inclusive
"""

import random

# Builds one possible solution as array of random integers
def buildChromosome(solsize):
    chromosome = []
    for i in range(solsize):
        chromosome.append(random.randint(1,5))
    return chromosome

# Evaluates the fitness(sum of numbers) of a solution
def testFitness(solution):
    fitness = 0
    for i in solution:
        fitness += i
    return fitness

# Creates an initial population
def createPopulation(popsize):
    population = []
    for i in range(popsize):
        population.append(buildChromosome(solsize))
    return population

# implements the logic of cross over between two solutions
def crossOver(parent1,parent2):
    child = []
    # pick a random midpoint
    midpoint = random.randint(1,solsize)
    #Take half from one, half from the other
    for i in range(solsize):
        if (i > midpoint):
            child.append(parent1[i])
        else:
            child.append(parent2[i])
    return child

# implements the logic of mutation within one solution
def mutate(mutationRate,chromosome):
    for i in range(len(chromosome)):
        if (random.random() < mutationRate):
            chromosome[i] = random.randint(1,solsize)
    return chromosome

# Logic for evolving generations of populations 
def draw(population):
    matingPool = []
    new_population = []
    # Calculate fitness of each solution
    for chromosome in population:
        fitness = testFitness(chromosome)
        n = fitness * 100
        # Add the solution n times to the mating pool
        for i in range(int(n)):
            matingPool.append(chromosome)
    # Reproduction logic
    for i in range(popsize):
        a = random.randint(0,(len(matingPool)-1))
        b = random.randint(0,(len(matingPool)-1))
        partnerA = matingPool[a]
        partnerB = matingPool[b]
        child = crossOver(partnerA,partnerB)
        mutated_child = mutate(mutationRate,child)
        new_population.append(mutated_child)
    return new_population

# kick off the GA
def setup():
    #create new population
    population = createPopulation(popsize)
    return population

# Display stats of each generation
def displayinfo(population):
    #ctr = 1
    pop_fitness = []
    print('Population size: ' + str(len(population)))
    for chromosome in population:
#        print('Chromosome #: '+str(ctr))
#        for i in chromosome:
#            print(i)
        fitness = testFitness(chromosome)
        pop_fitness.append(fitness)
#        print('Fitness: '+str(fitness))
        #ctr += 1
    avg_fitness = round(float(sum(pop_fitness))/float(len(pop_fitness)),2)
    print('Average fitness: '+ str(avg_fitness))

def getBest(population):
    for chromosome in population:
        if (testFitness(chromosome) == target):
            return chromosome
        else:
            return None

# Code for running the GA
popsize = 150
solsize = 5
max_num = 5
target = (max_num*solsize)
mutationRate = 0.01
finished = False
print('Generation: '+ str(1))
population = setup()
displayinfo(population)
bestsolution = getBest(population)
if bestsolution != None:
    for i in bestsolution:
        print(i)
else:
    genctr = 2
    while True:
        print('#############################')
        print('Generation: '+ str(genctr))
        population = draw(population)
        displayinfo(population)
        bestsolution = getBest(population)
        if bestsolution != None:
            print('Solution found: '+ str(bestsolution))
            break
        else:
            genctr += 1
