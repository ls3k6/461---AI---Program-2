import random
from itertools import product

facilitators = ["Lock", "Glen", "Banks", "Richards", "Shaw", "Singer", "Uther", "Tyler", "Numen", "Zeldin"]
activities = 
{
    "SLA100A": {"enrollment": 50, "preferred_facilitators": ["Glen", "Lock", "Banks", "Zeldin"], "other_facilitators": ["Numen", "Richards"]},
    "SLA100B": {"enrollment": 50, "preferred_facilitators": ["Glen", "Lock", "Banks", "Zeldin"], "other_facilitators": ["Numen", "Richards"]},
    "SLA191A": {"enrollment": 50, "preferred_facilitators": ["Glen", "Lock", "Banks", "Zeldin"], "other_facilitators": ["Numen", "Richards"]},
    "SLA191B": {"enrollment": 50, "preferred_facilitators": ["Glen", "Lock", "Banks", "Zeldin"], "other_facilitators": ["Numen", "Richards"]},
    "SLA201":  {"enrollment": 50, "preferred_facilitators": ["Glen", "Banks", "Zeldin", "Shaw"], "other_facilitators": ["Numen", "Richards", "Singer"]},
    "SLA291":  {"enrollment": 50, "preferred_facilitators": ["Lock", "Banks", "Zeldin", "Singer"], "other_facilitators": ["Numen", "Richards", "Shaw", "Tyler"]},
    "SLA303":  {"enrollment": 60, "preferred_facilitators": ["Glen", "Zeldin", "Banks"], "other_facilitators": ["Numen", "Singer", "Shaw"]},
    "SLA304":  {"enrollment": 25, "preferred_facilitators": ["Glen", "Banks", "Tyler"], "other_facilitators": ["Numen", "Singer", "Shaw", "Richards", "Uther", "Zeldin"]},
    "SLA394":  {"enrollment": 20, "preferred_facilitators": ["Tyler", "Singer"], "other_facilitators": ["Richards", "Zeldin"]},
    "SLA449":  {"enrollment": 60, "preferred_facilitators": ["Tyler", "Singer", "Shaw"], "other_facilitators": ["Zeldin", "Uther"]},
    "SLA451":  {"enrollment": 100, "preferred_facilitators": ["Tyler", "Singer", "Shaw"], "other_facilitators": ["Zeldin", "Uther", "Richards", "Banks"]},
}
rooms = 
{
    "Slater 003": 45,
    "Roman 216": 30,
    "Loft 206": 75,
    "Roman 201": 50,
    "Loft 310": 108,
    "Beach 201": 60,
    "Beach 301": 75,
    "Logos 325": 450,
    "Frank 119": 60,
}

times = ["10 AM", "11 AM", "12 PM", "1 PM", "2 PM", "3 PM"]


import random

def generate_random_schedule(activities, rooms, times, facilitators):
    schedule = {}
    for activity in activities:
        room = random.choice(list(rooms.keys()))
        time = random.choice(times)
        facilitator = random.choice(facilitators)
        schedule[activity] = {"room": room, "time": time, "facilitator": facilitator}
    return schedule


def calculate_fitness(schedule, rooms, activities):
    score = 0
    utilized_space = sum([activity['space'] for activity in schedule.values()])
    space_utilization = utilized_space / rooms
    for time, activity in schedule.items():
        for other_time, other_activity in schedule.items():
            if time != other_time and activity == other_activity:
                score -= 1
        score += space_utilization
    return score


def genetic_algorithm(population_size, rooms, activities, generation_size):
    fitness_scores = [calculate_fitness(schedule, space, activities) for schedule in population]
    parents = tournament_selection(population_size, fitness_scores, generation_size)
offspring = []
for i in range(generation_size):
        parent1 = parents[i]
        parent2 = parents[(i + 1) % generation_size]
        child = crossover(parent1, parent2)
        child = mutation(child, activities)
        offspring.append(child)
offspring_fitness_scores = [calculate_fitness(schedule, rooms, activities) for schedule in offspring]
combined_population = population + offspring
combined_fitness_scores = fitness_scores + offspring_fitness_scores
top_individuals = elitist_selection(combined_population, combined_fitness_scores, generation_size)
    
  return top_individuals
