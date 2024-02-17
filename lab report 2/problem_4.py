# Problem 2: Write a Python program to reversely print a list using recursion.


def reverse_print(lists, index):
    if index < 0:
        return
    else:
        print(lists[index], end=" ")
        reverse_print(lists, index - 1)


random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse_print(random_list, len(random_list) - 1)
