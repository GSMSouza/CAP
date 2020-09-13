import unittest
import numpy as np
import random
from clusterga.cluster import Pairwise
from clusterga.crossover import OnePoint
from clusterga.fitness import FitnessInterface
from clusterga.population import Individual


class MockFitness(FitnessInterface):

    def calculate(self, chromosome: np.ndarray) -> float:
        return 1.


Individual.fitness = MockFitness(np.array([]), Pairwise())


class CrossoverTestCase(unittest.TestCase):
    def test_one_point(self):
        individual_a = Individual(np.array([[1, 2, 3], [4, 5, 6]]))
        individual_b = Individual(np.array([[7, 8, 9], [10, 11, 12]]))
        random.seed(2)
        crossover = OnePoint(random)
        children_a, children_b = crossover.crossover(individual_a, individual_b)

        self.assertEqual(children_a is None, False)
        self.assertEqual(children_b is None, False)


if __name__ == '__main__':
    unittest.main()
