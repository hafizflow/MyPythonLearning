names = ['shifa', 'marwa', 'bithy']

# insert
names.insert(1, 'maha')
print(names)

# append
names.append('kaniz')
print(names)

# remove
names.remove('kaniz')
print(names)

# pop
names.pop()
print(names)

# del
del names[1]
print(names)

# clear
names.clear()
print(names)

# sort
numbers = [10, 2, 13, 4, 95, 26, 87, 28, 49]
numbers.sort(reverse=True)  # reverse order
print(numbers)

# sorting according length
surName = ['Michael', 'Bob', 'Tracy']


def myfun(e):
    return len(e)


surName.sort(key=myfun, reverse=True)
print(surName)

firstName = numbers.copy()
print(firstName)

# extends
num1 = [1, 2, 3]
num2 = [4, 5, 6]

num1.extend(num2)
print(num1)
