# 4. Transpose Matrix: Write a Python program to transpose a given
# matrix represented as a nested list.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    t_matrix = []

    for i in range(rows):
        t_row = []
        for j in range(cols):
            t_row.append(lists[j][i])
        t_matrix.append(t_row)
    return t_matrix


lists = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(transpose_matrix(lists))
