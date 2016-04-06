import random
import population
import individual


uniform_rate = 0.5
mutation_rate = 0.015
tournament_size = 5
elitism = True


def tournament(pop: population.Population) -> individual.Individual:
    tourn = population.Population()
    for _ in range(tournament_size):
        tourn.add(pop.indivs[random.randrange(0, len(pop.indivs))])
    return tourn.get_fittest()


def mutate(indiv: individual.Individual):
    # for i in range(individual.Individual.gene_length):
        # if elitism and i == 0:
            # continue
        # if random.random() <= mutation_rate:
            # indiv.genes[i // 8] ^= 1 << (i % 8)
    for i, _ in enumerate(indiv.genes):
        # if elitism and i == 0:
            # continue
        if random.random() <= mutation_rate:
            indiv.genes[i] = random.randint(0, 255)


def crossover(indiv1: individual.Individual, indiv2: individual.Individual) -> individual.Individual:
    new_indiv = individual.Individual()
    # for i in range(individual.Individual.gene_length):
        # if random.random() <= uniform_rate:
            # new_indiv.genes[i // 8] ^= indiv1.genes[i // 8] & (1 << (i % 8))
        # else:
            # new_indiv.genes[i // 8] ^= indiv1.genes[i // 8] & (1 << (i % 8))
    for i, _ in enumerate(new_indiv.genes):
        if random.random() <= uniform_rate:
            new_indiv.genes[i] = indiv1.genes[i]
        else:
            new_indiv.genes[i] = indiv2.genes[i]
    return new_indiv


def evolve(pop: population.Population) -> population.Population:
    new_population = population.Population()
    if elitism:
        new_population.add(pop.get_fittest())
    for _ in range((len(pop.indivs) - 1) if elitism else len(pop.indivs)):
        indiv1 = tournament(pop)
        indiv2 = tournament(pop)
        new_population.add(crossover(indiv1, indiv2))
    for indiv in new_population.indivs:
        mutate(indiv)
    return new_population

