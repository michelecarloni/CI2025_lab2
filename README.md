### Introduction

The project contains several algorithms for solving the 'Traveling Salesman Problem'.


### Algorithms

3 algorithms have been implemented:
- 1) Genetic Algorithm: it is a type of population-based evolutionary algorithm. It maintains a population filled with many candidate solutions (tours). In each iteration the parents are selected through 'tournament selection', then both recombination and mutation are applied, using a custom crossover and inversion mutation respectively.
- 2) Simulated Annealing: it is a local search technique. It starts with a single random tour and iteratively tweaks this solution to find a neighbor. If the new solution is better, in terms of fitness, it will be accepted, otherwise a probability define whether the solution should be discarded or accepted (in order to explore somewhere else in the landscape). This probability will be high at the beginning (high exploration) and through many iterations it will be lowered to prefere exploitation than exploration.
- 3) Tabu Search: Another local search algorithm. it maintains a memory to guide the process of discovering a great solution. The algorithm explores neighbor solutions of the current one for a certain number of steps and it maintains an array of solutions already explored. After this analysis the algorithm jumps to another area of the landscape and repeat the same process.


### Results

CONSIDERATIONS: The results reported are based on the value of the fitness. The fitness is basically the sum of the weights of the problem based on the solution. The interpretation is: the lower the weight, the closer 2 cities are. For problems that have negative weights, the more negative the fitness is, the better.


| PROBLEM | RESULT |
| g_10 |  |
| g_20 |  |
| g_50 |  |
| g_100 |  |
| g_200 |  |
| g_500 |  |
| g_1000 |  |
| r1_10 |  |
| r1_20 |  |
| r1_50 |  |
| r1_100 |  |
| r1_200 |  |
| r1_500 |  |
| r1_1000 |  |
| r2_10 |  |
| r2_20 |  |
| r2_50 |  |
| r2_100 |  |
| r2_200 |  |
| r2_500 |  |
| r2_1000 |  |