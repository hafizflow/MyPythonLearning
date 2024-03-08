# 23. List Duplicates Removal: Write a Python program to remove duplicates from
# a given list while preserving the order of the elements.

def remove_duplicate(lists):
    unique_list = []
    for x in lists:
        if x not in unique_list:
            unique_list.append(x)
    print(f'Unique list: {unique_list}')


remove_duplicate([4, 4, 4, 1, 2, 3, 4, 5, 6])
