# 28. Nested Dictionary Sorting: Given a nested dictionary containing product details
# (product name, price, and quantity), write a Python program to sort the products based
# on their prices in ascending order


products = {
    "Laptop": {"price": 1200, "quantity": 5},
    "Phone": {"price": 800, "quantity": 12},
    "Tablet": {"price": 500, "quantity": 11},
}


def dictionary_sorting(dic):
    lists = []
    for name, details in products.items():
        lists.append((name, details))
    lists.sort(key=lambda item: item[1]['price'])
    final_dict = dict(lists)
    print(final_dict)


dictionary_sorting(products)
