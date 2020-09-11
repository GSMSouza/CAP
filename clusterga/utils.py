import random as rd
from hashlib import sha1
import matplotlib.pyplot as plt
import numpy as np

class Random:

    def __init__(self, seed=2):
        self.seed = sha1(bytes(seed)).digest()

    def randint(self, low, high):
        rd.seed(self.seed, version=2)
        self.seed = sha1(self.seed).digest()
        return rd.randint(low, high)

    def random(self):
        rd.seed(self.seed, version=2)
        self.seed = sha1(self.seed).digest()
        return rd.random()

    def choices(self, population, n_samples):
        rd.seed(self.seed, version=2)
        self.seed = sha1(self.seed).digest()
        return rd.choices(population, k=n_samples)


def plot_history(max_fitness, mean_fitness):
    fig, ax1 = plt.subplots()
    t = np.arange(len(max_fitness))
    ax1.set_xlabel('Generation')
    ax1.set_ylabel('Fitness Values', color='tab:red')
    ax1.plot(t, max_fitness, color='tab:red')
    ax1.plot(t, mean_fitness, color='tab:blue')
    ax1.tick_params(axis='y', labelcolor='tab:red')
    #
    fig.tight_layout()
    plt.show()
