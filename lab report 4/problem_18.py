# 18. Dictionary Value Search: Given a dictionary of items and their prices,
# write a Python program to search for an item based on its price and print the item’s name.

def value_search(dic, key):
    for name, price in dic.items():
        if price == key:
            print(name)
    # print(dic.items())


items_dict = {"apple": 1.25, "banana": 0.75, "orange": 1.50, "milk": 3.00}
value_search(items_dict, 1.25)
