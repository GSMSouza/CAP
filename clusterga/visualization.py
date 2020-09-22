import matplotlib.pyplot as plt
import numpy as np


def plot_history(max_fitness, mean_fitness, img_path='./generation'):
    t = np.arange(len(max_fitness))
    plt.plot(t, mean_fitness, label="Valor médio")
    plt.plot(t, max_fitness, label="Melhor valor")

    plt.xlabel("Geração")
    plt.ylabel("Valor da função de apitidão")
    plt.legend()
    plt.title("Gráfico execução do Algoritmo genético")
    plt.savefig(img_path)
    plt.show()