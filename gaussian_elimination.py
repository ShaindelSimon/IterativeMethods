##Shain Simon
import numpy as np


def swap_rows(matrix, row1, row2):
    """ Swap two rows in a matrix. """
    matrix[[row1, row2]] = matrix[[row2, row1]]


def eliminate_column(matrix, column, n):
    """ Perform column elimination for Gaussian elimination. """
    for i in range(column + 1, n):
        ratio = matrix[i, column] / matrix[column, column]
        matrix[i, column:] -= ratio * matrix[column, column:]


def back_substitution(matrix, n):
    """ Perform back substitution. """
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = matrix[i, -1] / matrix[i, i]
        for j in range(i - 1, -1, -1):
            matrix[j, -1] -= matrix[j, i] * x[i]
    return x


def gaussian_elimination(A, b):
    """ Solve a system of linear equations Ax = b using Gaussian elimination. """
    n = len(b)
    augmented_matrix = np.hstack([A.astype(float), b.reshape(-1, 1)])

    for i in range(n):
        # Ensure the pivot element is non-zero
        if augmented_matrix[i, i] == 0:
            for j in range(i + 1, n):
                if augmented_matrix[j, i] != 0:
                    swap_rows(augmented_matrix, i, j)
                    break

        eliminate_column(augmented_matrix, i, n)

    return back_substitution(augmented_matrix, n)

if __name__=='__main__':
    A1 = np.array([
        [-1, 1, 3, -3, 1],
        [3, -3, -4, 2, 3],
        [2, 1, -5, -3, 5],
        [-5, -6, 4, 1, 3],
        [3, -2, -2, -3, 5]
    ])
    b1 = np.array([3, 8, 2, 14, 6])
    print("Q1:")
    print(gaussian_elimination(A1, b1))

    A2 = np.array([
        [ 2,  3,  4, 5, 6],
        [ -5, 3,  4, -2, 3],
        [ 4,  -5,  -2, 2, 6],
        [4, 5, -1, -2, -3],
        [5, 5, 3, -3, 5]
    ])
    b2 = np.array([70, 20, 26, -12, 37])
    print("Q2:")
    print(gaussian_elimination(A2, b2))



