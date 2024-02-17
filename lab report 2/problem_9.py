# Problem 7: write a python function that takes a list and prints only
# the positive numbers from the list. Hint: (Can use the continued keyword)


def only_positive(lists):
    for i in lists:
        if i >= 0:
            print(i, end=' ')


random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, -1, -2, -3, -4, -5, -6]
only_positive(random_list)
