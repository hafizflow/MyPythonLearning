# 9. Tuple Frequency Count: Given a tuple containing various elements,
# write a Python program to count the frequency of a specific element in the tuple.

def count_tuple(tup, target):
    count = 0
    for i in tup:
        if i == target:
            count += 1
    return count


my_tuple = ("apple", "banana", "cherry", "apple", "orange")
element_to_count = "apple"

print(count_tuple(my_tuple, element_to_count))
