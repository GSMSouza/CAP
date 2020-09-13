from numpy import ndarray, delete, vstack

from clusterga.population import Individual
import random as Random


class MutationInterface:

    def mutation(self, individual: Individual) -> Individual:
        raise NotImplementedError


class CreateOrDelete(MutationInterface):

    def __init__(self, samples: ndarray, max_groups: int, random: Random):
        self.samples = samples
        self.random = random
        self.max_groups = max_groups

    def mutation(self, individual: Individual) -> Individual:
        chromosome = individual.chromosome
        if self.random.random() <= 0.5 and chromosome.shape[0] > 2:
            return Individual(delete(chromosome,
                                     [self.random.randint(0, chromosome.shape[0] - 1)],
                                     axis=0))
        elif chromosome.shape[0] < self.max_groups:
            return Individual(vstack((chromosome,
                                      self.samples[self.random.randint(0,
                                                                       self.samples.shape[1])])))
        else:
            return Individual(delete(chromosome,
                                     [self.random.randint(0, chromosome.shape[0] - 1)],
                                     axis=0))
