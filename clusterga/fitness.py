from numpy import ndarray
from numpy.linalg import linalg
import numpy as np
from skfuzzy import cmeans_predict
from sklearn.metrics import pairwise_distances
from sklearn.metrics.cluster import calinski_harabasz_score, silhouette_score, davies_bouldin_score
from sklearn.metrics.cluster._unsupervised import check_number_of_labels
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import check_X_y, _safe_indexing

from clusterga.cluster import ClusterInterface


class FitnessInterface:

    def __init__(self, samples: ndarray, cluster: ClusterInterface):
        self.samples = samples
        self.cluster = cluster

    def calculate(self, chromosome: ndarray) -> float:
        raise NotImplementedError


class CalinskiHarabaz(FitnessInterface):

    def __init__(self, samples: ndarray, cluster: ClusterInterface):
        super().__init__(samples, cluster)

    def calculate(self, chromosome: ndarray) -> float:
        labels = self.cluster.run(chromosome, self.samples)

        n_samples, _ = self.samples.shape
        n_labels = chromosome.shape[0]

        extra_disp, intra_disp = 0., 0.
        mean = np.mean(self.samples, axis=0)
        for k in range(n_labels):
            cluster_k = self.samples[labels == k]
            mean_k = chromosome[k]
            extra_disp += len(cluster_k) * np.sum((mean_k - mean) ** 2)
            intra_disp += np.sum((cluster_k - mean_k) ** 2)

        return (1. if intra_disp == 0. else
                (extra_disp * (n_samples - n_labels) /
                 (intra_disp * (n_labels - 1.))))


class Silhouette(FitnessInterface):

    def __init__(self, samples: ndarray, cluster: ClusterInterface):
        super().__init__(samples, cluster)

    def calculate(self, chromosome: ndarray) -> float:
        labels = self.cluster.run(chromosome, self.samples)
        return silhouette_score(self.samples, labels)


class DaviesBouldin(FitnessInterface):

    def __init__(self, samples: ndarray, cluster: ClusterInterface):
        super().__init__(samples, cluster)

    def calculate(self, chromosome: ndarray) -> float:
        labels = self.cluster.run(chromosome, self.samples)
        self.samples, labels = check_X_y(self.samples, labels)
        le = LabelEncoder()
        labels = le.fit_transform(labels)
        n_samples, _ = self.samples.shape
        n_labels = len(le.classes_)
        check_number_of_labels(n_labels, n_samples)

        intra_dists = np.zeros(n_labels)
        centroids = np.zeros((n_labels, len(self.samples[0])), dtype=float)
        for k in range(n_labels):
            cluster_k = _safe_indexing(self.samples, labels == k)
            centroid = chromosome[k]
            centroids[k] = centroid
            intra_dists[k] = np.average(pairwise_distances(
                cluster_k, [centroid]))

        centroid_distances = pairwise_distances(centroids)

        if np.allclose(intra_dists, 0) or np.allclose(centroid_distances, 0):
            return 0.0

        centroid_distances[centroid_distances == 0] = np.inf
        combined_intra_dists = intra_dists[:, None] + intra_dists
        scores = np.max(combined_intra_dists / centroid_distances, axis=1)
        return 1 / np.mean(scores)


class SumSquaredError(FitnessInterface):

    def __init__(self, samples: ndarray, cluster: ClusterInterface):
        super().__init__(samples, cluster)

    def calculate(self, chromosome: ndarray) -> float:
        labels = self.cluster.run(chromosome, self.samples)
        sse = 0
        for k in range(chromosome.shape[0]):
            members = self.samples[k == labels]
            sse += (linalg.norm(members - chromosome[k], axis=0) ** 2).sum()
        return 1 / sse


class FPC(FitnessInterface):

    def __init__(self, samples: ndarray, cluster:ClusterInterface):
        super().__init__(samples, cluster)

    def calculate(self, chromosome: ndarray) -> float:
        u, u0, d, jm, p, fpc = cmeans_predict(self.samples.transpose(),
                                              chromosome, 2, error=0.005,
                                              maxiter=1000)
        return fpc
