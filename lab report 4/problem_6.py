# 6. Tuple Concatenation: Write a Python program to concatenate two tuples and create a new tuple.

def concat_tuple(tup1, tup2):
    return tup1 + tup2


tuple1 = (1, 2, 4)
tuple2 = ('a', 'b', 'x')

print(concat_tuple(tuple1, tuple2))
