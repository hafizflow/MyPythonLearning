# 25. Access Nested Dictionary: Given a nested dictionary containing student details, write a
# Python program to access and print specific information such as a student’s name, age, and address.

def access_nested_library(dic: dict, name):
    if name in dic.keys():
        print(dic[name]['name'])
        print(dic[name]['age'])
        print(dic[name]['address']['street'])
        print(dic[name]['address']['city'])


students = {
    "Alice": {
        "name": "Alice Smith",
        "age": 20,
        "address": {"street": "123 Main St", "city": "Anytown"}
    },
    "Bob": {
        "name": "Bob Jones",
        "age": 22,
        "address": {"street": "456 Elm St", "city": "Springfield"}
    }
}

access_nested_library(students, 'Bob')
