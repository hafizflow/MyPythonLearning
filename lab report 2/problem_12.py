# Problem 10: Write a python program having two lists and compare the values inside the
# list and make a new list with only the unique values, and the new list must be sorted.
# Example: [1,4,5,6,7] , [2,1,3,4,5]  newlist = [2,3,6,7]

def unique_sorted_list(list1, list2):
    unique_list = []

    for item in list1:
        if item not in unique_list and item not in list2:
            unique_list.append(item)
    for item in list2:
        if item not in unique_list and item not in list1:
            unique_list.append(item)
    return sorted(unique_list)


print(unique_sorted_list([1, 4, 5, 6, 7], [2, 1, 3, 4, 5]))
