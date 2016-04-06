import individual
import textwrap


solution = bytearray()


def set_solution(new_solution: str):
    global solution
    solution = bytearray([int(byte, 2) for byte in textwrap.wrap(new_solution, 8)])


def get_fitness(indiv) -> int:
    fitness = 0
    for i, byte in enumerate(solution):
        if indiv.genes[i] == byte:
            fitness += 1
    return fitness


def max_fitness() -> int:
    return len(solution)

