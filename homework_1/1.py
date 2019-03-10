import numpy as np


def print_matrix(matrix):
    print("Next level :")
    print(np.array(matrix))
    


def like_a_gauss(matrix):
    """
    Changes mat into Reduced Row-Echelon Form.
    """
    # Let's do forward step first.
    # at the end of this for loop, the matrix is in Row-Echelon format.
    for i in range(min(len(matrix), len(matrix[0]))):
        # every iteration, ignore one more row and column
        for r in range(i, len(matrix)):
            # find the first row with a nonzero entry in first column
            zero_row = matrix[r][i] == 0
            if zero_row:
                continue
            # swap current row with first row
            matrix[i], matrix[r] = matrix[r], matrix[i]
            print_matrix(matrix)
            # add multiples of the new first row to lower rows so lower
            # entries of first column is zero
            first_row_first_col = matrix[i][i]
            for rr in range(i + 1, len(matrix)):
                this_row_first = matrix[rr][i]
                scalarMultiple = -1 * this_row_first / first_row_first_col
                for cc in range(i, len(matrix[0])):
                    matrix[rr][cc] += matrix[i][cc] * scalarMultiple
                print_matrix(matrix)
            break

    # At the end of the forward step
    print_matrix(matrix)
    # Now reduce
    for i in range(min(len(matrix), len(matrix[0])) - 1, -1, -1):
        # divide last non-zero row by first non-zero entry
        first_elem_col = -1
        first_elem = -1
        for c in range(len(matrix[0])):
            if matrix[i][c] == 0:
                continue
            if first_elem_col == -1:
                first_elem_col = c
                first_elem = matrix[i][c]
            matrix[i][c] /= first_elem
        print_matrix(matrix)
        # add multiples of this row so all numbers above the leading 1 is zero
        for r in range(i):
            this_row_above = matrix[r][first_elem_col]
            scalarMultiple = -1 * this_row_above
            for cc in range(len(matrix[0])):
                matrix[r][cc] += matrix[i][cc] * scalarMultiple
            print_matrix(matrix)
        # disregard this row and continue

    print_matrix(matrix)


n = int(input("enter dimension of matrix:"))

matrix_A = list()

for i in range(n):
    row = [int(num) for num in input().split(" ")]
    matrix_A.append(row)

print("Now enter vector b:")

vector_b = [int(num) for num in input().split(" ")]

augmented_matrix = list()

for row, element in zip(matrix_A, vector_b):
    augmented_matrix.append(row + [element])

print("Augmented Matrix:")
print_matrix(augmented_matrix)

like_a_gauss(augmented_matrix)
