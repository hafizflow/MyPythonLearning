# def fun(my_list: list):
#     for i in range(len(my_list)):
#         for j in range(len(my_list) - 1 - i):
#             if my_list[j] > my_list[j + 1]:
#                 my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
#     return my_list
#
#
# print(fun([1, 4, 5, 6]))

# def nishat_sort(lists):
#     for i in range(len(lists)):
#         for j in range(i + 1, len(lists)):
#             if lists[i] < lists[j]:
#                 lists[i], lists[j] = lists[j], lists[i]
#     print(lists)
#
#
# nishat_sort([1, 4, 5, 6])

# def change_string(sentence: str, word1, word2):
#     words = sentence.split(' ')
#     print(words)
#
#     index_word1 = words.index(word1)
#     index_word2 = words.index(word2)
#     words[index_word1], words[index_word2] = words[index_word2], words[index_word1]
#     return ' '.join(words)
#
#
# sentence = "Nishat Haifz Anjum"
# word1 = "Nishat"
# word2 = "Anjum"
# swapped_sentence = change_string(sentence, word1, word2)
# print(swapped_sentence)

# def create_dict(list1, list2):
#     dictionary = {}
#     for i in range(len(list1)):
#         dictionary[list1[i]] = list2[i]
#     print(dictionary)
#
#
# k = [1001, 1002, 1003, 1004, 1005]
# v = ["usa", "canada", "china", "japan", "Uk"]
# create_dict(k, v)

# value = [1, 2, 3, 4, 5, 6, 7]
# value1 = [1, 2, 3]
#
# for i in value:
#     if i == 5:
#         continue
#     print('break')
#     for j in value1:
#         print(i, j)


# def sgpa_finder(score):
#     grade_mapping = {
#         'A+: (4.0)': range(80, 101),
#         'A: (3.75)': range(75, 80),
#         'A-: (3.5)': range(70, 75),
#         'B+: (3.25)': range(65, 70),
#         'B: (3.0)': range(60, 65),
#         'B-: (2.75)': range(55, 60),
#     }
#
#     for grade, marks in grade_mapping.items():
#         if score in marks:
#             print(f'Your Grade is {grade}')
#
#
# sgpa_finder(60)


# def total_waiver(fee: float, result: float):
#     if 3.5 < result <= 4:
#         waiver = 20
#     elif 3 <= result <= 3.5:
#         waiver = 10
#     else:
#         waiver = 5
#
#     print(f'{fee * (waiver / 100)}')
#
#
# total_waiver(100000, 3.5)

# i = 1
# odd = []
# while i <= 100:
#     odd.append(i)
#     i += 2
# print(odd)

# lists = ['india', 'china', 'nepal', 'myanmar']
#
# for i in range(len(lists) - 1):
#     print(lists[i], end=' ')

# f = [1, 2, 3]
# s = [2, 4, 5]
#
#
# def common_element(first, second):
#     common = []
#     for i in first:
#         if i in second:
#             common.append(i)
#
#     if len(common) == 0:
#         return 'No common element'
#     else:
#         return common
#
#
# print(common_element(f, s))

# lists = list(map(int, input('Enter item: ').split()))
# lists = input('Enter: ').split()
#
#
# def fun(x_list):
#     if len(x_list) < 2:
#         return 'Not Possible'
#     else:
#         x_list.pop(-1)
#         x_list.pop(0)
#         new = x_list
#         return new
#
#
# print(fun(lists))
# add = 0
# n = int(input())
# for i in range(n):
#     x, y = input().split()
#     x = int(x)
#     y = int(y)
#     for j in range(x, (x + (y * 2))):
#         if j % 2 != 0:
#             add = add + j
#     print(add)


# days_week = ['Saturday', 'Sunday', 'Tuesday', 'Thursday', 'Friday']
# days_week.insert(2, 'Monday')
# days_week.insert(4, 'Wednesday')
# print(days_week)
#
#
# def fun(day):
#     if day == 'Friday':
#         print('Today is Holiday')
#     else:
#         print('Working day')
#
#
# fun('Friday')

# info = input().split()
# count_char = 0
# count_vow = 0
# vowel = ['a', 'e', 'i', 'o', 'u']
# for i in info:
#     count_char += len(i)
#     for j in i.lower():
#         if j in vowel:
#             count_vow += 1
#
# print(f'Number of Character: {count_char}')
# print(f'Number of Vowel: {count_vow}')

