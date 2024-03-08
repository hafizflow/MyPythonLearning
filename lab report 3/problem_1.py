# 1. String Reverse: Write a Python function to reverse a given string and return the reversed string.
def string_rev(user_str):
    reverse_str = ''
    for i in range(len(user_str) - 1, -1, -1):
        reverse_str += user_str[i]
    print(reverse_str)


string_rev('Hello')
