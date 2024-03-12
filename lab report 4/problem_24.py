# 24. Dictionary Key Check: Write a Python program that takes a key as input and checks if it exists
# in a given dictionary. Print “Key Found” if the key is present and “Key Not Found” otherwise.


def key_check(dic: dict, key):
    if key in dic.keys():
        print('Key Found')
    else:
        print('Key Not Found')


dictionary = {1: 'Hafiz', 2: 'Nishat', 3: 'Rafi'}
key_check(dictionary, 7)
