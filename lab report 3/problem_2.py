# 2. Type Conversion: Given a list of integers, write a Python program to convert
# each element of the list to a string.
def type_conversion(int_list):
    # using list comprehension technique
    str_list = [str(x) for x in int_list]
    return str_list


print(type_conversion([1, 2, 3, 4, 5]))
