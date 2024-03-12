# 8. Tuple Sorting: Write a Python program to sort a tuple of integers in ascending order.

def sort_tuple(tup):
    list_tuple = list(tup)
    # applying bubble sort
    for i in range(len(list_tuple)):
        for j in range(len(list_tuple) - i - 1):
            if list_tuple[j] > list_tuple[j + 1]:
                list_tuple[j], list_tuple[j + 1] = list_tuple[j + 1], list_tuple[j]

    sorted_tup = tuple(list_tuple)
    return sorted_tup

    # we can do this whole process in one single line
    # return tuple(sorted(tup))


tuple1 = (9, 7, 6, 5, 1)
print(sort_tuple(tuple1))
