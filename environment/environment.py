from environment.person import Person
from random import sample


class Environment(object):
    ALIVE = True

    def __init__(self, population_size, initial_sick, contagion_rate, mortality_rate):
        self.mortality_rate = mortality_rate
        self.contagion_rate = contagion_rate
        population = []
        for i in range(population_size):
            population.append(Person(0, 100000))

        self.population = population
        self.sick = sample(population, initial_sick)
        self.last_sick = 1

        self.reward_history = []

    def transition(self, person, status):
        if status is not None:
            if status == person.status.sick:
                self.sick.append(person)

    def update(self, action, termination=False):

        new_infected = sample(self.population, min([len(self.population), self.contagion_rate*len(self.sick)]))
        for person in self.population:
            get_sick = person in new_infected
            # if get_sick:
            #     print('putaaaa')
            status = person.update(mortality_rate=self.mortality_rate, get_sick=get_sick, locked=action)
            self.transition(person, status)

        #No lockdown
        reward = -len(self.sick)
        discount = 0.9
        next_state = 0
        self.last_sick = len(self.sick)
        self.reward_history.append(reward)

        if len(self.sick):
            self.ALIVE = False
        return self.reward_history[-1], discount, next_state

    @staticmethod
    def reset(population_size, initial_sick, contagion_rate, mortality_rate):
        return Environment(population_size, initial_sick, contagion_rate, mortality_rate)