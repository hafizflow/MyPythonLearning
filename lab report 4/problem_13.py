# 13. Duplicate Removal: Write a Python program that takes a list
# of elements as input and creates a new set containing only the unique elements from the list.

def duplicate_remove(lists):
    unique_list = []
    for i in lists:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


list1 = (1, 6, 1, 9, 5, 7, 6)
print(duplicate_remove(list1))
