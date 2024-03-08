# 18. List Sorting: Write a Python program to sort a list of integers in ascending order.

# bubble sort
def list_sorting(lists):
    n = len(lists)
    for i in range(n):
        # each time remove the last index ( as though the last element is sorted )
        for j in range(0, n - i - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    print(f'Sorted list: {lists}')


given_list = [5, 2, 1, 2, 3, 4, 0, -1]
list_sorting(given_list)
