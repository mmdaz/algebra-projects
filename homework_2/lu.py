import numpy as np


def calculate_l_matrix(matrix_a):
    n = len(matrix_a)
    matrix_l = np.eye(n)
    matrix_u = list(list())
    for i in range(n):
        row = i
        for k in range(row + 1, n):
            multiple_number = matrix_a[k][0]


calculate_l_matrix(np.array([[1, 2], [1, 3]]))
