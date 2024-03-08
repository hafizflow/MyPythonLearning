# 21. List Manipulation: Given two lists of integers, write a Python program to create
# a new list that contains elements common to both lists.

l1 = [1, 2, 3, 5, 10]
l2 = [3, 1, 9, 10, 8]


def common_list(list1, list2):
    common = [i for i in list1 if i in list2]
    print(f'Common list: {common}')


common_list(l1, l2)
