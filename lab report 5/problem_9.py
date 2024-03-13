# 9.You are given an integer n, representing the size of a list. Next, you receive n strings from the user.
# Your task is to create a new list containing all the unique characters from these strings. Additionally,
# sort the characters in lexicographical order.
# Example:
# Input:
# 3
# Zahid Sani Wakif
# Output: ['S', 'W', 'Z', 'a', 'd', 'f', 'h', 'i', 'k', 'n']

n = 3
name_list = []
for i in range(n):
    name_list.append(input('Enter your name: '))

new_list = []
for name in name_list:
    for char in name:
        if char not in new_list:
            new_list.append(char)

print(sorted(new_list))
