# 1. Matrix Addition: Write a Python program to add two matrices represented as nested lists.

def matrix_addition(matrix1, matrix2):
    added_matrix = []
    for i in range(len(matrix1)):
        row_result = []
        for j in range(len(matrix2)):
            sum_element = matrix1[i][j] + matrix2[i][j]
            row_result.append(sum_element)
        added_matrix.append(row_result)
    # print added matrix
    for i in added_matrix:
        print(i)


first_matrix = [[10, 2, 3], [4, 5, 2], [2, 7, 9]]
second_matrix = [[7, 2, 3], [4, 12, 6], [7, 0, 8]]

matrix_addition(first_matrix, second_matrix)
