# 14. Set Intersection: Given two sets A and B, write a Python program
# to find their intersection and print the common elements.

def common_element(set_1, set_2):
    unique_list = []
    for i in set_1:
        if i in set_2:
            unique_list.append(i)
    print(set(unique_list))


set1 = {1, 4, 6, 9}
set2 = {1, 6, 7, 9}

common_element(set1, set2)
