# 22. List Element Count: Write a Python program to count the occurrences of a specific
# element in a given list.

def element_count(lists, target):
    count = 0
    for i in lists:
        if i == target:
            count += 1
    print(f'{target} in the list is: {count} times')


element_count([1, 4, 5, 6, 7, 7], 7)
