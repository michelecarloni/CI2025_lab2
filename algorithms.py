from Problem import Problem
from utils_algo import *


def algo_1(problem: Problem, pop_size, num_generations, elitism_size, k, crossover_rate, mutation_rate, show_process = False):
    """
    Runs the main evolutionary algorithm loop.
    """

    distance_matrix = problem.distance_matrix
    num_cities = distance_matrix.shape[0]
    
    # initializing
    population = create_initial_population(pop_size, num_cities)
    best_tour_so_far = None
    best_fitness_so_far = float('inf')
    
    fitness_history = []

    # conditional print, implemented just for style
    if not show_process:
        print(f"{problem.name} | Running...")

    for gen in range(num_generations):
        # calculate fitness for the entire population
        fitness_scores = [calculate_fitness(tour, distance_matrix) for tour in population]
        
        # find the indices of the N best individuals,
        # the first index is the one that refers to the individual with the best fitness
        elite_indices = np.argsort(fitness_scores)[:elitism_size]
        # creating a new population composed of the best individuals of the previous
        new_population = [population[i].copy() for i in elite_indices]
        
        # track the best-ever solution
        best_current_idx = elite_indices[0] 
        current_best_fitness = fitness_scores[best_current_idx]
        
        if current_best_fitness < best_fitness_so_far:
            best_fitness_so_far = current_best_fitness
            best_tour_so_far = population[best_current_idx].copy()

            # if True the new value computed will be printed, False otherwise
            if show_process:
                print(f"{problem.name} | Gen {gen}: New best cost = {best_fitness_so_far:.2f}")

        # add the best cost of this generation to the history
        fitness_history.append(current_best_fitness)

        # in this loop we compute the generation
        while len(new_population) < pop_size:
            # aelecting 2 parents using tournament selection
            parent1 = tournament_selection(population, fitness_scores, k)
            parent2 = tournament_selection(population, fitness_scores, k)
            
            # performing the cross over (random decision defined by crossover_rate)
            if random.random() < crossover_rate:
                offspring = crossover(parent1, parent2)
            else:
                offspring = parent1.copy() 
            
            # performing the mutation
            # (again, its a random decision that doesn't even depend on whether the crossover is done or not)
            if random.random() < mutation_rate:
                # here e we can choose to use inversion_mutation() and swap_mutation()
                inversion_mutation(offspring)
                
            new_population.append(offspring)

        # replace the old population with the new one
        population = new_population

    return best_tour_so_far, best_fitness_so_far, fitness_history


def simulated_annealing(problem: Problem, initial_temp, cooling_rate, num_iterations, show_process=False):
    """
    Runs the Simulated Annealing algorithm.
    """
    distance_matrix = problem.distance_matrix
    num_cities = distance_matrix.shape[0]

    # create a random solution that will be the starting point
    current_tour = np.random.permutation(num_cities)
    current_fitness = calculate_fitness(current_tour, distance_matrix)
    
    # set the best tour so far as the inital tour
    best_tour_so_far = current_tour.copy()
    best_fitness_so_far = current_fitness
    
    temperature = initial_temp
    fitness_history = []

    if not show_process:
        print(f"{problem.name} | Running SA...")


    # main loop where we iterate based on 'num_iterations' passed as input
    for i in range(num_iterations):
        
        # creating a neighbor solution that gets tweaked
        neighbor_tour = current_tour.copy()
        inversion_mutation(neighbor_tour) 
        
        # calculate the fitness of the neighbor solution
        neighbor_fitness = calculate_fitness(neighbor_tour, distance_matrix)
        
        # calculate the fitness delta. A negative delta is an improvement
        delta_fitness = neighbor_fitness - current_fitness
        
        # acceptance criteria
        if delta_fitness < 0:
            # in this case, there is an improvement so the solution is accepted
            current_tour = neighbor_tour
            current_fitness = neighbor_fitness
        else:
            # in order to explore and not gets stuck, even if the current solution is worse
            # than the previous one (in terms of fitness) we might accept it with a certain probability
            if temperature > 1e-6:
                acceptance_prob = math.exp(-delta_fitness / temperature)
                if random.random() < acceptance_prob:
                    current_tour = neighbor_tour
                    current_fitness = neighbor_fitness
        
        # update best-so-far
        if current_fitness < best_fitness_so_far:
            best_fitness_so_far = current_fitness
            best_tour_so_far = current_tour.copy()
            
            if show_process:
                print(f"{problem.name} | Iter {i}: New best cost = {best_fitness_so_far:.2f} (Temp: {temperature:.2f})")

        # cool down the temperature 
        temperature *= cooling_rate
        fitness_history.append(best_fitness_so_far)

    return best_tour_so_far, best_fitness_so_far, fitness_history


