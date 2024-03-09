# 2. Flatten Nested List: Write a Python program to flatten a given nested
# list and convert it into a single-dimensional list.

def flatted_nested_list(lists):
    new_matrix = []
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            new_matrix.append(lists[i][j])

    print(new_matrix)


matrix = [[1, 2], ['a', 'b', 'c'], [3.5, 4.5]]
flatted_nested_list(matrix)
