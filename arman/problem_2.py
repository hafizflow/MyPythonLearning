def swap_adjacent_pairs(lst):
    for i in range(0, len(lst) - 1, 2):
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


names = ['Azim', 'Bithi', 'Suzana', 'Tanaz', 'Nishat']
result = swap_adjacent_pairs(names)
print("Result:", result)
