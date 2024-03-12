# 5. List of Lists Concatenation: Given a list of nested lists, write a Python
# program to concatenate all the sublists into a single flat list.

def flat_list(lists):
    list_flat = []
    for i in range(len(lists)):
        for j in range(len(lists[0])):
            list_flat.append(lists[i][j])
    return list_flat


random_list = [
    [1, 2, 3],
    [3, 5, 6],
    [7, 8, 9]
]

print(flat_list(random_list))
