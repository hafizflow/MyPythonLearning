# 20. List Reversal: Write a Python program to reverse a given list without using any built-in functions.

def list_revere(lists: list):
    reverse_list = [lists[i] for i in range(len(lists) - 1, -1, -1)]
    print(reverse_list)


list_revere([1, 8, 6, 2, 5])
