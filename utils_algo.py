import math
import random
import numpy as np
from itertools import combinations


def create_initial_population(pop_size, num_cities):
    """Creates a list of random tours (solutions)."""
    population = []
    for _ in range(pop_size):
        tour = np.random.permutation(num_cities)
        population.append(tour)
    return population

def calculate_fitness(tour, distance_matrix):
    """
    Calculates the total cost (fitness) of a single tour.
    This is the value we want to MINIMIZE.
    Works for both symmetric and asymmetric matrices.
    """
    total_cost = 0
    num_cities = len(tour)
    for i in range(num_cities):
        city_a = tour[i]
        # Use modulo (%) to wrap around to the start city
        city_b = tour[(i + 1) % num_cities]
        
        # This correctly takes the cost from A -> B
        total_cost += distance_matrix[city_a, city_b]
        
    return total_cost

def tournament_selection(population, fitness_scores, k):
    """
    Selects one parent using k-tournament selection.    
    Picks k random individuals and returns the fittest one.
    """
    indices = np.random.choice(len(population), k, replace=False)
    k_fitnesses = [fitness_scores[i] for i in indices]
    best_local_idx = np.argmin(k_fitnesses)
    best_global_idx = indices[best_local_idx]
    
    return population[best_global_idx]

def crossover(parent1, parent2):
    """
    Perform crossover
    """
    num_cities = len(parent1)
    offspring = np.full(num_cities, -1)
    
    # Select two random cut points
    start, end = sorted(np.random.choice(num_cities, 2, replace=False))
    
    # Copy the slice from parent1
    offspring[start:end] = parent1[start:end]
    
    # Fill remaining slots from parent2
    parent2_ptr = 0
    offspring_ptr = 0
    cities_in_offspring = set(offspring[start:end])
    
    while -1 in offspring:
        # Find next available slot in offspring
        if offspring_ptr == start:
            offspring_ptr = end
            
        # Get city from parent2
        city_to_add = parent2[parent2_ptr]
        parent2_ptr += 1
        
        if city_to_add not in cities_in_offspring:
            offspring[offspring_ptr] = city_to_add
            offspring_ptr += 1
            
    return offspring




# DIFFERENT KINDS OF MUTATIONS

def swap_mutation(tour):
    """Performs a simple swap mutation on a tour (modifies in-place)."""
    idx1, idx2 = np.random.choice(len(tour), 2, replace=False)
    tour[idx1], tour[idx2] = tour[idx2], tour[idx1]


def inversion_mutation(tour):
    """
    Performs an inversion mutation (modifies in-place).
    """
    # Select two random cut points
    start, end = sorted(np.random.choice(len(tour), 2, replace=False))
    if start >= end:
        return 
    
    # Reverse the sub-sequence in-place
    tour[start:end] = tour[start:end][::-1]