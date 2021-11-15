# Classes Challenge 39: Epidemic Outbreak Terminal App
import random


class Simulation:

    def __init__(self):
        day_number = 1
        print("To simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))

        print("\nWe must first start by infecting a portion of the population.")
        self.infection_size = float(input("--Enter the percentage (0-100) of the population to initially infect: "))
        infection_percent = self.infection_size / 100

        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input("---Enter the probability (0-100) that a person gets infected when "
                                                 "exposed to the disease: "))

        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("---Enter the duration (in days) of the infection: "))

        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = float(input("---Enter the mortality rate (0-100)of the infection: "))

        print("\nWe must know how long to run the simulation.")
        self.sim_days = int(input("---Enter the number of days to simulate: "))
        self.infection_percent = infection_percent
        self.day_number = day_number


class Person:
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, simulation_object):
        number = random.randint(0, 100)
        if number < simulation_object.infection_probability:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True

    def update(self, simulation_object):
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                number = random.randint(0, 100)
                if number < simulation_object.mortality_rate:
                    self.die()
                elif self.days_infected == simulation_object.infection_duration:
                    self.heal()


class Population:
    def __init__(self, simulation_object):
        self.population = []
        for x in range(simulation_object.population_size):
            person = Person()
            self.population.append(person)

    def initial_infection(self, simulation_object):
        infected_count = int(round(simulation_object.infection_percent * simulation_object.population_size, 0))
        for v in range(infected_count):
            self.population[v].is_infected = True
            self.population[v].days_infected = 1

        random.shuffle(self.population)

    def spread_infection(self, simulation_object):
        for i in range(len(self.population)):
            if self.population[i].is_dead == False:
                if i == 0:
                    if self.population[i + 1].is_infected:
                        self.population[i].infect(simulation_object)
                elif i < len(self.population) - 1:
                    if self.population[i - 1].is_infected or self.population[i + 1].is_infected:
                        self.population[i].infect(simulation_object)
                elif i == len(self.population) - 1:
                    if self.population[i - 1].is_infected:
                        self.population[i].infect(simulation_object)

    def update(self, simulation_object):
        simulation_object.day_number += 1
        for x in self.population:
            x.update(simulation_object)

    def display_statistics(self, simulation_object):
        total_infected_count = 0
        total_death_count = 0
        for x in self.population:
            if x.is_infected:
                total_infected_count += 1
                if x.is_dead:
                    total_death_count += 1
        infected_percent = round(100 * (total_infected_count / simulation_object.population_size), 4)
        death_percent = round(100 * (total_death_count / simulation_object.population_size), 4)
        print("\n-----Day # " + str(simulation_object.day_number) + "-----")
        print("Percentage of Population Infected: " + str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print("Total People Infected: " + str(total_infected_count) + " / " + str(simulation_object.population_size))
        print("Total Deaths: " + str(total_death_count) + " / " + str(simulation_object.population_size))

    def graphics(self):
        status = []
        for x in self.population:
            if x.is_dead:
                char = "X"
            else:
                if x.is_infected:
                    char = "I"
                else:
                    char = "O"
            status.append(char)

        for letter in status:
            print(letter, end="-")

simul = Simulation()
popul = Population(simul)

popul.initial_infection(simul)
popul.display_statistics(simul)
popul.graphics()

input("\nPress enter to begin the simulation")

for x in range(1, simul.sim_days):
    popul.spread_infection(simul)
    popul.update(simul)
    popul.display_statistics(simul)
    popul.graphics()

    if x != simul.sim_days - 1:
        input("\nPress enter to advance to the next day.")



