# 16. Dictionary Keys and Values: Write a Python program that takes a dictionary
# as input and prints all the keys and values in separate lines.

def print_dictionary(dic: dict):
    print(dic.keys())
    print(dic.values())
    print(dic.items())


dictionary = {'Sani': 99, 'Zahid': 98, 'Hafiz': 68, 'Evan': 69}
print_dictionary(dictionary)
