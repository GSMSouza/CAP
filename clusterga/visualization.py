import matplotlib.pyplot as plt
import numpy as np


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