# lists = []
# new = []
# for i in range(20, 61):
#     if i % 2 == 0 or i % 5 == 0:
#         lists.append(i)
# for i in lists:
#     if i % 2 == 0:
#         new.append(i + 5)
#     elif i % 5 == 0:
#         new.append(i + 2)
# print(lists)
# print(new)

# lists = []
# for i in range(20, 61):
#     if i % 2 == 0:
#         lists.append(i + 5)
#     elif i % 5 == 0:
#         lists.append(i + 2)
# print(lists)

# dict = {}
# for i in range(20, 61):
#     if i % 2 == 0 or i % 5 == 0:
#         dict[i] = i + 7
#     elif i % 5 == 0:
#         dict[i] = i + 2
#     elif i % 2 == 0:
#         dict[i] = i + 5
#
# print(dict)
# print(len(dict))

# result = []
# for number in range(20, 61):
#     if number % 2 == 0:
#         result.append(number + 5)
#     if number % 5 == 0:
#         result.append(number + 2)
#
# print(len(result))


# student_result = {
#     "student1": {"Math": 75, "Physics": 83, "English": 76},
#     "student2": {"Math": 81, "Physics": 85, "English": 72},
#     "student3": {"Math": 75, "Physics": 81, "English": 85}
# }
# output_value = []
# for i in student_result:
#     individual = (student_result[i].values())
#     total = sum(individual)
#     avg = round(total / len(student_result[i]))
#     output_value.append(avg)
#
# print(f'Average {output_value}')


# avg = 0
# total = 0
# count = 0
# while True:
#     marks = int(input('Enter your mark: '))
#     if marks == -1:
#         break
#     total += marks
#     count += 1
#
# avg = round(total / count)
# print(avg)

# lists = ['1', '2', '3']
# x = list(map(int, lists))
# print(x)
# Two lists


# list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
# my_dict = dict(list_of_tuples)
# print(my_dict)


# keys = ['a', 'b', 'c', 'a']
# values = [1, 2, 3]
#
# dic = dict(zip(keys, values))
# print(dic)

# dic = {x: 0 for x in values}
# print(dic)

# city = dict()
# city['a'] = 1
# print(city)


# dic = {'a': 1, 'b': 2, 'c': 3}
# for key, value in dic.items():
#     print(key, value)

# update
# dic.update({'a': 90})
# print(dic)

# del dic['a']
# print(dic)

# dic.clear()
# dic.clear()
# print(dic)

# lists = [1, 2, 3]
# lists.clear()
# print(lists)

# a = {1, 2, 3}.union({4, 5})
# print(a)

# lists = [1, 2, 3, 4]
# z = [x for x in reversed(lists)]
# print(z)

# lists.sort(reverse=True)
# print(lists)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for i in matrix:
#     for j in i:
#         print(j, end=' ')
#     print()

# tup = (1, 2)
# tup += (4,)
# print(tup)

# lists = [1, 2, 3, 4]
# print(lists.index(1))

# a = 10
#
#
# def fun():
#     a = 5
#     print(a)
#
#
# print(a)
# fun()

# def generate(first, last, id):
#     password = ''
#     password += first[:3].upper()
#     password += str(ord(last[-1])) + str(ord(last[-2]))
#     s_id = id[2:5]
#     password += s_id[::-1]
#     return password
#
#
# print(generate('Umme', 'Ayman', '3215678'))

# def change(sentence: str, target):
# lists = sentence.split()
#
# for i in range(len(lists)):
#     if lists[i] == '5th':
#         lists[i] = target
# return ' '.join(lists)

# return sentence.replace('5th', target)


# print(change('I am in 5th semester', '7th'))


# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# dic = dict(zip(list1, list2))
# print(dic)


# grad = {
#     'A+': range(80, 100),
#     'A': range(75, 80)
# }
#
#
# def fun(dic: dict, num):
#     for grade, marks in dic.items():
#         if num in marks:
#             print(f'Your get {grade}')
#
#
# fun(grad, 76)

