import random
import string


class StringGeneticAlgorithm:

    def __init__(self, target, population_size, mutation_rate, num_generations):
            self.__target = target
            self.__mutation_rate = mutation_rate
            self.__num_generations = num_generations
            self.__population = self.__initial_population(population_size)

    def __initial_population(self, population_size):
            length = len(self.__target)
            words = []
            for index in range(population_size):
                word = "".join(random.sample(string.ascii_lowercase, k=length))
                words.append(word)
            return words

    def __fitness_assignment(self, candidate):
                score = 0
                for l1, l2 in zip(candidate, self.__target):
                    if l1 == l2:
                        score += 1
                return score

    def __selection(self, fitness_scores):
        population_size = len(self.__population)
        candidates = []
        for count in range(population_size):
            candidate = random.choices(self.__population, weights=fitness_scores, k=1)[0]
            candidates.append(candidate)
        return candidates


    def __cross_over(self, parent1, parent2):
            cross_over_point = len(parent1)//2
            child = parent1[:cross_over_point] + parent2[cross_over_point:]
            return child

    def __mutation(self, candidate):
        prob = random.random()
        mutated = list(candidate)
        if prob < self.__mutation_rate:
            letter = random.choice(string.ascii_lowercase)
            index = random.randint(0,len(candidate)-1)
            mutated[index] = letter
        return "".join(mutated)

    def __replacement(self):
        pass

    def run(self):

        generation = 0

        while generation < self.__num_generations:
            scores = []
            for candidate in  self.__population:
                score = self.__fitness_assignment(candidate)
                scores.append(score)

            #select candidates
            select_candidates = self.__selection(scores)

            #cross over
            children = []
            for count in range(len(self.__population)):
                parent1 = random.choice(select_candidates)
                parent2 = random.choice(select_candidates)
                child = self.__cross_over(parent1, parent2)
                children.append(child)

            #mutation
            mutated_candidates = []
            for candidate in children:
                mutated = self.__mutation(candidate)
                mutated_candidates.append(mutated)

            #replacement
            self.__population = mutated_candidates

            generation += 1

            print(self.__population)

algorithm = StringGeneticAlgorithm("hello", 50, 0.2,200)
algorithm.run()