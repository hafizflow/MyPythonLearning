# 4. Transpose Matrix: Write a Python program to transpose a given
# matrix represented as a nested list.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    t_matrix = []
    
    # making a 0 matrix
    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(0)
        t_matrix.append(new_row)

    for i in range(rows):
        for j in range(cols):
            t_matrix[j][i] = matrix[i][j]
    return t_matrix


lists = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose_matrix(lists))
