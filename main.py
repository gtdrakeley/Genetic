import population
import fitness
import evolution

fitness.set_solution('{}{}{}{}'.format('11', '0000', '0' * (8 * 63), '11'))

pop = population.Population.initial(100)
gen_count = 0
while pop.get_fittest().fitness() < fitness.max_fitness():
    gen_count += 1
    print('Generation #{}: Fittest - {}'.format(gen_count, pop.get_fittest().fitness()))
    pop = evolution.evolve(pop)
print('Solution found!')
print('Generation #{}'.format(gen_count))
print('Genes:\n\t{}'.format(''.join([format(byte, '0>8b') for byte in pop.get_fittest().genes])))

