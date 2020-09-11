from numpy import ndarray
from skfuzzy import cmeans_predict
from sklearn.metrics import pairwise_distances_argmin
import numpy as np


class ClusterInterface:

    def run(self, chromosome: ndarray, samples: ndarray):
        raise NotImplementedError


class Pairwise(ClusterInterface):

    def run(self, chromosome: ndarray, samples: ndarray):
        labels = pairwise_distances_argmin(samples, chromosome)
        return labels


class FuzzyCMeans(ClusterInterface):

    def run(self, chromosome: ndarray, samples: ndarray):
        u, u0, d, jm, p, fpc = cmeans_predict(samples.transpose(),
                                              chromosome, 2, error=0.005,
                                              maxiter=1000)
        return np.argmax(u, axis=0)
