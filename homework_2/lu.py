import numpy as np


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
