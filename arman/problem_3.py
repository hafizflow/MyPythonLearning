def swap_max_min(num):
    max_value_index = num.index(max(num))
    min_value_index = num.index(min(num))

    num[max_value_index], num[min_value_index] = num[min_value_index], num[max_value_index]
    print(num)


numbers = [4, 2, 8, 1, 7, 9, 20]
swap_max_min(numbers)
