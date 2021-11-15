# Classes Challenge 40: Epidemic Outbreak GUI App
import math
import random
import tkinter


class Simulation:
    def __init__(self):
        self.day_number = 1
        print("To simulate an epidemic outbreak, we must know the population size.")

        self.population_size = int(input("---Enter the population size: "))
        root = math.sqrt(self.population_size)
        if int(root + .5)**2 != self.population_size:
            root = round(root, 0)
            self.grid_size = int(root)
            self.population_size = self.grid_size**2
            print("Rounding population size to " + str(self.population_size) + " for visual purposes.")
        else:
            self.grid_size = int(math.sqrt(self.population_size))

        print("\nWe must first start by infecting a portion of the population.")
        self.infection_percent = float(input("---Enter the percentage (0-100) of the population to initially infect: "))
        self.infection_percent /= 100
        print("\nWe must know the risk a person has to contract the disease when exposed.")
        self.infection_probability = float(input("---Enter the probability (0-100) that a person gets infected when "
                                                 "exposed to the disease: "))
        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("---Enter the duration (in days) of the infection: "))
        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = float(input("---Enter the mortality rate (0-100) of the infection: "))
        print("\nWe must know how long to run the simulation.")
        self.sim_days = int(input("---Enter the number of days to simulate: "))


class Person():
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self, simulation):
        if random.randint(0, 100) < simulation.infection_probability:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True

    def update(self, simulation):
        if not self.is_dead:
            if self.is_infected:
                self.days_infected += 1
                if random.randint(0, 100) < simulation.mortality_rate:
                    self.die()
                elif self.days_infected == simulation.infection_duration:
                    self.heal()


class Population:
    def __init__(self, simulation):
        self.population = []
        for i in range(simulation.grid_size):
            row = []
            for j in range(simulation.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)

    def initial_infection(self, simulation):
        infected_count = int(round(simulation.infection_percent*simulation.population_size, 0))
        infections = 0
        while infections < infected_count:
            x = random.randint(0, simulation.grid_size - 1)
            y = random.randint(0, simulation.grid_size - 1)
            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected = 1
                infections += 1

    def spread_infection(self, simulation):
        for i in range(simulation.grid_size):
            for j in range(simulation.grid_size):
                if self.population[i][j].is_dead == False:
                    if i == 0:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)

                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(simulation)

                    elif i == simulation.grid_size-1:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                    else:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        elif j == simulation.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)
                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(simulation)

    def update(self, simulation):
        simulation.day_number += 1
        for row in self.population:
            for person in row:
                person.update(simulation)

    def display_statistics(self, simulation):
        total_infected_count = 0
        total_death_count = 0
        for row in self.population:
            for person in row:
                if person.is_infected:
                    total_infected_count += 1
                if person.is_dead:
                    total_death_count += 1
        infected_percent = round(100*(total_infected_count/simulation.population_size), 4)
        death_percent = round(100*(total_death_count/simulation.population_size), 4)

        print("\n-----Day # " + str(simulation.day_number) + "-----")
        print("Percentage of Population Infected: " + str(infected_percent) + "%")
        print("Percentage of Population Dead: " + str(death_percent) + "%")
        print("Total People Infected: " + str(total_infected_count) + " / " + str(simulation.population_size))
        print("Total Deaths: " + str(total_death_count) + " / " + str(simulation.population_size))


def graphics(simulation, population, canvas):
    square_dimension = 600//simulation.grid_size
    for i in range(simulation.grid_size):
        y = i*square_dimension
        for j in range(simulation.grid_size):
            x = j*square_dimension
            if population.population[i][j].is_dead:
                canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='red')
            else:
                if population.population[i][j].is_infected:
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='yellow')
                else:
                    canvas.create_rectangle(x, y, x+square_dimension, y+square_dimension, fill='green')

sim = Simulation()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")
sim_canvas = tkinter.Canvas(sim_window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='lightblue')
sim_canvas.pack(side=tkinter.LEFT)

pop = Population(sim)
pop.initial_infection(sim)
pop.display_statistics(sim)
input("Press Enter to begin simulation.")

for i in range(1, sim.sim_days):
    pop.spread_infection(sim)
    pop.update(sim)
    pop.display_statistics(sim)
    graphics(sim, pop, sim_canvas)
    sim_window.update()

    if i != sim.sim_days-1:
        sim_canvas.delete('all')
