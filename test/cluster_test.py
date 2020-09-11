import unittest
import numpy as np
from skfuzzy import cmeans_predict
from sklearn.datasets import load_iris
from sklearn.metrics import pairwise_distances_argmin

from clusterga.cluster import Pairwise, FuzzyCMeans


class ClusterTestCase(unittest.TestCase):
    samples = load_iris().data
    center = samples[[1, 50, 149]]

    def test_pairwise(self):
        labels_pairwise = Pairwise().run(self.center, self.samples)
        labels_pairwise_sklearn = pairwise_distances_argmin(self.samples, self.center)
        equal = labels_pairwise_sklearn == labels_pairwise
        self.assertEqual(equal.all(), True)

    def test_fuzzy_c_means(self):
        labels_pairwise = FuzzyCMeans().run(self.center, self.samples)
        u, u0, d, jm, p, fpc = cmeans_predict(self.samples.transpose(),
                                              self.center, 2, error=0.005,
                                              maxiter=1000)
        labels_fuzzy_c_means = np.argmax(u, axis=0)
        equal = labels_fuzzy_c_means == labels_pairwise
        self.assertEqual(equal.all(), True)


if __name__ == '__main__':
    unittest.main()
