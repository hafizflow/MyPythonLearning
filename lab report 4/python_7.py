# 7. Tuple Unpacking: Given a tuple with three elements (x, y, z),
# write a Python program to unpack the tuple and assign the values to three variables.

def unpack_tuple(tup):
    x, y, z = tup

    print(x)
    print(y)
    print(z)


my_tuple = (10, "apple", 3.14)
unpack_tuple(my_tuple)
