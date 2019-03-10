import numpy as np


def augmented_matrix_maker(coefficent_matrix, result_vector):
    augmented_matrix = np.column_stack((coefficent_matrix, result_vector))
    print("\nAugmented matrix is created:")
    print(np.matrix(augmented_matrix))
    return augmented_matrix.tolist()


def manager(matrix):
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            for j in range(i, len(matrix)):
                if matrix[j][i] != 0:
                    matrix[j], matrix[i] = matrix[i], matrix[j]
                    print("\n-------------------------------------------------")
                    print("Interchanging the row[%d] and row[%d}"%(i+1,j+1))
                    print(np.matrix(matrix))
                    break
    print("\nThe Managed Matrix is :")
    print(np.matrix(matrix))
    return matrix


def lower_triangle(matrix):
    print("\nMaking echelon form:")
    counter = 1
    for i in range(len(matrix)):
        if matrix[i][i] != 0:
            pivot = matrix[i][i]
            for j in range(i+1,len(matrix)):
                coefficient = matrix[j][i] / pivot
                if coefficient == 0:
                    continue
                print("----------------------------------------------------------")
                print("level %d, pivot %d" %(counter,i+1))
                for k in range(len(matrix[i])):
                    matrix[j][k] -= coefficient * matrix[i][k]
                print(np.matrix(matrix))
                print("row[%d] -= %f * row[%d]" % (i + 1, coefficient, j + 1))
                counter += 1

        else:
            print("----------------------------------------------------------")
            print("level %d, pivot %d" % (counter, i+1))
            print("No pivot in row [%d]"% (i+1))
            print(np.matrix(matrix))
            counter += 1
    return matrix

def reduced_echelon_form(matrix):
    print("\nMaking reduced echelon form:")
    counter = 1
    for i in reversed(range(len(matrix))):
        if matrix[i][i] != 0:
            pivot = matrix[i][i]
            for j in reversed(range(i)):
                coefficient = matrix[j][i] / pivot
                if coefficient == 0:
                    continue
                print("----------------------------------------------------------")
                print("level %d, pivot %d" % (counter, i + 1))
                for k in range(len(matrix[i])):
                    matrix[j][k] -= coefficient * matrix[i][k]
                print(np.matrix(matrix))
                print("row[%d] -= %f * row[%d]" % (j + 1, coefficient, i + 1))
                counter += 1

        if matrix[i][i] != 0:
            coefficient = matrix[i][i]
            for j in range(len(matrix[i])):
                matrix[i][j] /= coefficient

    return matrix


def solution_checker(matrix):
    print("\nChecking whether system has a solution.")
    for i in range(len(matrix[0])-1):
        print(".")
        if matrix[i][i] == 0 and matrix[i][len(matrix[i]) - 1] != 0:
            print("\nThe system doesn't have any solution because of contradiction in row %d " % (i+1))
    print("\nNo contradiction found. System has a solution at least.\n")
    for i in range(len(matrix[0])-1):
        if matrix[i][i] == 1:
            unique = True
            for j in range(i+1,len(matrix[i]) - 1):
                if matrix[i][j] != 0:
                    unique = False
            if unique:
                print("x%d = %f"%(i+1,matrix[i][len(matrix[i])-1]))
            else:
                print("x%d is a dependent variable"%(i+1))
        else:
            print("x%d is a free variable"%(i+1))


matrix2 = [[0,0,0,0],[0,-2,0,0],[0,2,5,-7],[1,-8,6,1]]
vector = [0,0,-11,4]
solution_checker(reduced_echelon_form(lower_triangle(manager(augmented_matrix_maker(matrix2,vector)))))

