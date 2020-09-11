import unittest

from sklearn.datasets import load_iris

from clusterga.cluster import Pairwise
from clusterga.fitness import FitnessInterface
from clusterga.population import Individual, PopulationForSamples
import numpy as np

from clusterga.utils import Random


class MockFitness(FitnessInterface):

    def calculate(self, chromosome: np.ndarray) -> float:
        return 1.


class PopulationTestCase(unittest.TestCase):
    def test_individual(self):

        Individual.fitness = MockFitness(np.array([]), Pairwise())
        chromosome = np.array([[1, 1], [2, 2]])
        new = Individual(chromosome)
        test_values = new.chromosome == chromosome
        test_reference = new.chromosome is chromosome
        self.assertEqual(test_values.all(), True)
        self.assertNotEqual(test_reference, True)

    def test_start_population_for_samples(self):
        Individual.fitness = MockFitness(np.array([]), Pairwise())
        population = PopulationForSamples(load_iris().data, Random(0))
        population.start(40, 10)
        self.assertEqual(len(population.individuals), population.size)

        not_null = None in population
        self.assertNotEqual(not_null, True)


if __name__ == '__main__':
    unittest.main()
