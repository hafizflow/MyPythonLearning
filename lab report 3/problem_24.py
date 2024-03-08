# 24. List Comprehension: Given a list of integers, write a Python program
# to create a new list that contains the squares of the elements using list comprehension.

def square_list(lists):
    new_list = [i ** 2 for i in lists]
    print(f'Square list: {new_list}')


square_list([1, 2, 3, 4, 5])
