# 22. Dictionary Frequency Count: Write a Python program that takes a string as input and
# creates a dictionary containing each character as a key and its frequency as the value.

def string_dict(string):
    dictionary = {}
    for char in string:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    print(dictionary)


string_dict('hhallo')
