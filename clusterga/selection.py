import random as Random


class SelectionInterface:

    def __init__(self, population, random):
        self.population = population
        self.random = random

    def select(self, n, individual):
        raise NotImplementedError


class Roulette(SelectionInterface):

    def __init__(self, population, random):
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


class Elitism(SelectionInterface):

    def __init__(self, population, random):
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