def tabu_search(problem: Problem, num_iterations, tabu_tenure, neighborhood_size, show_process=False):
    """
    Runs the Tabu Search algorithm.
    It explores a neighborhood of solutions at each step and moves to the best
    one that is not on the tabu list.
    """
    distance_matrix = problem.distance_matrix
    num_cities = distance_matrix.shape[0]

    # 1. Start with a single random solution
    current_tour = np.random.permutation(num_cities)
    current_fitness = calculate_fitness(current_tour, distance_matrix)
    
    # 2. Initialize best-so-far
    best_tour_so_far = current_tour.copy()
    best_fitness_so_far = current_fitness
    
    # 3. Initialize Tabu List
    # This list will store recent solutions as tuples
    # We use a simple list as a FIFO queue
    tabu_list = [] 
    
    fitness_history = []

    if not show_process:
        print(f"{problem.name} | Running Tabu Search...")

    # 4. Main loop
    for i in range(num_iterations):
        # 5. Generate a neighborhood of candidate solutions
        neighborhood = []
        for _ in range(neighborhood_size):
            neighbor = current_tour.copy()
            inversion_mutation(neighbor) # Modifies in-place
            neighborhood.append(neighbor)
        
        # 6. Find the best neighbor that is not on the tabu list
        best_neighbor = None
        best_neighbor_fitness = float('inf')

        for neighbor in neighborhood:
            neighbor_tuple = tuple(neighbor) # Use tuple for list/set comparison
            neighbor_fitness = calculate_fitness(neighbor, distance_matrix)

            is_tabu = neighbor_tuple in tabu_list
            
            # Aspiration Criterion:
            # We will accept a tabu move IF it is a new global best
            aspiration_met = neighbor_fitness < best_fitness_so_far
            
            # We select this neighbor if it's better than our current best *neighbor* AND
            # (it's not tabu OR it meets the aspiration criterion)
            if neighbor_fitness < best_neighbor_fitness:
                if not is_tabu or aspiration_met:
                    best_neighbor = neighbor
                    best_neighbor_fitness = neighbor_fitness

        # 7. Check if we found a valid move
        if best_neighbor is None:
            # This can happen if all neighbors are tabu and none are new bests
            # We'll just continue from the same spot, hoping a new tweak finds a non-tabu path
            fitness_history.append(best_fitness_so_far)
            continue

        # 8. Move to the best neighbor
        current_tour = best_neighbor
        current_fitness = best_neighbor_fitness
        
        # 9. Update Tabu List
        # Add the new tour to the tabu list
        tabu_list.append(tuple(current_tour))
        # Enforce the tenure: remove the oldest item if the list is too long
        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0) # Removes the first (oldest) item
        
        # 10. Update best-so-far (if needed)
        if current_fitness < best_fitness_so_far:
            best_fitness_so_far = current_fitness
            best_tour_so_far = current_tour.copy()
            
            if show_process:
                print(f"{problem.name} | Iter {i}: New best cost = {best_fitness_so_far:.2f}")

        fitness_history.append(best_fitness_so_far)
    
    return best_tour_so_far, best_fitness_so_far, fitness_history