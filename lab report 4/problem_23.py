# 23. Dictionary Comprehension: Given a list of integers, write a Python program to create a
# dictionary where the keys are the elements from the list, and the values are their squares.

def dictionary_comprehension(lists):
    dictionary = {}
    for x in lists:
        dictionary[x] = x ** 2
    print(dictionary)


list1 = [1, 2, 3, 4]
dictionary_comprehension(list1)
