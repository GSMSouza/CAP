from clusterga.crossover import OnePoint, Merge
from clusterga.mutation import CreateOrDelete
from clusterga.population import PopulationForSamples, BalancedPopulationForSamples, PopulationForRandom
from clusterga.selection import Roulette, Elitism, Tournament
from clusterga.fitness import CalinskiHarabaz, DaviesBouldin, SumSquaredError, FPC
from clusterga.cluster import Pairwise, FuzzyCMeans

mutation = {
    "CreateOrDelete": CreateOrDelete
}

crossover = {
    "OnePoint": OnePoint,
    "Merge": Merge
}

selection = {
    "Roulette": Roulette,
    "Elitism": Elitism,
    "Tournament": Tournament
}

population = {
    "SamplesSelect": PopulationForSamples,
    "BalancedPopulationForSamples": BalancedPopulationForSamples,
    "PopulationForRandom": PopulationForRandom
}

fitness = {
    "CalinskiHarabaz": CalinskiHarabaz,
    "DaviesBouldin": DaviesBouldin,
    "SumSquaredError": SumSquaredError,
    "FPC": FPC
}

cluster = {
    "Pairwise": Pairwise,
    "FuzzyCMeans": FuzzyCMeans
}

