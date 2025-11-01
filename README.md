### Introduction

The project contains several algorithms for solving the 'Traveling Salesman Problem'.


### Algorithms

3 algorithms have been implemented:
- 1) Genetic Algorithm: it is a type of population-based evolutionary algorithm. It maintains a population filled with many candidate solutions (tours). In each iteration the parents are selected through 'tournament selection', then both recombination and mutation are applied, using a custom crossover and inversion mutation respectively.
- 2) Simulated Annealing: it is a local search technique. It starts with a single random tour and iteratively tweaks this solution to find a neighbor. If the new solution is better, in terms of fitness, it will be accepted, otherwise a probability define whether the solution should be discarded or accepted (in order to explore somewhere else in the landscape). This probability will be high at the beginning (high exploration) and through many iterations it will be lowered to prefere exploitation than exploration.
- 3) Tabu Search: Another local search algorithm. it maintains a memory to guide the process of discovering a great solution. The algorithm explores neighbor solutions of the current one for a certain number of steps and it maintains an array of solutions already explored. After this analysis the algorithm jumps to another area of the landscape and repeat the same process.


### Results

CONSIDERATIONS: The results reported are based on the value of the fitness. The fitness is basically the sum of the weights of the problem based on the solution. The interpretation is: the lower the weight, the closer 2 cities are. For problems that have negative weights, the more negative the fitness is, the better.


| PROBLEM | Genetic Algorithm | Simulated Annealing | Tabu Search |
| --- | --- | --- | --- |
| g_10 | 1498 | 1498 | 1498 |
| g_20 | 1756 | 1809 | 1756 |
| g_50 | 2771 | 2679 | 2722 |
| g_100 | 4424 | 4760 | 4824 |
| g_200 | 8913 | 10520 | 8600 |
| g_500 | 36002 | 36490 | 20347 |
| g_1000 | 99749 | 95520 | 40955 |
| r1_10 | 184 | 191 | 184 |
| r1_20 | 365 | 344 | 337 |
| r1_50 | 879 | 992 | 674 |
| r1_100 | 1856 | 1750 | 1331 |
| r1_200 | 4436 | 5277 | 3975 |
| r1_500 | 15056 | 18836 | 14162 |
| r1_1000 | 35404 | 43177 | 34322 |
| r2_10 | -412 | -333 | -412 |
| r2_20 | -657 | -600 | -810 |
| r2_50 | -1642 | -1408 | -1666 |
| r2_100 | -2934 | -2559 | -2849 |
| r2_200 | -5935 | -3754 | -4715 |
| r2_500 | -11269 | -6880 | -8422 |
| r2_1000 | -17286 | -7970 | -12239 |