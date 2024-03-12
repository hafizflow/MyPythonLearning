# 11. Tuple Reversal: Write a Python program to reverse a tuple without using any built-in functions.

def tuple_reversal(tup):
    list_tup = list(tup)
    # applying bubble sort
    for i in range(len(list_tup)):
        for j in range(len(list_tup) - i - 1):
            if list_tup[j] < list_tup[j + 1]:
                list_tup[j], list_tup[j + 1] = list_tup[j + 1], list_tup[j]
    final_tuple = tuple(list_tup)
    return final_tuple


tup1 = (1, 2, 3, 4, 5)
print(tuple_reversal(tup1))
