# 13. List Manipulation: Given a list of integers, write a Python program using a for loop
# to find the sum, average, maximum, and minimum values in the list.

num = [1, 2, 3, 4, 5, 6]


def list_manipulation(lists):
    sum_value = 0
    max_value = num[0]
    min_value = num[0]

    for i in lists:
        sum_value = sum_value + i
        if max_value < i:
            max_value = i
        if min_value > i:
            min_value = i

    print(f'Sum value of list: {sum_value}')
    print(f'Average of the list value {sum_value / len(num)}')
    print(f'Max value in the list {max_value}')
    print(f'Min value in the list {min_value}')


list_manipulation(num)
