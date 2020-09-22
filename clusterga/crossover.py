from typing import Tuple
from numpy import hstack, copy,concatenate
from clusterga.population import Individual
import random as Random


class CrossoverInterface:

    def __init__(self, random: Random):
        self.random = random

    def crossover(self, individual_a: Individual, individual_b: Individual) -> Tuple[Individual, Individual]:
        raise NotImplementedError


class OnePoint(CrossoverInterface):

    def __init__(self, random: Random):
        super().__init__(random)

    def crossover(self, individual_a: Individual, individual_b: Individual) -> Tuple[Individual, Individual]:
        dimension = individual_a.chromosome.shape[1]
        c1 = individual_a.chromosome.reshape(
            (individual_a.chromosome.shape[0] * dimension))
        c2 = individual_b.chromosome.reshape(
            (individual_b.chromosome.shape[0] * dimension))
        min_ = min(c1.shape[0], c2.shape[0])
        index = self.random.randint(1, min_ - 1)

        c1, c2 = hstack((copy(c1[:index]), copy(c2[index:]))), hstack((copy(c2[:index]), copy(c1[index:])))

        return Individual(c1.reshape((c1.shape[0] // dimension, dimension))), Individual(c2.reshape((c2.shape[0] // dimension, dimension)))


class Merge(CrossoverInterface):

    def __init__(self, random: Random):
        super().__init__(random)

    def crossover(self, individual_a: Individual, individual_b: Individual) -> Tuple[Individual, Individual]:
        return Individual(concatenate((
            individual_a.chromosome, individual_b.chromosome
        ),axis=0))
