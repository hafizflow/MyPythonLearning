sum = 0
i = 0
data = int(input("Enter a number: "))
while data != 0:
    sum += data
    i += 1
    data = int(input("Enter a number: "))
    print("Enter, 0 to terminate")
print("The sum ", sum)

# problem 2
lists = [1, 2, 2, 3, 4, 5, 6, 6, 7]
for i in lists:
    initial_value = i
    j = 1
    while j < len(lists):
        if initial_value == lists[j]:
            lists.remove(lists[j])
        j = j + 1
print(lists)

# problem 1
lis = [1, 2, 3]
result = [[]]
for i in lis:
    result += [cur + [i] for cur in result]
for current in result:
    result += current + [i]
print(result)

# recursion
data = int(input("Enter: "))
result = 1

for i in range(1, data + 1):
    result = result * i
print(result)


def fact(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * fact(num - 1)


num = int(input("Enter a number: "))
print(f"Factorial of {num}: {fact(num)}")


def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


for i in range(6):
    print(fibonacci(i), end=' + ')

print(fibonacci(6))

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8)
tuple1 += (9, 10, 11, 12, 13, 14, 15)
print(tuple1)

# list unpacking
list1 = [1, 2, 3]
a, b, c = list1
print(a, b, c)

# sequence slicing
list2 = [1, 2, 3.7, 'python']
print(list2[:4])
