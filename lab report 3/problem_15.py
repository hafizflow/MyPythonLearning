# 15. List Sum: Write a Python program to find the sum of all elements in a given list of integers.

def list_sum(lists):
    # in problem 13 we solve it using for loop
    # so here I use python prebuilt function
    return sum(lists)


print(f'Sum of list: {list_sum([1, 2, 3])}')
