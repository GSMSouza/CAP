from clusterga.fitness import FitnessInterface
from numpy import ndarray, copy
import random as Random


class Individual:

    fitness: FitnessInterface

    def __init__(self, chromosome: ndarray):
        self.__chromosome = copy(chromosome)
        self.value = self.fitness.calculate(chromosome)

    @property
    def chromosome(self) -> ndarray:
        return copy(self.__chromosome)

    @chromosome.setter
    def chromosome(self, chromosome: ndarray):
        self.__chromosome = copy(chromosome)
        self.value = self.fitness.calculate(chromosome)

    def __str__(self):
        return "Individual: \nchromosome: \n{}\nvalue: {}\n".format(self.__chromosome, self.value)


class PopulationInterface:

    def __init__(self, samples: ndarray, random: Random):
        self.samples = samples
        self.individuals = []
        self.random = random
        self.size = 0
        self.sum_value = 0

    def start(self, size: int, max_groups: int):
        raise NotImplementedError

    def sort(self):
        self.individuals = sorted(self.individuals, key=lambda x: x.value, reverse=True)

    def next_gen(self, children):
        self.individuals += children
        self.sort()
        self.individuals = self.individuals[:self.size]
        self.sum_value = 0
        for i in self.individuals:
            self.sum_value += i.value

    def __iter__(self):
        return iter(self.individuals)

    def __getitem__(self, item):
        return self.individuals[item]

    def __str__(self):
        return "Population:\nSize:{}\nIndividuals:\n{}SizeIndividuals:\n{}".format(self.size,
                                                                                   self.individuals,
                                                                                   len(self.individuals))


class PopulationForSamples(PopulationInterface):

    def __init__(self, samples: ndarray, random: Random):
        super().__init__(samples, random)

    def start(self, size: int, max_groups: int):
        self.size = size

        for _ in range(size):
            selects = copy(
                self.samples[self.random.choices(range(
                    self.samples.shape[0]),
                    self.random.randint(
                        2, max_groups
                    )
                )]
            )
            self.individuals.append(Individual(selects))
            self.sum_value += self.individuals[-1].value
        else:
            self.sort()