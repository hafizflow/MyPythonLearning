# 20. Dictionary Key Removal: Given a dictionary of items and their quantities,
# write a Python program to remove a specific item from the dictionary based on user input.

def key_removal(dic, key):
    if key in dic:
        del dic[key]
    print(dic)


item_dict = {"apple": 5, "banana": 3, "orange": 2}
key_removal(item_dict, 'apple')
