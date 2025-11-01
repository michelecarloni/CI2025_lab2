import numpy as np
from itertools import combinations






# CHECKING CHARACTERISTICS OF THE PROBLEMS

def check_negative_value(distance_matrix):
    # Negative values?
    return np.any(distance_matrix < 0)


def check_diagonal_all_zero(distance_matrix):
    # Diagonal is all zero?
    return np.allclose(np.diag(distance_matrix), 0.0)


def check_symmetry(distance_matrix):
    # Symmetric matrix?
    return np.allclose(distance_matrix, distance_matrix.T)


def check_triangular_inequality(distance_matrix):
    # Triangular inequality
    return all(
        distance_matrix[x, y] <= distance_matrix[x, z] + distance_matrix[z, y]
        for x, y, z in list(combinations(range(distance_matrix.shape[0]), 3))
    )

