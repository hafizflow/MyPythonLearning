# 21. Dictionary Sorting: Given a dictionary with names as keys and corresponding
# ages as values, write a Python program to sort the dictionary based on age in ascending order.
def dict_sort(dic: dict):
    sorted_list = []
    for name, age in dic.items():
        sorted_list.append((name, age))
    sorted_list.sort(key=lambda item: item[1])
    return dict(sorted_list)


people_dict = {"Alice": 30, "Bob": 25, "Charlie": 32}
print(dict_sort(people_dict))
