# 19. List Filtering: Given a list of integers, write a Python program to create a new
# list that contains only the even numbers from the original list.

def list_filtering(lists):
    # list comprehension technique
    even_list = [i for i in lists if i % 2 == 0]
    print(f'Even list: {even_list}')


list_filtering([1, 2, 3, 4, 7, 9, 4])
