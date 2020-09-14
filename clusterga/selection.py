import random as Random

from clusterga.population import PopulationInterface


class SelectionInterface:

    def __init__(self, population: PopulationInterface, random: Random):
        self.population = population
        self.random = random

    def select(self, n, individual):
        raise NotImplementedError


class Roulette(SelectionInterface):

    def __init__(self, population: PopulationInterface, random: Random):
        super().__init__(population, random)

    def select(self, n, individual):
        probability = self.random.random()
        if self.population[-1].value < 0:
            self.population.sum_value += (-self.population[-1].value) * len(self.population)
            for ind in self.population:
                if probability <= ((-self.population[-1].value) + ind.value) / self.population.sum_value:
                    return ind
                else:
                    probability -= ((-self.population[-1].value) + ind.value) / self.population.sum_value

        for ind in self.population:
            if probability <= ind.value / self.population.sum_value:
                return ind
            else:
                probability -= ind.value / self.population.sum_value
        return self.population[-2]

class Elitism(SelectionInterface):

    def __init__(self, population: PopulationInterface, random: Random):
        super().__init__(population, random)

    def select(self, n, individual):
        selects = []
        equals = 0
        for i in range(n):
            if self.population[0] is individual:
                equals += 1
            else:
                selects.append(self.population[i])
        else:
            while equals > 0:
                if self.population[n+equals] is individual:
                    continue
                else:
                    selects.append(self.population[n+equals])
                    equals -= 1


class Tournament(SelectionInterface):

    def __init__(self, population: PopulationInterface, random: Random):
        super().__init__(population, random)

    def select(self, n, individual, n_tournament=4):
        best = self.population[self.random.randint(0, self.population.size)]
        for i in range(n_tournament-1):
            n = self.random.randint(0, self.population.size)
            if self.population[n].value > best.value:
                best = self.population[n]
        else:
            return best