# student_result = {
#     "student1": {"Math": 75, "Physics": 83, "English": 76},
#     "student2": {"Math": 81, "Physics": 85, "English": 72},
#     "student3": {"Math": 75, "Physics": 81, "English": 85}
# }
#
# lists = []
#
# for i in student_result:
#     marks = student_result[i].values()
#     total = sum(marks)
#     avg = round(total / len(student_result[i]))
#     lists.append(avg)
#
# print(lists)


# first_matrix = [[10, 2, 3], [4, 5, 2], [2, 7, 9]]
# second_matrix = [[7, 2, 3], [4, 12, 6], [7, 0, 8]]

# first_matrix.extend(second_matrix)
# print(first_matrix)

# new = first_matrix + second_matrix
# print(new)

# x = [j for i in first_matrix for j in i]
# print(x)

# x = []
# for i in first_matrix:
#     for j in i:
#         x.append(j)
# print(x)

# for i in first_matrix:
#     x.extend(i)
# print(x)

# final = []
# for i in range(2):
#     row = []
#     for j in range(3):
#         row.append(input())
#     final.append(row)
# print(final)

# dic = {i: 'a' for i in range(3)}
# print(dic)

# first_matrix = [[10, 2, 3], [4, 5, 2], [2, 7, 9]]
# dic = {}
#
# for i in first_matrix:
#     for j in i:
#         if j not in dic:
#             dic[j] = 1
#         else:
#             dic[j] += 1
# print(dic)


# matrix = [
#     [8, 2, 3],
#     [4, 5, 2],
#     [6, 2, 7],
# ]
# new = []
# row = len(matrix)
# col = len(matrix[0])
#
# for i in range(row):
#     rows = []
#     for j in range(col):
#         rows.append(matrix[j][i])
#     new.append(rows)
# print(new)


# my_tuple = (10, "apple", 3.14)
# x, y, z = my_tuple
# print(x, y, z)


# tuple1 = [9, 7, 6, 5, 1]
#
# for i in range(len(tuple1)):
#     for j in range(len(tuple1) - i - 1):
#         if tuple1[j] > tuple1[j + 1]:
#             tuple1[j], tuple1[j + 1] = tuple1[j + 1], tuple1[j]
#
# print(tuple1)

# lists = [2, 1, 2, 2, 3, 2]
# new = []
# for i in lists:
#     if lists.count(i) < 2:
#         new.append(i)
# print(new)

# set1 = {1, 4, 6, 9}
# set2 = {1, 6, 7, 9}
# set3 = set()
#
# for i in set1:
#     if i in set2:
#         set3.add(i)
# print(set3)

# dictionary = {"Israt": 100, 'Raha': 89}
# dictionary.update({'Israt': 90})
# dictionary['nishat'] = 100
# print(dictionary)

# my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# for i, j in my_dict.items():
#     if j == 30:
#         print(i)

# nishat = {"name": "Alice", "age": 30, "city": "New York"}
# lol = {"Israt": 100, 'Raha': 89}
#
# for i, j in lol.items():
#     nishat[i] = j
# print(nishat)

# nishat.update(lol)
# print(nishat)


# nishat = {"name": "Alice", "age": 30, "city": "New York"}
# del nishat['name']
# nishat.pop('name')
# print(nishat)

# people_dict = {"Alice": 30, "Bob": 25, "Charlie": 32}
# new = []
# for i, j in people_dict.items():
#     new.append((i, j))
# new.sort(key=lambda x: x[1])
#
# print(dict(new))

# lists = [1, 2, 3]
# dic = {x: x ** 2 for x in lists}
# print(dic)


# products = {
#     "Laptop": {"price": 1200, "quantity": 5},
#     "Phone": {"price": 800, "quantity": 12},
#     "Tablet": {"price": 500, "quantity": 11},
# }
# new = []
# for i, j in products.items():
#     new.append((i, j))
# new.sort(key=lambda z: z[1]['price'])
# x = dict(new)
# for i in x.items():
#     print(i)


# string = 'hafiz'
# new = ''
# print(string[::-1])

# for i in string:
#     new = i + new
# print(new)

# for i in range(len(string) - 1, -1, -1):
#     new += string[i]
# print(new)

# x = [1, 2, 3]
# u = []
# for i in x:
#     u.append(str(i))
# print(u)

# c = 18
# f = (9 / 5 * c) + 32
# print(f)


# x = 56
# count = 0
# while x > 0:
#     r = x % 10
#     count += r
#     x = x // 10
# print(count)
