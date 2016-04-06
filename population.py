import individual
import fitness


class Population:
    def __init__(self):
            self.indivs = list()

    @staticmethod
    def initial(size: int):
        ret = Population()
        ret.indivs = [individual.Individual() for _ in range(size)]
        return ret

    def add(self, indiv: individual.Individual):
        self.indivs.append(indiv)

    def get_fittest(self) -> individual.Individual:
        return max(self.indivs, key=lambda indiv: fitness.get_fitness(indiv))

