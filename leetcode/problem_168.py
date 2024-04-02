# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
# 'V', 'W', 'X', 'Y', 'Z']

# columnNumber = 702
# # div = columnNumber // 26
# # rem = columnNumber % 26
# # res = letters[div - 1] + letters[rem - 1]
# # print(res)
#
# div = columnNumber
# res = ''
# print(div // 26)
#
# while div // 26 > 26:
#     print('Inside')
#
#     div = div // 26
#     print(div)
#     rem = columnNumber % 26
#     res += letters[div] + letters[rem]
#
# print(res)


# letters = []
#
# for i in range(26):
#     char = chr(ord('A') + i)
#     letters.append(char)
#
# columnNumber = 28
# div = (columnNumber // 26)
# rem = (columnNumber % 26)
# res = letters[rem - 1]
# print(res)
#
# if div <= 26:
#     res = letters[div - 1] + res
#     print(res)
# else:
#     while div > 26:
#         rem = div % 26
#         res = letters[rem - 1] + res
#         div = div // 26
#     res = letters[div - 1] + res
#     print(res)

# columnNumber = 27
#
# result = ''
# while columnNumber > 0:
#     columnNumber -= 1
#     result = chr(columnNumber % 26 + 65) + result
#     columnNumber //= 26
# print(result)
