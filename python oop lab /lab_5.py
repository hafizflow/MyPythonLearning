# print(""" "hello" 'hi'""")


# value = list(map(int, input().split()))
# print(value)


# pro = 3
# while pro <= 50:
#     pro = pro * 3
#
# print(pro)

# word = str(input())
# mod_word = ''
# char = ['$', '%', '#']
#
# for i in range(len(word)):
#     if i <= 2:
#         mod_word += str(input(f'Enter index {i}: '))
#     elif len(word) - i <= 3:
#         mod_word += char[len(word) - i - 1]
#     else:
#         mod_word = mod_word + word[i].upper()
# print(mod_word)

# arr = [1, 2, 3, 4.5, 'python']
# new = arr[-4:-2]
# lol = arr[-3:]
# kol = arr[:-3]
# mol = arr[:]
# print(new)
# print(lol)
# print(kol)
# print(mol)

# string comprehension
# expression(element) for element in old list condition
# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
#
# new = [(x * x if x % 2 == 0 else x) for x in number]
# print(new)

# value = []
#
# for i in number:
#     if i % 2 == 0:
#         value.append(i * i)
# print(value)

# fruit = ['apple', 'orange', 'cherry']
#
# new_fruit = [x for x in fruit if 'a' in x]
# print(new_fruit)

# 2d list
lists = [[1, 2, 3, 4], [4, 5, 6, 7]]
add = 0
# for i in range(len(lists)):
#     for j in range(len(lists[i])):
#         add = add + lists[i][j]
# print(add)

# for i in lists:
#     for j in i:
#         add += j
# print(add)

# dictionary
