# 19. Dictionary Merging: Given two dictionaries, write a Python program to merge them
# into a single dictionary and print the result.

def marge_dictionary(dic1: dict, dic2: dict):
    marge_dict = dic1.copy()
    marge_dict.update(dic2)
    return marge_dict


dict1 = {"name": "Hafiz", "age": 23}
dict2 = {"city": "New York", "occupation": "Software Engineer"}

print(marge_dictionary(dict1, dict2))
