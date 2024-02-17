# Problem 1: Write a Python function that takes a list and returns a new list
# with unique elements from the first list.


# way 1
# def unique_item(lists):
#     new_list = list(set(lists))
#     print(new_list)
#
#
# test_list = [2, 2, 24, 4, 5, 5, 4, 8, 9]
# unique_item(test_list)


# way 2
def unique(lists):
    unique_list = []
    for i in lists:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


test_list = [2, 2, 24, 4, 5, 5, 4, 8, 9]
print(unique(test_list))
