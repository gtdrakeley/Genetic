import random
import fitness


class Individual:
    gene_length = 64

    def __init__(self):
        self.genes = bytearray([random.randint(0, 255) for _ in range(Individual.gene_length)])

    @staticmethod
    def set_gene_length(length):
        Individual.gene_length = length

    def fitness(self):
        return fitness.get_fitness(self)

