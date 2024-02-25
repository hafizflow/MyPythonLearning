# map
# student_id = list(map(int, input().split(' ')))
# print(student_id)


# num = [1, 2, 3, 4, 5, 6]
#
#
# def sumValue(n):
#     summation = 0
#     for x in n:
#         summation = summation + x
#     return summation
#
# result = list(map(sumValue, [num]))
# print(result)

# result = list(map(sumValue, [num]))
# print(result)


# num = [1, 2, 3, 4, 5, 6]
# result = list(map(sum, [num]))
# print(result)


# def check(n):
#     if n % 2 == 0:
#         print('Even number')
#     else:
#         print('Odd number')
#
#
# num = [1, 2, 3, 4]
# list(map(check, num))


# def square_value_and_print(n):
#     return n ** 2
#
#
# # def sqaure_value(n):
# #     for i in n:
# #         print(i ** 2)
#
#
# num = [1, 2, 3, 4]
# result = list(map(square_value_and_print, num))
# print(result)

# num = [1, 2, 3, 4, 5, 6]

# def sum_value(n):
#     add = 0
#     if len(n) == -1:
#
#
#
# result = list(map(sum_value, num))
# print(result)


# number = {9: 'anzum', 2: 'nishat', 3: 'hafiz', 4: 5, 5: 6, 6: 7}
#
#
# for i in number:
#     print(f'keys {i} -> {number[i]}')


# numb = {1: 2, 2: 'hafiz', 3: 4.5, 4: 'python', 5: [1, 2, 4], 6: 8, 7: 9}

# numb = [i ** 2 for i in numb.values() if type(i) == int]
# print(numb)

# new_map = {}

# for i in numb.values():
# if type(i) == list or type(i) == float:
#     new_map[i] = i
#     j = j + 1


# for i, j in numb.items():
#     if type(j) == list or type(j) == float:
#         new_map[i] = j
#
# print(new_map)


# string
# String = 'Hello'
# String2 = "Hello"
# String3 = "Python Programming"
# String4 = """'Hello'
# world"""
#
# print(String4)

# String operation
# String comparison
# str1 = 'Python; Emon Hello'
# str2 = 'hafiz'

# value = str1 == str2
# print(value)


# string concatenation
# print(str1 + ' ' + str2)


# string slicing
# print(str1[4:10])
# print(str1[4:13:2])
# print(str1.split(';'))


# upper
# lower
# replace
# find
# rStrip
# split
# starts
# ends

# set update
# set.discard()
# set.add

# all
# any
# len
# sorted
# max
# enumerate
# sum
# min

# l1 = {"eat", "sleep", "repeat"}
# s1 = "geek"
#
# print(any(l1))
numb = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(all(x % 2 == 0 for x in numb))
print(any(x % 2 == 0 for x in numb))
# print(any ())
