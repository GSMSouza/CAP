from clusterga.crossover import OnePoint
from clusterga.mutation import CreateOrDelete
from clusterga.population import PopulationForSamples
from clusterga.selection import Roulette, Elitism
from clusterga.fitness import CalinskiHarabaz, DaviesBouldin, SumSquaredError, FPC
from clusterga.cluster import Pairwise, FuzzyCMeans

mutation = {
    "CreateOrDelete": CreateOrDelete
}

crossover = {
    "OnePoint": OnePoint
}

selection = {
    "Roulette": Roulette,
    "Elitism": Elitism
}

population = {
    "SamplesSelect": PopulationForSamples
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

