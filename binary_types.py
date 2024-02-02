# binary type data

# bytes (range 0 to 256)
# needed for many image related work (zip, shrink)
# bytes is immutable
randomList1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 255]
byteType = bytes(randomList1)
print(type(byteType))

# bytearray (range 0 to 256)
# needed for many image related work (zip, shrink)
# bytearray is mutable
randomList2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 255]
byteArrayType = bytearray(randomList2)
byteArrayType[0] = 100  # changeable/mutable
print(type(byteArrayType))
