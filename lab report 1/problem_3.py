# Given a list of unique numbers, swap the minimal
# and maximal elements of this list. Print the resulting list.

def swap_max_min():
    lists = [4, 6, 1, 9, 10]
    max_value_index = lists.index(max(lists))
    min_value_index = lists.index(min(lists))

    lists[max_value_index], lists[min_value_index] = lists[min_value_index], lists[max_value_index]
    print(lists)


swap_max_min()
