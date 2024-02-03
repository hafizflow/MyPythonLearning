# [expression for item in iterable if condition == True]

num = [1, 2, 3, 4, 5]
double = [x * 2 for x in num]
print(double)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = []

# only if 'kiwi'
for x in fruits:
    if 'kiwi' in x:
        new.append(x)
print(new)

for x in fruits:
    if 'kiwi' in x:
        new.pop()
print(new)

for x in fruits:
    if x != 'apple':
        new.append(x)
print(new)

new_fruits = [x for x in fruits if 'a' in x]
print(new_fruits)

new_fruits = [x for x in fruits if 'a' not in x]
print(new_fruits)

new_fruits = [x for x in fruits if x != 'apple']
print(new_fruits)
