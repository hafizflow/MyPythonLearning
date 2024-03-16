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
