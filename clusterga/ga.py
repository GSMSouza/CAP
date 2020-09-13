import random
from clusterga.population import PopulationForSamples, Individual, PopulationInterface
from clusterga.crossover import CrossoverInterface
from clusterga.fitness import FitnessInterface
from clusterga.cluster import ClusterInterface
from clusterga.mutation import MutationInterface
from clusterga.selection import SelectionInterface
from clusterga import dict_factory as dic


def ga(samples, fitness_function="CalinskiHarabaz", gen=100, size_pop=40, p_crossover=0.5, p_mutation=0.1,
       max_groups=10, seed=2, mutation_operator="CreateOrDelete", crossover_operator="OnePoint",
       population_operator="SamplesSelect", selection_operator="Roulette", clustering="Pairwise"):

    random.seed(seed)
    mutation = crossover = population = selection = cluster = fitness = None

    if type(mutation_operator) is MutationInterface:
        mutation = mutation_operator
    else:
        try:
            mutation = dic.mutation[mutation_operator](samples, max_groups, random)
        except KeyError:
            print("Execept: keys {} or object type MutationInterface".format(dic.mutation.keys()))
    if type(crossover_operator) is CrossoverInterface:
        crossover = crossover_operator
    else:
        try:
            crossover = dic.crossover[crossover_operator](random)
        except KeyError:
            print("Execept: keys {} or object type MutationInterface".format(dic.crossover.keys()))
    if type(population_operator) is PopulationInterface:
        population = population_operator
    else:
        try:
            population = dic.population[population_operator](samples, random)
        except KeyError:
            print("Execept: keys {} or object type MutationInterface".format(dic.population.keys()))
    if type(selection_operator) is SelectionInterface:
        selection = selection_operator
    else:
        try:
            selection = dic.selection[selection_operator](population, random)
        except KeyError:
            print("Execept: keys {} or object type MutationInterface".format(dic.selection.keys()))
    if type(clustering) is ClusterInterface:
        cluster = clustering
    else:
        try:
            cluster = dic.cluster[clustering]()
        except KeyError:
            print("Execept: keys {} or object type MutationInterface".format(dic.cluster.keys()))
    if type(fitness_function) is FitnessInterface:
        fitness = fitness_function
    else:
        try:
            fitness = dic.fitness[fitness_function](samples, cluster)
        except KeyError:
            print("Execept: keys {} or object type MutationInterface".format(dic.fitness.keys()))

    Individual.fitness = fitness

    population.start(size_pop, max_groups)
    mean = []
    best = []

    for i in range(gen):
        children = []
        for individual in population:
            if random.random() < p_crossover:
                individual_b = selection.select(1, individual)
                children_a, children_b = crossover.crossover(individual, individual_b)
                children.append(children_a)
                children.append(children_b)
            if random.random() < p_mutation:
                children.append(mutation.mutation(individual))
        else:
            population.next_gen(children)
            mean.append(population.sum_value / population.size)
            best.append(population[0].value)
    else:
        return population[0]
