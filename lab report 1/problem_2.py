# Given a list of numbers, swap adjacent items in
# pairs (A[0] with A[1], A[2] with A[3], etc.).
# Print the resulting list. If a list has an odd
# number of elements, leave the last element in place

def swap_list_elements():
    lists = [4, 3, 1, 6, 8, 10]
    for i in range(0, len(lists) - 1, 2):
        lists[i], lists[i + 1] = lists[i + 1], lists[i]
    print(lists)


swap_list_elements()
