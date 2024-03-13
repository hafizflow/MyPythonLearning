# 6. Unique Characters: Write a Python program that takes a string as input and checks if it contains
# all unique characters (no character repeats). Use a `for` loop and `break` when a character repeats.

user_str = input('Enter a string: ')

for i in range(len(user_str)):
    if user_str[i] in user_str[i + 1:]:
        print('String does not contain all unique characters.')
        break
else:
    print('String contain all unique characters')
