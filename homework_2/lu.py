import numpy as np
from pr1 import *


def lu_factor(matrix_a):
    n = len(matrix_a)
    matrix_l = np.eye(n)
    for i in range(n):
        row = i
        pivot = matrix_a[i][i]
        for k in range(row + 1, n):
            multiple_number = matrix_a[k][i] / pivot
            matrix_l[k][i] = multiple_number
            for j in range(len(matrix_a[i])):
                matrix_a[k][j] -= multiple_number * matrix_a[i][j]

    result_dic = {
        "matrix_l": matrix_l,
        "matrix_u": matrix_a
    }
    return result_dic

def linear_sys_solver(matrix_a, b):
    L_U_FACTOR = lu_factor(matrix_a)
    matrix_l = L_U_FACTOR.get("matrix_l")
    matrix_u = L_U_FACTOR.get("matrix_u")
    y = solution_checker(reduced_echelon_form(lower_triangle(
    matrix_standardize_for_row_reduction(augmented_matrix_maker(matrix_l, b)))))
    x = solution_checker(reduced_echelon_form(lower_triangle(
    matrix_standardize_for_row_reduction(augmented_matrix_maker(matrix_u, y)))))

    return x

matrix_1 = [[3, -2, 0, 0, 0, 0], [-2, 3, -2, 0, 0, 0], [0, -2, 2 / 3, -2, 0, 0], [0, 0, -2, 3, -2, 0],
            [0, 0, 0, -2, 3, -2],
            [0, 0, 0, 0, -2, 3]]
vector_1 = [1, -1, -10 / 3, -1, -1, 1]

    