numbers = [10, 2, 3, 4, 51, 6, 79, 8, 9, 10]

maxNum = numbers[0]
minNum = numbers[0]
for i in numbers:
    if i > maxNum:
        maxNum = i
    if i < minNum:
        minNum = i
print("Maximum number: ", maxNum)
print("Maximum number: ", minNum)


# factorial
def factorial(num):
    if num < 1:
        return 1
    else:
        return factorial(num - 1) * num


fact = factorial(5)
print(fact)


# fibonacci
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


print("Fibonacci series: ")
for i in range(11):
    print(fibonacci(i))

for i in range(10, 1, -2):
    print(i)

for i in range(1, 10, 2):
    print(i)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(len(list1)):
    print(list1[i])

for i in list1:
    print(i)

sum


def add():
    total = 4 + 16
    print(total)


add()

list = ['hello', 'hi', 'world', 'tour']


def fun(l):
    for i in range(len(l)):
        print(l[i])


fun(list)

name = ['rafi', 'auntu', 'marwa']
id = ['5801', '5437', '5803']

name_id = []


def addTwoLists(names, student_id):
    for i in range(len(names)):
        name_id.insert(i, names[i] + ' ' + student_id[i])

    for i in range(len(names)):
        print(name_id[i])


addTwoLists(name, id)

lists = [' ', 0, 6, True, ' ', ' ']
for i in range(len(lists)):
    if lists[i] == ' ':
        lists[i] = 'Hello'
print(lists)

for i in range(len(lists)):
    if lists[i] == ' ':
        lists.remove(' ')
        data_type = input('Enter data type: ')

        value = input(f'Enter value at index {i + 1}: ')
        changed_value = 0
        if data_type == 'str':
            changed_value = str(value)
        elif data_type == 'int':
            changed_value = int(value)
        else:
            changed_value = float(value)
        lists.insert(i, changed_value)
print(lists)

lists1 = ['Hafiz' for x in lists if ' ' in x]
print(lists1)
